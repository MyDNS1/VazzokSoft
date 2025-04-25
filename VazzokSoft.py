import phonenumbers
import os
from colorama import Fore, Style, init
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import number_type, is_valid_number

init(autoreset=False)

banner = f"""{Fore.MAGENTA}
▗▖  ▗▖ ▗▄▖ ▗▄▄▄▄▖▗▄▄▄▄▖ ▗▄▖ ▗▖ ▗▖
▐▌  ▐▌▐▌ ▐▌   ▗▞▘   ▗▞▘▐▌ ▐▌▐▌▗▞▘
▐▌  ▐▌▐▛▀▜▌ ▗▞▘   ▗▞▘  ▐▌ ▐▌▐▛▚▖ 
 ▝▚▞▘ ▐▌ ▐▌▐▙▄▄▄▖▐▙▄▄▄▖▝▚▄▞▘▐▌ ▐▌              
 ▗▄▄▖ ▗▄▖ ▗▄▄▄▖▗▄▄▄▖             
▐▌   ▐▌ ▐▌▐▌     █               
 ▝▀▚▖▐▌ ▐▌▐▛▀▀▘  █               
▗▄▄▞▘▝▚▄▞▘▐▌     █                                         
"""

def main():
    os.system("clear")
    print(banner)
    print(f"{Fore.MAGENTA}\n1. {Fore.LIGHTMAGENTA_EX}Поиск по номеру телефона\n{Fore.MAGENTA}2. {Fore.LIGHTMAGENTA_EX}Авторы\n{Fore.MAGENTA}3. {Fore.LIGHTMAGENTA_EX}Выход{Style.RESET_ALL}")
    choice = input(f"\n{Fore.MAGENTA}Выберите функцию — {Fore.LIGHTMAGENTA_EX}")
    if choice == "1":
        phonesearch()
    elif choice == "2":
        info()
    elif choice == "3":
        exit()

def phonesearch():
    os.system("clear")
    print(banner)
    number = input(f"\n{Fore.LIGHTMAGENTA_EX}Введите номер телефона (пример: +79999999999): ")
    parsed_number = phonenumbers.parse(number)
    print(f"\n{Fore.MAGENTA}Страна:{Fore.LIGHTMAGENTA_EX}", geocoder.description_for_number(parsed_number, "ru"))
    print(f"{Fore.MAGENTA}Оператор:{Fore.LIGHTMAGENTA_EX}", carrier.name_for_number(parsed_number, "ru"))
    print(f"{Fore.MAGENTA}Часовые пояса:{Fore.LIGHTMAGENTA_EX}", timezone.time_zones_for_number(parsed_number))
    print(f"{Fore.MAGENTA}Тип номера:{Fore.LIGHTMAGENTA_EX}", number_type(parsed_number))
    print(f"{Fore.MAGENTA}Валидный номер:{Fore.LIGHTMAGENTA_EX}", is_valid_number(parsed_number))
    print(f"\n{Fore.MAGENTA}Нажмите ENTER чтобы продолжить...")
    input()
    main()

def info():
    os.system("clear")
    print(banner)
    print(f"{Fore.MAGENTA}Сссылка на наш канал — https://t.me/+8NZBaE13O7JkYzJi{Fore.LIGHTMAGENTA_EX}\n\nНажмите ENTER чтобы продолжить...")
    input()
    main()

main()