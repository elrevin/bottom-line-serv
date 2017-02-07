from django.db import models


class Member (models.Model):
    qr_code = models.CharField(max_length=256, default='', null=True)
