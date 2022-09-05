import time
from paho.mqtt import client as mqtt_client
import platform
broker = 'broker.emqx.io'
port = 1883
topic = "topicName/weather"
client_id = 'omkar'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client

def publish(client):
    mysystem = platform.uname
    system = 'OS:'+my_system.system
    system = 'Sys Name' + my_system.node
    


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()


//https://wokwi.com/projects/337346829713670739