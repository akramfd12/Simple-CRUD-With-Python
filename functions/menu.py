def menu_utama ():
    menu_utama = """
    Selamat datang di Perpustakaan
    Menu Utama:
    1. Admin
    2. Pinjam Buku
    3. Exit Program
    """
    return menu_utama

def menu_admin():
    menu_admin = """
    Selamat datang di Menu Admin
    Menu Admin:
    1. Menambahkan daftar buku
    2. Menampilkan Data
    3. Mengupdate Data 
    4. Menghapus Data
    5. Visualisasi Data
    6. Statistik Data
    7. Kembali ke Menu Utama
    8. Exit Program
    """
    return menu_admin

def menu_pinjam():
    menu_pinjam = """
    Selamat datang di Menu Peminjaman Buku
    Menu Peminjaman Buku:
    1. Pinjam Buku Baru
    2. Selesaikan Pinjaman
    3. Daftar Pinjam
    4. Kembali ke Menu Utama
    5. Exit Program
    """
    return menu_pinjam

def menu_search_book():
    menu_search = """
    Search Book
    1. Cari Buku
    2. Kembali ke Menu Sebelumnya
    """
    return menu_search 

def menu_admin_read():
    menu_admin_read = """
    Menu Search
    1. Daftar Buku
    2. Daftar Peminjam Buku
    3. Kembali ke Menu Admin
    """
    return menu_admin_read 

def menu_search_pinjam():
    menu_search = """
    Search Book
    1. Cari Peminjam Buku
    2. Kembali Ke Menu Sebelumnya
    """
    return menu_search 

def menu_delete():
    menu_delete = """
    Menu Delete
    1. Hapus Buku
    2. Hapus Peminjam
    3. Kembali Ke Menu Sebelumnya
    """
    return menu_delete 

def menu_stat_total():
    menu_stat_total = """
    Menu Statistik
    1. Tanpa Filter
    2. Filter Tahun
    3. Filter Tahun dan Bulan
    4. Kembali ke Menu Sebelumnya
    """
    return menu_stat_total

def menu_visualisasi():
    menu_vis = """
    Menu Visualisasi
    1. Barlplot
    2. Histogram
    3. Lineplot
    4. Scatterplot
    5. pivotdata
    6. Kembali ke Menu Sebelumnya
    """
    return menu_vis