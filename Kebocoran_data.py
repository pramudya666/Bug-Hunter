import os
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from rich.console import Console
from rich.table import Table

console = Console()

def check_broken_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        console.print(f"[red]Error fetching {url}: {e}[/red]")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    broken_links = []

    for link in links:
        link_url = link['href']
        if not link_url.startswith('http'):
            continue
        
        try:
            link_response = requests.head(link_url, allow_redirects=True)
            if link_response.status_code != 200:
                broken_links.append(link_url)
        except requests.RequestException as e:
            broken_links.append(link_url)

    return broken_links

def search_google(query):
    results = []
    for url in search(query, num_results=10):
        results.append(url)
    return results

def run_sqlmap(target):
    os.system(f"sqlmap -u {target} --batch")

def run_nmap(target):
    os.system(f"nmap {target}")

def run_bandit(target):
    os.system(f"bandit -r {target}")

def run_wafw00f(target):
    os.system(f"wafw00f {target}")

def main():
    url = input("Masukkan URL website yang ingin diperiksa: ")
    
    console.print(f"[blue]Memeriksa tautan rusak di {url}...[/blue]")
    broken_links = check_broken_links(url)
    if broken_links:
        console.print("[red]Tautan rusak ditemukan:[/red]")
        for link in broken_links:
            console.print(link)
    else:
        console.print("[green]Tidak ada tautan rusak ditemukan.[/green]")

    console.print(f"\n[blue]Mencari informasi di Google untuk {url}...[/blue]")
    google_results = search_google(url)
    console.print("[green]Hasil pencarian Google:[/green]")
    for result in google_results:
        console.print(result)

    console.print(f"\n[blue]Menjalankan SQLMap pada {url}...[/blue]")
    run_sqlmap(url)

    console.print(f"\n[blue]Menjalankan Nmap pada {url}...[/blue]")
    run_nmap(url)

    console.print(f"\n[blue]Menjalankan Bandit pada {url}...[/blue]")
    run_bandit(url)

    console.print(f"\n[blue]Menjalankan WAFW00F pada {url}...[/blue]")
    run_wafw00f(url)

if __name__ == "__main__":
    main()