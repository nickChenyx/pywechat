# -*- encoding=utf-8 -*-
import time

'''
Wechat Back Msg template.

@date:2017/5/24
@author:nickChen
'''


def text(receivedmsg, text):
    back_msg = """
<xml>
<ToUserName><![CDATA[{0}]]></ToUserName>
<FromUserName><![CDATA[{1}]]></FromUserName>
<CreateTime>{2}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{3}]]></Content>
</xml>
"""
    ntime = int(time.time())
    string = back_msg.format(receivedmsg.fromUser,
                             receivedmsg.toUser, ntime, text)
    return string
