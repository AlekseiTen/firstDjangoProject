from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание категории", blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Категории'  # Настройка для наименования набора объектов
        ordering = ("name",)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description}'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание продукта", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="сategories", blank=True, null=True)
    photo = models.ImageField(upload_to="products/photo", blank=True, null=True, verbose_name="Изображение продукта")
    price = models.IntegerField(verbose_name="Цена", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Дата последнего изменения")


    class Meta:
        verbose_name = 'Продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Продукты'  # Настройка для наименования набора объектов
        ordering = ("name",)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.category} {self.price}'
