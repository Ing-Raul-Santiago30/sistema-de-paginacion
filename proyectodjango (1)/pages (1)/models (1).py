from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    order = models.IntegerField(default=0,verbose_name="orden")
    slug = models.CharField(unique= True, max_length=150, verbose_name="URL Amigable")
    visible = models.BooleanField(verbose_name="Visible")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado el ")

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural ="Paginas"

    def __str__(self):
        return self.title
        

