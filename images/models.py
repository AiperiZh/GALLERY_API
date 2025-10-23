from django.db import models


class ImageItem(models.Model):
    title = models.CharField(max_length=100,verbose_name="Заголовок" )
    description = models.TextField(blank=True, verbose_name="Описание")
    image_url = models.CharField(max_length=500, verbose_name="URL изображения")
    cloudinary_public_id = models.CharField(max_length=255, verbose_name="Public ID в облаке")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Галерея изображений"
        ordering = ["-uploaded_at"]
