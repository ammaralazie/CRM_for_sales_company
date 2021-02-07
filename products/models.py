from django.db import models
from django.utils.text import slugify
from .utils import slugid
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    PRDName=models.CharField(max_length=300,verbose_name="name of product")
    PRDName_ar=models.CharField(max_length=300,verbose_name="name of product in arabic")
    PRDPrice=models.DecimalField(default=0 , max_digits=5, decimal_places=2,verbose_name="The price in arabic")
    PRDPrice_ar=models.DecimalField(default=0 , max_digits=5, decimal_places=2,verbose_name="The price")
    PRDDiscription=models.TextField(verbose_name="Discribtion of product")
    PRDDiscription_ar=models.TextField(verbose_name="Discribtion of product in arabic")
    PRDIamge=models.ImageField(default='/none.jpeg',upload_to='media')
    
    CHOICES_TYPE=(('Carpets and meridians','Carpets and meridians'),('the games','the games'),('Electrical','Electrical'),('Mobile phones','Mobile phones'))
    CHOICES_TYPE_ar=(('سجادات و زوالي','سجادات و زوالي'),('الالعاب','الالعاب'),('الكهربائيات','الكهربائيات'),('الهواتف المحمولة','الهواتف المحمولة'))
   
    PRDType=models.CharField(max_length=90,choices=CHOICES_TYPE,verbose_name="Type of product")
    PRDType_ar=models.CharField(max_length=90,choices=CHOICES_TYPE_ar,verbose_name="Type of product in arabic")

    CHOICES_STATE=(('new','new'),('old','old'))
    CHOICES_STATE_ar=(('جديد','جديد'),('قديم','قديم'))

    PRDSate=models.CharField(choices=CHOICES_STATE,max_length=20,verbose_name="state of product ")
    PRDSate_ar=models.CharField(choices= CHOICES_STATE_ar,max_length=20 ,verbose_name="state of product in arabic")
    PRDDiscount=models.DecimalField(blank=True,null=True ,default=0 , max_digits=5, decimal_places=2,verbose_name="The Discount")
    PRDDiscount_ar=models.DecimalField(blank=True,null=True,default=0 , max_digits=5, decimal_places=2,verbose_name="The Discount in arabic")
    PRDSlug=models.SlugField(blank=True,null=True)


    def __str__(self):
        return str(self.PRDName)

    def save(self,*args,**kwargs):
        if not self.PRDSlug :
            self.PRDSlug=slugify(slugid)
        super(Product,self).save(*args,**kwargs)

#________________#

class Sort(models.Manager):
    def sort_by_date(self):
        return OrderItem.objects.order_by('date_add')

    def sort_by_name(self):
        return OrderItem.objects.order_by('customer')

    def sort_by_name(self):
        return OrderItem.objects.order_by('address.covernorate')


class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    date_add=models.DateTimeField(default=datetime.datetime.now)
    address=models.ForeignKey('Address',on_delete=models.CASCADE,null=True,blank=True)
    complate=models.CharField(null=True,blank=True, max_length=20)
    objects=Sort()
    def __str__(self):
        return str(self.customer)+ ' '+str(self.product)+' '+str(self.date_add)

    def totleprice(self):
        if self.product.PRDDiscount:
            totle=self.quantity * self.product.PRDDiscount
        else:
            totle=self.quantity * self.product.PRDPrice
        return totle

    def totalorders(self):
        x=self.complate.all().count()
        return x
   

#_____________________#

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

 #   COVERNORATE=(
 #       ('الأنبار','الأنبار'),('ديالى','ديالى'),('أربيل','أربيل'),('بابل','بابل'),('بغداد','بغداد'),('البصرة','البصرة'),('حلبجة','حلبجة'),('دهوك','دهوك'),('القادسية','القادسية'),('ذي قار','ذي قار'),('السليمانية','	السليمانية'),('صلاح الدين','صلاح الدين'),('كركوك','كركوك'),('كربلاء','كربلاء'),('المثنى','المثنى'),('ميسان','ميسان'),('النجف','النجف'),('نينوى','نينوى'),('واسط','واسط')
  #  )

    covernorate=models.CharField(default='بغداد',max_length=30)
    state=models.CharField(max_length=100)
    phone_number1=models.CharField(max_length=11)
    phone_number2=models.CharField(max_length=11)
    email=models.EmailField(blank=True ,null=True)
    date_add=models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.covernorate)+'  ' +str(self.state)+'  '+str(self.date_add)
