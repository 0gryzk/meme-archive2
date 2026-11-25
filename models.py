from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']


class Meme(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название мема")
    year = models.PositiveIntegerField(verbose_name="Год появления")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='memes',
        verbose_name="Категория"
    )
    description = models.TextField(verbose_name="Описание мема")
    image = models.ImageField(
        upload_to='memes/images/',
        blank=True,
        null=True,
        verbose_name="Фото"
    )
    video = models.FileField(
        upload_to='memes/videos/',
        blank=True,
        null=True,
        verbose_name="Видео (MP4)"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        verbose_name = "Мем"
        verbose_name_plural = "Мемы"
        ordering = ['-created_at']