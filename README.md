# 🎵 Python Lyrics Player

Sebuah script Python sederhana untuk menampilkan lirik lagu favoritmu dengan efek *typing* (mengetik) yang sinkron secara real-time di terminal.

---

## ✨ Fitur Utama

*   **⌨️ Typewriter Effect**: Teks muncul per karakter, memberikan kesan visual yang lebih hidup.
*   **⏱️ Precise Timing**: Kontrol penuh atas jeda antar baris dan kecepatan ketik setiap kalimat.
*   **🪶 Ultra Lightweight**: Hanya menggunakan modul bawaan Python (`sys`, `time`). Tidak perlu `pip install`.
*   **🎨 Highly Customizable**: Mudah diubah untuk lagu apa pun hanya dengan mengedit struktur list.

---

## 🚀 Cara Menjalankan

1.  **Instalasi Python**: Pastikan Python (versi 3.6+) sudah terpasang di sistem kamu.
2.  **Simpan File**: Simpan kode Python kamu dengan nama, misalnya `lyrics.py`.
3.  **Eksekusi**: Buka terminal atau CMD, lalu jalankan:
    ```bash
    python lyrics.py
    ```

---

## ⚙️ Konfigurasi & Kustomisasi

Kamu bisa memodifikasi skrip ini di dalam fungsi `run_liric()` pada bagian variabel `lines`.

### 1. Struktur Baris Lirik
Format penulisan lirik menggunakan *tuple* di dalam *list*:
`("Teks Lirik", Jeda_Setelah_Baris, Kecepatan_Ketik)`

```python
lines = [
    # Contoh: Lirik normal
    ("No one's gotta know", 0.5, 0.08), 
    
    # Contoh: Lirik cepat (beat cepat/rap)
    ("Low, low, low, lowkey", 0.3, 0.04), 
    
    # Contoh: Lirik lambat (dramatis/vibrato lama)
    ("Till the sun starts waking", 1.2, 0.2),
]


### 2. Parameter Detail
Parameter	Deskripsi	Rekomendasi
Teks Lirik	Kalimat yang akan ditampilkan.	Gunakan \n untuk baris baru manual.
Jeda Baris	Waktu tunggu (detik) sebelum lanjut ke baris berikutnya.	0.5 - 2.0 detik.
Speed Type	Jeda antar karakter (detik). Semakin kecil, semakin cepat.	0.05 (Cepat), 0.1 (Sedang), 0.2 (Lambat).
