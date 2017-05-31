# -*-coding:utf-8-*-
import os
import requests
import datetime
import threading
'''
Quick start:
    import token_helper as th
       access_token = th.get() # Already get token

Get Wechat Access Token And Cache in two hours.

@date: 2017/5/24
@author: nickChen
'''
path = os.path.abspath(os.path.dirname(__file__))


def get_token():
    appid = 'wx1d2d32edd36367cc'
    appsecret = '536ac2c29e35f15225e84f7ff2b8ed2d'
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential\
&appid={0}&secret={1}'.format(appid, appsecret)
    # print('url: ',url)
    r = requests.get(url)
    if 'access_token' in r.json():
        # print('===> HOLDING ACCESS TOKEN:\n',r.json(),'<===')
        with open(path + '/wechat-token.tkn', 'w') as f:
            f.write(r.json()['access_token'])
        return r.json()['access_token']
    else:
        print(r.json())
        return None


def getlasttimefortoken():
    filename = 'last_time_for_get_token.time'
    if not os.path.exists(path + '/' + filename):
        os.system('touch %s' % (path + '/' + filename))
    with open(path + '/' + filename, 'r+') as f:
        string = f.readline()
        print('last time for get token:', string)
        if string == '':
            return None
        lasttime = datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    return lasttime


def setlasttimefortoken(time):
    with open(path + '/last_time_for_get_token.time', 'w') as f:
        f.write(time.strftime('%Y-%m-%d %H:%M:%S'))


def istimetogettoken():
    last_token_time = getlasttimefortoken()
    cache_time = 60 * 60 * 2 - 10
    if not last_token_time:
        setlasttimefortoken(datetime.datetime.now())
        return True
    if (datetime.datetime.now() - last_token_time).total_seconds() \
            > cache_time:
        setlasttimefortoken(datetime.datetime.now())
        return True
    return False


def readtokenfile():
    with open(path + '/wechat-token.tkn', 'r') as f:
        return f.readline()


def get():
    token = readtokenfile()
    if istimetogettoken():
        print('prepare to get token')
        token = get_token()
    return token


if __name__ == '__main__':
    print('access_token:', get())
