#include <LiquidCrystal.h>

char message[15];
byte row;
// Initialising the library by associating any needed LCD interface pin
// Arduino pin numbers and connections
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  row = 0;
  Serial.begin(9600);
  lcd.begin(16, 2);
}

void loop() {
  
  Serial.readBytes(message, 15); //Reading the message as serial data
  								 //Storing the data in variable
  lcd.clear();
  lcd.setCursor(0, row);
  lcd.print(message);
  row = ! row;
  delay(1000);					//Program waits for 1000ms
 
}