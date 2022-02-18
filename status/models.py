from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
import string
import random
def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Status.objects.filter(code=code).count() == 0:
            break

    return code


class Status(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='name')
    post = models.CharField(null=True, blank=True,max_length=2000)
    code = models.CharField(
        max_length=8, default=generate_unique_code, unique=True)
    image = models.ImageField(blank=True, null=True, max_length=2000)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.user.code)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.code
