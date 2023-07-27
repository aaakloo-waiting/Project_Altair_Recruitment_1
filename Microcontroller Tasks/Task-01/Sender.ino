#include <Wire.h>

int pushButton=A1; 	//pushbutton is connected in A1 pin
int x = 0;

void setup() {
  Wire.begin();					//It sets the m.c. as Master MC.
  pinMode(pushButton, INPUT);	//Sets pushButton ready to give input signals
}

void loop() {
  Wire.beginTransmission(1); 	//Starts transmitting to slave #1
  x=digitalRead(pushButton); 	//Reads input signal from pushButton 
  Wire.write(x);              	//writes the data in Master MC. 
  Wire.endTransmission();    	// stops transmitting
  
  delay(200);					//Program waits for 500ms
}