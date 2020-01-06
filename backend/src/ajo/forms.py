from .models import AjoAccount

class  AjoAccountModelForm(form.ModelForm):
	class Meta:
		model = AjoAccount
		fields = ["account_name", "account_number"]