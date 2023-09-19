import time

from huggingface_hub import snapshot_download

repo_id = "THUDM/chatglm2-6b"
local_dir = '/Users/Leego/Projects/Python/models/THUDM'
cache_dir = local_dir + "/cache"
while True:
    try:
        snapshot_download(
            cache_dir=cache_dir,
            local_dir=local_dir,
            repo_id=repo_id,
            local_dir_use_symlinks=False,
            resume_download=True,
            allow_patterns=["*.model", "*.json", "*.bin", "*.py", "*.md", "*.txt"],
            ignore_patterns=["*.safetensors", "*.msgpack", "*.h5", "*.ot", ],
        )
    except Exception as e:
        print(e)
        time.sleep(1)
    else:
        print('下载完成')
        break
