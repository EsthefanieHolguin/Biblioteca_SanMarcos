from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    """
    Formulario para la creación y edición de libros.

    Este formulario se basa en el modelo Libro y se utiliza para recopilar
    información sobre los libros, permitiendo su creación y edición.

    Atributos:
        model: Clase del modelo asociado al formulario (Libro).
        fields: Lista de campos del modelo a incluir en el formulario.

    Campos Adicionales:
        categoria: Campo ChoiceField que representa la categoría del libro.

    Métodos:
        __init__: Inicializa el formulario y ajusta el widget del campo 'categoria'.
    """

    class Meta:
        model = Libro
        fields = '__all__'

    # Opciones para el campo 'categoria'
    CATEGORIAS_CHOICES = [
        ('novelas', 'Novelas'),
        ('suspenso', 'Suspenso'),
        ('historia', 'Historia'),
        ('test', 'Test'),
    ]
        
    categoria = forms.ChoiceField(choices=CATEGORIAS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    