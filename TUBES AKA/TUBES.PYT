import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import random

# Metode Bubble Sort
def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j]["popularity"] > data[j + 1]["popularity"]:
                data[j], data[j + 1] = data[j + 1], data[j]

# Data dummy Spotify (genre, artis, popularitas)
def generate_spotify_data(size):
    genres = ["Pop", "Rock", "Jazz", "Hip-Hop", "Classical"]
    artists = ["Artist A", "Artist B", "Artist C", "Artist D", "Artist E"]
    return [
        {
            "genre": random.choice(genres),
            "artist": random.choice(artists),
            "popularity": random.randint(1, 100)
        }
        for _ in range(size)
    ]

# Grafik untuk menyimpan data
sizes = []
bubble_sort_times = []

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, bubble_sort_times, label='Bubble Sort', marker='o', linestyle='-')
    plt.title('Bubble Sort Performance on Spotify Data')
    plt.xlabel('Number of Songs')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Fungsi untuk mencetak tabel waktu eksekusi
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Number of Songs", "Bubble Sort Time (s)"]
    for i in range(len(sizes)):
        table.add_row([sizes[i], bubble_sort_times[i]])
    print(table)

# Program utama
while True:
    try:
        size = int(input("Masukkan jumlah lagu (atau ketik -1 untuk keluar): "))
        if size == -1:
            print("Program selesai. Terima kasih!")
            break
        if size <= 0:
            print("Masukkan jumlah lagu yang positif!")
            continue

        sizes.append(size)

        # Generate data Spotify
        spotify_data = generate_spotify_data(size)

        # Ukur waktu eksekusi Bubble Sort
        start_time = time.time()
        bubble_sort(spotify_data)
        bubble_sort_times.append(time.time() - start_time)

        # Cetak tabel waktu eksekusi
        print_execution_table()

        # Perbarui grafik
        update_graph()

    except ValueError:
        print("Masukkan jumlah lagu yang valid!")
