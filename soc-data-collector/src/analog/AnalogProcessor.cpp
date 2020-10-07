#include <Arduino.h>

int sensorPin3 = A3;
int sensorPin4 = A4;
int sensorValue3 = 0;
int sensorValue4 = 0;

void InitializeAnalogSensor() {

}

void ReadAnalogData() {
    sensorValue3 = analogRead(sensorPin3);
    sensorValue4 = analogRead(sensorPin4);
    float voltage3 = sensorValue3 * (5.0 / 1023.0);
    float voltage4 = sensorValue4 * (5.0 / 1023.0);
    Serial.print("A ");
    Serial.print(voltage3);
    Serial.print(" A ");
    Serial.print(voltage4);
    Serial.println("");
}