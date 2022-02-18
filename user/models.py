from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='name')
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=2000, null=False)

    def get_absolute_url(self):
        return reverse('user:profile', kwargs={'slug': self.slug})

    def get_absolute_url_detail(self):
        return reverse('user:profile_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username
