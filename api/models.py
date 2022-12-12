from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,null=False,blank=False)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Batch(models.Model):
    _id = models.IntegerField(primary_key=True)
    batchtiming = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self) -> str:
        return f"{self.batchtiming}"


class BatchesInfo(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    batch  = models.ForeignKey(Batch,on_delete=models.CASCADE,)
    month  = models.CharField(max_length=100)
    class Meta:
        unique_together = (("person", "month"),)
    def __str__(self) -> str:
        return f"{self.person} {self.batch} {self.month}"
