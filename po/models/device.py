from django.db import models

from po.models.member import Member


class Device (models.Model):
    token = models.CharField(max_length=64, default="", null=False)
    uuid = models.CharField(max_length=64, default="", null=False,)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, default=None)
    model = models.CharField(max_length=256, default="", null=True)

    class Meta:
        unique_together = (("token", "uuid"),)
