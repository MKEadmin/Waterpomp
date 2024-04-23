#install : paho MQTT 
import paho.mqtt.client as mqtt
import columnData

TOPIC = [("DZHF/+/+", 0)]
MQTT_BROKER = "192.168.1.124"
CLIENT_NAME = "Logger"

def handle_data(topic, data):
    if topic[2] not in columnData.LEVEL3 or topic[1] not in columnData.LEVEL2:
        return
    
    data = int(round(float(data), 2))
    
    if topic[2] == columnData.LEVEL:
        columnData.addLevel(topic[1], data)
    elif topic[2] == columnData.DIRECTION:
        columnData.addDirection(topic[1], data)
    
def on_message(client, userdata, message):
    topic = message.topic.split('/')
    data = message.payload.decode("utf-8")
    handle_data(topic, data)

client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

client.loop_start()

client.subscribe(TOPIC)
client.on_message=on_message 

if __name__ == "__main__":
    import time
    while True:
        #pass # do not use pass... to much CPU consumption
        time.sleep(10)
        
    client.loop_stop()


