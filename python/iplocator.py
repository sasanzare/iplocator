#!/usr/bin/python3
# iplocateor v 0.1.0 by @sasan zare 2020/01/21
# API documentation https://api.ipdata.co/
# API documentation http://ip-api.com/json/
# API documentation https://ipinfo.io/
# API documentation http://api.db-ip.com/v2/free/
# importing the asyncio library
import asyncio
# importing the requests library
import requests
print(' Please input IP :')
IP = input()
# async function
async def main():
    loop = asyncio.get_event_loop()
    res_1 = (await (loop.run_in_executor(None, requests.get, ("https://api.ipdata.co/"+IP+"?api-key=test")))).json()
    res_2 = (await (loop.run_in_executor(None, requests.get, ("http://ip-api.com/json/"+IP)))).json()
    res_3 = (await (loop.run_in_executor(None, requests.get, ("https://ipinfo.io/"+IP+"/geo")))).json()
    res_4 = (await (loop.run_in_executor(None, requests.get, ("http://api.db-ip.com/v2/free/"+IP)))).json()
#Made by sasan zare
    print('''   ================================+================================
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

    ================================+================================
    IP : '''+IP)
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["Property", "API_1","API_2","API_3","API_4"]
    table.add_row(["Country", res_1["country_name"],res_2["country"]," ",res_4["countryName"]])
    table.add_row(["CountryCode", res_1["country_code"],res_2["countryCode"],res_3["country"],res_4["countryCode"]])
    table.add_row(["City", res_1["city"],res_2["city"],res_3["city"],res_4["city"]])
    table.add_row(["regionName", res_1["region"],res_2["regionName"],res_3["region"]," "])
    table.add_row(["timezone", res_1["time_zone"]["name"],res_2["timezone"],res_3["timezone"]," "])
    table.add_row(["continent_name", res_1["continent_name"]," "," ",res_4["continentName"]])
    table.add_row(["Is_tor", res_1["threat"]["is_tor"]," "," ",""])
    table.add_row(["Is_proxy", res_1["threat"]["is_proxy"]," "," ",""])
    table.add_row(["Is_anonymous", res_1["threat"]["is_anonymous"]," "," ",""])
    table.add_row(["Is_known_attacker", res_1["threat"]["is_known_attacker"]," "," ",""])
    table.add_row(["Is_known_abuser", res_1["threat"]["is_known_abuser"]," "," ",""])
    table.add_row(["Is_threat", res_1["threat"]["is_threat"]," "," ",""])
    table.add_row(["Is_bogon", res_1["threat"]["is_bogon"]," "," ",""])
# printing the output
    print(table)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
