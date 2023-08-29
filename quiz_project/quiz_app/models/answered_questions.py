from django.contrib.auth.models import User
from django.db import models

from quiz_app.models.questions import Questions


class Answered_Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    submitted_answer = models.CharField(max_length=255)
    score = models.FloatField()
