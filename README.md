# 🕵️ IP Validator: Cek Alamat IPv4

> "Maaf, IP kamu tidak terdaftar di daftar tamu. Silakan putar balik." 🚫

Project kecil ini adalah **satpam digital** yang tugasnya cuma satu: ngecek apakah sebuah alamat IPv4 itu **asli** atau **abal-abal**. Dibuat pakai Python, dikawal pakai **TDD** (Test-Driven Development), dan ditulis sambil ngeluh karena `true` ternyata harus `True`. 😭

---

## 🤔 Ini Apaan Sih?

Kamu kasih alamat IP, dia jawab valid atau nggak. Udah, gitu aja. Simpel, tapi lumayan bikin pusing kalau salah titik atau salah spasi.

Contoh IP yang **lolos** masuk 🎉:
- `192.168.1.1` (IP andalan semua router di dunia)
- `10.0.0.1`
- `255.255.255.255`

Contoh IP yang **ditendang** 🥾:
- `256.100.50.25` → angkanya kebanyakan, kayak porsi nasi padang
- `192.abc.1.1` → ini IP atau password wifi?
- `10.10.10` → kurang satu, ibarat sendal cuma sebelah
- `10.10.10.10.10` → kelebihan satu, kayak tamu yang nggak diundang

---

## 📏 Aturan Mainnya

Alamat IPv4 dianggap valid kalau:

1. Terdiri dari **tepat 4 bagian**, dipisah titik (`.`)
2. Tiap bagian harus **angka** (huruf dilarang masuk 🙅)
3. Tiap angka harus ada di rentang **0 sampai 255**

Selain itu? Ditolak. Satpamnya galak. 😤

---

## 🚀 Cara Pakai

### 1. Clone dulu repo-nya

```bash
git clone https://github.com/vio12-porto/ip_validator_py.git
cd ip_validator_py
```

### 2. Jalankan program interaktif

```bash
python3 main.py
```

Nanti kamu disuruh masukin IP. Ketik `exit` kalau udah capek.

```
Enter an IPv4 address to validate (or 'exit' to quit): 192.168.1.1
✅ '192.168.1.1' is a valid IPv4 address.

Enter an IPv4 address to validate (or 'exit' to quit): 999.1.1.1
❌ '999.1.1.1' is NOT a valid IPv4 address.

Enter an IPv4 address to validate (or 'exit' to quit): exit
Exiting the validator. Goodbye!
```

> Di Windows, kalau `python3` nggak jalan, coba `python main.py` atau `py main.py`.

### 3. Pakai langsung di kode kamu

```python
from ip_validator import IPValidator

validator = IPValidator()
print(validator.is_valid_ipv4("192.168.1.1"))   # True
print(validator.is_valid_ipv4("256.1.1.1"))     # False
```

---

## 🧪 Jalankan Test

Ada 5 test yang siap menguji kesabaran, eh, kode kamu:

```bash
python3 test_ip_validator_class.py
```

Kalau semuanya `ok`, berarti kamu berhasil. Kalau ada yang merah, tarik napas dulu, baca error-nya pelan-pelan, biasanya cuma salah ketik. 🍵

| Test | Ngecek apa |
|------|------------|
| `test_valid_ipv4` | IP normal harus lolos |
| `test_invalid_ipv4_letters` | Ada huruf? Tolak |
| `test_invalid_ipv4_out_of_range` | Angka di atas 255? Tolak |
| `test_invalid_ipv4_too_few_octets` | Kurang dari 4 bagian? Tolak |
| `test_invalid_ipv4_too_many_octets` | Lebih dari 4 bagian? Tolak |

---

## 📁 Isi Folder

```
ip_validator_py/
├── ip_validator.py              # Otak si satpam 🧠
├── main.py                      # Program interaktifnya 💬
├── test_ip_validator_class.py   # Tukang tes, galak tapi adil 🔍
└── README.md                    # Kamu lagi baca ini 👋
```

---

## 🧠 Cerita TDD Singkat

Project ini dibuat dengan siklus **Red → Green → Refactor**:

- 🔴 **Red**: tulis test dulu, method masih `pass`, test gagal (`None is not true`)
- 🟢 **Green**: tulis kode secukupnya sampai test lolos
- 🔵 **Refactor**: rapikan kode tanpa bikin test merah lagi

Moral ceritanya: **jangan lupa hapus `pass` setelah nulis kodenya.** Percayalah, ini pengalaman pribadi. 🫠

---

## 🐛 Kesalahan Klasik (Hall of Shame)

Bug-bug yang pernah mampir waktu bikin project ini:

- `def is _valid_ipv4` ← ada spasi nyasar di nama fungsi
- `return true` ← Python bilang: "true siapa? Maksud kamu `True`?"
- Indentasi campur tab dan spasi ← Pylance langsung emosi
- `git push` ditolak ← ternyata GitHub udah punya isi duluan

---

## 📜 Lisensi

Bebas dipakai, bebas dicontek, bebas dijadikan bahan belajar. Kalau berguna, kasih ⭐ ya, itu gratis dan bikin penulisnya senyum seharian.

---

<p align="center">
  Dibuat dengan ☕, kesabaran, dan banyak <code>Ctrl+S</code> yang kelupaan.
</p>
