from django.db import models
from django.urls import reverse


# Create your models here.
class MainCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Наименование основной категории")

    class Meta:
        verbose_name = 'Основная категория'
        verbose_name_plural = "Основные категории"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={'category_id': self.pk})


# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     maincategory = models.ForeignKey(MainCategory, on_delete=models.PROTECT, null=True) #related_name='sub'
#
#     def __str__(self):
#         return self.name


class Note(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="Наименование")  # Здесь verbose для наименования столбцов на русском
    content = models.TextField(verbose_name="Контент")
    photo = models.ImageField(upload_to='photo_work/%Y/%m/%d/', verbose_name="Фото", blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name="Создан")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    is_published = models.BooleanField(default="True", verbose_name="Публиковать?")
    category = models.ForeignKey(MainCategory, on_delete=models.PROTECT, null=True, related_name='sub', unique=False)

    title_en = models.CharField(max_length=255, blank=True)
    content_en = models.TextField(blank=True)
    password = models.CharField(max_length=8, blank=True)

    salt1 = models.TextField(verbose_name="Salt_контент", blank=True)
    nonce1 = models.TextField (verbose_name='nonce_контент', blank=True)
    tag1 = models.TextField(verbose_name='tag_контент', blank=True)

    salt2 = models.TextField(verbose_name="Salt_заголовок", blank=True)
    nonce2 = models.TextField (verbose_name='nonce_заголовок', blank=True)
    tag2 = models.TextField(verbose_name='tag_заголовок', blank=True)



    def get_absolute_url1(self):
        return reverse("onenote", kwargs={'note_id': self.pk})

    def get_absolute_url(self):
        return reverse("viewnote", kwargs={'note_id': self.pk})

    def __str__(self):
        return self.title



    # Поработаем с видом админки
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = "Заметки"
        ordering = ["-created_at"]
