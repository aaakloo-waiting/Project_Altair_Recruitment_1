char message[15] = "Project Altair"; //Message to transmit

void setup() {
  // Begin the Serial at 9600 Baud
  Serial.begin(9600);
}

void loop() {
  Serial.write(message, 15); //Writing the serial input
  delay(1000);				 //Program waits for 1000ms
}