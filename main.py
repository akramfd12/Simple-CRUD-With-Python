#Import Library
import sys
import pandas as pd
from functions.create import create_book, create_pinjam
from functions.update import update_book, update_flagpinjam
from functions.read import read_book, search_book, read_pinjam
from functions.delete import delete_book
from functions.exitprog import close_prog
from functions.menu import * 

def test():
    df = read_pinjam()
    print(df)
    input_user = (input("Masukkan ID: "))
    update_flagpinjam(input_user)

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
            df = read_book()
            print(df)
            print(menu_search())
            while True:
                input_search_book = int(input("\nMasukkan angka: "))
                if input_search_book == 1:
                    input_user_read = int(input("\nMasukkan ID buku: "))
                    df_search = search_book(input_user_read)
                    print(df_search)
                    print(menu_search())
                elif input_search_book == 2:
                    # keluar dari menu search → kembali ke menu admin
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
            df = read_book()
            print(df)
            input_pilih_delete = input("\nMasukkan ID yang mau dihapus: ")
            delete_book(input_pilih_delete)

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
            df = read_pinjam()
            print(df)

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