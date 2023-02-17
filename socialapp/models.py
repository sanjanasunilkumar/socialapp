from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models import Count

class Posts(models.Model):
    post=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    like=models.ManyToManyField(User,related_name="like")


    @property
    def fetch_comments(self):
        return self.comments_set.all()


    def _str_(self):
        return self.post



class Comments(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    created_date=models.DateField(auto_now_add=True)

    def _str_(self):
        return self.comment


class Userprofile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="image",null=True)
    place=models.CharField(max_length=100)
    dob=models.CharField(max_length=50)
    phone=models.PositiveBigIntegerField()