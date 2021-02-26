#include <Arduino.h>

const int num_channels = 16;
const int num_control_pins = 4;

// Define Mux control pins
int s0_pin = 2;
int s1_pin = 3;
int s2_pin = 4;
int s3_pin = 5;
int mux_sig_pin = A0;

// Define Mux array access
int mux_channel_arr[num_channels][num_control_pins]={
    {0,0,0,0}, //channel 0
    {1,0,0,0}, //channel 1
    {0,1,0,0}, //channel 2
    {1,1,0,0}, //channel 3
    {0,0,1,0}, //channel 4
    {1,0,1,0}, //channel 5
    {0,1,1,0}, //channel 6
    {1,1,1,0}, //channel 7
    {0,0,0,1}, //channel 8
    {1,0,0,1}, //channel 9
    {0,1,0,1}, //channel 10
    {1,1,0,1}, //channel 11
    {0,0,1,1}, //channel 12
    {1,0,1,1}, //channel 13
    {0,1,1,1}, //channel 14
    {1,1,1,1}  //channel 15
};


void InitializeMux() {
    pinMode(s0_pin, OUTPUT); 
    pinMode(s1_pin, OUTPUT); 
    pinMode(s2_pin, OUTPUT); 
    pinMode(s3_pin, OUTPUT); 
    pinMode(mux_sig_pin, INPUT);

    digitalWrite(s0_pin, LOW);
    digitalWrite(s1_pin, LOW);
    digitalWrite(s2_pin, LOW);
    digitalWrite(s3_pin, LOW);
}

void ReadMuxChannels() {
    for(int channel = 0; channel < num_channels; channel++) {
        int control_pin_arr[] = {s0_pin, s1_pin, s2_pin, s3_pin};

        // Set the control pins needed to read the desired channel
        for(int i = 0; i < num_control_pins; i ++) {
            digitalWrite(control_pin_arr[i], mux_channel_arr[channel][i]);
        }

        float analog_voltage = (analogRead(mux_sig_pin)/1023.0)*5.0;

        Serial.print("AMUX");
        Serial.print(channel);
        Serial.print(": ");
        Serial.print(analog_voltage);
        Serial.println(" [V]");
    }
}