#!/usr/bin/python3
# iplocateor v 0.0.1 by @sasan zare 2020/01/06
# API documentation http://ip-api.com/json/
# importing the requests library
import requests
#Please input IP
print(' Please input IP :')
IP = input()
# Api-endpoint
URL = "http://ip-api.com/json/"+IP
request = requests.get(url = URL)
# Extracting data in json format
data = request.json()
#Made by sasan zare
print('''================================+================================
                _______  _______  _______  _______
               (  ____ \(  ___  )/ ___   )(  ___  )
               | (    \/| (   ) |\/   )  || (   ) |
               | (_____ | (___) |    /   )| (___) |
               (_____  )|  ___  |   /   / |  ___  |
                     ) || (   ) |  /   /  | (   ) |
               /\____) || )   ( | /   (_/\| )   ( |
               \_______)|/     \|(_______/|/     \|

 Ip locate
 By: @sasan zare

================================+================================ ''')
#Create table
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Country", "CountryCode","RegionName","City","Timezone","Isp"]
table.add_row([data["country"], data["countryCode"], data["regionName"], data["city"],data["timezone"],data["isp"]])
# printing the output
print(" IP : "+IP)
print(table)
