#include <Arduino.h>
#include "ThermocoupleProcessor.h"
#include "AnalogProcessor.h"
#include "AnalogMultiplexer.h"

int serialBaudRate = 9600;
int delayBetweenReadings = 1000;

void setup() {
  Serial.begin(serialBaudRate);  

  InitializeThermocoupleSensor();
  InitializeMux();
}

void loop() {
  ReadThermocoupleData();
  PublishSerialThermocoupleData();
  ReadAnalogData();
  ReadMuxChannels();
  
  delay(delayBetweenReadings);
}