import os
import subprocess
from googlesearch import search

def detect_waf(url):
    print(f"Mendeteksi WAF untuk {url}...")
    result = subprocess.run(['wafw00f', url], capture_output=True, text=True)
    print(result.stdout)

def detect_sql_injection(url):
    print(f"Mendeteksi kerentanan SQL Injection untuk {url}...")
    result = subprocess.run(['sqlmap', '-u', url, '--batch', '--dbs'], capture_output=True, text=True)
    print(result.stdout)

def main():
    query = input("Masukkan URL website yang ingin dianalisis: ")
    
    # Mencari informasi terkait website
    print("Mencari informasi terkait website...")
    for j in search(query, num_results=5):
        print(j)

    # Deteksi WAF
    detect_waf(query)

    # Deteksi SQL Injection
    detect_sql_injection(query)

if __name__ == "__main__":
    main()