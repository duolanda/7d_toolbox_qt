# 7D_Toolbox_Qt
使用 Python Qt 编写的 FFmpeg GUI，方便个人在 Mac 上使用。可能会部分参考[小丸工具箱](https://maruko.appinn.me/index.html)。

## 设计理念
目标是以最快的速度实现最基本、最常用的功能。像是处理进度显示、后缀名错误检查这样的功能不打算做，Python 只是为了跨平台的 GUI，实际上执行都是调用 ffmpeg 命令行，所以在其他电脑执行时有可能会遇到 ffmpeg 版本不同引起的兼容问题。Qt 在美观度上着实欠佳，不排除后续转用 electron 的可能性（对，这就是为什么不打算深入开发，因为可能会换技术栈，也可能大概率弃坑）。

为了更好地解耦，界面部分集中在 `.ui` 文件转换而来的 `mainwindow_ui.py`；逻辑部分集中在 `toolbox_wrapper.py`；程序入口为 `main.py`，它将作为桥梁继承 `Ui_MainWindow` 类，获取各组件的属性（如输入框中的文件地址）并调用 `ToolboxWrapper` 类中的函数完成处理。

## 部署
目前第三方库只需要安装 PySide6。
```
pip install pyside6
```
请提前将 ffmpeg 添加至系统环境变量，可通过以下命令检查
```
ffmpeg -version
```


## 预期实现功能
- [x] 音频、视频混流成一个视频
- [x] mkv、flv 转封装
- [ ] 视频拼接
- [ ] 音频拼接
- [ ] 视情况从小丸工具箱移植？

## 待修复 Bug
- [ ] 如果遇到重名文件，ffmpeg 会提示是否覆盖，卡住 GUI