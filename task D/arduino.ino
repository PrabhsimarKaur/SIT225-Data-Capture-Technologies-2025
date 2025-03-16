#include <SPI.h>
#include <WiFiNINA.h>
#include <PubSubClient.h>
#include <Arduino_LSM6DS3.h>

// WiFi Credentials
const char* ssid = "MANPREET SINGH 4G";
const char* password = "Kaur1983";

// MQTT Server Details (HiveMQ Cloud)
const char* mqttServer = "your-cluster.hivemq.cloud";
const int mqttPort = 8883;
const char* mqttUser = "hivemq.webclient.1742109140513 ";
const char* mqttPassword = " 5@>93HDb8RhTJaf:P%xr ";

// MQTT Topic for Sending Data
const char* topic = "gyro/data";

// Create WiFi and MQTT Client
WiFiClient wifiClient;
PubSubClient client(wifiClient);

void connectToWiFi() {
  Serial.print("Connecting to WiFi...");
  while (WiFi.begin(ssid, password) != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }
  Serial.println("Connected!");
}

void connectToMQTT() {
  client.setServer(mqttServer, mqttPort);
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ArduinoNano33IoT", mqttUser, mqttPassword)) {
      Serial.println("Connected to MQTT!");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" Retrying...");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  connectToWiFi();
  connectToMQTT();

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
}

void loop() {
  if (!client.connected()) {
    connectToMQTT();
  }
  client.loop();

  float x, y, z;
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(x, y, z);
    String payload = "{\"x\": " + String(x) + ", \"y\": " + String(y) + ", \"z\": " + String(z) + "}";
    client.publish(topic, payload.c_str());
    Serial.println("Published: " + payload);
  }
  delay(1000);
}
