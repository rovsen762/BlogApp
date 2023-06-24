from django.db import models


class PageVisit(models.Model):
    user_ip = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    page = models.CharField(max_length=255)

    def __str__(self):
        return self.page