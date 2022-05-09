from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Category {self.name}, slug {self.slug}'


class Genre(models.Model):
    name = models.CharField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Genre {self.name}, slug {self.slug}'


class Title(models.Model):
    name = models.CharField()
    year = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='titles'
    )
    # ManyToManyField - думаю тут так нужно разные жанры к разным произведениям
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name='titles'
    )

    # в POST запросе в Response есть поле "rating", нужно учесть в модели.
    def __str__(self):
        return f'Title {self.name}, genre {self.genre}, {self.year}'


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение.',
    )
    text = models.CharField(max_length=1000)
    score = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(1),
            MinValueValidator(10)
        ],
        verbose_name='Оценка.',
    )

    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации',
    )

    def __str__(self):
        return f'Reviews(id={self.pk}, text ={self.text})'


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Произведение',
    )

    review = models.ForeignKey(
        Review, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Ревью',
    )
    text = models.TextField(
        max_length=1000,
        verbose_name='Текст комментария',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )

    def __str__(self):
        return f'Comment(pk={self.pk}, author={self.author}, text={self.text})'
