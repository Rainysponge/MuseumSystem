import json
import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    if request.method == 'POST':
        if request.user:
            rsp = {
                "rsp": "2",
                "message": "已经有一个用户登陆了"
            }
            return HttpResponse(json.dumps(rsp), content_type='application/json')
        concat = request.POST
        # print(concat)
        # 格式，信息缺失交给前端判断
        userName = concat['userName']
        password = concat['password']

        user = auth.authenticate(username=userName, password=password)
        if user is None:
            rsp = {
                "rspCode": "1",
                "message": "用户密码或账号错误"
            }

        else:
            rsp = {
                "rspCode": "0",
                "message": "登陆成功"
            }
            auth.login(request, user)
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
