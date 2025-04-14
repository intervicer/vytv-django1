from django.contrib import admin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category", "slug")
    prepopulated_fields = {"slug": ("category",)}
    fieldsets = (
        ("", {
            "fields": ("category", "slug"),
        }),
    )

admin.site.register(Category, CategoryAdmin)


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fieldsets = (
        ("", {
            "fields": ("title", "image",),
        }),
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date", "slug", "main_page", "category")
    inlines = [ArticleImageInline]
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        ("", {
            "fields": ("pub_date", "title", "description", "main_page", "category"), # Переконалися, що 'category' є
        }),
        (("Додатково",), {
            "classes": ("grp-collapse grp-closed",),
            "fields": ("slug",),
        }),
    )

    def delete_file(self, pk, request):
        """Delete an image."""
        obj = get_object_or_404(ArticleImage, pk=pk)
        return obj.delete()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.category:
            url = reverse('articles-categories-list', kwargs={'slug': obj.category.slug})
            return redirect(url)

admin.site.register(Article, ArticleAdmin)
