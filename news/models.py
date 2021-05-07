from django.db import models

from categories.models import CategoryModel


class NewsModel(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='news', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
