from .db_config import close_conn
def close_prog():
    print("Program dan koneksi sudah ditutup, terimakasih")
    close_conn()
