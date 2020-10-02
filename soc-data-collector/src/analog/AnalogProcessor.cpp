#include <Arduino.h>

int sensorPin = A3;
int sensorValue = 0;

void InitializeAnalogSensor() {

}

void ReadAnalogData() {
    sensorValue = analogRead(sensorPin);
    float voltage= sensorValue * (5.0 / 1023.0);
    //Serial.print("Voltage: ");
    //Serial.print(voltage);
    //Serial.println("");
}