from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    category = models.CharField(max_length=100, verbose_name="Categoria")
    dimensions = models.CharField(max_length=100, blank=True, null=True, verbose_name="Medidas")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    is_sold = models.BooleanField(default=False, verbose_name="Vendido")
    is_featured = models.BooleanField(default=False, verbose_name="Destaque")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Imagem")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['-is_featured', '-created_at']

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.email