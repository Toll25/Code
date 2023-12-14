#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <WiFi.h>
#include <WebServer.h>
#include <SPIFFS.h>

#define SSID "HTLIoT"
#define WIFI_PW "hollabrunn"
#define ANALOG_INPUT_PIN 36

int brightness = 78;
WebServer myServer( 80 );
Adafruit_SSD1306 oled(128, 64,&Wire, -1);

int prevPotStrength=0;
int prevStrength=0;
int strength=0;

void handleRoot() {
  File file = SPIFFS.open("/test.html", "r");  // Open the HTML file
  if (file) {
    myServer.streamFile(file, "text/html");  // Stream the file content as HTML
    file.close();  // Close the file
  } else {
    myServer.send(500, "text/plain", "Couldnt read file");
  }
}
void handleBlupp( ) {
  String answer = "<h1>Hello world! ";
  answer += String( brightness );
  answer += "</h1>";
  for ( int i = 0; i < myServer.args( ); i++ ) {
    Serial.print( myServer.argName( i ) );
    Serial.print( ": " );
    strength=(myServer.arg(myServer.argName(i))).toInt()*0.63;
    Serial.println( myServer.arg( myServer.argName( i ) ) );
  }
  myServer.send( 200, "text/html", answer );
}
void setup() {
  SPIFFS.begin();
  Serial.begin( 9600 );
  pinMode( ANALOG_INPUT_PIN, ANALOG);
  analogReadResolution(6);
  ledcSetup(0,100,6);
  ledcAttachPin(32,0);
  if(!oled.begin(SSD1306_SWITCHCAPVCC, 0x3C)){
    Serial.println("OLED FAILED");
  }
  oled.clearDisplay();
  oled.setTextColor(SSD1306_WHITE);
  oled.write("Starting Up");
  oled.display();
  Serial.print( "Connecting to " );
  Serial.print( SSID );
  WiFi.begin( SSID, WIFI_PW );
  while ( ! WiFi.isConnected() ){
    Serial.print( "." );
    delay( 200 );
  }
  Serial.println( "OK" );
  Serial.print( "IP-Address: " );
  Serial.println( WiFi.localIP( ) );
  myServer.on( "/", handleRoot );
  myServer.on( "/blupp.html", handleBlupp );
  myServer.begin( );
}


void loop() {

  int potStrength=analogRead(ANALOG_INPUT_PIN);

  Serial.println(strength, DEC);

  if(potStrength==prevPotStrength){
    
  }else{
    strength=potStrength;
  }

  prevPotStrength=potStrength;

  ledcWrite(0, strength);

  oled.clearDisplay();
  oled.setCursor(0,0);
  oled.print((strength*100)/63);
  oled.display();
  myServer.handleClient( );
  delay( 100 );
}