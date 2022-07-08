import phonenumbers
import folium
from pytz import timezone
from mynumbers import number
from phonenumbers import geocoder
from phonenumbers import timezone
key = '3e4f4cbccdf94e27a303b89ba4ed3c7a'


setNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(setNumber, "en")
time_zone = timezone.time_zones_for_geographical_number(setNumber)
# "en" stands for the language i.e english  other trials("fr")

# Printing the location of the person depending on the phone number .
print("Country:", yourLocation)
print("Timezone:", time_zone)



#Service Provider 

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))



#For Map Location

from opencage.geocoder import OpenCageGeocode

geocoder =  OpenCageGeocode(key)
query = str(yourLocation)
result = geocoder.geocode(query)
# print(result)

latitude = result[0]['geometry']['lat']
longtitude = result[0]['geometry']['lng']

print(latitude,longtitude)


my_map = folium.Map(location=[latitude,longtitude], zoom_start = 9 )

folium.Marker([latitude,longtitude], popup = yourLocation).add_to((my_map))

# Saving the map as an html file.
my_map.save("location.html")
#once run, it automatically creates the html file

