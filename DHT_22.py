from Sensor import Sensor
from machine import Pin 
from dht import DHT22
from time import sleep
#Test Shit
class DHT22CLASS(Sensor):
    def __init__(self, server_ip,client_id,pin_no):
        super().__init__(server_ip,client_id)
        super().add_subscribe_to_topic(b'Sensors/temp_hum')
        self.sensor = DHT22(Pin(pin_no,Pin.IN,Pin.PULL_UP))
    def poll_sensor(self):
        try:
            self.sensor.measure()
            temp= self.sensor.temperature()
            hum = self.sensor.humidity()
            if isinstance(temp, float) and isinstance(hum,float):
                msg = (b'{0:3.1f} ,{1:3.1f}'.format(temp, hum))
                self.publish_topic('Sensors/temp',msg)
                #self.client.publish('Sensors/temp', msg)  # Publish sensor data to MQTT topic
            else:
                print('cannot interpret values')
        except OSError:
            print('Failed to read sensor.')
            
            

    
        