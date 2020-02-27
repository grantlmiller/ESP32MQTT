from Device import Device
class Sensor(Device):
    def __init(self,server_ip,client_ip):
        super().__init__(self,server_ip,client_ip)
        #super().add_subscribe_to_topic(b'Sensors/#')
        self.poll_time = 4
    def poll_sensor(self):
        print('implement poll sensor dummy')

   

