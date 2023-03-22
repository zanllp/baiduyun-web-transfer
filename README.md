# baiduyun-web-transfer


本项目是对 https://github.com/zanllp/stable-diffusion-webui-baidu-netdisk 的简单包装，裹了一层。

功能基本一致只是缺了获取一些快捷文件夹的方式而已，但是可以单独跑起来不需要stable-diffusion-webui。具体readme可以直接参考他的



# 安装

```bash
git clone git@github.com:zanllp/baiduyun-web-transfer.git --recursive
cd baiduyun-web-transfer
python -m venv venv #可选，推荐
source venv/bin/activate #可选，推荐
pip install -r requirements.txt
uvicorn app:app #然后打开网页操作
```
# 有什么用
当我们需要在没有可视化桌面的地方使用百度云盘时，这个项目可以作为一个将百度云盘作为存储转储工具的选择。该项目提供了一个Web UI，通过隧道方式（我习惯 vscode remote）可以在本地访问，支持查看本地和百度云盘中的文件结构，并支持使用拖放操作在本地和云盘之间上传和下载文件。

这个项目可以在任何地方使用，只需要一个Web浏览器即可。因此，它非常适合在云服务器、Colab、JupyterLab ~~wsl~~ 等没有可视化桌面的地方使用。
