# 第三方组件说明

主项目原创部分使用根目录 MIT LICENSE；本文件及各组件的既有许可、版权和例外继续适用，见 LICENSE-SCOPE.md。FFmpeg 许可材料已去重归档并保留索引，详见 tools/ffmpeg/licenses/README.md；历史完整发行的“随附”说明不意味着小包包含原生引擎及全部对应源。

## FFmpeg

本项目随附 BtbN Windows x64 shared 构建，位于 `tools/ffmpeg/bin`。构建版本为 FFmpeg `n9.0.2-14-gebafaee10a-20260929`。虽然上游文件名标为 `lgpl-shared`，本次核查确认实际 `avformat-63.dll` 静态包含通过 Chromaprint 链接的 GPL FFTW，故 **V0.7 将这个独立引擎整体按 GPL 3 或更高版本履约分发**。FFmpeg 核心及其他子组件的原始 LGPL、BSD、MIT、Apache 等许可仍各自保留；不能只据上游标签或核心的 `-L` 输出推断全部链接依赖。

实际核验的历史包：`ffmpeg-n9.0.2-14-gebafaee10a-win64-lgpl-shared-9.0.zip`  
SHA-256：`3acc157a5b9628bdc360c93a1267280c425e9d39cf689fd24cd208d3e5b5d9e2`。本项目原始十个二进制文件与这个历史包中的文件逐一 SHA-256 一致，V0.7 不分发 ffplay。

- 构建发布：[BtbN 历史发布 2026-09-29](https://github.com/BtbN/FFmpeg-Builds/releases/tag/autobuild-2026-09-29-13-10)
- 对应 FFmpeg 源码提交：[FFmpeg/FFmpeg@ebafaee10ab45fce1964bd09efcd848e2da5b401](https://github.com/FFmpeg/FFmpeg/tree/ebafaee10ab45fce1964bd09efcd848e2da5b401)
- 构建脚本版本：[BtbN/FFmpeg-Builds@6c9aec5fc9a72ec3abedd1fa84db141fa18cf52b](https://github.com/BtbN/FFmpeg-Builds/tree/6c9aec5fc9a72ec3abedd1fa84db141fa18cf52b)
- 官方许可说明：[FFmpeg License and Legal Considerations](https://ffmpeg.org/legal.html)

完整 GPL 3 文本在 `tools/ffmpeg/licenses/COPYING.GPLv3`；LGPL 2.1/3、GPL 2 和核心许可说明及外部库的原始版权/许可在同目录。`tools/ffmpeg/LICENSE.txt` 是上游保留的核心 LGPL 文本，不能单独表示整个组合引擎的许可。外部依赖索引见 `tools/ffmpeg/THIRD-PARTY-LICENSES.txt`，来源和哈希见 `tools/ffmpeg/provenance.json`。

完整对应源、依赖源归档、原始 Cargo.lock、子模块源及构建/修改配方以同版本 `你的猫咪文件助手-V0.7-Windows-x64-Sources.zip` 提供；文件清单及说明见 `tools/ffmpeg/source/distribution-manifest.json`、`tools/ffmpeg/source/README.md`。应用下载页须同时提供此源包及哈希。免费和商业发行都保留这些许可和用户修改、再分发的权利。

此构建未启用 x264/x265，但这不排除其他 GPL 依赖。视频 H.264/H.265 使用 OpenH264 与 Kvazaar 编码器。主桌面应用通过独立命令行进程、普通媒体文件和标准流调用引擎，不在自身进程中链接 FFmpeg DLL。用户可修改、重新编译和替换引擎及 LGPL 组件；本应用其他条款不得限制相应许可赋予的权利。完整 configure 参数可运行 `tools/ffmpeg/bin/ffmpeg.exe -version` 查看。

This software is based in part on the work of the Independent JPEG Group. 对 FFmpeg 内的 IJG 衍生文件，本项目没有增加、删除或修改代码；原始说明和完整源一并保留。其他历史构建对依赖的修改以随附原始构建脚本为准。

LCEVC 原始许可为 BSD-3-Clause-Clear，并明确不授予专利；其 COPYING 附加说明也保留。媒体格式和硬件接口的专利/商业授权须按使用地区及实际产品独立评估。完整核查事实和发行条件见 `docs/third-party-audit.md`。

## 图片排列算法（V0.7）

Gilbert 二维曲线源代码 Copyright (c) 2018, Jakub Červený，采用 BSD 2-Clause 许可。固定提交为 `9b080a74c5e3b6fe189785c52742f83ac85ba181`，原始 `gilbert2d.py`、完整许可和 SHA-256 来源记录位于 `licenses/gilbert`。本项目的 C# 排列实现参考此公开源代码，分发时保留原始版权、条件和免责文本。

- 上游：[jakubcerveny/gilbert 固定提交](https://github.com/jakubcerveny/gilbert/tree/9b080a74c5e3b6fe189785c52742f83ac85ba181)。
- 目标网站的行为参考不构成代码或素材授权；本项目没有分发其未授权的私有代码、素材或界面，也没有获得或声称获得其商业背书。

## 7-Zip 与归档工作进程

V0.7 继续使用未经修改的官方 7-Zip 26.04 Windows x64 完整 `7z.dll`，通过独立 `.NET` 工作进程动态调用。附带 `7z.exe` 可用于独立验证；不附带 WinRAR。RAR 仅解码与验证，不利用 unRAR 代码实现 RAR 创建。密码恢复工作进程扩展继续按 LGPL 2.1 或更高版本提供完整对应源码。

7-Zip Copyright (C) 1999–2026 Igor Pavlov。许可组合包括 LGPL 2.1 或更高版本、部分代码的 BSD 2/3 条款许可，以及 RAR 解码代码的 unRAR 限制。原始完整许可和版权文本位于 `licenses/7zip/License.txt`，LGPL 全文位于 `licenses/7zip/copying.txt`；同时保留工具目录中的原始许可。

- 官方二进制：[7z2604-x64.exe](https://github.com/ip7z/7zip/releases/download/26.04/7z2604-x64.exe)，SHA-256 `d54bf805f9f3704d1e8db2fa3498ae7ef2df0312b40b558e7c71c734430a665d`。
- 对应完整源码：[7z2604-src.tar.xz](https://github.com/ip7z/7zip/releases/download/26.04/7z2604-src.tar.xz)，SHA-256 `9691944c0fe0d01bb49373a704fb983fd33bc98b1738695179dfbf99ac1734f6`；随包位于 `licenses/7zip/7z2604-src.tar.xz`。
- 本包完整 DLL SHA-256：`899cd73d7fc60e1c1c35c7de0f5bed3dc69bfe2cecbd48014d868a347970a0b1`；来源记录位于 `licenses/7zip/provenance.json`。
- [官方商业应用 FAQ](https://www.7-zip.org/faq.html)、[官方许可](https://www.7-zip.org/license.txt)。

归档工作进程及其互操作层以 LGPL 2.1 或更高版本提供。完整对应源码、项目文件、构建说明和许可证随包位于 `licenses/archive-worker`，不依赖主应用源码即可重建。接口声明基于官方 7-Zip 接口；上游对应源码一并附带。主桌面应用通过进程通信调用工作进程。

V1.0 的归档临时文件归属辅助代码 `ArchiveTemporaryJournal.cs` 同样以 LGPL 2.1 或更高版本提供，同时编译入工作进程与应用基础设施程序集。对应源码保留在工作进程源码目录，并包含于本版本完整应用源码包。

用户可以在设置中选择兼容的完整 x64 `7z.dll`，也可以修改并重建工作进程。对这些 LGPL 组件的修改、替换及为调试修改而进行的逆向工程，不受本应用其他条款限制。替换后需自行验证格式兼容和许可证。开源许可合规并不构成对所有使用场景的零版权风险承诺。

开发验收中的 RAR4/RAR5 样本来自 SharpCompress 0.50.4，保留其 MIT 许可和来源记录；样本仅进入验收工具，不进入正式用户包。测试没有执行样本中的程序文件。

V0.6 新增的恢复验收样本由本项目使用原创文本及确定性测试数据生成，来源和校验值在验收工具的 `fixtures/recovery/provenance.json` 中记录。RAR 样本使用开发机本地 RAR 工具生成，用户包不分发 RAR/WinRAR 程序。内置数字模式由本项目原创规则生成，不使用外部密码库或泄露数据；规则版本与生成校验记录见 `shared/recovery-patterns-provenance.json`。

## .NET 与 WPF

新版 Windows EXE 使用 .NET 10 桌面运行环境（包含 WPF）。用户便携包采用自包含发布，附带运行该程序所需的运行环境；开发 SDK 仅用于构建，不进入用户包。

随自包含发布提供的真实运行环境包 `Microsoft.NETCore.App.Runtime.win-x64` 和 `Microsoft.WindowsDesktop.App.Runtime.win-x64` 10.0.12 的 nuspec 均声明 MIT 许可与源提交 `95017c711e6afc1085133d440e42b4bd78155701`。同包 MIT 原始文本、Core 第三方声明、nuspec 和哈希保存在 `licenses/dotnet`；SDK 分发原文单独标注为 SDK 材料，不能取代实际运行库许可。

- 运行环境源码：[dotnet/runtime](https://github.com/dotnet/runtime)
- WPF 源码：[dotnet/wpf](https://github.com/dotnet/wpf)
- Windows 桌面运行环境发布：[.NET 下载与支持](https://dotnet.microsoft.com/download/dotnet/10.0)

猫咪素材由用户提供，用户说明其为 GPT 生成的自家猫咪形象；本项目没有引入未授权的外部猫咪素材库。应用界面由本项目开发，本应用没有添加第三方 NuGet 依赖。
