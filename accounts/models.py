from django.db import models

# why made this database when you have nothing new field to add????!!!! @batti tauke... why not use django user model???
class Login(models.Model):
    user_name = models.CharField(max_length=20)
    hash_password = models.TextField()
