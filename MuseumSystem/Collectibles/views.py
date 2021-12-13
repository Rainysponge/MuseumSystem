import json
import logging

from django.http import HttpResponse
from django.shortcuts import render

from user.utils import userIsLogin
from .models import collectible, device, monitorLimit


# Create your views here.

def addCollectible(request):
    isLogin, userPk = userIsLogin()
    if not isLogin:
        rsp = {
            "rsp": "1",
            "message": "用户未登录",
        }
        return HttpResponse(json.dumps(rsp), content_type='application/json')
    # 用户已经登陆
    if request.method == "POST":
        info = json.loads(request.body)
        name = info['name']
        # pic
        time = info['time']
        category = info['category']
        location = info['location']
        content = info['content']
        deviceId = info['deviceId']
        loves = 0

        collectibleList = collectible.objects.filter(name=name)
        device = monitorLimit.objects.filter(deviceId=deviceId)
        if len(collectibleList) > 0:
            rsp = {
                "rsp": "2",
                "message": "藏品已经被录入",
                "collectible": name,
            }
            return HttpResponse(json.dumps(rsp), content_type='application/json')
        try:
            c = collectible.objects.create(name=name, time=time, category=category,
                                           location=location, content=content, loves=loves)

            c.save()
        except Exception as e:
            rsp = {
                "rsp": "3",
                "message": str(3),
                "collectible": name,
            }
            return HttpResponse(json.dumps(rsp), content_type='application/json')

        rsp = {
            "rsp": "0",
            "message": "藏品录入成功",
            "collectible": c.name,
        }
        return HttpResponse(json.dumps(rsp), content_type='application/json')
