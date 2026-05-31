# 🏠 Aplikasi Manajemen Kos Mandiri (Django)

Aplikasi web sederhana untuk manajemen informasi kamar kos dan pengajuan sewa (booking) dengan fitur unggah bukti transfer DP manual.

---

## 🚀 Fitur Utama

1. **Halaman Publik (User):**
   - Melihat daftar kamar kos yang tersedia beserta fasilitasnya.
   - Mengajukan sewa (booking) dengan mengisi data diri.
   - Melihat ketentuan pembayaran DP (Transfer Bank) dan mengunggah foto bukti transfer langsung dari formulir.

2. **Dashboard Admin (Wajib Login):**
   - Menggunakan tema modern berbasis Tailwind CSS (*Django Unfold*).
   - Melakukan CRUD (Tambah, Edit, Hapus) data kamar.
   - Memverifikasi pengajuan booking dan mengecek berkas foto bukti transfer dari penyewa.
   - Mengubah status booking menjadi *Pending*, *Disetujui*, atau *Ditolak*.

---

## 🛠️ Teknologi yang Digunakan

- **Backend:** Django 
- **Database:** SQLite
- **UI Publik:** Tailwind CSS (via CDN)
- **UI Admin:** Django Unfold Theme

---

## 📂 Struktur Utama Proyek

```text
proyek_kos/
├── kos_management/      # Folder konfigurasi utama Django
├── rooms/               # App untuk fitur kamar & booking
│   └── fixtures/        # Folder data dummy awal (.json)
├── templates/           # Folder berkas HTML
├── media/               # Folder penyimpanan berkas foto unggahan
└── manage.py            # Utilitas perintah Django
