#include <Arduino.h>
#include "ThermocoupleProcessor.h"
#include "AnalogProcessor.h"
#include "AnalogMultiplexer.h"

void setup() {
  Serial.begin(9600);  

  InitializeThermocoupleSensor();
  InitializeAnalogSensor();
  InitializeMux();
}

void loop() {
  ReadThermocoupleData();
  PublishSerialThermocoupleData();
  ReadAnalogData();

  ReadMuxChannel(0);
  
  delay(1000);
}