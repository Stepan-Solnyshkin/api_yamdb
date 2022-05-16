from datetime import date

from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Title, Review
from users.models import User


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')

    def create(self, validated_data):
        genre = Genre.objects.create(**validated_data)
        return genre


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, required=False)
    genre = GenreSerializer(many=True, required=False)
    rating = serializers.IntegerField()

    class Meta:
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category')
        read_only_fields = ('genre', 'category', 'rating')
        model = Title


class TitleCreateSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(many=True, write_only=True,
                                         slug_field='slug', required=False,
                                         queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(many=False, write_only=True,
                                            slug_field='slug', required=False,
                                            queryset=Category.objects.all())

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')

    def validate_year(self, value):
        if not 0 < value < date.today().year:
            raise serializers.ValidationError(
                'Нельзя добавлять произведения, которые еще не вышли!'
            )
        return value


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Review

        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=['title', 'user'],
                message='Уже оставлен отзыв произведение.'
            )
        ]


class TokenSerializer(serializers.ModelSerializer):
    confirmation_code = serializers.CharField(allow_blank=False)
    username = serializers.CharField(max_length=150, allow_blank=False)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name',
                  'last_name', 'bio', 'role')


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username')
