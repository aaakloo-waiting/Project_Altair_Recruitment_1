#include <Arduino.h>
#include <SoftwareSerial.h>
​
// Bluetooth module pins
#define BT_RX 0
#define BT_TX 1
​
// Motor control pins
#define MOTOR1_ENA 3
#define MOTOR1_IN1 11
#define MOTOR1_IN2 10
#define MOTOR2_ENB 9
#define MOTOR2_IN3 6
#define MOTOR2_IN4 5

SoftwareSerial bluetooth(BT_RX, BT_TX);
​
void setup() {
    pinMode(MOTOR1_ENA, OUTPUT);
    pinMode(MOTOR1_IN1, OUTPUT);
    pinMode(MOTOR1_IN2, OUTPUT);
    pinMode(MOTOR2_ENB, OUTPUT);
    pinMode(MOTOR2_IN3, OUTPUT);
    pinMode(MOTOR2_IN4, OUTPUT);
​
    bluetooth.begin(9600);
}
​
void loop() {
    if (bluetooth.available()) {
        char command = bluetooth.read();
        executeCommand(command);
    }
}
​
void executeCommand(char command) {
    switch (command) {
        case 'F':
            moveForward();
            break;
        case 'B':
            moveBackward();
            break;
        case 'L':
            turnLeft();
            break;
        case 'R':
            turnRight();
            break;
        case 'S':
            stopBot();
            break;
        default:
            // Invalid command, do nothing or send an error response
            break;
    }
}
​
void moveForward() {
    digitalWrite(10, HIGH);
    digitalWrite(5, HIGH);
}
​
void moveBackward() {
    digitalWrite(6, HIGH);
    digitalWrite(11, HIGH);   
}
​
void turnLeft() {
    digitalWrite(10, HIGH);
    digitalWrite(11, HIGH);
}
​
void turnRight() {
    digitalWrite(5, HIGH);
    digitalWrite(6, HIGH);
}
​
void stopBot() {
    digitalWrite(5, LOW);
    digitalWrite(6, LOW);
    digitalWrite(10, LOW);
    digitalWrite(11, LOW);
}