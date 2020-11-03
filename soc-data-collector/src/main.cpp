#include <Arduino.h>
#include "ThermocoupleProcessor.h"
#include "AnalogProcessor.h"

void setup() {
  Serial.begin(9600);  

  InitializeThermocoupleSensor();
  InitializeAnalogSensor();
}

void loop() {
  ReadThermocoupleData();
  PublishSerialThermocoupleData();
  ReadAnalogData();

  delay(250);
}