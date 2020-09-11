#include <Arduino.h>
#include "TcProcessor.h"

void setup() {
  Serial.begin(9600);  
  InitializeSensor();
}

void loop() {
  CollectData();
}