#Import Library
import sys
import pandas as pd
from functions.create import create_book, create_pinjam
from functions.update import update_book, update_flagpinjam
from functions.read import read_book, search_book, read_pinjam, search_pinjam, merge_book_pinjam
from functions.delete import delete_book, delete_pinjam
from functions.exitprog import close_prog
from functions.menu import * 

def test():
    pd.set_option('display.max_columns', None)
    df = merge_book_pinjam()
    print(df)
    # input_user = int((input("Masukkan ID: ")))
    # df_search_pinjam = search_pinjam(input_user)
    # print(df_search_pinjam)

def admin():
    pd.set_option('display.max_columns', None)
    run = True
    while run:
        print(menu_admin())
        input_user = int(input("Masukkan angka menu yang ingin dijalankan: "))
        #Input Daftar Buku
        if input_user == 1: 
            create_book()
            
        #Read Data
        if input_user == 2:
            while True:
                print(menu_admin_read())
                input_menu_read = int(input("\nMasukkan angka: ")) 
                #Menampilkan Data Buku
                if input_menu_read == 1:
                    df = read_book()
                    df_total_buku = len(df)
                    print(df)
                    print(f"Total Buku {df_total_buku}")
                    print(menu_search_book())
                    while True:
                        input_search_book = int(input("\nMasukkan angka: "))
                        #Search Book
                        if input_search_book == 1:
                            input_user_read = int(input("\nMasukkan ID buku: "))
                            df_search_book = search_book(input_user_read)
                            print(df_search_book)
                            print(menu_search_book())
                        elif input_search_book == 2:
                            # keluar dari menu search → kembali ke menu admin
                            break
                        else:
                            print("Pilihan tidak valid!")
                #Menampilkan Data Peminjaman
                elif input_menu_read == 2:
                    df_pinjam = read_pinjam()
                    df_total_buku = len(df_pinjam)
                    print(df_pinjam)
                    print(f"Total peminjam {df_total_buku}")
                    print(menu_search_pinjam())
                    while True :
                        input_search_pinjam = int(input("\nMasukkan angka: "))
                        #Search Peminjam
                        if input_search_pinjam == 1:
                            input_user_pinjam = int(input("\nMasukkan ID peminjam: "))
                            df_search_pinjam = search_pinjam(input_user_pinjam)
                            print(df_search_pinjam)
                        elif input_search_pinjam == 2:
                            # keluar dari menu search → kembali ke menu admin
                            break
                        else:
                            print("Pilihan tidak valid!")
                elif input_menu_read == 3:
                    break
                else:
                    print("Pilihan tidak valid!")

        #Update Data
        if input_user == 3:
            df = read_book()
            print(df)
            input_pilih_update = input("\nMasukkan ID yang mau diupdate: ")
            update_book(input_pilih_update)

        #Delete Data
        if input_user == 4:
            print(menu_delete())
            while True:
                print(menu_delete())
                input_delete = int(input("\nMasukkan angka: "))
                if input_delete == 1:
                    df = read_book()
                    print(df)
                    input_pilih_delete_book = int(input("\nMasukkan ID yang mau dihapus: "))
                    delete_book(input_pilih_delete_book)
                elif input_delete == 2:
                    df_pinjam = read_pinjam()
                    print(df_pinjam)
                    input_pilih_delete_pinjam = int(input("\nMasukkan ID yang mau dihapus: "))
                    delete_pinjam(input_pilih_delete_pinjam)
                elif input_delete == 3:
                    break
                else:
                    print("Pilihan tidak valid!")

        #Visualisasi data
        if input_user == 5:
            pass

        #Statistik data
        if input_user == 6:
            pass

        #Back to menu
        if input_user == 7:
            run = False

        #Selesai
        if input_user == 8:
            close_prog()
            sys.exit()

def pinjam_buku():
    pd.set_option('display.max_columns', None)
    run = True
    while run:
        print(menu_pinjam())
        input_menu_pinjam  = int(input("Pilih angka menu pinjam: "))
        #Input Pinjam
        if input_menu_pinjam == 1:
            create_pinjam()

        #Selesai Pinjam
        if input_menu_pinjam == 2:
            df = read_pinjam()
            print(df)
            input_user = (input("Masukkan ID: "))
            update_flagpinjam(input_user)

        #Read data daftar pinjam
        if input_menu_pinjam == 3:
            df_pinjam = read_pinjam()
            df_total_buku = len(df_pinjam)
            print(df_pinjam)
            print(f"Total peminjam {df_total_buku}")
            print(menu_search_pinjam())
            while True :
                input_search_pinjam = int(input("\nMasukkan angka: "))
                #Search Peminjam
                if input_search_pinjam == 1:
                    input_user_pinjam = int(input("\nMasukkan ID peminjam: "))
                    df_search_pinjam = search_pinjam(input_user_pinjam)
                    print(df_search_pinjam)
                elif input_search_pinjam == 2:
                    # keluar dari menu search → kembali ke menu admin
                    break
                else:
                    print("Pilihan tidak valid!")

        #Back to menu
        if input_menu_pinjam == 4:
            run = False
        
        #Selesai
        if input_menu_pinjam == 5:
            close_prog()
            sys.exit()

def main():
    run = True
    while run:
        print(menu_utama())
        input_menu_awal = int(input("Pilih angka menu utama: "))
        #MenuAdmin
        if input_menu_awal == 1:
            admin()
        #MenuPinjam
        if input_menu_awal == 2:
            pinjam_buku() 
        #Selesai
        if input_menu_awal == 3:
            close_prog()
            run = False 
        
if __name__ == "__main__":
    main()