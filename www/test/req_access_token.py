# -*- encoding:utf-8 -*-
import requests
'''
This srcipt works to  getting ACCESS_TOKEN for wechat !
@author: nickChen
@time: 2017/5/22
'''
appid = 'wx1d2d32edd36367cc'
appsecret = '536ac2c29e35f15225e84f7ff2b8ed2d'
url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential\
       &appid={0}&secret={1}'.format(appid, appsecret)
print('url: ', url)
r = requests.get(url)
print(r.text)
