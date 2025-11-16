import pandas as pd
from .read import merge_book_pinjam

# def pinjam_statistic_total (id1,id2)):
#     df = merge_book_pinjam()
#     df = df[["id_buku","title"]]
#     df_clean = df.rename(columns={"id_buku": "total"})
#     count_title = df_clean.groupby(["title"]).count()
#     # count_title = count_title.sort_values(by=['total'], ascending=False).head(5)
#     count_title = count_title.describe()
#     print(count_title)

def pinjam_statistic_total (column_total):
    df = merge_book_pinjam()
    df_total = df[["id_buku",column_total]]
    df_clean = df_total.rename(columns={"id_buku": "total"})
    count_book_groupby = df_clean.groupby(column_total).count()
    count_book = count_book_groupby.sort_values(by=['total'], ascending=False)
    mean_book = count_book_groupby.mean().item()
    median_book = count_book_groupby.median().item()
    unique_orang = df["nama_pinjam"].nunique()
    # count_title = count_title.describe()
    print(count_book)
    print(f"Mean:{mean_book}")
    print(f"Median:{median_book}")
    print(f"Jumlah unik orang:{unique_orang}")

def pinjam_statistic_total_year (column_total, year_pinjam):
    df = merge_book_pinjam()
    df_total_filter = df[df["year_pinjam"] == year_pinjam] 
    df_total = df_total_filter[["id_buku",column_total]]
    df_clean = df_total.rename(columns={"id_buku": "total"})
    count_book_groupby = df_clean.groupby(column_total).count()
    count_book = count_book_groupby.sort_values(by=['total'], ascending=False)
    mean_book = count_book_groupby.mean().item()
    median_book = count_book_groupby.median().item()
    unique_orang = df_total_filter["nama_pinjam"].nunique()
    # count_title = count_title.describe()
    print(count_book)
    print(f"Mean:{mean_book}")
    print(f"Median:{median_book}")
    print(f"Jumlah unik orang:{unique_orang}")

def pinjam_statistic_total_year_month (column_total, year_pinjam, month_start, month_end):
    df = merge_book_pinjam()
    df_total_filter_year = df[df["year_pinjam"] == year_pinjam]
    df_total_filter = df_total_filter_year[(df_total_filter_year['month_pinjam'] >= month_start) & (df_total_filter_year['month_pinjam'] <= month_end)]
    df_total = df_total_filter[["id_buku",column_total]]
    df_clean = df_total.rename(columns={"id_buku": "total"})
    count_book_groupby = df_clean.groupby(column_total).count()
    count_book = count_book_groupby.sort_values(by=['total'], ascending=False)
    mean_book = count_book_groupby.mean().item()
    median_book = count_book_groupby.median().item()
    unique_orang = df_total_filter["nama_pinjam"].nunique()
    # count_title = count_title.describe()
    print(count_book)
    print(f"Mean:{mean_book}")
    print(f"Median:{median_book}")
    print(f"Jumlah unik orang:{unique_orang}")
    