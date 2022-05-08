from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Category(id={self.pk}, name ={self.name})'


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Genre(id={self.pk}, name ={self.name})'


class Title(models.Model):
    name = models.CharField(max_length=50)
    year = models.DateField
    category = models.ForeignKey(
        Category, related_name='title'
    )

    def __str__(self):
        return f'Title(id={self.pk}, name ={self.name})'


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )
    text = models.CharField(max_length=1000)
    score = models.IntegerField()

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return f'Reviews(id={self.pk}, text ={self.text})'


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='comments'
    )

    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )

    def __str__(self):
        return f'Comment(pk={self.pk}, text={self.author}, group' \
               f'={self.text})'
