import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from .stat_data import *

def filtered_year(year_pinjam):
    df = merge_book_pinjam()
    df = pd.DataFrame(df)
    df_filter = df[df['year_pinjam'] == year_pinjam]
    return df_filter

def barplot(kolom, year_pinjam):
    df = filtered_year(year_pinjam)
    df = pd.DataFrame(df)
    df_count = df.groupby(kolom)["id_buku"].count().reset_index(name='total')
    print(df_count)
    plt.figure()
    sns.barplot(data=df_count, x=kolom, y="total")
    plt.title(f"Rata-rata jumlah peminjam tahun {year_pinjam} berdasarkan {kolom}")
    plt.xlabel(kolom)
    plt.ylabel("total")
    plt.show()


def histogram(kolom, year_pinjam):
    df = filtered_year(year_pinjam)
    df = pd.DataFrame(df)
    # df_hist = df[kolom]
    # df_count = df.groupby(kolom)["id_buku"].count().reset_index(name='total')
    plt.figure()
    plt.hist(df[kolom], bins=10, color='skyblue', edgecolor='black')
    plt.title(f"Distribusi {kolom}")
    plt.xlabel(kolom)
    plt.ylabel('Frekuensi')
    plt.show()

def lineplot(kolom, year_pinjam):
    df = filtered_year(year_pinjam)
    df = pd.DataFrame(df)
    df_count = df.groupby(kolom)["id_buku"].count().reset_index(name='total')
    print(df_count)
    plt.figure()
    sns.lineplot(data=df_count, x=kolom, y="total", markers="o")
    plt.title(f"Trend jumlah peminjam tahun {year_pinjam} berdasarkan {kolom}")
    plt.xlabel(kolom)
    plt.ylabel("total")
    plt.show()

def scatterplot(kolom, year_pinjam):
    df = filtered_year(year_pinjam)
    df = pd.DataFrame(df)
    input_y = input("Masukkan 1 Kolom kembali: ")
    sns.scatterplot(x=kolom, y=input_y, data=df, palette='viridis')
    plt.title(f'Hubungan {kolom} dan {input_y}')
    plt.xlabel(kolom)
    plt.ylabel(input_y)
    plt.show()

def pivot_data():
    # df = filtered_year(year_pinjam)
    df = merge_book_pinjam()
    df = pd.DataFrame(df)
    # print(df)
    df_count = df.groupby(["year_pinjam", "month_pinjam"])["id_buku"].count().reset_index(name="total")
    df_pivot = df_count.pivot(index='year_pinjam', columns='month_pinjam', values='total')
    return(df_pivot)

def col_vis():
    df_merge = merge_book_pinjam()
    df_columns = df_merge[["title","genre","lamahari","month_pinjam","year_pinjam","flag_late","nama_pinjam"]]
    return df_columns.columns
   

