import time

from huggingface_hub import snapshot_download

repo_id = "moka-ai/m3e-base"
local_dir = '/Users/Leego/Projects/Python/models/moka-ai/m3e-base'
cache_dir = local_dir + "/cache"
while True:
    try:
        snapshot_download(
            cache_dir=cache_dir,
            local_dir=local_dir,
            repo_id=repo_id,
            local_dir_use_symlinks=False,
            resume_download=True,
            allow_patterns=["*.safetensors"],
            ignore_patterns=["*.msgpack", "*.h5", "*.ot", ],
        )
    except Exception as e:
        print(e)
        time.sleep(1)
    else:
        print('下载完成')
        break
