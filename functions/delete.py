from .db_config import delete_data_book
def delete_book(input_pilih_delete):
    # input_pilih_delete = input("Masukkan Judul Buku: ")
    delete_data_book(input_pilih_delete)
    print("Data buku berhasil dihapus!")