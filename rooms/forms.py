from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        # Tambahkan payment_proof di baris berikut
        fields = ['tenant_name', 'tenant_phone', 'tenant_email', 'duration_months', 'notes', 'payment_proof']
        widgets = {
            'tenant_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Nama Lengkap Anda'}),
            'tenant_phone': forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Contoh: 08123456789'}),
            'tenant_email': forms.EmailInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'nama@email.com'}),
            'duration_months': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded', 'min': 1}),
            'notes': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 2, 'placeholder': 'Catatan khusus jika ada'}),
            # Widget khusus untuk upload file bukti transfer
            'payment_proof': forms.FileInput(attrs={'class': 'w-full p-2 border rounded', 'accept': 'image/*'}),
        }