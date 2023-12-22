from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    """
    Formulario para la creación y edición de usuarios.

    Attributes:
    - model (Usuario): Modelo asociado al formulario.
    - fields (list): Lista de campos a incluir en el formulario.

    """

    class Meta:
        """
        Clase Meta para configuración adicional del formulario.

        Attributes:
        - model (Usuario): Modelo asociado al formulario.
        - fields (list): Lista de campos a incluir en el formulario.

        """
        
        model = Usuario
        fields = '__all__'