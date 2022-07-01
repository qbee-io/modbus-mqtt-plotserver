import paho.mqtt.client as mqtt
import json
import time
import requests
import yaml


config_file = "/etc/mqtt2plotserver/config.yml"

# Open the file and load the file
config = {}
with open(config_file) as f:
  config = yaml.safe_load(f)

def on_message(client, userdata, msg):
    #print("message received: " + msg.topic + " " + str(msg.payload))
    payload = json.loads(msg.payload.decode('utf-8'))
    print("decoded message:", payload)

    ts = time.time()
    for k,v in payload.items():
        plot_payload = {
                "tag": k,
                "value": v,
                "ts" : ts
        }
        try:
            url = f"http://localhost:{config['plot_server']['port']}"
            requests.post(url,json=plot_payload)
        except:
            pass


def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    mqtt_topic = config["mqtt"]["topic"]
    client.subscribe(mqtt_topic)


client = mqtt.Client('localqbee')
mqtt_user = config["mqtt"]["user"]
mqtt_pw = config["mqtt"]["password"]
# using passwordless setup for now
#client.username_pw_set(mqtt_user,mqtt_pw)

client.on_connect = on_connect
client.on_message = on_message

client.connect('127.0.0.1',1883)
client.loop_forever()
