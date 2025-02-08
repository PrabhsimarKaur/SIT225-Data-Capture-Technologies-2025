#include <DHT.h>


#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);


void setup()
{
  Serial.begin(9600);
  dht.begin();

  delay(5000);
}

void loop()
{
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  Serial.println(String(humidity) + "," + String(temperature));

  

  delay(15 *1000);
}

