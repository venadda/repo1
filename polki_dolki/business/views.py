from django.shortcuts import render
from business.models import Vendor,VendorFollowUpsModel,Product
from business.forms import VendorRegistrationForm,VendorReadOnlyForm,VendorFollowUpsForm,ProductForm
from django.views.generic import View
from django.forms import formset_factory,modelformset_factory
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.http import HttpResponse,JsonResponse
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def test(request):
    if request.method=='GET':
        return JsonResponse({'status': 'good'})
    if request.method=='POST':
        print('requested',request.POST)
        return JsonResponse({'status':'good'})
class OrderListJson(BaseDatatableView):
    # The model we're going to show
    model = Vendor

    # define the columns that will be returned
    columns = ["id", "first_name", "middle_name", "last_name", "contact_no", "email_id", "company", "content",
        "website_url",
        'company_phone', 'company_email', 'product', 'prod_specialize', 'prod_price_range', 'company_gst',
        "created_by", "updated_by"]
    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non-sortable columns use empty
    # value like ''
    order_columns = ['id', 'first_name', 'last_name', 'contact_no', 'email_id']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        # We want to render user as a custom column
        #if column == 'first_name':
            # escape HTML for security reasons
        #    return escape('{0} {1}'.format(row.customer_firstname, row.customer_lastname))
        #else:
        return super(OrderListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)

        # more advanced example using extra parameters
        filter_customer = self.request.GET.get('customer', None)

        if filter_customer:
            customer_parts = filter_customer.split(' ')
            qs_params = None
            for part in customer_parts:
                q = Q(customer_firstname__istartswith=part) | Q(customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs

    def get(self, request, *args, **kw):
        return render(request, None, {})


class vendorView(View):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    template_name = "vendors.html"
    data = Vendor.objects.all().values()
    vf = formset_factory(VendorRegistrationForm, extra=0)
    forms = vf(initial=data)
    def get(self, request, *args, **kw):
        return render(request, self.template_name, {'forms': self.forms,'msg':None})

    def post(self, request, *args, **kw):
        return render(request, self.template_name, {'forms': self.forms,'msg':None})
    '''
    @csrf_exempt
    def post(self,request,*args,**kw):
        if request.is_ajax:
            print('it is ajax')
            return JsonResponse({'status': 'good'})
    '''


class VendorEdit(View):
    def get(self,request,*args,**kw):
        context = self.kwargs.get('id')
        ob = Vendor.objects.filter(pk=context).first()
        #vf = VendorRegistrationForm(ob.values())
        form = VendorRegistrationForm(instance=ob)
        return render(request,'vendoredit.html',{'form':form,'msg':None})


class VendorRowView(View):
    message = ''
    template_name = "vendorrowview.html"

    def get(self, request, *args, **kw):
        context = self.kwargs.get('id')
        ob=Vendor.objects.filter(pk=context).first()
        form = VendorReadOnlyForm(instance=ob)

        return render(request, self.template_name, {'form': form, 'msg': self.message})
        #return  self.http_method_not_allowed(request, self.template_name, {'form': form, 'msg': self.message})


class VendorDelete(View):
    message ='Record Deleted Successfully'
    template_name = "vendors.html"
    def get(self,request,*args,**kw):
        context = self.kwargs.get('id')
        try:
            Vendor.objects.filter(pk=context).delete()
            Vendor.save(commit=False)
        except Exception as err:
            self.message='Transaction Failed'

        data = Vendor.objects.all().values()
        vf = formset_factory(VendorRegistrationForm, extra=0)
        forms = vf(initial=data)
        return render(request, self.template_name, {'forms': forms,'msg':self.message})


class VendorFollowUpsListView(View):
    message = 'Record Deleted Successfully'
    template_name = 'VendorFollowUpsListView.html'
    context_object_name = 'VendorFollowUpsModel'
    context = ''
    def get(self,request,*args,**kw):
        self.context = self.kwargs.get('id')

        data = VendorFollowUpsModel.objects.filter(vendor_id=self.context)
        if data.count()>1:
            formset = modelformset_factory(VendorFollowUpsModel,form=VendorFollowUpsForm,fields=( 'vendor_id','first_name','middle_name','last_name','primary_no','secondary_no','company_email_id',
            'company_name','content','website_url','product','reference','comments','created_by','created_date','updated_by','updated_date','vendor_id','id'),extra=0)
        else:
            formset = modelformset_factory(VendorFollowUpsModel, form=VendorFollowUpsForm, fields=(
            'vendor_id', 'first_name', 'middle_name', 'last_name', 'primary_no', 'secondary_no', 'company_email_id',
            'company_name', 'content', 'website_url', 'product', 'reference', 'comments', 'created_by', 'created_date',
            'updated_by', 'updated_date', 'vendor_id', 'id'), extra=1)
        try:
            #queryset = Vendor.objects.filter(vendor_id=self.context)
            forms = formset(queryset=data)
            return render(request,self.template_name,{'forms':forms,'msg':'','vendor_id':self.context})

        except Exception as err:
            self.message = 'Error : '+ str(err)
            ob=VendorFollowUpsModel()
            vf = formset_factory(VendorFollowUpsForm,extra=1)
            forms = vf()
            return render(request,self.template_name,{'forms':forms,'vendor_id':self.context,'msg':self.message})


class AddVendorFollowupsView(View):
    message = ''
    template_name = 'addvendorfollowup.html'
    required_css_class = 'required'
    print('vendorfollowups add screen')

    def get(self,request,*args,**kw):
        vendor_id = self.kwargs.get('id')
        vendor = Vendor.objects.filter(id=8)
        ob = VendorFollowUpsModel()
        form = VendorFollowUpsForm(instance=ob)
        form.vendor_id=vendor
        return render(request,self.template_name,{'form':form,'vendor_id':vendor_id})

    def post(self,request,*args,**kw):
        vendor_id = self.kwargs.get('id')
        ob = VendorFollowUpsModel()
        form = VendorFollowUpsForm(instance=ob)
        return render(request,self.template_name,{'form':form,'vendor_id':vendor_id})


class EditVendorFollowups(View):
    message = ''
    template_name = 'vendorfollowupsedit.html'

    required_css_class = 'required'

    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        print(id)
        ob = VendorFollowUpsModel()
        form = VendorFollowUpsForm(instance=ob)
        return render(request,self.template_name,{'form':form,'vendor_id':id})

    def post(self,request,*args,**kwargs):
        vendor_id = self.kwargs.get('id')
        ob = VendorFollowUpsModel()
        form = VendorFollowUpsForm(instance=ob)
        return render(request,self.template_name,{'form':form,'vendor_id':vendor_id})

class DeleteVendorFollowups(View):
    message = ''
    template_name = 'VendorFollowUpsListView.html'

    required_css_class = 'required'

    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        vendor_id = self.kwargs.get('vendor_id')
        print(id)
        vendor = Vendor.objects.filter(pk=vendor_id)
        print(vendor_id)
        delete_vendor = VendorFollowUpsModel.objects.filter(pk=id)
        if delete_vendor:
            #delete_vendor.delete()
            self.message = 'Record deleted successfully'
        else:
            self.message = 'Record delete has been failed'

        forms = VendorFollowUpsForm(instance=vendor_id)
        return render(request,self.template_name,{'forms':forms,'vendor_id':id})

class VendorProductsList(View):
    message = ''
    template_name = 'vendorproducts.html'

    required_css_class = 'required'

    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        vendor_id = self.kwargs.get('vendor_id')

        product = Product.objects.filter(vendor_id=vendor_id)
        formset = modelformset_factory(Product, form=ProductForm, fields=('id','vendor_id','type','status','created_by','created_date','updated_by','updated_by'))
        forms = formset(queryset=product)
        return render(request,self.template_name,{'forms':forms,'vendor_id':id})


class AddVendorProducts(View):
    message = ''
    template_name = 'addproducttypes.html'

    required_css_class = 'required'

    def get(self,request,*args,**kwargs):
        vendor_id = self.kwargs.get('vendor_id')

        product = Product()
        form = ProductForm()
        return render(request,self.template_name,{'form':form,'vendor_id':vendor_id})
