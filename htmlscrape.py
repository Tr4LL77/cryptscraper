import os, sys, time, re, requests
from bs4 import BeautifulSoup

# ===== TERMINAL COLORS =====
MERAH   = "\033[91m"
MERAHG  = "\033[31m"
HIJAU   = "\033[92m"
CIAN    = "\033[96m"
UNGU    = "\033[95m"
PUTIH   = "\033[97m"
TEBAL   = "\033[1m"
REDUP   = "\033[2m"
RESET   = "\033[0m"

# ===== UTILITY FUNCTIONS =====
def bersihkan():
    os.system("clear")

def ketik_pelan(teks, d=0.015):
    for c in teks:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(d)
    print()

def glitch_aclls(teks):
    for _ in range(3):
        bersihkan()
        print(MERAHG + TEBAL + teks + RESET)
        time.sleep(0.08)

def loading_aclls(pesan):
    for i in range(1, 7):
        sys.stdout.write(f"\r{REDUP}{pesan} [{'#'*i}{'.'*(6-i)}]{RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
    print()

def nama_aman(teks):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', teks)

# ===== BANNER =====
def banner_aclls():
    bersihkan()
    print(MERAH + TEBAL)
    print(r"""
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀
⣼⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣧⠀
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⡄
⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿
⢿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿
⠘⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿
⠀⢻⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡟
⠀⠀⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠟⠀
⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣶⣤⣀⣀⣀⣠⣴⣾⣿⣿⣿⣿⡿⠋⠀⠀
⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
            CryptScraper
        Website HTML Downloader
          Terminal-Based Tool
    """)
    print(RESET)

# ===== MAIN PROGRAM =====
def main():
    while True:
        banner_aclls()

        ketik_pelan(UNGU + "Initializing website data retrieval process..." + RESET)
        time.sleep(0.5)

        glitch_aclls("STARTING PROCESS")
        loading_aclls("Preparing connection")

        # ===== IMPROVED URL INPUT UI =====
        print(CIAN + TEBAL + "\n┌────────────────────────────────────────────┐" + RESET)
        print(CIAN + TEBAL + "│            TARGET WEBSITE INPUT            │" + RESET)
        print(CIAN + TEBAL + "├────────────────────────────────────────────┤" + RESET)
        print(PUTIH + "│ • Enter a public website URL                │")
        print(PUTIH + "│ • Must include http:// or https://          │")
        print(PUTIH + "│ • Example: https://example.com              │")
        print(CIAN + TEBAL + "└────────────────────────────────────────────┘" + RESET)

        url = input(TEBAL + PUTIH + "\n[ CryptScraper ] >>> " + RESET).strip()

        if not url.startswith("http"):
            ketik_pelan(MERAH + "\nInvalid URL format." + RESET)
            time.sleep(1)
            continue

        headers = {
            "User-Agent": "CryptScraper-Terminal-Client"
        }

        ketik_pelan(MERAH + "\nConnecting to target server..." + RESET)
        loading_aclls("Downloading HTML content")

        try:
            r = requests.get(url, headers=headers, timeout=25)
            r.raise_for_status()
        except Exception as e:
            ketik_pelan(MERAH + f"\nFailed to retrieve data: {e}" + RESET)
            time.sleep(2)
            continue

        soup = BeautifulSoup(r.text, "html.parser")
        judul = soup.title.string if soup.title else "website_result"

        # ===== PREVIEW BEFORE SAVE =====
        status_code = r.status_code
        content_size = len(r.content)
        size_kb = round(content_size / 1024, 2)

        print(CIAN + TEBAL + "\n┌───────────────────────────── Target Preview ───────────────────────────┐" + RESET)
        print(PUTIH + f"│ Title       : {judul}")
        print(PUTIH + f"│ Status Code : {status_code}")
        print(PUTIH + f"│ Size        : ~{size_kb} KB")
        print(CIAN + TEBAL + "└────────────────────────────────────────────────────────────────────────┘" + RESET)

        confirm = input(TEBAL + PUTIH + "\nDo you want to save this HTML? [Y/n]: " + RESET).strip().lower()
        if confirm == "n":
            ketik_pelan(MERAH + "Skipped saving HTML for this URL.\n" + RESET)
            time.sleep(1)
            continue

        # ===== SAVE HTML =====
        nama_file = nama_aman(judul) + ".html"
        folder = "/storage/emulated/0/Download/CryptScraper"
        if not os.path.exists(folder):
            os.makedirs(folder)

        path_full = os.path.join(folder, nama_file)

        with open(path_full, "w", encoding="utf-8") as f:
            f.write(soup.prettify())

        ketik_pelan(HIJAU + "\nProcess completed successfully." + RESET)
        ketik_pelan(CIAN  + "HTML file has been saved." + RESET)
        ketik_pelan(PUTIH + f"File location:\n{path_full}" + RESET)

        # ===== REPEAT MENU =====
        print(CIAN + TEBAL + "\n────────────────────────────────────────────" + RESET)
        print(PUTIH + "1. Scrape another website")
        print(PUTIH + "2. Exit")
        choice = input(TEBAL + PUTIH + "Select option [1/2]: " + RESET).strip()

        if choice != "1":
            ketik_pelan(UNGU + "\nExiting CryptScraper. Goodbye." + RESET)
            break

# ===== EXECUTION =====
if __name__ == "__main__":
    main()