import phonenumbers

from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+918870111110")

print("\n Location \n")

print(geocoder.description_for_number(phone_number1,"en"))


