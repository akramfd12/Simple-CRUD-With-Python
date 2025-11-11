-- Create Database
CREATE DATABASE library_db;

-- Create Table book
CREATE TABLE IF NOT EXISTS `book` (
  `id` INT auto_increment PRIMARY KEY,
  `title` varchar(255) DEFAULT NULL,
  `writer` varchar(255) DEFAULT NULL,
  `genre` varchar(255) DEFAULT NULL,
  `publication_year` int DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `recorddate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Create Table pinjam
 CREATE TABLE IF NOT EXISTS `pinjam` (
  `id` INT auto_increment PRIMARY KEY,
  `id_buku` INT DEFAULT NULL, 
  `nama_pinjam` varchar(255) DEFAULT NULL,
  `tanggal_pinjam` DATE DEFAULT NULL,
  `tanggal_selesai` DATE DEFAULT NULL,
  `lamahari_pinjam` INT DEFAULT NULL,
  `flag_pinjam` varchar(255) DEFAULT NULL,
  `recorddate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

