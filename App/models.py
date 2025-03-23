from django.db import models
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator, EmailValidator
from django.forms import CharField

class User(models.Model):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message='Username may contain only letters, numbers, and @/./+/-/_ characters.'
            ),
            MinLengthValidator(3)
        ]
    )
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator(message='Enter a valid email address.')]
    )
    password = models.CharField(
        max_length=128,
        validators=[MinLengthValidator(8)]
    )

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Tag(models.Model):
    name = models.CharField(
        max_length=40, 
        verbose_name='Название тэга', 
        null=True,
        validators=[MinLengthValidator(1)]
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

class Article(models.Model):
    title = models.CharField(
        max_length=256, 
        verbose_name='Название',
        validators=[MinLengthValidator(1)]
    )
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    mainTag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='mainTag', verbose_name='Основной тэг')
    tags = models.ManyToManyField(Tag, related_name='article')
    author = models.IntegerField(null=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'




