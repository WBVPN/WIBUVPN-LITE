# ✨ WIBUVPN LITE (Optimized V9) ✨

![Version](https://img.shields.io/badge/Version-9.0_Optimized-blue.svg)
![Status](https://img.shields.io/badge/Status-Stable_&_Clean-brightgreen.svg)
![OS](https://img.shields.io/badge/Supported_OS-Ubuntu_20.04_|_Debian_10-orange.svg)

Script Auto-Install VPN Premium super ringan & super cepat yang telah dioptimalkan khusus untuk efisiensi, anti-bug, dan keamanan tingkat tinggi.

## 💻 Kebutuhan Sistem (OS)
Script ini direkomendasikan dan dirancang khusus untuk berjalan dengan sangat lancar pada:
* **Ubuntu 20.04** (Sangat Direkomendasikan)
* **Debian 10**

## 🌐 Protokol & Layanan yang Didukung
* **SSH & OpenVPN:** Mendukung Websocket & Stunnel
* **Xray Core:** Vmess, Vless, Trojan, Shadowsocks (Multiport via HAProxy/Nginx)
* **SlowDNS:** DNS Tunneling Premium
* **NoobzVPN:** Protokol kustom anti-blokir berkecepatan tinggi

## 🚀 Fitur & Optimasi Terbaru
- **SSL Anti-Limit (ZeroSSL):** Pergantian engine sertifikat ke ZeroSSL. Tidak akan ada lagi *error* instalasi Nginx/HAProxy akibat limit harian/mingguan Let's Encrypt!
- **Anti-Nyangkut (IPv6 Fix):** Proses instalasi 100% mulus karena sistem otomatis melumpuhkan IPv6 yang sering membuat `wget` mentok di VPS baru.
- **Smart Auto-Backup:** Jadwal *backup* otomatis ke Telegram ditingkatkan menjadi setiap 12 jam agar VPS tidak terbebani proses *zip* yang terlalu sering.
- **Auto Non-Interactive:** Tidak ada lagi dialog interaktif (layar pink) yang mengganggu saat update paket instalasi awal.
- **Bebas Link Iklan/OpenClash:** Output pembuatan akun via terminal maupun Bot Telegram kini sudah 100% bersih dari embel-embel link iklan OpenClash.
- **Bot Telegram Super Stabil:** Perbaikan total pada struktur Bot Telegram untuk mencegah *error database locked* (SQLite) akibat bentrok *session* atau *spam token*.
- **Tampilan Premium & Bersih:** Penamaan bot dan menu sudah diseragamkan dengan *brand* `FREE WIBUVPNSTORE`.
- **Bebas Tracker:** Terhubung eksklusif hanya ke repositori perizinan IP milik Anda sendiri (`WBVPN/WIBUVPN-LITE`).

---

## 📞 Hubungi Developer
Untuk pertanyaan lebih lanjut atau pendaftaran IP, silakan hubungi:
👉 **[t.me/wibuvpn](https://t.me/wibuvpn)**

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