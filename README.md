# cryptscraper

**Website HTML Downloader - Terminal-Based Tool**

Tools sederhana untuk mendownload HTML dari website publik dengan tampilan terminal yang menarik.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Termux](https://img.shields.io/badge/Termux-Supported-green)
![Platform](https://img.shields.io/badge/Platform-Android%2FLinux-orange)

---

## Fitur Utama
- [x] Download HTML lengkap dari website publik
- [x] Preview judul, status code, dan ukuran file sebelum download
- [x] Tampilan terminal dengan warna dan animasi keren
- [x] File disimpan otomatis di folder terorganisir
- [x] Validasi URL otomatis
- [x] Bisa scrape website berulang-ulang tanpa restart

## 📦 Instalasi di Termux

### 1. Update Package Termux
```bash
pkg update && pkg upgrade
```

2. Install Python & Git

```bash
pkg install python git
```

3. Install Module Python yang Diperlukan

```bash
pip install requests beautifulsoup4
```

4. Download CryptScraper

```bash
git clone https://github.com/Tr4LL 77/cryptscraper
```

5. Masuk ke Folder CryptScraper

```bash
cd cryptscraper
```

🚀 Cara Menggunakan

Menjalankan Tools:

```bash
python htmlscrape.py
```

Langkah Penggunaan:

1. Ketik URL website (contoh: https://example.com)
2. Tunggu proses download (loading animation)
3. Lihat preview informasi website
4. Konfirmasi save (tekan Y untuk simpan, N untuk batal)
5. File HTML tersimpan otomatis di folder Download

Contoh Penggunaan Lengkap:

```bash
$ python htmlscrape.py

Initializing website data retrieval process...

┌────────────────────────────────────────────┐
│            TARGET WEBSITE INPUT            │
├────────────────────────────────────────────┤
│ • Enter a public website URL                │
│ • Must include http:// or https://          │
│ • Example: https://example.com              │
└────────────────────────────────────────────┘

[ CryptScraper ] >>> https://github.com

┌───────────────────────────── Target Preview ───────────────────────────┐
│ Title       : GitHub: Let's build from here · GitHub
│ Status Code : 200
│ Size        : ~245.78 KB
└────────────────────────────────────────────────────────────────────────┘

Do you want to save this HTML? [Y/n]: y

Process completed successfully.
HTML file has been saved.
File location:
/storage/emulated/0/Download/CryptScraper/Github_Let_s_build_from_here_GitHub.html
```

📁 Struktur Folder Output

Semua file disimpan di:

```
/storage/emulated/0/Download/CryptScraper/
├── website_title_1.html
├── website_title_2.html
├── another_site.html
└── ...
```

Catatan: Nama file otomatis diambil dari judul website dan karakter spesial diganti dengan underscore.

⚙️ Module yang Diperlukan

· requests - Untuk mengambil data dari website
· beautifulsoup4 - Untuk parsing HTML

🎨 Tampilan Tools

```
            CryptScraper
        Website HTML Downloader
          Terminal-Based Tool
```

❓ Troubleshooting

Error: "ModuleNotFoundError: No module named 'requests'"

```bash
pip install requests beautifulsoup4
```

Error: "Command 'git' not found"

```bash
pkg install git
```

Website tidak bisa diakses

· Pastikan URL benar (http:// atau https://)
· Cek koneksi internet
· Website mungkin memblokir scraper

⚠️ Disclaimer & Etika Penggunaan

PERINGATAN PENTING:

1. ❌ JANGAN gunakan untuk website ilegal
2. ❌ JANGAN scrape website tanpa izin pemilik
3. ❌ JANGAN gunakan untuk aktivitas malicious
4. ✅ GUNAKAN hanya untuk website testing pribadi
5. ✅ GUNAKAN hanya untuk tujuan edukasi
6. ✅ HORMATI robots.txt dan terms of service

Penulis tidak bertanggung jawab atas penyalahgunaan tools ini.
