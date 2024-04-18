from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todos(models.Model):# nov 21
    name=models.CharField(max_length=200)
    options=(
        ("todo","todo"),#  for backend,for frontend
        ("inprogress","inprogress"),
        ("completed","completed")
    )
    status=models.CharField(max_length=200,choices=options,default="todo")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    # namukku todomodelinu vendi oru database table venam athinu makemigrations,migrate cheyyanam