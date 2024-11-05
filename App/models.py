from django.db import models
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator, EmailValidator
from django.forms import CharField

class Notification(models.Model): 
    email = models.EmailField(
        validators=[
            EmailValidator(message="Введите действительный адрес электронной почты")
        ]
    )
    name = CharField(
        max_length=100,  
        validators=[
            MinLengthValidator(2, message="Имя должно содержать не менее 2 символов"),
            MaxLengthValidator(100, message="Имя должно содержать не более 100 символов")
        ]
    ) 
    tel = models.CharField(
        max_length=15,  
        validators=[
            RegexValidator(
                r'^\+?1?\d{9,15}$',
                message="Введите телефонный номер в формате +1234567890, максимум 15 цифр"
            )
        ]
    )
    massage = models.TextField(
        validators=[
            MaxLengthValidator(500, message="Сообщение должно содержать не более 500 символов")
        ]
    )


    