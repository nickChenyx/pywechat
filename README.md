# PyWechat

> PyWechat helps you connect to wechat development fastly.

**PyWechat** use `flask` & `requests` to build micro-service.  

## Quick Start

```shell
cd www/utils
vim token_helper.py
```

- configure your special info

```python
'''Enter your appid and appsecret, token_helper will help refresh token and save.'''
def get_token():
    appid = 'xxxxxxxxxxx'  # Input your appid
    appsecret = 'xxxxxxxxxxxxxxx'  # Input your appsecret
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential\
    ....
```

- Now, just have fun!!!

```shell
cd ..
python index.py
```

- Already feature:
  - if service has received text message:"你好", then push "you too" back.