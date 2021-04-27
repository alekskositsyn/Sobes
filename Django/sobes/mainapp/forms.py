from django import forms
from .models import GoodItem


class CreateForm(forms.ModelForm):
    class Meta:
        model = GoodItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
