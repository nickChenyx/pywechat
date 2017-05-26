# -*- coding: utf-8 -*-
"""
提醒水果应季，及预报
"""
import requests
import yaml
import sys
import os
import re


path = os.path.dirname(__file__)
detailpath = path + '/detail.yml'
coresponsepath = path + '/co.yml'


def readyaml(filepath):
    try:
        ymldict = {}
        with open(filepath, 'r') as f:
            ymldict = yaml.load(f)
        return ymldict
    except Exception as ex:
        print(ex)
        return "YAML file:{} read error!".format(filepath)


def listfruitbymonth(month):
    fruitdict = readyaml(detailpath)
    if month in fruitdict:
        return fruitdict[month]
    return None

def istimetohandlemsg(string):
    pattern = re.compile('([1-9]|1[0-2]+)月')
    match = pattern.match(string)
    if match:
        print(match.group(),' macth! It\'s time to back fruit msg.')
        return True
    else:
        return False

if __name__ == "__main__":
    print(listfruitbymonth("1月"))
    istimetohandlemsg("1月")
    istimetohandlemsg("0月")
    istimetohandlemsg("12月")
    istimetohandlemsg("13月")
    istimetohandlemsg("1d月")
    istimetohandlemsg("-1月")
    istimetohandlemsg("月")

