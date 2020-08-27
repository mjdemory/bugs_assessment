from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from custom_user.models import MyUser
# Create your models here.


class Ticket(models.Model):
    N = 'New'

    title = models.CharField(max_length=80)
    filed_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    user_filed = models.ForeignKey(MyUser, on_delete=models.CASCADE)
