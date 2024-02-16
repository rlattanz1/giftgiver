from django.db import models

# Create your models here.
class Gift(models.Model):
    body = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.body
