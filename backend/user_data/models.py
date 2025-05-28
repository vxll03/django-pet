from django.db import models

class UserProfile(models.Model):
    def __str__(self) -> str:
        return self.user.username
    
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name='profile')

    