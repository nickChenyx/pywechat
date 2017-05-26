# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
'''
Common Wechat Normal Message Model.

@date:2017/5/24
@author:nickChen
'''


class WechatMsg():
    def __init__(self, data):
        self.fromUser = ''
        self.toUser = ''
        self.createTime = ''
        self.msgType = ''
        self.content = ''    # text msg only
        self.picUrl = ''     # pic msg only
        self.mediaId = ''    # pic & voice msg
        self.format = ''     # voice msg only
        self.recognition = ''     # voice msg onlys
        self.thumbMediaId = ''    # video msg only
        self.location_X = ''      # location msg only
        self.location_Y = ''      # location msg only
        self.scale = ''      # location msg only
        self.label = ''      # locaiton msg only
        self.title = ''      # link msg only
        self.description = ''     # link msg only
        self.url = ''        # link msg only
        self.msgId = ''
        self.init(data)

    def init(self, data):
        root = ET.fromstring(data)
        self.fromUser = root.findtext(".//FromUserName")
        self.toUser = root.findtext(".//ToUserName")
        self.createTime = root.findtext(".//CreateTime")
        self.msgType = root.findtext(".//MsgType")
        self.content = root.findtext(".//Content")
        self.picUrl = root.findtext(".//PicUrl")
        self.mediaId = root.findtext(".//MediaId")
        self.format = root.findtext(".//Format")
        self.recognition = root.findtext(".//Recognition")
        self.thumbMediaId = root.findtext(".//ThumbMediaId")
        self.location_X = root.findtext(".//Location_X")
        self.location_Y = root.findtext(".//Location_Y")
        self.scale = root.findtext(".//Scale")
        self.label = root.findtext(".//Label")
        self.title = root.findtext(".//Title")
        self.description = root.findtext(".//Description")
        self.url = root.findtext(".//Url")
        self.msgId = root.findtext(".//MsgId")
