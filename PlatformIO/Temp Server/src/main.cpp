#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <SPIFFS.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define SSID "HTLIoT"
#define WIFI_PW "hollabrunn"
#define ANALOG_INPUT_PIN 36

// GPIO where the DS18B20 is connected to
const int oneWireBus = 4;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor
DallasTemperature sensors(&oneWire);

float temp = 0;

WebServer myServer(80);

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

void handleGetTemperature()
{
    myServer.send(200, "text/plain", String(temp));
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
    myServer.on("/getTemperature", handleGetTemperature);
    myServer.begin();
    sensors.begin();
}

void loop()
{
    sensors.requestTemperatures();
    float temperatureC = sensors.getTempCByIndex(0);
    temp = temperatureC;
    Serial.print(temperatureC);
    Serial.println("°C");
    myServer.handleClient();
    delay(50);
}
