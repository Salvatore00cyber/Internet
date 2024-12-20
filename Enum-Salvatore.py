import sys
from modules.email_enumeration.cli import email_search
from modules.username_enumeration.script import username_search
from modules.suddomain_enumeration import domain_search

def print_banner():
    print("""
                       
              

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠶⠶⠚⠛⠛⠛⠛⠛⠛⠛⠷⠶⢦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠞⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⣀⠄⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⡤⠤⠤⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⢄⡀⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⠏⠀⢀⣀⣠⣶⠟⠁⠀⠀⠀⣠⠴⠀⢀⠔⠋⢁⠎⠀⡇⠘⡄⠉⠲⣍⠑⠢⢄⡀⠀⠀⠀⠙⣷⣦⣤⡀⠀⠙⣷⡀⠀⠀⠀
⠀⠀⢀⣾⠃⠀⣴⠏⣼⡿⣣⠀⠀⢀⡴⠋⠠⢄⡴⠃⠀⠀⡞⠀⠀⠃⠀⠹⡄⠀⠈⢳⡀⠤⠘⠢⡀⠀⠀⢾⢻⣷⡘⣦⡀⠈⢿⡄⠀⠀
⠀⠀⣾⠁⣠⢺⣿⢘⣭⣾⠃⠀⡰⠋⠀⠀⢀⡜⠁⠁⠀⢺⠀⣴⣞⡳⣶⡄⠁⠀⠉⠀⠱⡄⠀⠀⠈⠢⡀⠈⢷⣬⡓⢻⣷⢦⠈⢿⡄⠀
⠀⣼⠃⢰⡇⢸⣷⡿⢻⠁⢀⠞⠀⠀⠀⠀⡜⠀⠀⠀⠀⠈⠀⠈⠁⣷⠿⠃⠀⠀⠀⠀⠀⢱⡀⠀⠀⠀⠱⡄⠀⢿⢿⣾⡿⢸⣧⠈⣷      #######################⠀
⢠⡟⠀⣾⣿⢸⣫⣶⠇⠀⡞⠀⠀⠒⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡃⠀⠀⠀⠀⠀⠀⠀⠀⠃⠠⠀⠀⠀⢹⡀⠘⣷⣌⠧⢸⣿⠀⢸⡇    #  Copyrit of         #
⣼⡇⣰⢻⣿⣸⡿⠋⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠻⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⢸⣿⣧⣼⡿⢀⠀⣷   # [double]   Internet #
⣿⠀⣿⡀⢿⡟⢡⡇⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠸⣆⠻⣿⠃⣼⠀⢿  #######Salvatore#######
⣿⠀⢿⣷⠘⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⡟⠀⣹⣯⡁⢸⣷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⢿⣦⠙⣼⣿⠀⢸
⣿⠀⠘⣿⣇⣿⡏⡄⠀⣄⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⠃⠀⢰⣇⠀⠀⣿⣿⣿⣿⣿⣷⡆⠀⠀⠀⠀⠀⢸⠁⢀⠸⣿⢰⣿⠇⠀⣾
⢻⡇⣷⡈⢻⣿⢀⣿⠀⢸⡀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⠀⢠⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⡾⠀⣼⡆⢿⡿⠃⣼⠀⣿
⠘⣧⠘⣿⣦⡙⢸⣿⣦⡀⢣⠀⡠⠤⠒⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⣿⢀⣾⣿⣿⣿⣿⣿⣿⣿⠒⠢⠤⣀⣰⠁⡰⣿⡇⢚⣴⣾⠏⢸⡇
⠀⢻⡄⢈⠻⣿⣼⣿⡇⣷⡈⢦⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⡰⢃⣼⠁⣿⣧⣾⡿⡃⢀⡿⠀
⠀⠈⢿⡀⢷⣌⠛⢿⣧⢸⣷⡀⠑⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠜⠁⣼⡟⢸⡿⠟⣉⡴⠃⣼⠃⠀
⠀⠀⠈⢿⡄⠻⢿⣶⣬⣁⢿⣧⢳⣄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣠⡖⣹⣿⢃⣥⣴⣾⠟⢁⣼⠃⠀⠀
⠀⠀⠀⠈⢻⣆⠀⢝⠻⠿⢿⣿⣦⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰⣿⡿⠿⠟⣋⠁⢠⡾⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢷⡀⠙⠶⣶⣤⣤⣥⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣼⣥⣤⣶⡶⠛⢁⣴⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⢦⣀⠀⢭⣉⣙⣉⣉⣁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⣉⣉⣋⣉⡩⠁⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣤⡈⠙⠛⠻⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⢉⣠⡶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣦⣄⣀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⣀⣤⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

#this tools For Cyber Sec Created by Internet <>⠀⠀


×××××××××××××××××××××××××××××××××××××××××××××                                           
×             Enumeration Cyber Sec         ×
××××××××××××××÷÷÷××××××××××××××××××××××××××××
×  options :                                ×
×                                           ×
× 1:=> Search by Username                   ×
× 2:=> Search by Email                      ×
× 3:=> Subdomain enumeration                ×
×                                           ×
××××××××××××××××××Salvatore××××××××××××××××××










    """)

def main():
    print_banner()

    try:
        option = int(input("Enter your choice (1/2/3): "))

        if option == 1:
            username = input("Enter the username to search: ")
            username_search(username)
        elif option == 2:
            email = input("Enter the email to search: ")
            email_search(email)
        elif option == 3:
            domain = input("Enter the domain to search: ")
            domain_search(domain)
        else:
            print("Invalid option. Please choose a number from 1 to 3.")
            sys.exit(1)

    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

if __name__ == "__main__":
    main()
