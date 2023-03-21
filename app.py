
from fastapi import FastAPI
import os
import sys
from fastapi.responses import FileResponse
sys.path.append(os.path.join(os.path.dirname(__file__), 'external/baiduyun'))
from external.baiduyun.scripts.api import baidu_netdisk_api
from external.baiduyun.scripts.bin import check_bin_exists, download_bin_file, cwd as bd_cwd
if not check_bin_exists():
  download_bin_file()
app = FastAPI()
@app.get("/")
def index():
  return FileResponse(os.path.join(bd_cwd, "vue/dist/index.html"))
baidu_netdisk_api('', app)