# ✨ WIBUVPN LITE (Optimized V9) ✨

Script Auto-Install VPN Premium super ringan & super cepat yang telah dioptimalkan khusus untuk efisiensi dan keamanan.

## 🚀 Fitur & Optimasi Terbaru
- **Anti-Nyangkut (IPv6 Fix):** Proses instalasi 100% mulus karena sistem otomatis melumpuhkan IPv6 yang sering membuat `wget` mentok di VPS baru.
- **Auto Non-Interactive:** Tidak ada lagi dialog interaktif (layar pink) yang mengganggu saat update paket instalasi awal.
- **Bebas Link Iklan/OpenClash:** Output pembuatan akun via terminal maupun Bot Telegram kini sudah 100% bersih dari embel-embel link OpenClash yang tidak perlu.
- **Bot Telegram Super Stabil:** Perbaikan total pada struktur Bot Telegram (Bot Give, Private, Public, dll) untuk mencegah *error database locked* (SQLite) akibat bentrok *session*.
- **Tampilan Premium & Bersih:** Penamaan bot dan menu sudah diseragamkan dengan *brand* `FREE WIBUVPNSTORE`.
- **Bebas Tracker:** Terhubung eksklusif hanya ke repositori perizinan IP milik Anda sendiri (`WBVPN/WIBUVPN-LITE`).

---

## 🛠️ Cara Instalasi (2 Langkah Aman)

Untuk memastikan VPS dalam keadaan bersih dan kernel terbaru sebelum instalasi VPN, ikuti 2 langkah berikut:

**❇️ Langkah Pertama (Update & Restart):**
```bash
export DEBIAN_FRONTEND=noninteractive NEEDRESTART_MODE=a NEEDRESTART_SUSPEND=1; apt update -y && apt upgrade -y && apt install -y wget curl screen dos2unix && reboot
```
*(Setelah menjalankan perintah di atas, VPS Anda akan terputus/restart otomatis. Tunggu 1-2 menit, lalu login kembali ke VPS Anda).*

**❇️ Langkah Kedua (Instalasi Inti):**
```bash
sysctl -w net.ipv6.conf.all.disable_ipv6=1 && sysctl -w net.ipv6.conf.default.disable_ipv6=1 && wget -O install.sh https://raw.githubusercontent.com/WBVPN/WIBUVPN-LITE/main/install.sh && chmod +x install.sh && screen -S setup-session ./install.sh
```

---

## 🔄 Cara Menghubungkan Ulang (Jika Terputus)
Jika saat proses instalasi VPS Anda *disconnected* atau terputus koneksinya, tidak perlu khawatir. Anda bisa kembali ke layar instalasi yang sedang berjalan dengan perintah:

```bash
screen -r -d setup-session
```

---

*Hak Cipta © Dioptimalkan secara eksklusif untuk WBVPN*