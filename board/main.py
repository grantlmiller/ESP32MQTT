import wifi_connect
from DHT_22 import DHT22CLASS
from time import sleep
wifiname = 'WIFIEC0805'
pswd =  'KJ24UF74ZT3IQ9TQ'
wifi_connect.wifi_connect(wifiname,pswd)
server_ip = '192.168.0.52'
#set up sensors 
dht_on_pin_15 = DHT22CLASS(server_ip,'room_temp',15)
while True:
    sleep(dht_on_pin_15.poll_time)
    dht_on_pin_15.poll_sensor
    