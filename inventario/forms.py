from django import forms
from .models import Proveedor, Producto



class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono', 'email']
        widgets = {
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección del proveedor'})
        }



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'proveedor']

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None or precio < 10:
            raise forms.ValidationError("El precio debe ser al menos 10.")
        if precio % 10 != 0:
            raise forms.ValidationError("El precio debe ser múltiplo de 10.")
        return precio
