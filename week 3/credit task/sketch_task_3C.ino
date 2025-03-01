#include "thingProperties.h"
#include <DHT.h>

#define DHTPIN 2       // DHT22 data pin connected to D2
#define DHTTYPE DHT22  // Define sensor type

DHT dht(DHTPIN, DHTTYPE);


void setup() {
    Serial.begin(115200);
    delay(1500); 
    initProperties();
    ArduinoCloud.begin(ArduinoIoTPreferredConnection);
    dht.begin();
}

void loop() {
    ArduinoCloud.update();  // Update IoT cloud variables

    temperature = dht.readTemperature(); // Read temperature in Celsius
    humidity = dht.readHumidity();       // Read humidity

    if (isnan(temperature) || isnan(humidity)) {
        Serial.println("Failed to read from DHT sensor!");
        return;
    }

    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.print(" °C, Humidity: ");
    Serial.print(humidity);
    Serial.println(" %");

    // Trigger alarm if temperature > 35°C or humidity > 80%
    if (temperature > 35 || humidity > 80) {
        alarmTriggered = true;
    } else {
        alarmTriggered = false;
    }

    delay(2000);  // Wait 2 seconds before next reading
}
