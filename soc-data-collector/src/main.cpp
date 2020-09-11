#include <Arduino.h>
#include "TcProcessor.h"

int sensorPin = A3;
int sensorValue = 0;

void setup() {
  Serial.begin(9600);  

  InitializeSensor();
}

void loop() {
  CollectData();

  sensorValue = analogRead(sensorPin);
  float voltage= sensorValue * (5.0 / 1023.0);
  Serial.print("    Voltage: ");
  Serial.print(voltage);
  Serial.println("");
  delay(500);
}