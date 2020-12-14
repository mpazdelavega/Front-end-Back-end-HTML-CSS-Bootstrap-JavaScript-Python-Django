from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField( max_length=50,verbose_name ="Titulo")
    description = models.TextField(verbose_name ="Descripción ")
    image = models.ImageField(verbose_name ="Imagen",upload_to="projects")
    link = models.URLField(verbose_name= "Direccion Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name ="Fecha Creación")
    update = models.DateTimeField(auto_now=True,verbose_name ="Fecha Ultima Actualización")
    
    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['title']

    def __str__(self):
        return self.title