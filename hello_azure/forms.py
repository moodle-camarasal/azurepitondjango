from django import forms

class SociosForm(forms.Form):
    empresa = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Empresa'}), label='')
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre del responsable'}), label='')
    cargo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Cargo'}), label='')
    correo = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Correo electrónico'}), label='')
    telefono = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}), label='')
    codigo = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Numero de socio'}), label='')


"""
class SociosForm(forms.Form):
  #  empresa = forms.CharField(label='Empresa', max_length=100, widget=forms.HiddenInput)
    empresa = forms.CharField(label='Empresa', max_length=100)
    nombre = forms.CharField(label='Nombre del responsable', max_length=100)
    cargo = forms.CharField(label='Cargo', max_length=100)
    correo = forms.EmailField(label='Correo electrónico', max_length=100)
    telefono = forms.CharField(label='Teléfono', max_length=20)
    codigo = forms.CharField(label='Numero de socio', max_length=10)
"""