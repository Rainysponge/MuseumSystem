import json
import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .utils import userIsLogin, userLogin


@csrf_exempt
def login(request):
    # print(request.user)

    # with open("./user.txt", 'r') as f:
    #     userPk = int(f.read())
    isLogin, userPk = userIsLogin()
    if isLogin:
        rsp = {
            "rsp": "2",
            "message": "用户已登陆",
            "userInfo": userPk,
        }
        return HttpResponse(json.dumps(rsp), content_type='application/json')
    if request.method == 'POST':
        info = json.loads(request.body)
        # print(info)
        # 格式，信息缺失交给前端判断
        userName = info['userName']
        password = info['password']

        user = auth.authenticate(username=userName, password=password)
        if user is None:
            rsp = {
                "rspCode": "1",
                "message": "用户密码或账号错误"
            }

        else:
            auth.login(request, user)
            rsp = {
                "rspCode": "0",
                "message": "登陆成功"
            }
            userLogin(user.pk)

        return HttpResponse(json.dumps(rsp), content_type='application/json')
        # json_result = json.loads(postBody)
        # print(json_result)
        # data = {
        #     'test1': 1,
        #     'test2': 2,s
        #     'test3': 3
        # }
    #     return HttpResponse(json.dumps(data), content_type='application/json')
    # else:
    #     return HttpResponse(json.dumps({"1": "2"}), content_type='application/json')


@csrf_exempt
def register(request):
    pass


@csrf_exempt
def logout(request):
    if request.method == 'POST':
        isLogin, userPk = userIsLogin()
        if isLogin:
            user = User.objects.filter(pk=userPk)[0]
            # print(user)
            rsp = {
                "rsp": "0",
                "message": "用户已登出",
                "userInfo": user.username,
            }
            auth.logout(request)
            userLogin(-1)
            return HttpResponse(json.dumps(rsp), content_type='application/json')

        rsp = {
            "rsp": "1",
            "message": "用户未登录",
            "userInfo": "",
        }
        return HttpResponse(json.dumps(rsp), content_type='application/json')
