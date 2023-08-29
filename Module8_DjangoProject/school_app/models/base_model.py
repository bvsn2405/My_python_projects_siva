from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class BaseModel(models.Model):
    created_on = models.DateTimeField(default=datetime.now())
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
