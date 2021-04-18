#include <Arduino.h>
#include "ThermocoupleProcessor.h"
#include "AnalogProcessor.h"
#include "AnalogMultiplexer.h"
#include "DigitalProcessor.h"

unsigned long serialBaudRate = 115200;
int delayBetweenReadings = 200;

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