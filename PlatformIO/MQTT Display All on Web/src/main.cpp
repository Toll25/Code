#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <SPIFFS.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>


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

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i=0;i<length;i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
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

void loop()
{
    sensors.requestTemperatures();
    float temperatureC = sensors.getTempCByIndex(0);
    temp = temperatureC;
    Serial.print(temperatureC);
    String json = "{\"name\":\"ESP-34\",\"value\":"+String(temp)+"}";
    client.publish("HTL/NB/4AHITS/temperatures", json.c_str());
    Serial.println("°C");
    myServer.handleClient();
    if (!client.connected()) {
        reconnect();
    }
    delay(10000);
    client.loop();
}
