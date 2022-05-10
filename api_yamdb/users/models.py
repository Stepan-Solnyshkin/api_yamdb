from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLES = (
        (ADMIN, 'Администратор'),
        (USER, 'Аутентифицированный пользователь'),
        (MODERATOR, 'Модератор'),
    )

    role = models.CharField(
        'Роль',
        max_length=20,
        choices=ROLES,
        default='user'
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
