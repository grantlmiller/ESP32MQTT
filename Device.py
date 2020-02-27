from mqtt.simple import MQTTClient

class Device():
    def __init__(self,server_ip,client_id):
        self.subscribed_topics = [b'DeviceRequest/#']
        self.publish_topics=[b'DeviceResponse']
        self.server_address =server_ip
        self.client_id = 'DeviceID'
        self.client = MQTTClient(self.client_id, self.server_address)
        self.client.connect()
        #todo add location 

        
    def add_subscribe_to_topic(self,topic):
        self.subscribed_topics.append(topic)
    def add_publish_topic(self,topic):
        self.publish_topics.append(topic)
    def publish_topic(self,topic,message):
        if(topic in self.publish_topics):
            self.client.publish(topic,message)
        else:
            print('topic not in list')
        
    



    

    