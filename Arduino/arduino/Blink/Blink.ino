void setup() {
  
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}


void loop() {
  
  if(Serial.available() > 0) {
    char value = Serial.read();
    if(value =='N') digitalWrite(13,HIGH);
    else if(value =='F') digitalWrite(13, LOW);
    
    
  }
}




