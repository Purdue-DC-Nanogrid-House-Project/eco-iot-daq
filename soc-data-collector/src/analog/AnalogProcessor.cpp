#include <Arduino.h>

int sensorPin1 = A1;
int sensorPin2 = A2;
int sensorPin3 = A3;
int sensorPin4 = A4;
int sensorPin5 = A5;

int sensorValue1;
int sensorValue2;
int sensorValue3;
int sensorValue4;
int sensorValue5;

void InitializeAnalogSensor() {
    sensorValue1 = 0;
    sensorValue2 = 0;
    sensorValue3 = 0;
    sensorValue4 = 0;
    sensorValue5 = 0;
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
    
    Serial.print("ANLG1: ");
    Serial.print(voltage1);
    Serial.println(" [V]");

    Serial.print("ANLG2: ");
    Serial.print(voltage2); 
    Serial.println(" [V]");

    Serial.print("ANLG3: ");
    Serial.print(voltage3);
    Serial.println(" [V]");

    Serial.print("ANLG4: ");
    Serial.print(voltage4);
    Serial.println(" [V]");

    Serial.print("ANLG5: ");
    Serial.print(voltage5);  
    Serial.println(" [V]");  
}