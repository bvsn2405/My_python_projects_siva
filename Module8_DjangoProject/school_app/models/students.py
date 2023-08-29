from django.db import models
from django.contrib.auth.models import User
from school_app.models.base_model import BaseModel

class Students(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    guardian = models.CharField(max_length=255)
    relation = models.CharField(max_length=100)
    


