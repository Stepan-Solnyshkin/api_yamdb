from django.contrib import admin
from .models import Genre, Review, Comment, Title, Category


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "year",
        "description",
        "genre",
    )

    list_editable = ("genre",)
    search_fields = ("description",)
    list_filter = ("year",)
    empty_value_display = "-пусто-"


admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(Category)
