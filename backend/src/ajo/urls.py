from django.urls import path

from .views import ajo_account_detail_view, ajo_account_list_view



app_name = 'accounts'

urlpatterns = [
	path('', ajo_account_list_view, name='list'),
	path('<str:account_number>/', ajo_account_detail_view, name='detail')
]
