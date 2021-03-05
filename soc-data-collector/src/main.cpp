#include <Arduino.h>
#include "ThermocoupleProcessor.h"
#include "AnalogProcessor.h"
#include "AnalogMultiplexer.h"
#include "DigitalProcessor.h"

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
  ReadDigitalData();
  
  delay(delayBetweenReadings);
}