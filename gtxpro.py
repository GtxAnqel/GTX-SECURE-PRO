# gtxpro.py

import os
from modules import userscan, ipscan, sitechecker

def menu():
    os.system("clear")
    print("""
███████╗████████╗██╗  ██╗██╗  ██╗███████╗ ██████╗ ██████╗ ███████╗
██╔════╝╚══██╔══╝██║  ██║╚██╗██╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
███████╗   ██║   ███████║ ╚███╔╝ █████╗  ██║   ██║██████╔╝███████╗
╚════██║   ██║   ██╔══██║ ██╔██╗ ██╔══╝  ██║   ██║██╔═══╝ ╚════██║
███████║   ██║   ██║  ██║██╔╝ ██╗███████╗╚██████╔╝██║     ███████║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝     ╚══════╝

         🌐 GTX-SECURE PRO | Etik Hacker Terminali
    """)

    print("""
[1] Kullanıcı Adı Taraması (UserScan)
[2] IP Analiz (IPScan)
[3] Site Güvenlik Kontrolü (SiteChecker)
[0] Çıkış
""")

def main():
    while True:
        menu()
        sec = input("[?] Seçimin: ")
        if sec == "1":
            userscan.start()
        elif sec == "2":
            ipscan.start()
        elif sec == "3":
            sitechecker.start()
        elif sec == "0":
            break
        else:
            print("[!] Geçersiz seçim!")
        input("Devam etmek için ENTER...")

if __name__ == "__main__":
    main()
