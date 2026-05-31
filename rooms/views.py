from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Booking
from .forms import BookingForm

def landing_page(request):
    # Menampilkan 3 kamar terbaru yang tersedia di landing page
    featured_rooms = Room.objects.filter(is_available=True)[:3]
    return render(request, 'landing.html', {'featured_rooms': featured_rooms})

def room_list(request):
    # Menampilkan semua kamar
    rooms = Room.objects.all()
    # Filter sederhana berdasarkan ketersediaan jika ada parameter query
    status_filter = request.GET.get('status')
    if status_filter == 'available':
        rooms = rooms.filter(is_available=True)
    return render(request, 'room_list.html', {'rooms': rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        # Sertakan request.FILES untuk menangkap file bukti transfer
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(request, 'room_detail.html', {'room': room, 'form': form})
def booking_success(request):
    return render(request, 'success.html')