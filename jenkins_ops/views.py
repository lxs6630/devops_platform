
# Create your views here.
from django.shortcuts import  render,HttpResponse,redirect
# from .apps import AppnameConfig
from jenkins_ops.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
import simplejson
import hashlib
from jenkins_ops.get_tomcat_log import *
from jenkins_ops.exec_jenkins import *
from django.middleware.csrf import get_token ,rotate_token
@require_http_methods(["GET",'POST'])
def auth_info(request):
    response = {}
    try:
        if  request.method=='POST':
            req = simplejson.loads(request.body)  # json格式传过来的数
            print(req['username'],req['password'])
            # Book.objects.create(
            #     **req
            # )
            # Book.objects.create(   #x-www-form-urlencoded传过来的数据
            #     **{"book_name":request.POST.get('book_name')},
            # )
            response['msg'] = 'success'
            response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
def encryption(str):
    sh = hashlib.md5()
    sh.update(str.encode())
    return sh.hexdigest()
def test(requset):
    passwd=encryption('123456')
    print(passwd)
    Userinfo.objects.create(
        **{'username':'xian','password':passwd}
    )
    return render(requset,'test.html')
@require_http_methods(["GET",'POST'])
def login(request):
    response = {}
    # v = request.session   #session保存在服务端
    # print(type(v))
    # from django.contrib.sessions.backends.db import SessionStore
    if request.method =='GET':
        get_token(request)
    if request.method == 'POST':
        req = simplejson.loads(request.body)  # json格式传过来的数
        user=req['username']
        pwd=req['password']
        flag = Userinfo.objects.filter(username=user, password=pwd).count()
        if flag:
            # request.session['is_login'] = True
            #request.session['username'] = user
            response['resp_code'] = '0000'
            response['username']=user
        else:
            response['msg'] = '用户名或者密码错误'
            response['resp_code'] = '1111'

    return JsonResponse(response)
@require_http_methods(["GET",'POST'])
def java_manage(request):
    response={}
    req=simplejson.loads(request.body)
    ip=req['ip']
    app=req['project']
    action=req['action']
    time.sleep(2)
    log=exec_cmd(ip, 'wlsadmin', 'Pass1234', 'cat /midware/easyops/data/%s/logs/%s.log' % (app,app))
    response['log']=log
    return  JsonResponse(response)
@require_http_methods(["GET",'POST'])
def jenkins_manage(request):
    response = {}
    req = simplejson.loads(request.body)
    app = req['project']
    action = req['action']
    obj=Run_jenkins('http://10.203.105.90:8500','admin','admin',app)
    build_info=obj.get_build_info()
    response['log']=build_info
    return JsonResponse(response)
def jenkins_get_jobs(requset):
    response = {}
    obj = Run_jenkins('http://10.203.105.90:8500', 'admin', 'admin', 'None')
    jobs=obj.job_list()
    response['jobs']=jobs
    return JsonResponse(response)