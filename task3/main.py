import paho.mqtt.client as mqtt
import mysql.connector

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'test'
}


def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("testtopic/1") 
    else:
        print("Failed to connect, return code %d", rc)

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    if msg.topic == "home/sensors/room1/temperature":
        store_temperature(data)
    elif msg.topic == "home/sensors/room1/humidity":
        store_humidity(data)

def store_temperature(temp):
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    query = "INSERT INTO sensor_data (temperature) VALUES (%s)"
    cursor.execute(query, (temp,)) 
    cnx.commit()
    cursor.close()
    cnx.close()

def store_humidity(humidity):
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    query = "INSERT INTO sensor_data (humidity) VALUES (%s)"
    cursor.execute(query, (humidity,)) 
    cnx.commit()
    cursor.close()
    cnx.close()

client = mqtt.Client(client_id="clientId-Y2QoCUeGWr", userdata=None, protocol=mqtt.MQTTv5)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("test", "")
client.connect("14b5793c334743769b3e9fb1e4008401.s2.eu.hivemq.cloud", 8884)
client.connect("ssl://localhost", 8884)
client.subscribe("encyclopedia/#", qos=1)

client.on_subscribe = on_subscribe
client.on_message = on_message

client.subscribe("test/#", qos=1)

client.publish("test/temperature", payload="hot", qos=1)

store_humidity(client.on_message)


client.loop_forever()

