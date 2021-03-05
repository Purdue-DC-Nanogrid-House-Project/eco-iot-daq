#include <Arduino.h>

// Define Analog Pins
const int num_digital_pins = 33;
int digSensorPinArr[num_digital_pins]{
    22, 23, 24, 25, 26, 27, 28, 29, 
    30, 31, 32, 32, 33, 34, 35, 36, 
    37, 38, 39, 40, 41, 42, 43, 44, 
    45, 46, 47, 48, 49, 50, 51, 52, 
    53
};
int digSensorValueArr[num_digital_pins]{
    0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 
    0
};

void ReadDigitalData() {
    for (int index=1; index <= num_digital_pins; index++){
        digSensorValueArr[index-1] = digitalRead(digSensorPinArr[index-1]);

        Serial.print("DIGL");
        Serial.print(index);
        Serial.print(": ");
        Serial.print(digSensorValueArr[index-1]);
        Serial.println(" [-]");
    }
}