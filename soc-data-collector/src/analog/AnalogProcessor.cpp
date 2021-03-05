#include <Arduino.h>

// Define Analog Pins
const int num_analog_pins = 15;
uint8_t anaSensorPinArr[num_analog_pins]{
    A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15
};
int anaSensorValueArr[num_analog_pins]{
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
};

void ReadAnalogData() {
    for (int index=1; index <= num_analog_pins; index++){
        anaSensorValueArr[index-1] = analogRead(anaSensorPinArr[index-1]);
        float voltage = anaSensorValueArr[index-1] * (5.0 / 1023.0);

        Serial.print("ANLG");
        Serial.print(index);
        Serial.print(": ");
        Serial.print(voltage);
        Serial.println(" [V]");
    }
}