import requests
from colorama import Fore, Style

def start():
    print(Fore.CYAN + "\n[+] Kullanıcı Adı Taraması Başladı\n" + Style.RESET_ALL)
    username = input(Fore.YELLOW + "[?] Kullanıcı adı gir: " + Style.RESET_ALL)

    sites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "YouTube": f"https://www.youtube.com/{username}",
    }

    for name, url in sites.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] {name}: BULUNDU ➜ {url}")
            else:
                print(Fore.RED + f"[-] {name}: YOK")
        except requests.exceptions.RequestException:
            print(Fore.MAGENTA + f"[!] {name}: Hata (siteye ulaşılamadı)")

    print(Style.RESET_ALL)
