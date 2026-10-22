# YourCatFileAssistant v1.0.2 · MIT 源码合集版

本目录是为“首次解压后少于 100 条、文件总大小不超过 25,000,000 字节”整理的源码合集。源码、配置、文档及第三方材料以未压缩、可直接阅读的文本合并保存，未把另一个完整 ZIP 藏在里面。全部图片/图标原始字节保留；固定二进制测试样本合并为 Base64 数据。

## 阅读与还原

- `sources/CatFileAssistant.*.txt`：按项目分组的完整 C#、XAML、项目文件和文本资源，以 ORIGINAL FILE 标记每个原文件。
- `sources/Acceptance-Tests.txt`：验收源码与文本测试素材。
- `sources/Build-and-Maintenance.txt`：完整构建、恢复和维护脚本源码。
- `sources/ThirdParty-License-Materials.txt`：已有第三方许可材料原文及保留的附加声明。
- `sources/Dependency-Metadata.txt`：固定版本、SHA-256、原生引擎源码索引及其他依赖许可。
- `images`：未改动的原始图片与图标；原路径记录在 Source-Map.json。
- `LICENSE`：维护者原创部分使用 MIT，允许商业使用。第三方及已有 LGPL 组件例外见 LICENSE-SCOPE.md 与 THIRD-PARTY-NOTICES.md。

需要 Python 3.11+。在此目录执行：

```powershell
python -B Restore-Source.py --destination ../YourCatFileAssistant-workspace
```

脚本会读取 Source-Map.json，验证全部原文件 SHA-256，并在一个全新目录恢复标准工程。之后可以用 IDE 打开该工程的 CatFileAssistant.sln，按还原后的 README 安装 .NET SDK 10.0.401、固定 FFmpeg 和 7-Zip 等依赖，再构建。以下一键脚本也可代为还原、恢复依赖和构建：

```powershell
./Build.ps1 -SourceCompanion 'X:/downloads/你的猫咪文件助手-V1.0.2-Windows-x64-Sources.zip'
```

默认工作目录位于本目录之外。脚本拒绝覆盖现有目录；失败不把不完整还原结果当成可构建工程。

**100 条限制适用于 ZIP 和首次解压目录。运行还原脚本后，标准源码工程会恢复成 1,585 个原文件；安装依赖与构建还会生成更多文件，并需要额外磁盘空间。**这一步是明确的构建前准备，不属于“首次解压后少于 100 条”的承诺。

本包不带 SDK、FFmpeg/7-Zip 二进制和大型对应源归档。原 FFmpeg 历史 URL 先前返回 404，恢复脚本支持从维护者另行提供的固定完整配套包中恢复，拒绝静默使用 latest。小包不能代替二进制发行所需的完整第三方对应源码。

## 验证

还原后的每个文件应与上一版 MIT 源码副本逐字节一致，哈希见 Source-Map.json。程序行为、界面和素材未因本次文件合并而修改。本次已从还原后的标准工程重新执行 Release 编译，5 个项目构建通过，0 警告、0 错误；同时验证了原文件逐字节还原及原生依赖恢复。未重新执行 GUI、安装或性能验收。

所有本机路径与历史私有运行记录继续排除；作者主动展示的联系信息保留。没有向 GitHub 提交或推送。
