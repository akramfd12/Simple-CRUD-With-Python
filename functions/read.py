from .db_config import read_data_book,read_data_pinjam
import pandas as pd
def read_book():
    print("Menampilkan Daftar Buku")
    df = pd.DataFrame(read_data_book())
    return df

def search_book(id):
    df = read_book()
    df = df[df['id'] == id]
    return df

def read_pinjam():
    print("Menampilkan Daftar Pinjam")
    df = pd.DataFrame(read_data_pinjam())
    df.rename(columns={
    'lamahari_pinjam': 'lamahari',
    'flag_pinjam': 'status'}, inplace=True)
    return df