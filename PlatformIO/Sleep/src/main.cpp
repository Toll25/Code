#include <Arduino.h>
#include <OneWire.h>
#include <WiFi.h>
#include <DallasTemperature.h>
#include <PubSubClient.h>

// WiFi credentials
#define SSID "HTLIoT"
#define WIFI_PW "hollabrunn"

// GPIO where the DS18B20 is connected to
const int oneWireBus = 4;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor
DallasTemperature sensors(&oneWire);

// MQTT server details
const char* mqtt_server = "broker.hivemq.com";
const char* mqtt_topic = "mytesttopic";

WiFiClient wifiClient;
PubSubClient client(wifiClient);

float temp = 0;

// Function to reconnect to MQTT broker
void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect with a unique client ID
    if (client.connect("ESP32Client")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(9600);

  // Start WiFi
  Serial.print("Connecting to ");
  Serial.print(SSID);
  WiFi.begin(SSID, WIFI_PW);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(200);
  }
  Serial.println("OK");
  Serial.print("IP-Address: ");
  Serial.println(WiFi.localIP());

  // Start MQTT
  client.setServer(mqtt_server, 1883);

  // Start temperature sensor
  sensors.begin();
}

void loop() {
  // Request temperature from sensor
  sensors.requestTemperatures();
  float temperatureC = sensors.getTempCByIndex(0);
  temp = temperatureC;
  Serial.print(temperatureC);
  Serial.println("°C");

  // Connect to MQTT and send data
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Prepare payload
  String payload = "Temperature: " + String(temperatureC) + " °C";
  client.publish(mqtt_topic, payload.c_str());

  // Print the temperature to serial monitor
  Serial.println(payload);

  // Ensure all messages are sent before disconnecting
  client.loop();
  delay(100);  // Short delay to ensure message delivery

  // Disconnect from WiFi and MQTT
  client.disconnect();
  WiFi.disconnect(true);  // Disconnect and turn off WiFi

  // Allow some time for disconnection to complete
  delay(100);

  // Prepare for deep sleep
  Serial.println("Going to sleep for a minute...");
  esp_sleep_enable_timer_wakeup(60 * 1000000);  // 60 seconds
  esp_deep_sleep_start();
}
