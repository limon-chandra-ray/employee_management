# from django.db import models
# from django.contrib.auth.hashers import make_password, check_password
# class CustomUser(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128)

#     def __str__(self):
#         return self.username
    
#     # Override save to hash password when creating or updating a user
#     def save(self, *args, **kwargs):
#         self.password = make_password(self.password)  # Hash the password
#         super().save(*args, **kwargs)