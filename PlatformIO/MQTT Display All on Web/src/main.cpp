#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <SPIFFS.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include <nlohmann/json.hpp>
#include <iostream>
#include <SD.h>


using json = nlohmann::json;


#define SSID "HTLIoT"
#define WIFI_PW "hollabrunn"
#define ANALOG_INPUT_PIN 36

// GPIO where the DS18B20 is connected to
const int oneWireBus = 4;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor
DallasTemperature sensors(&oneWire);

IPAddress server(172, 16, 0, 2);

float temp = 0;

WebServer myServer(80);

JsonDocument doc;

json data;

void callback(char* topic, byte* payload, unsigned int length) {
    // Convert the payload byte array to a string
    std::string jsonString(reinterpret_cast<char*>(payload), length);

    // Parse the string
    json jsonData = json::parse(jsonString);

    std::string name = jsonData["name"].get<std::string>();
    json value = jsonData["value"];

    // Store the "name" and "value" into the map
    data[name] = value;

    // Print the "name" value to the Serial
    std::cout << data.dump(4) << std::endl;

    // Open the file in write mode
    File file = SD.open("data.json", FILE_WRITE);

    if (file) {
        // Write data to the file
        file.write(payload, length);
        file.close();
    } else {
        Serial.println("Error opening file for writing");
    }
}


void handleRoot() 
{
    File file = SPIFFS.open("/test.html", "r"); 
    if (file)
    {
        myServer.streamFile(file, "text/html"); 
        file.close();                            
    }
    else
    {
        myServer.send(500, "text/plain", "Couldnt read file");
    }
}

WiFiClient wifiClient;


PubSubClient client(wifiClient);

void reconnect() {

  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");

    if (client.connect("broker.hivemq.com")) {
      Serial.println("connected");

      //client.publish("HTL/NB/4AHITS/temperatures","hello world");

      client.subscribe("HTL/NB/4AHITS/temperatures");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");

      delay(5000);
    }
  }
}

void setup()
{
    SPIFFS.begin();
    Serial.begin(9600);
    Serial.print("Connecting to ");
    Serial.print(SSID);
    WiFi.begin(SSID, WIFI_PW);
    while (!WiFi.isConnected())
    {
        Serial.print(".");
        delay(200);
    }
    Serial.println("OK");
    Serial.print("IP-Address: ");
    Serial.println(WiFi.localIP());
    myServer.on("/", handleRoot);
    client.setServer("broker.hivemq.com", 1883);
    client.setCallback(callback);
    myServer.begin();
    sensors.begin();
}

unsigned long lastPublishTime = 0;
const unsigned long publishInterval = 10000; // 10 seconds

void loop() {
    // Handle MQTT client events
    if (!client.connected()) {
        reconnect();
    }
    client.loop();

    // Check for incoming client connections and handle them
    myServer.handleClient();

    // Get current time
    unsigned long currentTime = millis();

    // Check if it's time to publish
    if (currentTime - lastPublishTime >= publishInterval) {
        // Request temperature readings
        sensors.requestTemperatures();
        float temperatureC = sensors.getTempCByIndex(0);
        temp = temperatureC;
        Serial.print(temperatureC);

        // Publish temperature data
        String json = "{\"name\":\"ESP-34\",\"value\":"+String(temp)+"}";
        client.publish("HTL/NB/4AHITS/temperatures", json.c_str());

        Serial.println("�C");

        // Update last publish time
        lastPublishTime = currentTime;
    }
}

