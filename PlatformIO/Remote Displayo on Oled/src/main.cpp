#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <cstring>
#include <WiFi.h>

// Create an instance of the server
WiFiServer server(80);

#define ANALOG_INPUT_PIN 36
#define SSID "HTLIoT"
#define WIFI_PW "hollabrunn"

Adafruit_SSD1306 oled(128, 64,&Wire, -1);

const int oneWireBus = 4;

float temp=0;
String secondTemp="0";

OneWire oneWire(oneWireBus);

DallasTemperature sensors(&oneWire);

int otherTemp(String otherTemp);

WiFiClient client;
IPAddress serverIP(172, 18, 40, 114); // IP address of the other Arduino server
const int HTTP_PORT = 80;
const String PATH_NAME = "/temperature";
const String HTTP_METHOD = "GET";

void setup() {
  Serial.begin(9600);

  // Connect to WiFi
  WiFi.begin(SSID, WIFI_PW);
  while (!WiFi.isConnected()){
    Serial.print(".");
    delay(200);
  }
  Serial.println("OK");
  Serial.print("IP-Address: ");
  Serial.println(WiFi.localIP());

  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.println(WiFi.localIP());

  if(!oled.begin(SSD1306_SWITCHCAPVCC, 0x3C)){
    Serial.println("OLED FAILED");
  }
  oled.clearDisplay();
  oled.setTextColor(SSD1306_WHITE);
  oled.write("Starting Up");
  oled.display();
  sensors.begin();

}

void loop() {
  sensors.requestTemperatures();
  float temperatureC = sensors.getTempCByIndex(0);
  temp = temperatureC;

  if (!client.connected()) {
    Serial.println("Connecting to server");
    if (client.connect(serverIP, HTTP_PORT)) {
      Serial.println("Connected to server");
      client.print(HTTP_METHOD + " " + PATH_NAME + " HTTP/1.1\r\n");
      client.print("Host: ");
      client.print(serverIP);
      client.print("\r\n");
      client.print("Connection: close\r\n");
      client.print("\r\n");
    } else {
      Serial.println("Connection failed");
    }
  }

  //while (client.connected() && !client.available()) {
  //  delay(100);
  //}

  if (client.available()) {
    String response = client.readStringUntil('\r');
    Serial.println("Response: " + response);
    // Process the response here if needed
  }

  oled.clearDisplay();
  oled.setCursor(0, 0);
  oled.print("My Temp:");
  oled.print(temperatureC);
  oled.print("C");
  oled.setCursor(0, 20);
  oled.print("Other Temp:");
  // Print the second temperature if you have it available
  // oled.print(secondTemp);
  oled.print("C");
  oled.display();

  delay(100);
}

int otherTemp(String otherTemp){
  Serial.println("New Second Temp: " + otherTemp);
  secondTemp=otherTemp;
  return 1;
}