import phonenumbers

from test import number


from phonenumbers import geocoder

c_num = phonenumbers.parse(number,"CH")

print(geocoder.description_for_number(c_num, "en"))



from phonenumbers import carrier

service_num = phonenumbers.parse(number, "RO")

print(carrier.name_for_number(service_num, "en"))