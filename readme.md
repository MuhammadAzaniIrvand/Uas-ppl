# 🏠 Aplikasi Manajemen Kos Mandiri - Django

Aplikasi berbasis web sederhana untuk mengelola manajemen kos. Dibangun menggunakan framework Django (Python) dan Tailwind CSS untuk tampilan halaman utama.

## ✨ Fitur Utama
1. **Sisi Pengguna Publik**:
   - Landing page yang menyajikan sekilas informasi kos.
   - Daftar kamar yang dapat difilter berdasarkan status ketersediaan.
   - Detail kamar dan form pemesanan langsung untuk calon penghuni.
2. **Sisi Admin (Dashboard)**:
   - Manajemen penuh (CRUD) data Kamar (Nomor, Tipe, Harga, Fasilitas, Foto, Status).
   - Verifikasi pengajuan sewa (Booking) dengan status Menunggu, Disetujui, atau Ditolak.
   - Hak akses aman (Hanya admin terdaftar yang dapat masuk).

---

## 🛠️ Langkah-Langkah Instalasi

Ikuti langkah di bawah ini untuk menjalankan proyek di perangkat lokal Anda.

### 1. Kloning Repository
```bash
git clone <URL_REPOSITORY_ANDA>
cd kos_management