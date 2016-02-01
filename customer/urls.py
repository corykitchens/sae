from django.conf.urls import patterns, url, include
from customer.views import CustomerList, ViewCustomer, NewCustomer, KillCustomer,\
    EditCustomer, ViewCustomer_Address, EditCustomer_Address, DeleteCustomer_Address, Customer_AddressDetail,\
    NewCustomer_Address, Customer_AddressList

customer_urls = patterns('',
    url(r'^$', ViewCustomer.as_view(), name='customer_detail'),
    url(r'^Update$', EditCustomer.as_view(), name='customer_update'),
    url(r'^Delete$', KillCustomer.as_view(), name='customer_delete'),
)

customer_address_urls = patterns('',
    url(r'^$', ViewCustomer_Address.as_view(), name='customer_address_detail'),
    url(r'^Alternate$', Customer_AddressDetail.as_view(), name='customer_address_detail_alt'),
    url(r'^Update$', EditCustomer_Address.as_view(), name='custmomer_address_update'),
    url(r'^Delete$', DeleteCustomer_Address.as_view(), name='customer_address_delete'),
)

urlpatterns = patterns('',
    url(r'^$', CustomerList.as_view(), name='customer_list'),
    url(r'^(?P<slug>[\w-]+).customer/', include(customer_urls)),
    url(r'^NewPerson$', NewCustomer.as_view(), name='customer_add'),
    url(r'^Categories$', Customer_AddressList.as_view(), name='customer_address_list'),
    url(r'^(?P<slug>[\w-]+).cat/', include(customer_address_urls)),
    url(r'^NewCategory$', NewCustomer_Address.as_view(), name='customer_address_add'),
)