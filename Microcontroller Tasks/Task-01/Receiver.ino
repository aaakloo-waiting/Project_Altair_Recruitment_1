#include <Wire.h>

int TestLed = 13;	//pin-13 refers to the built-in LED
int x = 0;

void setup() {
  Wire.begin(1);				//As the function parameter specifies, working as Slave #1 MC
  Wire.onReceive(receiveEvent); //Receiving the data from Master
  pinMode(TestLed, OUTPUT); 	//RGB LED functions as OUTPUT
}

void loop(){
	delay (50);		//Program waits for 100ms
}

void receiveEvent(int howMany) {
  x = Wire.read();  
  //If data is received, blink the LED for 1000ms
  if (x == 1) {
    digitalWrite(TestLed, HIGH);
    delay(1000);
    digitalWrite(TestLed, LOW);
    delay(1000);
  }
  else{
    digitalWrite(TestLed, LOW);
  }
}
