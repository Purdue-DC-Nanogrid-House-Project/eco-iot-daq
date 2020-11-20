#include <Arduino.h>

int sensorPin1 = A1;
int sensorPin2 = A2;
int sensorPin3 = A3;
int sensorPin4 = A4;
int sensorPin5 = A5;

int sensorValue1 = 0;
int sensorValue2 = 0;
int sensorValue3 = 0;
int sensorValue4 = 0;
int sensorValue5 = 0;

void InitializeAnalogSensor() {

}

void ReadAnalogData() {
    sensorValue1 = analogRead(sensorPin1);
    sensorValue2 = analogRead(sensorPin2);
    sensorValue3 = analogRead(sensorPin3);
    sensorValue4 = analogRead(sensorPin4);
    sensorValue5 = analogRead(sensorPin5);
    
    float voltage1 =  sensorValue1 * (5.0 / 1023.0);
    float voltage2 =  sensorValue2 * (5.0 / 1023.0);
    float voltage3 = (sensorValue3 * (5.0 / 1023.0) * 27.402 - 43.672 + 14.7) * 6.89476;
    float voltage4 = (sensorValue4 * (5.0 / 1023.0) * 48.285 - 6.665 + 14.7) * 6.89476;
    float voltage5 =  sensorValue5 * (5.0 / 1023.0);
    
    Serial.print("A ");
    Serial.print(voltage1);
    Serial.print(" A ");
    Serial.print(voltage2);        
    Serial.print(" A ");
    Serial.print(voltage3);
    Serial.print(" A ");
    Serial.print(voltage4);
    Serial.print(" A ");
    Serial.print(voltage5);    
    Serial.println("");
}