#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include <PubSubClient.h>

const char* ssid = "ini_ssid_wifi";
const char* password = "";
const char* mqtt_server = "14b5793c334743769b3e9fb1e4008401.s2.eu.hivemq.cloud"; 
const int mqtt_port = 8884;
const char* mqtt_client_id = "clientId-Y2QoCUeGWr";

WiFiClient espClient;
PubSubClient mqttClient(espClient);

float temperature = 25.5;
float humidity = 70.0;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) { delay(500); }

  mqttClient.setServer(mqtt_server, mqtt_port); 
  while (!mqttClient.connect(mqtt_client_id)) { delay(500); } 
}

void loop() {
  if (!mqttClient.connected()) { mqttClient.connect(mqtt_client_id); }

  String temperatureStr = String(temperature);
  String humidityStr = String(humidity);

  mqttClient.publish("test/temperature", temperatureStr.c_str());
  mqttClient.publish("test/humidity", humidityStr.c_str());

  delay(5000);
}
