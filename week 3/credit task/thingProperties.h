#include <ArduinoIoTCloud.h>
#include <Arduino_ConnectionHandler.h>
#include "arduino_secrets.h"

const char SSID[]     = SECRET_SSID;
const char PASS[]     = SECRET_OPTIONAL_PASS;

// Define your Cloud variables here
float temperature;
float humidity;
bool alarmTriggered = false;

void initProperties() {
  ArduinoCloud.addProperty(temperature, READ, ON_CHANGE);
  ArduinoCloud.addProperty(humidity, READ, ON_CHANGE);
  ArduinoCloud.addProperty(alarmTriggered, READWRITE, ON_CHANGE);
}
WiFiConnectionHandler ArduinoIoTPreferredConnection(SSID, PASS);
