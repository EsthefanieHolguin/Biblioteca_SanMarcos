#encoding:utf-8
from django import forms
from .models import Prestamo


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'
        widgets = {
            'flg_estado_prestamo': forms.Select(attrs={'class': 'regDropDown'}),
            'fecha_devolucion_real': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(PrestamoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_devolucion_real'].required = False
   
