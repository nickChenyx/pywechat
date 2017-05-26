# -*- coding:utf-8 -*-
import token_helper as th
import requests
import simplejson
import sys
sys.path.append('../utils/')
'''
try to set custom menu

@date:2017/5/24
@author:nickChen
'''
token = th.get()


def post():
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?\
    access_token={}".format(token)
    print(url)
    msg = """
 {
     "button":[
     {
          "type":"click",
          "name":"Today-Music",
          "key":"V1001_TODAY_MUSIC"
      },
      {
           "name":"Menue",
           "sub_button":[
           {
               "type":"view",
               "name":"search",
               "url":"http://www.soso.com/"
            },
            {
                 "type":"miniprogram",
                 "name":"wxa",
                 "url":"http://mp.weixin.qq.com",
                 "appid":"wx286b93c14bbf93aa",
                 "pagepath":"pages/lunar/index.html"
             },
            {
               "type":"click",
               "name":"bingo~",
               "key":"V1001_GOOD"
            }]
       }]
 }
"""
    jsonmsg = simplejson.loads(msg)
    r = requests.post(url, data=simplejson.dumps(jsonmsg))
    print(r.text)


if __name__ == '__main__':
    post()
