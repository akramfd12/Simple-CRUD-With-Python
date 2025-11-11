from .db_config import delete_data_book, delete_data_pinjam
def delete_book(input_pilih_delete):
    # input_pilih_delete = input("Masukkan Judul Buku: ")
    delete_data_book(input_pilih_delete)
    print("Data buku berhasil dihapus!")

def delete_pinjam(input_pilih_delete):
    delete_data_pinjam(input_pilih_delete)
    print("Data peminjam berhasil dihapus")