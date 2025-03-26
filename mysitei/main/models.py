from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category = models.CharField("Category", max_length=250,)
    slug = models.SlugField("Slug")

    class Meta:
        verbose_name = "Category for publication"
        verbose_name_plural = "Category for publication"

    def __str__(self):
        return self.category


class Article(models.Model):
    title = models.CharField("Title", max_length=250)
    description = models.TextField(blank=True, verbose_name="Text")
    pub_date = models.DateTimeField("Date of publication", default=timezone.now)
    slug = models.SlugField("Slug", unique_for_date="pub_date")
    main_page = models.BooleanField("Main", default=False, help_text="Show")
    category = models.ForeignKey(Category, related_name='news', blank=True, null=True, verbose_name="Category",
                                 on_delete=models.CASCADE)
    objects = models.Manager()

