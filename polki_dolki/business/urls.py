from django.urls import path
from business.views import (vendorView,OrderListJson,test,VendorEdit,VendorDelete,VendorRowView,VendorFollowUpsListView,
                            AddVendorFollowupsView,EditVendorFollowups,DeleteVendorFollowups,VendorProductsList,AddVendorProducts)
urlpatterns = [
    path('vendorList',vendorView.as_view(),name='vendorList'),
    path('vendoredit/<int:id>',VendorEdit.as_view(),name='vendoredit'),
    path('vendordelete/<int:id>',VendorDelete.as_view(),name='vendordelete'),
    path('vendorrowview/<int:id>',VendorRowView.as_view(),name='vendorrowview'),
    path('orderlist',OrderListJson.as_view(),name='orderlist'),
    path('test',test,name='test'),
    path('vendorfollowupslistview/<int:id>',VendorFollowUpsListView.as_view(),name='vendorfollowupslistview'),
    path('addvendorfollowup/<int:id>',AddVendorFollowupsView.as_view(),name='addvendorfollowup'),
    path('vendorfollowupsEdit/<int:id>',EditVendorFollowups.as_view(),name='vendorfollowupsEdit'),
    path('vendorfollowupsDel/<int:id>/<int:vendor_id>',DeleteVendorFollowups.as_view(),name='vendorfollowupsDel'),
    path('vendorproductslist/<int:id>',VendorProductsList.as_view(),name='vendorproductslist'),
    path('addvendorproducts/<int:id>',AddVendorProducts.as_view(),name='addvendorproducts'),
]