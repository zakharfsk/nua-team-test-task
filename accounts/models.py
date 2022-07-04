from django.db import models

# Create your models here.


class UserModel(models.Model):
    username = models.CharField(max_length=255, unique=True)
    user_id = models.BigIntegerField(blank=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    user_json = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Інформація про користувача'
        verbose_name_plural = 'Інформація про користувача'
        ordering = ('-created_at',)
