from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej: Juan Pérez", "autocomplete": "name"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "tucorreo@empresa.cl", "autocomplete": "email"}))
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "+56 9 ...", "autocomplete": "tel"}))
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Cuéntanos qué necesitas proteger"}))
    acepta_privacidad = forms.BooleanField(label="Acepto la política de privacidad", required=True, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
