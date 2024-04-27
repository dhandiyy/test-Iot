//seuaikan pin pada tempat led
const int pinLed = 2;

void setup() {
  //nilai harus sama dengan baudRate pada code Python
  Serial.begin(115200); 
  pinMode(pinLed, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char perintah = Serial.read();

    if (perintah == '1') {
      digitalWrite(pinLed, HIGH);  
    } else if (perintah == '0') {
      digitalWrite(pinLed, LOW); 
    }
  }
}
