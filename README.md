# ✨ WIBUVPN LITE (Optimized V9) ✨

Script Auto-Install VPN Premium super ringan & super cepat yang telah dioptimalkan khusus untuk efisiensi dan keamanan.

## 🚀 Fitur & Optimasi
- **Bebas Tracker:** Terhubung eksklusif hanya ke repositori perizinan IP milik Anda sendiri (`WBVPN/WIBUVPN-LITE`).
- **JSDelivr CDN:** Membuka kecepatan download maksimal tanpa terkena *rate-limit* GitHub di VPS Indonesia.
- **Auto Non-Interactive:** Tidak ada lagi dialog interaktif yang mengganggu saat instalasi paket (anti-nyangkut di layar biru/pink).
- **Paralel Service:** *Restart* puluhan *service* dilakukan secara paralel, tidak perlu menunggu satu-satu.

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
sysctl -w net.ipv6.conf.all.disable_ipv6=1 && sysctl -w net.ipv6.conf.default.disable_ipv6=1 && wget -O install.sh https://raw.githubusercontent.com/WBVPN/WIBUVPN-LITE/main/install.sh && chmod +x install.sh && ./install.sh
```

---

## 🔄 Cara Menghubungkan Ulang (Jika Terputus)
Jika saat proses instalasi VPS Anda *disconnected* atau terputus koneksinya, tidak perlu khawatir. Anda bisa kembali ke layar instalasi yang sedang berjalan dengan perintah:

```bash
screen -r -d setup-session
```

---

*Hak Cipta © Dioptimalkan secara eksklusif untuk WBVPN*