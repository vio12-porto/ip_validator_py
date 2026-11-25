# 🕵️ IP Validator: Cek Alamat IPv4

> "Maaf, IP kamu tidak terdaftar di daftar tamu. Silakan putar balik." 🚫

Project kecil ini adalah **satpam digital** yang tugasnya cuma satu: ngecek apakah sebuah alamat IPv4 itu **asli** atau **abal-abal**. Dibuat pakai Python, dikawal pakai **TDD** (Test-Driven Development), dan ditulis sambil ngeluh karena `true` ternyata harus `True`. 😭

---

## 🤔 Apa itu IP Validator?

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
Enter an IPv4 address to validate (or 'exit' to quit): 192.168.1.1
✅ '192.168.1.1' is a valid IPv4 address.

Enter an IPv4 address to validate (or 'exit' to quit): 999.1.1.1
❌ '999.1.1.1' is NOT a valid IPv4 address.

Enter an IPv4 address to validate (or 'exit' to quit): exit
Exiting the validator. Goodbye!
```

## 📁 Isi Folder

```
ip_validator_py/
├── ip_validator.py              # Otak si satpam 🧠
├── main.py                      # Program interaktifnya 💬
├── test_ip_validator_class.py   # Tukang tes, galak tapi adil 🔍
└── README.md                    # Kamu lagi baca ini 👋
```
