# 🎵 Python Lyrics Player

Sebuah script Python sederhana untuk menampilkan lirik lagu  dengan efek *typing* (mengetik) secara real-time di terminal.

## ✨ Fitur
- **Typewriter Effect**: Teks muncul per huruf, bukan per baris.
- **Dynamic Timing**: Jeda antar baris disesuaikan dengan ritme lagu.
- **Lightweight**: Tanpa library eksternal, cukup pakai bawaan Python.

## 🚀 Cara Menjalankan

1. Pastikan kamu sudah menginstal [Python](https://www.python.org).
2. Clone repository ini atau simpan kode ke dalam file `.py`.
3. Jalankan perintah berikut di terminal:
   ```bash
   python nama_file_kamu.py

## ⚙️ Konfigurasi & Kustomisasi

Kamu bisa memodifikasi script ini agar sesuai dengan lagu lain atau preferensi tampilanmu. Semua pengaturan ada di dalam fungsi `run_liric()` pada bagian `#config`:

### 1. Mengatur Kecepatan & Jeda

| Variabel | Fungsi | Cara Ubah |
| :--- | :--- | :--- |
| `def_sleep` | Jeda awal sebelum script mulai berjalan. | Ubah nilainya (misal `2` untuk menunggu 2 detik). |
| `typing_speed` | Kecepatan munculnya setiap huruf. | Semakin kecil angkanya, semakin cepat ketikannya (contoh: `0.05`). |

### 2. Mengubah Lirik & Durasi (`lines`)
Bagian `lines` adalah sebuah **Array (List)** yang berisi teks lirik dan durasi jeda setelah baris tersebut selesai diketik.

**Format:** `("Teks Lirik", Jeda_Detik)`

```python
lines = [
    ("Lirik baris pertama", 0.5), # Muncul, lalu diam 0.5 detik
    ("Lirik baris kedua", 1.2),   # Muncul, lalu diam 1.2 detik
]

