from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=250)
    slug=models.CharField(max_length=250)
    img=models.ImageField(upload_to='product')

    
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])
    
    def __str__(self):
        return'{}'.format(self.name)
    
class products(models.Model):
    name=models.CharField(max_length=250)
    slug=models.CharField(max_length=250)
    img1=models.ImageField(upload_to='product')
    img2=models.ImageField(upload_to='product')
    img3=models.ImageField(upload_to='product')
    img4=models.ImageField(upload_to='product')
    desc=models.TextField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)
    ytlink=models.CharField(max_length=1000,)
    loc=models.CharField(max_length=250,default="location")

    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])
    def __str__(self):
        return'{}'.format(self.name)

