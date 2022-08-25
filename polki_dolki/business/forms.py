from django import forms
from django.forms import ModelForm
from .models import Vendor,VendorFollowUpsModel,SubProduct,Product
from django.contrib.auth.models import User
from django.forms import ModelChoiceField

class VendorRegistrationForm(ModelForm):
    class Meta:
        model = Vendor
        fields = (
            "id", "first_name", "middle_name", "last_name", "contact_no", "email_id", "company", "content",
            "website_url",
            'company_phone', 'company_email', 'product', 'prod_specialize', 'prod_price_range', 'company_gst',
            "created_by","updated_by")


class VendorReadOnlyForm(ModelForm):
    id = forms.CharField(label='ID',help_text='Unique Vendor Id',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'Vender Unique ID','readonly':'readonly'}),required=False,disabled=True)
    first_name = forms.CharField(label='First Name',help_text='Vendor First Name',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'First Name','readonly':'readonly'}))
    middle_name = forms.CharField(label='Middle Name',help_text='Vendor Middle Name',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'Middle Name','readonly':'readonly'}))
    last_name = forms.CharField(label='Last Name',help_text='Vendor Last Name',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'Last Name','readonly':'readonly'}))
    contact_no = forms.CharField(label='Contact Number',help_text='Vendor Contact Number',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'Contact No','readonly':'readonly'}))
    email_id = forms.EmailField(label='Email Account',help_text='Personal Email Account',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'Eamil Account','readonly':'readonly'}))
    company = forms.CharField(label='Company',help_text='Comapany profile',widget=forms.Textarea(attrs={'class': 'form-control form-control-alternative','rows':10,'cols':30,'placeholder':'Company Profile','readonly':'readonly'}))
    content = forms.CharField(label='Company',help_text='Comapany profile',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'Description','readonly':'readonly'}))
    website_url = forms.CharField(label='Website URL',help_text='Comapany Website link',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'Website URL','readonly':'readonly'}))
    company_phone =forms.CharField(label='Company Phone',help_text='Company Phone Number',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'Company Phone','readonly':'readonly'}))
    company_email = forms.CharField(label='Company Email',help_text='Comapany Email Account',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'Company Email','readonly':'readonly'}))
    product =forms.CharField(label='Product',help_text='Comapany Products',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'Product','readonly':'readonly'}))
    prod_specialize =forms.CharField(label='Product Specialize',help_text='Product Specilization',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'Specialize','readonly':'readonly'}))
    prod_price_range =forms.CharField(label='Price Range',help_text='Price Range',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'Price Range','readonly':'readonly'}))
    company_gst =forms.CharField(label='Company GST',help_text='Comapany GST Details',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','placeholder':'GST','readonly':'readonly'}))
    created_by =forms.CharField(label='Created By',help_text='Created By Employee ',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','readonly': 'readonly','placeholder':'Select a User'}))
    updated_by = forms.CharField(label='Updated By',help_text='Updated By Employee ',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative','readonly': 'readonly','placeholder':'Select a User'}))
    updated_date = forms.CharField(label='Created Date',help_text='Created Date Employee ',widget=forms.DateInput(attrs={'class': 'form-control form-control-alternative','readonly': 'readonly','placeholder':'Select a date'}))
    created_date = forms.CharField(label='Updated Date',help_text='Update Date Employee ',widget=forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control form-control-alternative','readonly': 'readonly','placeholder':'Select a date'}))
    #auto_now

    class Meta:
        model = Vendor

        fields = (
            "id", "first_name", "middle_name", "last_name", "contact_no", "email_id", "company", "content",
            "website_url",
            'company_phone', 'company_email', 'product', 'prod_specialize', 'prod_price_range', 'company_gst',
            "created_by","updated_by",'created_date','updated_date')


class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "{} {}".format(obj.id,obj.name)


class VendorFollowUpsForm(ModelForm):
    id = forms.CharField(label='ID',help_text='id',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'ID','readonly':'readonly'}),required=True)
    vendor_id = forms.ModelChoiceField(label='Vendor ID', queryset=None,to_field_name='first_name',
                                       help_text='Vendor reference id', widget=forms.TextInput(
            attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Vendor ID','readonly':'readonly'}))
    first_name = forms.CharField(label='First Name',max_length=20,help_text='Vendor First Name',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'First Name'}),required=True)
    middle_name = forms.CharField(label='Middle Name',max_length=20,help_text='Vendor Middle Name',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Middle Name'}),required=False)
    last_name = forms.CharField(label='Last Name',max_length=20,help_text='Vendor Last Name',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative border border-primary rounded','placeholder':'Last Name'}),required=True)
    primary_no = forms.CharField(label='Primary Phone No',max_length=15,help_text='Contact Person primary contact number',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Phone Number'}),required=True)
    secondary_no= forms.CharField(label='Secondary No',max_length=15,help_text='Contact Person secondary contact number',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Phone Number'}),required=False)
    company_email_id = forms.EmailField(label='Company Email ID',help_text='Contact Person Email Account',widget=forms.EmailInput(attrs={'class': 'form-control form-control-alternative   border border-primary rounded','placeholder':'Email Account'}),required=True)
    company_name = forms.CharField(label='Company Name',max_length=30,help_text='Contact Person Company Name',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Company Name'}),required=True)
    content = forms.CharField(label='Content',max_length=200,help_text='Contact Person Company Details',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Company Details'}),required=True)
    website_url = forms.CharField(label='Website Url',max_length=40,help_text='Contact Person Company Website Link details',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Website URL'}),required=True)
    product = forms.CharField(label='Product',max_length=15,help_text='company product details',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Product '}),required=True)
    reference = forms.CharField(label='Reference',max_length=20,help_text='Person reference details',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Reference Details'}),required=True)
    comments = forms.CharField(label='Comments',max_length=200,help_text='Contact Person primary contact number',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Phone Number'}),required=True)
    created_by = forms.ModelChoiceField(label='Created By',queryset=User.objects.all(),help_text='employee created by',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Created By','readonly':'readonly'}),required=True)
    #created_by = forms.ChoiceField(label='Created By',help_text='employee created by',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Vender Unique ID'}),required=True)
    created_date = forms.DateTimeField( label='Created Date',help_text='created date',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Created Date Time','readonly':'readonly'}),required=True)
    updated_by = UserModelChoiceField(label='Updated By',queryset=User.objects.all(),help_text='Employee updated by',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Updated By','readonly':'readonly'}),required=True)
    #updated_by = forms.ModelChoiceField(label='Updated By',help_text='Employee updated by',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Vender Unique ID'}),required=True)
    updated_date = forms.DateTimeField( label='Updated Date',help_text='Last updated date',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Updated Date Time','readonly':'readonly'}),required=True)


    class Meta:
        model = VendorFollowUpsModel
        fields = ('id', 'vendor_id', 'first_name', 'middle_name', 'last_name', 'primary_no', 'secondary_no', 'company_email_id',
                  'company_name', 'content', 'website_url', 'product', 'reference', 'comments', 'created_by',
                  'created_date', 'updated_by', 'updated_date')


    #super(VendorFollowUpsForm, self).__init__(*args, **kwargs)
    #self.fields['test_vendor_id'] = forms.ModelChoiceField(queryset=Vendor.objects.filter(id=8))
PRODUCT_TYPE_CHOICES =(
    ("1", "Clothing"),
    ("2", "Furniture"),
    ("3", "Shoes"),
    ("4", "Watches"),
    ("5", "Bags"),
    ("6", "cosmetics"),
    ("7", "Jewelery"),
    ("8", "home decor"),
    ("9", "toys"),
)

SUB_PRODUCT_TYPE_CHOICES =(
    ("1", "Clothing"),
    ("2", "Furniture"),
    ("3", "Shoes"),
    ("4", "Watches"),
    ("5", "Bags"),
    ("6", "cosmetics"),
    ("7", "Jewelery"),
    ("8", "home decor"),
    ("9", "toys"),
)

class ProductForm(ModelForm):
    id = forms.CharField(label='ID',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'ID','readonly':'readonly'}),required=True)
    vendor_id = forms.ModelChoiceField(label='Vendor ID', queryset=None,to_field_name='first_name',
                                       help_text='Vendor id', widget=forms.TextInput(
            attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Vendor ID','readonly':'readonly'}))
    type = forms.ChoiceField(label='Type', choices = PRODUCT_TYPE_CHOICES,widget=forms.Select(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Created By','readonly':'readonly'}))
    status = forms.BooleanField(label='Status',required=False,widget=forms.CheckboxInput(attrs={'class':'form-control form-control-alternative','tabindex': '-1'}))
    created_by = forms.ModelChoiceField(label='Created By',queryset=User.objects.all(),widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Created By','readonly':'readonly'}),required=True)
    #created_by = forms.ChoiceField(label='Created By',help_text='employee created by',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Vender Unique ID'}),required=True)
    created_date = forms.DateTimeField( label='Created Date',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Created Date Time','readonly':'readonly'}),required=True)
    updated_by = UserModelChoiceField(label='Updated By',queryset=User.objects.all(),help_text='Employee updated by',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Updated By','readonly':'readonly'}),required=True)
    #updated_by = forms.ModelChoiceField(label='Updated By',help_text='Employee updated by',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Vender Unique ID'}),required=True)
    updated_date = forms.DateTimeField( label='Updated Date',help_text='Last updated date',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Updated Date Time','readonly':'readonly'}),required=True)


    class Meta:
        model = VendorFollowUpsModel
        fields = ('id', 'vendor_id', 'type', 'status', 'created_by',
                  'created_date', 'updated_by', 'updated_date')
'''
    widgets = {
        'status': forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check-input form-control', 'id': 'id'})
    }
'''

class SubProductForm(ModelForm):
    id = forms.CharField(label='ID', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-alternative  border border-primary rounded', 'placeholder': 'ID',
               'readonly': 'readonly'}), required=True)
    product_id = forms.ModelChoiceField(label='Product ID', queryset=None, to_field_name='type',
                                       help_text='Product id', widget=forms.TextInput(
            attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Product ID',
                   'readonly': 'readonly'}))
    sub_product_type = forms.ChoiceField(label='Sub Product Type', choices=SUB_PRODUCT_TYPE_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control form-control-alternative  border border-primary rounded',
               'placeholder': 'Created By', 'readonly': 'readonly'}))
    status = forms.BooleanField(label='Status', required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-control form-control-alternative', 'tabindex': '-1'}))
    created_by = forms.ModelChoiceField(label='Created By', queryset=User.objects.all(), widget=forms.TextInput(
        attrs={'class': 'form-control form-control-alternative  border border-primary rounded',
               'placeholder': 'Created By', 'readonly': 'readonly'}), required=True)
    # created_by = forms.ChoiceField(label='Created By',help_text='employee created by',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Vender Unique ID'}),required=True)
    created_date = forms.DateTimeField(label='Created Date', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-alternative  border border-primary rounded',
               'placeholder': 'Created Date Time', 'readonly': 'readonly'}), required=True)
    updated_by = UserModelChoiceField(label='Updated By', queryset=User.objects.all(), help_text='Employee updated by',
                                      widget=forms.TextInput(attrs={
                                          'class': 'form-control form-control-alternative  border border-primary rounded',
                                          'placeholder': 'Updated By', 'readonly': 'readonly'}), required=True)
    # updated_by = forms.ModelChoiceField(label='Updated By',help_text='Employee updated by',widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative  border border-primary rounded','placeholder':'Vender Unique ID'}),required=True)
    updated_date = forms.DateTimeField(label='Updated Date', help_text='Last updated date', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-alternative  border border-primary rounded',
               'placeholder': 'Updated Date Time', 'readonly': 'readonly'}), required=True)


    class Meta:
        model = SubProduct
        fields = ('id', 'product_id', 'sub_product_type', 'status', 'created_by',
                  'created_date', 'updated_by', 'updated_date')