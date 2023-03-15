from django.db import models


class TimeStamp(models.Model):
    """
    This is custom timestamp model :
        For inheritance to all model
    """

    created = models.DateTimeField('created at', auto_now_add=True)
    updated = models.DateTimeField('updated at', auto_now=True)

    class Meta:
        abstract = True

