from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост в блоге'
        verbose_name_plural = 'Посты в блоге'
