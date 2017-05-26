# -*- encoding=utf-8 -*-
from flask import Flask, request
import fruit.fruit as fruit
import hashlib
import requests
import time
from datetime import datetime
import utils.token_helper as th
import xml.etree.ElementTree as ET
from model.wechat_msg import *
import sys
import io
import model.Wechat_BackMsg as t_backmsg
'''
Flask App , Running for Wechat.
* hold connect between wechat and service
* accept msg from user(mark by openID)
* feedback for user's seed.

// TODO
* Event Post handle.
* Custon Menu.

@date:2017/5/24
@author:nickChen
'''

app = Flask(__name__)

access_token = ''


@app.route('/', methods=['GET'])
def wechat_signature():
    timestamp = request.args.get('timestamp')
    if(timestamp):
        nonce = request.args.get('nonce')
        global access_token
        token = access_token
        list = [timestamp, nonce, token]
        dictionary_sorted_list = sorted(list)
        sha1_str = hashlib.sha1(''.join(dictionary_sorted_list).encode())
        print("===>")
        print(sha1_str.hexdigest(), "\n\n", request.args.get('signature'))
        print("<===")
        if(sha1_str.hexdigest() == request.args.get('signature')):
            print('sha1 equal...')
            return request.args.get('echostr')
    return 'hello,world!'


@app.route('/', methods=['POST'])
def receive():
    msg = WechatMsg(request.data)
    printmsg(msg)
    if msg.msgType == 'text':
        if msg.content == '你好':
            print('正在回复...')
            string = t_backmsg.text(msg, 'you too')
            print('回复内容', string)
            return string
        elif fruit.istimetohandlemsg(msg.content):
            print('正在回复...')
            fruitlist = fruit.listfruitbymonth(msg.content)
            print('fruitlist',fruitlist)
            backmsg = ' | '.join(fruitlist)
            string = t_backmsg.text(msg, backmsg)
            print('回复内容', string)
            return string
    return 'success'


def printmsg(msg):
    t = msg.msgType
    if t == 'text':
        print('收到了消息', msg.content)
    elif t == 'image':
        print('收到了图片', msg.picUrl)
    elif t == 'voice':
        print('收到了语音', msg.format)
    elif t == 'video' or t == 'shortvideo':
        print('收到了 ', t)
    elif t == 'location':
        print('收到了地理位置', msg.location_X, msg.location_Y,
              msg.scale, ' >', msg.label)
    elif t == 'link':
        print('收到了链接 【', msg.title, '】', msg.description, msg.url)
    else:
        print('Oops,WTF???')


if __name__ == '__main__':
    access_token = th.get()
    app.debug = True
    app.run(host='0.0.0.0', port=80)
