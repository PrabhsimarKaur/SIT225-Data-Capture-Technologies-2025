#include <Arduino_LSM6DS3.h>

void setup() {
    Serial.begin(115200);
    while (!Serial);

    if (!IMU.begin()) {
        Serial.println("Failed to initialize IMU!");
        while (1);
    }
    Serial.println("Gyroscope Initialized");
}

void loop() {
    float x, y, z;
    
    if (IMU.gyroscopeAvailable()) {
        IMU.readGyroscope(x, y, z);
        
        // Send data in CSV format
        Serial.print(millis());  // Timestamp in milliseconds
        Serial.print(",");
        Serial.print(x);
        Serial.print(",");
        Serial.print(y);
        Serial.print(",");
        Serial.println(z);
    }

    delay(100);  // Adjust sampling frequency
}
