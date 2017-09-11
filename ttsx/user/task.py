from django.conf import settings
from django.core.mail import send_mail
from celery import task

@task
def send(request):
    uemail = request.session['email']
    msg = '<a href="http://127.0.0.1:8000/user/active/" target="_blank">点击激活</a>'
    send_mail('注册激活', '', settings.EMAIL_FROM,
              [uemail], html_message=msg)

