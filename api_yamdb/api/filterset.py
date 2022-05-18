import django_filters

from reviews.models import Title


class TitleFilter(django_filters.FilterSet):
    """Класс определяет, как фильтровать различные поля модели."""
    genre = django_filters.CharFilter(field_name='genre__slug')
    category = django_filters.CharFilter(field_name='category__slug')
    name = django_filters.CharFilter(field_name='name',
                                     lookup_expr='icontains')

    class Meta:
        model = Title
        fields = ('name', 'year')
