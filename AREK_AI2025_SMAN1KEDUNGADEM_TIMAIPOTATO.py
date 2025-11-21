# ====================== WARNA ANSI ======================
H = "\033[92m"  # Hijau = Info Bot / Sukses
K = "\033[93m"  # Kuning = Daftar produk / Bantuan
M = "\033[91m"  # Merah = Error / Peringatan
C = "\033[96m"  # Cyan = Input user / Struk
R = "\033[0m"   # Reset warna
# ========================================================

products = {
    "potato": {"name": "Potato (Kentang Goreng Original)", "price": 2000},
    "cheese potato": {"name": "Cheese Potato (Kentang Keju Premium)", "price": 5000}
}

cart = {}

print(f"{H}Bot Sales: Halo! Selamat datang di toko kentang kami 😄{R}")
print(f"{H}Bot Sales: Ketik 'bantuan' untuk melihat daftar perintah!{R}")

while True:
    user = input(f"{C}Anda: {R}").lower().strip()

    # ================= EXIT ==================
    if user in ["exit", "keluar"]:
        print(f"{H}Bot Sales: Terima kasih sudah berbelanja! 👋{R}")
        break

    # ================= SAPA BOT ==================
    elif user in ["halo", "hi", "yo", "p"]:
        print(f"{H}Bot Sales: Ada yang bisa saya bantu?{R}")

    # ================= BANTUAN ==================
    elif user == "bantuan" in user or "help" in user:
        print(f"{K}Perintah Tersedia:")
        print(" - beli       : melihat menu pembelian")
        print(" - harga      : melihat daftar harga")
        print(" - keranjang  : lihat isi keranjang")
        print(" - struk      : cetak tagihan belanja")
        print(" - keluar     : keluar program" + R)

    # ================= BELI ==================
    elif user == "beli":
        print(f"{K}Daftar Menu Kami:")
        print(" 1. Potato (Original)")
        print("    Ukuran : Medium Cup")
        print("    Topping: Garam, Saus Tomat\n")
        print(" 2. Cheese Potato (Keju Premium)")
        print("    Ukuran : Large Cup")
        print("    Topping: Cheese Sauce, Mayo\n" + R)
        print(f"{H}Gunakan format: tambah [produk] [jumlah]{R}")

    # ================= HARGA ==================
    elif user == "harga":
        print(f"{K}Harga Menu:")
        for key, item in products.items():
            print(f" - {item['name']} : Rp{item['price']}{R}")

    # ================= TAMBAH PRODUK ==================
    elif user.startswith("tambah"):
        try:
            cmd, nama_qty = user.split(" ", 1)
            *nama_list, jumlah = nama_qty.split()
            nama = " ".join(nama_list)

            jumlah = int(jumlah)

            if nama in products:
                cart[nama] = cart.get(nama, 0) + jumlah
                print(f"{H}Berhasil tambah {jumlah} {nama} ke keranjang 🛒{R}")
            else:
                print(f"{M}Produk tidak ditemukan! Ketik 'harga' untuk lihat daftar produk{R}")

        except:
            print(f"{M}Format salah! Contoh: tambah cheese potato 2{R}")

    # ================= KERANJANG ==================
    elif user == "keranjang":
        if not cart:
            print(f"{M}Keranjang masih kosong 😅{R}")
        else:
            print(f"{C}Isi keranjang Anda:")
            for name, qty in cart.items():
                print(f" - {products[name]['name']} x{qty}")
            print(R)

    # ================= STRUK ==================
    elif user == "struk":
        if not cart:
            print(f"{M}Belum ada pesanan!{R}")
        else:
            print(f"{C}\n=== STRUK PEMBELIAN ===")
            total = 0
            for name, qty in cart.items():
                subtotal = products[name]["price"] * qty
                total += subtotal
                print(f"{products[name]['name']} x{qty} : Rp{subtotal}")
            print(f"TOTAL BAYAR : Rp{total}")
            print("======================={R}")
            print(f"{H}Bot Sales: Terima kasih sudah belanja 🤩{R}\n")

    # ================= UNKNOWN COMMAND ==================
    else:
        print(f"{M}Perintah tidak dikenal! Ketik 'bantuan' atau 'help' 👈{R}")
