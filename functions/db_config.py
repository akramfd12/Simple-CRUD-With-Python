#import library
import mysql.connector
from dotenv import load_dotenv
import os

#load env
load_dotenv('db.env')

#input username and password database
db_host = os.getenv("mysql_host")
user_name = os.getenv("mysql_username") 
pwd = os.getenv("mysql_password")
db_name = os.getenv("mysql_database")

#make variabel to connect database
db = mysql.connector.connect(
    host = db_host,
    user = user_name,
    password = pwd,
    database = db_name,
    )

#insert query data book
def create_data_book (title, writer, genre, publication_year, publisher):
    cursor_create_book = db.cursor()
    cursor_create_book.execute("""INSERT INTO book (title, writer, genre, publication_year,publisher, recorddate)
                               VALUES (%s, %s,%s, %s, %s, NOW())""", (title, writer, genre, publication_year, publisher))
    db.commit()
    cursor_create_book.close()

#read query data book
def read_data_book():
    cursor_read_book = db.cursor(dictionary=True)
    cursor_read_book.execute("SELECT * FROM book")
    rows = cursor_read_book.fetchall()
    cursor_read_book.close()
    return rows

#update query data book
def update_data_book(id_updatebook, title, writer, genre, publication_year, publisher):
    cursor_update_book = db.cursor()
    cursor_update_book.execute(""" UPDATE book SET title = %s, writer = %s, genre = %s, 
                              publication_year = %s, publisher = %s, recorddate = NOW() 
                              WHERE id = %s """, 
                         (title, writer, genre, publication_year, publisher, id_updatebook))
    db.commit()
    cursor_update_book.close()

#delete query data book
def delete_data_book(id_deletebook):
    cursor_delete_book = db.cursor()
    cursor_delete_book.execute(""" DELETE FROM book WHERE id = %s  """,(id_deletebook,))
    db.commit()
    cursor_delete_book.close()

#insert query data pinjam
def create_data_pinjam (id_buku, nama_pinjam, tanggal_pinjam, lamapinjam):
    cursor_create_pinjam = db.cursor()
    cursor_create_pinjam.execute("""INSERT INTO pinjam (id_buku, nama_pinjam, tanggal_pinjam, tanggal_selesai, lamahari_pinjam, flag_pinjam, recorddate)
                                 VALUES (%s, %s, %s, %s, %s, %s, NOW())""", 
                                 (id_buku, nama_pinjam, tanggal_pinjam, None, lamapinjam, "borrowed",))
    db.commit()
    cursor_create_pinjam.close()

#read query data pinjam
def read_data_pinjam():
    cursor_read_pinjam = db.cursor(dictionary=True)
    cursor_read_pinjam.execute("SELECT * FROM pinjam")
    rows = cursor_read_pinjam.fetchall()
    cursor_read_pinjam.close()
    return rows

#update flag dan tanggal selesai pinjam
def update_data_flagpinjam(tanggal_selesai, id_pinjam):
    cursor_update_flagpinjam = db.cursor()
    cursor_update_flagpinjam.execute(""" UPDATE pinjam SET tanggal_selesai = %s, flag_pinjam = %s, recorddate = NOW() WHERE id = %s """, 
                         (tanggal_selesai, "finished", id_pinjam))
    db.commit()
    cursor_update_flagpinjam.close()

def close_conn():
    db.close

