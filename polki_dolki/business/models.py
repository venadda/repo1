from django.db import models
from django.contrib.auth.models import User
from datetime import date,datetime
from django.utils import timezone
# Create your models here.
class Vendor(models.Model):

    id = models.PositiveIntegerField(primary_key=True,help_text='unique Id auto generates')
    first_name = models.CharField( blank=False, max_length=20, null=False,verbose_name='First Name',help_text='Vendor First Name')
    middle_name = models.CharField( blank=True, max_length=20, null=True,verbose_name='Middle Name',help_text='Vendor MMiddle Name')
    last_name = models.CharField( blank=False, max_length=20, null=False,verbose_name='Last Name',help_text='Vendor Last Name')
    contact_no = models.CharField( blank=False, max_length=15, null=False,verbose_name='Contact No',help_text='Vendor Contact Number')
    email_id = models.CharField(blank=False, max_length=50, null=False,verbose_name='Email Account',help_text='Vendor Email Account eg:myemail@gamail.com')
    company = models.CharField( blank=False, max_length=100, null=False,verbose_name='Company Name',help_text='Vendor Company Name')
    content = models.TextField(blank=True, max_length=500, null=True,verbose_name='Description',help_text='Company Information')
    website_url = models.CharField( blank=False, max_length=100, null=False,verbose_name='Web URL',help_text='Company website URL')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,help_text='Employee created the record',related_name='created_by', db_column='created_by')
    created_date = models.DateField(blank=True, null=True,verbose_name='Created Date', help_text='Published Date',default=date.today)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE,help_text='Modified by employee details',db_column='updated_by')
    updated_date = models.DateField( blank=True, null=True,verbose_name='Updated Date',help_text='Last updated date')
    company_phone = models.CharField( blank=False, max_length=15, null=False,verbose_name='Company Phone',help_text='company phone number')
    company_email = models.CharField( blank=False, max_length=50, null=False,verbose_name='Company Email',help_text='company email account')
    product  = models.CharField( blank=False, max_length=50, null=False,verbose_name='Product',help_text='Product Name')
    prod_specialize = models.CharField( blank=False, max_length=500, null=False,verbose_name='Product Specialize',help_text='Product Specialize details')
    prod_price_range = models.CharField( blank=False, max_length=50, null=False,verbose_name='Price Range',help_text='Product Price Rande details')
    company_gst = models.CharField( blank=False, max_length=500, null=False,verbose_name='GST',help_text='company GST details')

    class Meta:
        db_table = 'vendor'
        ordering=['first_name']

    def __str__(self):
        return self.first_name


class VendorFollowUpsModel(models.Model):

    id = models.AutoField(auto_created = True,primary_key=True,help_text='unique Id auto generates',db_column='id')
    first_name = models.CharField(max_length=20,db_column='first_name',blank=False,null=False,help_text='Contact Person First Name')
    middle_name = models.CharField(max_length=20,db_column='middle_name',blank=True,null=True,help_text='Contact Person Middle Name')
    last_name = models.CharField(max_length=20,db_column='last_name',blank=False,null=False,help_text='Contact Person Last Name')
    primary_no = models.CharField(max_length=15,db_column='primary_no',blank=False,null=False,help_text='Contact Person primary contact number')
    secondary_no=models.CharField(max_length=15,db_column='secondary_no',blank=True,null=True,help_text='Contact Person secondary contact number')
    company_email_id = models.CharField(max_length=100,db_column='company_email_id',blank=False,null=False,help_text='Contact Person Email Account')
    company_name = models.CharField(max_length=30,db_column='company_name',blank=False,null=False,help_text='Contact Person Company Name')
    content = models.CharField(max_length=200,db_column='content',blank=True,null=True,help_text='Contact Person Company Details')
    website_url = models.CharField(max_length=40,db_column='website_url',blank=False,null=False,help_text='Contact Person Company Website Link details')
    product = models.CharField(max_length=15,db_column='product',blank=False,null=False,help_text='company product details')
    reference = models.CharField(max_length=20,db_column='reference',blank=True,null=True,help_text='Person reference detai')
    comments = models.CharField(max_length=200,db_column='comments',blank=True,null=False,help_text='Contact Person primary contact number')
    created_by = models.ForeignKey(to=User,related_name='+',on_delete=models.CASCADE,help_text='employee created by', db_column='created_by')
    created_date = models.DateTimeField( blank=True, null=True,verbose_name='created Date',help_text='created date',db_column='created_date',default=datetime.now)
    updated_by = models.ForeignKey(to=User,related_name='+',on_delete=models.CASCADE,help_text='Employee updated by', db_column='updated_by')
    updated_date = models.DateTimeField( blank=True, null=True,verbose_name='Updated Date',help_text='Last updated date',db_column='updated_date',default=None)
    vendor_id = models.ForeignKey(to=Vendor,on_delete=models.CASCADE,blank=False,null=False,db_column='vendor_id',help_text='Vendor reference id')

    class Meta:
        db_table = 'vendor_follow_ups'
        ordering=['id','first_name']

class Product(models.Model):
    vendor_id = models.ForeignKey(to=Vendor,related_name='+',on_delete=models.CASCADE,db_column='vendor_id',blank=False,null=False,help_text='Vendor reference ID')
    id = models.AutoField(auto_created = True,primary_key=True,help_text='unique Id auto generates',db_column='id')
    type =  models.CharField(max_length=100,db_column='type',blank=False,null=False,help_text='Product Type')
    status  = models.BooleanField(db_column='status',help_text='Product Status',default=True)
    created_by  = models.ForeignKey(to=User,related_name='+',on_delete=models.CASCADE,db_column='created_by',blank=False,null=False,help_text='Product Created by')
    created_date  = models.DateTimeField(db_column='created_date',blank=False,null=False,help_text='Product created date')
    updated_by  = models.ForeignKey(to=User,related_name='+',on_delete=models.CASCADE,db_column='updated_by',blank=False,null=False,help_text='Product updated by')
    updated_date  = models.DateTimeField(max_length=20,db_column='updated_date',blank=False,null=False,help_text='Product last update date')

    class Meta:
        db_table = 'product'
        ordering=['vendor_id','id']

class SubProduct(models.Model):
    product_id = models.ForeignKey(to=Product,related_name='+',on_delete=models.CASCADE,db_column='product_id',blank=False,null=False,help_text='Sub Product reference ID')
    id = models.AutoField(auto_created = True,primary_key=True,help_text='unique Id auto generates',db_column='id')
    sub_product_type =  models.CharField(max_length=50,db_column='sub_product_type',blank=False,null=False,help_text='Sub Product Type')
    status  = models.BooleanField(db_column='status',help_text='Sub Product Status',default=True)
    created_by  = models.ForeignKey(to=User,related_name='+',on_delete=models.CASCADE,db_column='created_by',blank=False,null=False,help_text='Sub Product Created by')
    created_date  = models.DateTimeField(db_column='created_date',blank=False,null=False,help_text='Sub Product created date')
    updated_by  = models.ForeignKey(to=User,related_name='+',on_delete=models.CASCADE,db_column='updated_by',blank=False,null=False,help_text='Sub Product updated by')
    updated_date  = models.DateTimeField(max_length=20,db_column='updated_date',blank=False,null=False,help_text='Sub Product last update date')

    class Meta:
        db_table = 'sub_product'
        ordering=['product_id','id','sub_product_type']


class ProductCategory(models.Model):
    product_id = models.ForeignKey(to=Product,related_name='+',on_delete=models.CASCADE,db_column='product_id',blank=False,null=False,help_text='Category Product reference ID')
    id = models.AutoField(auto_created = True,primary_key=True,help_text='unique Id auto generates',db_column='id')
    category_type =  models.CharField(max_length=50,db_column='category_type',blank=False,null=False,help_text='Category Type')
    status  = models.BooleanField(db_column='status',help_text='Category Status',default=True)
    created_by  = models.ForeignKey(to=User,related_name='+',on_delete=models.CASCADE,db_column='created_by',blank=False,null=False,help_text='Product Created by')
    created_date  = models.DateTimeField(db_column='created_date',blank=False,null=False,help_text='Category created date')
    updated_by  = models.ForeignKey(to=User,related_name='+',on_delete=models.CASCADE,db_column='updated_by',blank=False,null=False,help_text='Category updated by')
    updated_date  = models.DateTimeField(max_length=20,db_column='updated_date',blank=False,null=False,help_text='Category last update date')

    class Meta:
        db_table = 'product_category'
        ordering=['product_id','id','category_type']


class Gender(models.Model):
    product_id = models.ForeignKey(to=Product,related_name='+',on_delete=models.CASCADE,db_column='product_id',blank=False,null=False,help_text='Gender reference ID')
    id = models.AutoField(auto_created = True,primary_key=True,help_text='unique Id auto generates',db_column='id')
    gender =  models.CharField(max_length=10,db_column='gender',blank=False,null=False,help_text='gender')
    created_by  = models.ForeignKey(to=User,related_name='+',on_delete=models.CASCADE,db_column='created_by',blank=False,null=False,help_text='Gender Created by')
    created_date  = models.DateTimeField(db_column='created_date',blank=False,null=False,help_text='Gender created date')
    updated_by  = models.ForeignKey(to=User,related_name='+',on_delete=models.CASCADE,db_column='updated_by',blank=False,null=False,help_text='Gender updated by')
    updated_date  = models.DateTimeField(max_length=20,db_column='updated_date',blank=False,null=False,help_text='Gender last update date')

    class Meta:
        db_table = 'gender'
        ordering=['product_id','id','gender']
