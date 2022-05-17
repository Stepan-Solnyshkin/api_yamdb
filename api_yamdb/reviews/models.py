from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=50, unique=True,)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'Category {self.name}, slug {self.slug}'


class Genre(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=50, unique=True,)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'Genre {self.name}, slug {self.slug}'


class Title(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(date.today().year)])
    description = models.TextField()
    category = models.ForeignKey(
        Category, blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='titles'
    )
    genre = models.ManyToManyField(Genre, through='GenreTitle')

    class Meta:
        ordering = ('category', 'name')

    def __str__(self):
        return f'Title {self.name}, genre {self.genre}, {self.year}'


class GenreTitle(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'genre'],
                name='unique_genre_for_a_title'
            )
        ]

    def __str__(self):
        return f'GenreTitle {self.pk}, title {self.title},' \
               f'genre {self.genre}.'


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
    )
    text = models.CharField(max_length=1000)
    score = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
        verbose_name='Оценка',
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )

    class Meta:
        ordering = ('title',)
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            ),
        ]

    def __str__(self):
        return f'Reviews(id={self.pk}, text ={self.text})'


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    review = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments')
    text = models.TextField(
        max_length=1000,
        verbose_name='Текст комментария',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )

    class Meta:
        ordering = ('review', 'author')

    def __str__(self):
        return f'Comment(pk={self.pk}, author={self.author}, text={self.text})'
