from django.db import models


class USER(models.Model):
    login = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    def __str__(self):
        return f"login ={self.login}; name ={self.name}; age= {self.age}"


class TRANSACTION(models.Model):
    title = models.CharField(max_length=200)
    transaction = models.IntegerField()
    user = models.ForeignKey(USER, on_delete=models.CASCADE,related_name='transactions')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"title = {self.title}; transation={self.transaction}; user={self.user}"


