from django.db import models
from inoks.models.ProductCategory import ProductCategory


class Product(models.Model):
    productImage = models.ImageField(upload_to='product/', null=True, blank=True, verbose_name='Ürün Resmi')
    name = models.TextField(blank=True, null=True, verbose_name='Ürün Adı')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discountPrice = models.CharField(max_length=120, blank=True, null=True, verbose_name='İndirimli Fiyatı')
    stock = models.CharField(max_length=120, blank=True, null=True, verbose_name='Stok Adeti')
    category = models.ManyToManyField(ProductCategory)
    discountStartDate = models.DateField(null=True, verbose_name='İndirim Başlama Tarihi')
    discountFinishDate = models.DateField(null=True, verbose_name='İndirim Bitiş Tarihi')
    info = models.TextField(blank=True, null=True, verbose_name='Ürün Bilgileri')
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')

    def __str__(self):
        return '%s ' % self.name
