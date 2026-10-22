param([string]$SourceCompanion,[string]$FfmpegArchive,[string]$SevenZipArchive,[string]$ExtractorPath,[string]$Destination)
$ErrorActionPreference='Stop'
if(-not $Destination){$Destination=Join-Path (Split-Path $PSScriptRoot -Parent) 'YourCatFileAssistant-workspace'}
& python -B (Join-Path $PSScriptRoot 'Restore-Source.py') --destination $Destination
if($LASTEXITCODE -ne 0){throw 'Source restoration failed'}
$workspace=(Resolve-Path -LiteralPath $Destination).Path
$restore=@{}
if($SourceCompanion){$restore.SourceCompanion=$SourceCompanion}
if($FfmpegArchive){$restore.FfmpegArchive=$FfmpegArchive}
if($SevenZipArchive){$restore.SevenZipArchive=$SevenZipArchive}
if($ExtractorPath){$restore.ExtractorPath=$ExtractorPath}
& (Join-Path $workspace 'scripts/restore-dependencies.ps1') @restore
& (Join-Path $workspace 'scripts/build.ps1')
