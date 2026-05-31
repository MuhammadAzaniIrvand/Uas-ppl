from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('Reguler', 'Reguler (Kamar Mandi Luar)'),
        ('Eksklusif', 'Eksklusif (Kamar Mandi Dalam + AC)'),
        ('VIP', 'VIP (Fasilitas Lengkap + Water Heater)'),
    ]

    room_number = models.CharField("Nomor Kamar", max_length=10, unique=True)
    room_type = models.CharField("Tipe Kamar", max_length=20, choices=ROOM_TYPES, default='Reguler')
    price_per_month = models.DecimalField("Harga per Bulan (Rp)", max_digits=10, decimal_places=0)
    facilities = models.TextField("Fasilitas")
    is_available = models.BooleanField("Tersedia", default=True)
    image = models.ImageField("Foto Kamar (Opsional)", upload_to='rooms/', blank=True, null=True)

    def __str__(self):
        return f"Kamar {self.room_number} - {self.get_room_type_display()}"

    @property
    def room_image_url(self):
        if self.image:
            return self.image.url
        
        # Peta gambar default berdasarkan Tipe Kamar
        default_images = {
            'Reguler': 'https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=500&q=80',
            'Eksklusif': 'https://images.unsplash.com/photo-1598928506311-c55ded91a20c?auto=format&fit=crop&w=500&q=80',
            'VIP': 'https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=500&q=80'
        }
        return default_images.get(self.room_type, default_images['Reguler'])


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Menunggu Konfirmasi'),
        ('Disetujui', 'Disetujui'),
        ('Ditolak', 'Ditolak'),
    ]

    room = models.ForeignKey(Room, verbose_name="Kamar", on_delete=models.CASCADE, related_name='bookings')
    tenant_name = models.CharField("Nama Lengkap", max_length=100)
    tenant_phone = models.CharField("Nomor WhatsApp/HP", max_length=15)
    tenant_email = models.EmailField("Email")
    duration_months = models.IntegerField("Durasi Sewa (Bulan)", default=1)
    notes = models.TextField("Catatan Tambahan", blank=True, null=True)
    
    # Field baru untuk menyimpan foto bukti transfer DP (Wajib diisi)
    payment_proof = models.ImageField("Bukti Transfer DP", upload_to='proofs/', blank=False, null=False)
    
    status = models.CharField("Status Pengajuan", max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.room.room_number} oleh {self.tenant_name}"