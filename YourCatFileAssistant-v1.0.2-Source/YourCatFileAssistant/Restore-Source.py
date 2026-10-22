"""Restore the complete standard source tree from readable, uncompressed collections."""
import argparse,pathlib,json,hashlib,base64,shutil,tempfile,os
ROOT=pathlib.Path(__file__).resolve().parent

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--destination',required=True);a=ap.parse_args()
 destination=pathlib.Path(a.destination).resolve()
 if destination.exists():raise ValueError('Destination already exists; refusing to overwrite it')
 if destination==ROOT or destination.is_relative_to(ROOT):raise ValueError('Choose a destination outside this distribution directory')
 destination.parent.mkdir(parents=True,exist_ok=True)
 index=json.loads((ROOT/'Source-Map.json').read_text(encoding='utf-8'));fixtures=json.loads((ROOT/'Test-Fixtures.json').read_text(encoding='utf-8'))
 if index['format']!='YourCatFileAssistant-readable-source-collection-v1':raise ValueError('Unsupported source collection format')
 staging=pathlib.Path(tempfile.mkdtemp(prefix='cfa-source-restore-',dir=destination.parent));seen=set()
 try:
  for e in index['sourceFiles']:
   relative=pathlib.PurePosixPath(e['path']);output=(staging/pathlib.Path(*relative.parts)).resolve()
   if relative.is_absolute() or '..' in relative.parts or not output.is_relative_to(staging.resolve()):raise ValueError('Unsafe output path')
   if e['path'].casefold() in seen:raise ValueError('Duplicate source output path')
   seen.add(e['path'].casefold())
   if e['kind']=='fixture-base64':data=base64.b64decode(fixtures[e['path']],validate=True)
   else:
    part=(ROOT/e['file']).resolve()
    if not part.is_relative_to(ROOT):raise ValueError('Unsafe source collection path')
    with part.open('rb') as source:
     if e['kind']=='text-range':source.seek(e['offset'])
     elif e['kind']!='file':raise ValueError('Unknown source storage kind')
     data=source.read(e['bytes'])
   if len(data)!=e['bytes'] or hashlib.sha256(data).hexdigest()!=e['sha256']:raise ValueError('Source integrity mismatch: '+e['path'])
   output.parent.mkdir(parents=True,exist_ok=True);output.write_bytes(data)
  # Atomic creation of a new workspace; never merge with an existing project.
  if destination.exists():raise ValueError('Destination appeared during restoration')
  staging.rename(destination)
 except BaseException:
  if staging.exists() and staging.resolve().is_relative_to(destination.parent.resolve()):shutil.rmtree(staging)
  raise
 print(json.dumps({'success':True,'filesRestored':len(seen),'applicationVersion':index['applicationVersion']},ensure_ascii=False))
if __name__=='__main__':main()
