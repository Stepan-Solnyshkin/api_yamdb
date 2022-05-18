from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Category(models.Model):
    """Модель для определения категории."""
    name = models.CharField(
        max_length=256, unique=True, verbose_name='название категории'
    )
    slug = models.SlugField(
        max_length=50, unique=True, verbose_name='slug категории'
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'Category {self.name}, slug {self.slug}'


class Genre(models.Model):
    """Модель для определения жанра."""
    name = models.CharField(
        max_length=150, unique=True, verbose_name='название жанра'
    )
    slug = models.SlugField(
        max_length=50, unique=True, verbose_name='slug жанра'
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'Genre {self.name}, slug {self.slug}'


class Title(models.Model):
    """Модель для определения произведений."""
    name = models.CharField(
        max_length=150, verbose_name='название произведения'
    )
    year = models.PositiveSmallIntegerField(
        db_index=True, validators=[MaxValueValidator(date.today().year)],
        verbose_name='год создания произведения'
    )
    description = models.TextField(
        blank=True, verbose_name='описание произведения'
    )
    category = models.ForeignKey(
        Category, blank=True, null=True,
        on_delete=models.SET_NULL,
        verbose_name='категория',
        related_name='titles'
    )
    genre = models.ManyToManyField(
        Genre, through='GenreTitle',
        blank=True, verbose_name='жанр'
    )

    class Meta:
        ordering = ('category', 'name')

    def __str__(self):
        return f'Title {self.name}, genre {self.genre}, {self.year}'


class GenreTitle(models.Model):
    """Модель создания связи между произведениями и их жанрами."""
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
    """Модель для определения рецензии."""
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
    """Модель для определения комментария."""
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
