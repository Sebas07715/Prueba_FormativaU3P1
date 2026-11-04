from django import forms
from .models import Ticket
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['nombre_comprador', 'email_comprador', 'cantidad']
    
    def clean_cantidad(self):

        cant = self.cleaned_data.get('cantidad')
        if cant is None or cant < 1 or cant > 10:
            raise forms.ValidationError("La cantidad debe ser entre 1 y 10 entradas.")
        return cant
