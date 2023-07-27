#include <LiquidCrystal.h>

volatile int count = 0;

int interruptPin = 2;
float speedRPM = 0.00;

LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void encoderPulse()
{
  count++;
} 
void setup() {
  lcd.begin(16, 2);
  lcd.print("DC-Motor Speed:");
  lcd.setCursor(7, 1);
  lcd.print("rpm");  
  pinMode(interruptPin, INPUT_PULLUP);  
  attachInterrupt(digitalPinToInterrupt(interruptPin), encoderPulse, RISING);
}
void loop() {
  
  lcd.setCursor(0, 1);
  count = 0;
  delay(100);
  
  speedRPM = (float)count * 6.25;
  lcd.print(speedRPM);
}