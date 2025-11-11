from .db_config import update_data_book, update_data_flagpinjam

def update_book(id_updatebook): 
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
        
    publication_year = input("Masukkan Tahun Terbit (Harus dalam angka): ")
    while publication_year == '':
        print("Tahun Terbit tidak boleh kosong")
        publication_year = input("Masukkan Tahun Terbit (Harus dalam angka): ")

    publisher = input("Masukkan Nama Penerbit: ")
    while publisher == '':
        print("Nama penerbit tidak boleh kosong")
        publisher = input("Masukkan nama penerbit: ")
    
    update_data_book(id_updatebook, title, writer, genre, publication_year, publisher)
    print("Data buku berhasil diupdate!")

def update_flagpinjam(id_pinjam):
    tanggal_selesai = input("Masukkan tanggal selesai (format: YYYY-MM-DD): ").strip()
    while tanggal_selesai == '':
        print("Tanggal selesai tidak boleh kosong")
        tanggal_selesai = input("Masukkan tanggal selesai (format: YYYY-MM-DD): ").strip()

    update_data_flagpinjam(tanggal_selesai, id_pinjam)
    print("Buku berhasil dikembalikan!")

