#encoding:utf-8
from django import forms
from .models import Prestamo


class PrestamoForm(forms.ModelForm):
    """
    Formulario para el modelo Prestamo.

    Attributes:
        ESTADOS_CHOICE (list): Opciones para el campo 'estado_prestamo'.

    Fields:
        estado_prestamo (ChoiceField): Campo para seleccionar el estado del préstamo.
            - choices: Opciones definidas en ESTADOS_CHOICE.
            - widget: Selector de opciones con clase 'form-control'.
        fecha_devolucion_real (DateField): Campo para ingresar la fecha real de devolución.
            - widget: Campo de entrada de fecha con tipo 'date'.

    Methods:
        __init__: Método de inicialización para personalizar la creación del formulario.

    """
    
    class Meta:
        model = Prestamo
        fields = '__all__'

    ESTADOS_CHOICE =[
        ('vigente','Préstamo Vigente'),
        ('finalizado','Préstamo Finalizado'),
        ('atrasado','Devolución Atrasada'),
    ]

    widgets = {
        'estado_prestamo': forms.Select(attrs={'class': 'regDropDown'}),
        'fecha_devolucion_real': forms.DateInput(attrs={'type': 'date'}),
    }
            
    estado_prestamo = forms.ChoiceField(choices=ESTADOS_CHOICE, widget=forms.Select(attrs={'class': 'form-control'}))




""" EVALUAR SI SE UTILIZA ESTE METODO A FUTURO

    def __init__(self, *args, **kwargs):
    
        ""
        Método de inicialización para personalizar la creación del formulario.

        Args:
            *args: Argumentos posicionales.
            **kwargs: Argumentos de palabras clave.

        Returns:
            None
        ""

        super().__init__(*args, **kwargs)

        # Personalizar atributos o comportamientos adicionales si es necesario
        # ...

        # Ejemplo: Desactivar el campo fecha_devolucion_real si el estado no es 'finalizado'
        if 'instance' in kwargs and kwargs['instance']:
            estado_actual = kwargs['instance'].estado_prestamo
            if estado_actual != 'finalizado':
                self.fields['fecha_devolucion_real'].widget.attrs['disabled'] = True
                self.fields['fecha_devolucion_real'].required = False
"""

   
