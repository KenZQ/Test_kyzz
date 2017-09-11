from django.db import models

<<<<<<< HEAD
=======
# Create your models here.


from django.db import models

>>>>>>> eb56ee4ff6af628628001f5376ec6db14738889d
class UserInfo(models.Model):
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=40)
    uemail=models.CharField(max_length=30)
    isValid=models.BooleanField(default=True)
    isActive=models.BooleanField(default=False)

class UserAddressInfo(models.Model):
    uname=models.CharField(max_length=20)
    uaddress=models.CharField(max_length=100)
    uphone=models.CharField(max_length=11)
<<<<<<< HEAD
    user=models.ForeignKey('UserInfo')
=======
    user=models.ForeignKey('UserInfo')
>>>>>>> eb56ee4ff6af628628001f5376ec6db14738889d
