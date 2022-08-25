from django.contrib.auth.models import User
from business.models import Vendor
from rest_framework import routers, serializers, viewsets

class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = (
            "id", "first_name", "middle_name", "last_name", "contact_no", "email_id", "company", "content",
            "website_url",
            'company_phone', 'company_email', 'product', 'prod_specialize', 'prod_price_range', 'company_gst',
            'created_by', 'updated_by')
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
