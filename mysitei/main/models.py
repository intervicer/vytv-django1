from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    category = models.CharField("Категорія", max_length=250, help_text="Максимум 250 символів")
    slug = models.SlugField("Слаг")
    objects = models.Manager()


    class Meta:
        verbose_name = 'Категорія для публікації'
        verbose_name_plural = 'Категорії для публікацій'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        try:
            url = reverse('articles-categories-list', kwargs={"slug": self.slug})
            return url
        except:
            url = "/admin/"
        return url



class Article(models.Model):
    title = models.CharField("Заголовок", max_length=250, help_text="Максимум 250 символів")
    description = models.TextField(blank=True, verbose_name="Опис")
    pub_date = models.DateTimeField("Дата публікації", default=timezone.now)
    slug = models.SlugField("Слаг", unique_for_date="pub_date")
    main_page = models.BooleanField("Головна", default=False, help_text="Показувати")
    category = models.ForeignKey(Category, related_name='news', blank=True,
                                 null=True, verbose_name=u'Категорія', on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Публікація"
        verbose_name_plural = "Публікації"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            url = reverse("news-detail", kwargs={"year": self.pub_date.strftime("%Y"),
                                                 "month": self.pub_date.strftime("%m"),
                                                 "day": self.pub_date.strftime("%d"),
                                                 "slug": self.slug, })
        except:
            url = "/"
        return url


class ArticleImage(models.Model):
    image = models.ImageField('Фото', upload_to='photos')
    article = models.ForeignKey(Article, verbose_name='Стаття', related_name='images', on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=250, help_text='Максимум 250 сим.', blank=True)

    class Meta:
        verbose_name = "Фото для статті"
        verbose_name_plural = "Фото для статей"

    def __str__(self):
        return self.title

    def filename(self):
        return self.image.name.rsplit("/", 1)[-1]
