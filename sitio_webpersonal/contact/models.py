from django.db import models

# Create your models here.

class Registrado(models.Model):
    name = models.CharField( max_length=50,verbose_name ="Nombre", null=True)
    email = models.CharField( max_length=50,verbose_name ="Email")
    content = models.TextField(max_length=50,verbose_name ="Descripción", null=True )

    class Meta:
        verbose_name="Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['-name']

    def __unicode__(self):
        return self.email
    
    def __str__(self):
        return self.email