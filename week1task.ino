void setup() {
  Serial.begin(9600); 
  pinMode(13, OUTPUT); 
}

void loop() {
  if (Serial.available() > 0) { 
    int num = Serial.parseInt(); 
    for (int i = 0; i < num; i++) {
      digitalWrite(13, HIGH); 
      delay(500); 
      digitalWrite(13, LOW); 
      delay(500); 
    }
    
    int randomNum = random(1000, 5000);
    Serial.println(randomNum); 
  } 

}