# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
#
#
# class CustomUser(AbstractUser):
#     # Дополнительные поля для пользовательской модели
#     bio = models.TextField(_('О себе'), blank=True)
#     date_of_birth = models.DateField(_('Дата рождения'), null=True, blank=True)
#     profile_picture = models.ImageField(_('Аватар'), upload_to='profile_pictures/', blank=True)
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         verbose_name = _('Пользователь')
#         verbose_name_plural = _('Пользователи')
