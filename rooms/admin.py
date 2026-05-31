from django.contrib import admin
from django.utils.html import format_html # Import utilitas html
from .models import Room, Booking

admin.site.site_header = "Panel Admin Kos"
admin.site.site_title = "Admin Kos"
admin.site.index_title = "Manajemen Data Kos"

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price_per_month', 'is_available')
    list_filter = ('room_type', 'is_available')
    search_fields = ('room_number', 'facilities')
    list_editable = ('is_available',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # Tambahkan fungsi custom show_payment_proof di list_display
    list_display = ('room', 'tenant_name', 'tenant_phone', 'status', 'show_payment_proof', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('tenant_name', 'tenant_phone', 'room__room_number')
    list_editable = ('status',)

    # Fungsi untuk menyajikan link bukti pembayaran dengan aman di panel admin
    def show_payment_proof(self, obj):
        if obj.payment_proof:
            return format_html('<a href="{}" target="_blank" class="btn btn-xs btn-info">Buka Bukti Transfer</a>', obj.payment_proof.url)
        return "Belum Mengunggah"
    
    show_payment_proof.short_description = "Bukti Transfer"