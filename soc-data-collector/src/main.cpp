#include <Arduino.h>
#include "ThermocoupleProcessor.h"
#include "AnalogProcessor.h"

void setup() {
  Serial.begin(9600);  

  InitializeThermocoupleSensor();
  InitializeAnalogSensor();
}

void loop() {
float *temp;

  temp = ReadThermocoupleData();
  ReadAnalogData();

  for (int i=0; i<8; i++){
    Serial.print(temp[i], 2);
    Serial.print(" ");
  }
  Serial.println("");

  delay(250);
}