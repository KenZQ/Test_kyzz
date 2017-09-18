from django.conf import settings
from django.core.mail import send_mail
from celery import task

@task
def send(id, uemail,yzm):
    msg = '<a href="http://127.0.0.1:8000/user/active%s/?yzm=%s" target="_blank">点击激活</a>'%(id,yzm)
    send_mail('注册激活', '', settings.EMAIL_FROM,
              [uemail], html_message=msg)

@task
def reset(id, uemail,yzm):
    msg = '<a href="http://127.0.0.1:8000/user/reset_page%s/?yzm=%s" target="_blank">点击重置密码</a>'%(id,yzm)
    send_mail('重置密码', '', settings.EMAIL_FROM,
              [uemail], html_message=msg)

