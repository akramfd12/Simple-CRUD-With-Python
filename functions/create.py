from .db_config import create_data_book, create_data_pinjam

def create_book():
    title = input("Masukkan Judul Buku: ")
    while title == '':
        print("Judul tidak boleh kosong")
        title = input("Masukkan Judul Buku: ")

    writer = input("Masukkan Penulis: ")
    while writer == '':
        print("Penulis tidak boleh kosong")
        writer = input("Masukkan Penulis: ")

    genre = input("Masukkan Genre: ")
    while genre == '':
        print("Genre tidak boleh kosong")
        genre = input("Masukkan Genre: ")
        
    publication_year = int(input("Masukkan Tahun Terbit (Harus dalam angka): "))
    while publication_year == '':
        print("Tahun Terbit tidak boleh kosong")
        publication_year = int(input("Masukkan Tahun Terbit (Harus dalam angka): "))

    publisher = input("Masukkan Nama Penerbit: ")
    while publisher == '':
        print("Nama penerbit tidak boleh kosong")
        publisher = input("Masukkan nama penerbit: ")

    create_data_book(title, writer, genre, publication_year,publisher)
    print("Data buku berhasil dibuat!")

def create_pinjam():
    id_buku = input("Masukkan ID buku: ")
    while id_buku == '':
        print("ID buku tidak boleh kosong")
        id_buku = input("Masukkan ID Buku: ")

    nama_pinjam = input("Masukkan nama peminjam: ")
    while nama_pinjam == '':
        print("Nama peminjam tidak boleh kosong")
        nama_pinjam = input("Masukkan nama peminjam: ")

    tanggal_pinjam = input("Masukkan tanggal pinjam (format: YYYY-MM-DD): ")
    while tanggal_pinjam == '':
        print("Tanggal Pinjam tidak boleh kosong")
        tanggal_pinjam = input("Masukkan tanggal pinjam (format: YYYY-MM-DD): ")
        
    lamapinjam = int(input("Masukkan durasi pinjam (Hari): "))
    while lamapinjam == '':
        print("Durasi pinjam tidak boleh kosong")
        lamapinjam = input("Masukkan durasi pinjam (Hari): ")

    create_data_pinjam(id_buku, nama_pinjam, tanggal_pinjam, lamapinjam)
    print("Data peminjaman buku berhasil dibuat!")
