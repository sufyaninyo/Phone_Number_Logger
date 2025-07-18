#hi again That's me sufyanito 
    #our today project will be like phoneinfoga tool
        #so yeah let's start

import phonenumbers
import time
from phonenumbers import geocoder, carrier 
from phonenumbers import timezone

print("'########::'##::::'##::'#######::'##::: ##:'########:'##::::::::'#######:::'######::::'######:::'########:'########::")
print(" ##.... ##: ##:::: ##:'##.... ##: ###:: ##: ##.....:: ##:::::::'##.... ##:'##... ##::'##... ##:: ##.....:: ##.... ##:")
print(" ##:::: ##: ##:::: ##: ##:::: ##: ####: ##: ##::::::: ##::::::: ##:::: ##: ##:::..::: ##:::..::: ##::::::: ##:::: ##:")
print(" ########:: #########: ##:::: ##: ## ## ##: ######::: ##::::::: ##:::: ##: ##::'####: ##::'####: ######::: ########::")
print(" ##.....::: ##.... ##: ##:::: ##: ##. ####: ##...:::: ##::::::: ##:::: ##: ##::: ##:: ##::: ##:: ##...:::: ##.. ##:::")
print(" ##:::::::: ##:::: ##: ##:::: ##: ##:. ###: ##::::::: ##::::::: ##:::: ##: ##::: ##:: ##::: ##:: ##::::::: ##::. ##::")
print(" ##:::::::: ##:::: ##:. #######:: ##::. ##: ########: ########:. #######::. ######:::. ######::: ########: ##:::. ##:")
print("..:::::::::..:::::..:::.......:::..::::..::........::........:::.......::::......:::::......::::........::..:::::..::")
print("                                        🔍 OSINT Phone Scanner | by sufyanito\n")







phone_number = input("Enter the phone number with country code: ")
num = phonenumbers.parse(phone_number)

print("Searching for information...")
time.sleep(2)

print("-------------------------------------------------------------")

print("are the number is valid? ", phonenumbers.is_valid_number(num))
print("country : ", geocoder.country_name_for_number(num, "en"))
print("possible :", phonenumbers.is_possible_number(num))
print("carrier : ", carrier.name_for_number(num, "en"))
print("TimeZone : ", timezone.time_zones_for_number(num))

print("--------------------------------------------------------------")



