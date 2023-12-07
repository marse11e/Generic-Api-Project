from django.db import models

class Contact(models.Model):
    name = models.CharField(
        max_length=122,
        verbose_name='Полное Имя',
        help_text='Введите полное имя контакта.'
    )
    email = models.EmailField(
        max_length=122,
        verbose_name='Адрес электронной почты',
        help_text='Введите адрес электронной почты контакта.'
    )
    phone = models.CharField(
        max_length=12,
        verbose_name='Номер телефона',
        help_text='Введите номер телефона контакта.'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание или дополнительную информацию о контакте.'
    )

    def __str__(self):
        return self.name
