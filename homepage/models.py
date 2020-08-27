from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from custom_user.models import MyUser
# Create your models here.


class Ticket(models.Model):
    N = 'N'
    InP = 'INP'
    D = 'D'
    Invalid = 'INV'
    status_choices = [
        (N, 'New'), (InP, 'In Progess'), (D, "Done"), (Invalid, 'Invalid')
    ]

    title = models.CharField(max_length=80)
    filed_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    user_filed = models.ForeignKey(MyUser, related_name='user_filed', on_delete=models.CASCADE)
    ticket_status = models.CharField(max_length=3, choices=status_choices, default=N)
    user_assigned = models.ForeignKey(MyUser, related_name='user_assigned', on_delete=models.CASCADE)
    user_completed = models.ForeignKey(MyUser, related_name='user_completed', on_delete=models.CASCADE)

    def __str__(self):
        return self.description
