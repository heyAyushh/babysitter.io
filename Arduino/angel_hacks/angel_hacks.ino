
#include <ESP8266WiFi.h>
#include <ArduinoJson.h>
#include <ESP8266HTTPClient.h>
#define devID "anah"
#define key "3443"
#include <DHT.h>
#define DHTPIN 2 
#define DHTTYPE DHT22
#define Lightpin A0
#define Soundpin 14
#define Wetpin 5
DHT dht(DHTPIN, DHTTYPE); 

const char* ssid     = "StartUP-Oasis";
const char* password = "P@$$w0rd@1947";

void setup() {
  Serial.begin(115200); 

  initWifi();
  makeIFTTTRequest();

  // Deep sleep mode until RESET pin is connected to a LOW signal (pushbutton is pressed)
}

void loop() {
  Serial.print("maA KI CHU");
  makeIFTTTRequest();
  delay(2000);
  // sleeping so wont get here
}

// Establish a Wi-Fi connection with your router
void initWifi() {
  Serial.print("Connecting to: "); 
  Serial.print(ssid);
  WiFi.begin(ssid, password);  

  int timeout = 10 * 4; // 10 seconds
  while(WiFi.status() != WL_CONNECTED  && (timeout-- > 0)) {
    delay(250);
    Serial.print(".");
  }
  Serial.println("");

  if(WiFi.status() != WL_CONNECTED) {
     Serial.println("Failed to connect, going back to sleep");
  }

  Serial.print("WiFi connected in: "); 
  Serial.print(millis());
  Serial.print(", IP address: "); 
  Serial.println(WiFi.localIP());
}

// Make an HTTP request to the IFTTT web service
void makeIFTTTRequest() { 
    StaticJsonBuffer<300> JSONbuffer;   //Declaring static JSON buffer
    JsonObject& JSONencoder = JSONbuffer.createObject(); 
    float h = dht.readHumidity(); 
    float t = dht.readTemperature(); 
    
    int LightIntensity =analogRead(Lightpin);
    int SoundPin= digitalRead(Soundpin);
    int WetPin= digitalRead(Wetpin);
    
    
    JSONencoder["Temperature"] = t;
    JSONencoder["Humidity"] = h;
    JSONencoder["LightIntensity"] = LightIntensity;
    JSONencoder["SoundIntenstity"] = SoundPin;
    JSONencoder["Wet"] = WetPin;
    char JSONmessageBuffer[300];
    JSONencoder.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
    Serial.println(JSONmessageBuffer);
 
    HTTPClient http;    //Declare object of class HTTPClient
 
    http.begin("http://1cd4ce79.ngrok.io/api/injest");      //Specify request destination
    http.addHeader("Content-Type", "application/json");  //Specify content-type header
 
    int httpCode = http.PUT(JSONmessageBuffer);   //Send the request
    String payload = http.getString();                                        //Get the response payload
 
    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload
 
    http.end();  //Close connection
 
}
