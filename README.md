#### 拉库命令
```
ql repo https://github.com/Ubugs/MyScript.git "tg_" "" "ql_"
```
互助池自动上车需要在脚本同目录下添加以下文件

tg_config.py
```
api_id = 123456
api_hash = 'xxxx'
proxy = {
    'proxy_type': 'socks5',
    'addr': '127.0.0.1',
    'port': 18899,
    'username': 'user', #可选
    'password': 'pwd' #可选
}
```