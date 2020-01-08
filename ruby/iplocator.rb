#!/usr/bin/ruby
# iplocateor v 0.0.1 by @sasan zare 2020/01/07
# API documentation http://ip-api.com/json/
# require class Net::HTTP
require 'net/http'
# require Json
require 'json'
#Please input IP
print(' Please input IP : ')
IP = gets
# Api-endpoint
uri = URI('http://ip-api.com/json/'+IP.chomp )
response = Net::HTTP.get_response(uri)
#Json to Object
responseObject= JSON.parse(response.body)
p = "[+]"
#Made by sasan zare
puts('================================+================================
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

 IP : '+responseObject['query']+"\r\n"+ p + " country : " + responseObject['country']+"\r\n" + p + " CountryCode : " + responseObject['countryCode']+"\r\n" + p + " RegionName : " + responseObject['regionName']+"\r\n" + p + " City : " + responseObject['city']+"\r\n" + p + " Timezone : " + responseObject['timezone']+"\r\n" + p + " Isp : " + responseObject['isp']+"\r\n")
