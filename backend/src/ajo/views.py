from django.shortcuts import get_object_or_404, render
# Create your views here.


from .models import AjoAccount



def ajo_account_list_view(request):
	queryset = AjoAccount.objects.all()
	template_name = 'ajo/list.html'
	context = {
		'all_ajo_accounts':queryset,
	}
	return render(request, template_name, context)



def ajo_account_detail_view(request, account_number):
	#obj = AjoAccount.objects.get(account_number=account_number)
	obj = get_object_or_404(AjoAccount, account_number=account_number)
	template_name = 'ajo/detail.html'
	context = {
		'account':obj
	}
	return render(request, template_name, context)