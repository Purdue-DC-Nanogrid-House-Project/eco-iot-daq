#include <Arduino.h>
#include <EEPROM.h>

#define PINEN 7 //Mux Enable pin
#define PINA0 4 //Mux Address 0 pin
#define PINA1 5 //Mux Address 1 pin
#define PINA2 6 //Mux Address 2 pin
#define PINSO 12 //TCAmp Slave Out pin (MISO)
#define PINSC 13 //TCAmp Serial Clock (SCK)
#define PINCS 9  //TCAmp Chip Select Change this to match the position of the Chip Select Link

static float FloatTemp[8];
int Temp[8];
int SensorFail[8];
char failMode[8];
float floatTemp;
float floatInternalTemp;
int internalTemp;
int intTempFrac;
unsigned int Mask;
char NumSensors = 2;
char UpdateDelay;
char i, j;
char Rxchar;
char Rxenable;
char Rxptr;
char Cmdcomplete;
char R;
char Rxbuf[32];
char adrbuf[3];
char cmdbuf[3];
char valbuf[12];
int val = 0;
int Param; 
unsigned long time;

void InitializeThermocoupleSensor() {
    if (EEPROM.read(511)==1)
    {
        NumSensors = EEPROM.read(0);
        UpdateDelay = EEPROM.read(1);
    }

    pinMode(PINEN, OUTPUT);     
    pinMode(PINA0, OUTPUT);    
    pinMode(PINA1, OUTPUT);    
    pinMode(PINA2, OUTPUT);    
    pinMode(PINSO, INPUT);    
    pinMode(PINCS, OUTPUT);    
    pinMode(PINSC, OUTPUT);    

    digitalWrite(PINEN, HIGH);  // enable on
    digitalWrite(PINA0, LOW);   // low, low, low = channel 1
    digitalWrite(PINA1, LOW); 
    digitalWrite(PINA2, LOW); 
    digitalWrite(PINSC, LOW);   //put clock in low
}

void ReadThermocoupleData() {
    if (millis() > (time + ((unsigned int)UpdateDelay*1000))) {
        time = millis();
        if (j<(NumSensors-1)) j++;
        else j=0;
      
        switch (j) //select channel
        {
            case 0:
            digitalWrite(PINA0, LOW); 
            digitalWrite(PINA1, LOW); 
            digitalWrite(PINA2, LOW);
            break;
            case 1:
            digitalWrite(PINA0, HIGH); 
            digitalWrite(PINA1, LOW); 
            digitalWrite(PINA2, LOW);
            break;
            case 2:
            digitalWrite(PINA0, LOW); 
            digitalWrite(PINA1, HIGH); 
            digitalWrite(PINA2, LOW);
            break;
            case 3:
            digitalWrite(PINA0, HIGH); 
            digitalWrite(PINA1, HIGH); 
            digitalWrite(PINA2, LOW);
            break;
            case 4:
            digitalWrite(PINA0, LOW); 
            digitalWrite(PINA1, LOW); 
            digitalWrite(PINA2, HIGH);
            break;
            case 5:
            digitalWrite(PINA0, HIGH); 
            digitalWrite(PINA1, LOW); 
            digitalWrite(PINA2, HIGH);
            break;
            case 6:
            digitalWrite(PINA0, LOW); 
            digitalWrite(PINA1, HIGH); 
            digitalWrite(PINA2, HIGH);
            break;
            case 7:
            digitalWrite(PINA0, HIGH); 
            digitalWrite(PINA1, HIGH); 
            digitalWrite(PINA2, HIGH);
            break;
        }
        
        delay(5);
        digitalWrite(PINCS, LOW); //stop conversion
        delay(5);
        digitalWrite(PINCS, HIGH); //begin conversion
        delay(100);  //wait 100 ms for conversion to complete
        digitalWrite(PINCS, LOW); //stop conversion, start serial interface
        delay(1);
      
      Temp[j] = 0;
      FloatTemp[j] = 0;
      failMode[j] = 0;
      SensorFail[j] = 0;
      internalTemp = 0;
      for (i=31;i>=0;i--)
      {
          digitalWrite(PINSC, HIGH);
          delay(1);
          
        if ((i<=31) && (i>=18))
        {
          // these 14 bits are the thermocouple temperature data
          // bit 31 sign
          // bit 30 MSB = 2^10
          // bit 18 LSB = 2^-2 (0.25 degC)
          
          Mask = 1<<(i-18);
          if (digitalRead(PINSO)==1)
          {
            if (i == 31)
            {
              Temp[j] += (0b11<<14);//pad the temp with the bit 31 value so we can read negative values correctly
            }
            Temp[j] += Mask;
            //Serial.print("1");
          }
        }
        //bit 17 is reserved
        //bit 16 is sensor fault
        if (i==16)
        {
          SensorFail[j] = digitalRead(PINSO);
        }
        
        if ((i<=15) && (i>=4))
        {
          //these 12 bits are the internal temp of the chip
          //bit 15 sign
          //bit 14 MSB = 2^6
          //bit 4 LSB = 2^-4 (0.0625 degC)
          Mask = 1<<(i-4);
          if (digitalRead(PINSO)==1)
          {
            if (i == 15)
            {
              internalTemp += (0b1111<<12); //pad the temp with the bit 31 value so we can read negative values correctly
            }
            
            internalTemp += Mask;
          }
        }
        //bit 3 is reserved
        if (i==2)
        {
          failMode[j] += digitalRead(PINSO)<<2;//bit 2 is set if shorted to VCC
        }
        if (i==1)
        {
          failMode[j] += digitalRead(PINSO)<<1;//bit 1 is set if shorted to GND
        }
        if (i==0)
        {
          failMode[j] += digitalRead(PINSO)<<0;//bit 0 is set if open circuit
        }
        
        digitalWrite(PINSC, LOW);
        delay(1);
      }

      //Serial.print("#");
      //Serial.print(j+1,DEC);
      //Serial.print(": ");
      if (SensorFail[j] == 1)
      {
        Serial.print("FAIL");
        if ((failMode[j] & 0b0100) == 0b0100)
        {
          Serial.print(" SHORT TO VCC");
        }
        if ((failMode[j] & 0b0010) == 0b0010)
        {
          Serial.print(" SHORT TO GND");
        }
        if ((failMode[j] & 0b0001) == 0b0001)
        {
          Serial.print(" OPEN CIRCUIT");
        }
      }
      else
      {
        floatTemp = (float)Temp[j] * 0.25;
        FloatTemp[j] = floatTemp;
        //Serial.print(floatTemp,2);
        //Serial.print(" degC");
    }//end reading sensors

    floatInternalTemp = (float)internalTemp * 0.0625;
   
  }//end time
  if (Serial.available() > 0)    // Is a character waiting in the buffer?
  {
    Rxchar = Serial.read();      // Get the waiting character

    if (Rxchar == '@')      // Can start recording after @ symbol
    {
      if (Cmdcomplete != 1)
      {
        Rxenable = 1;
        Rxptr = 1;
      }//end cmdcomplete
    }//end rxchar
    if (Rxenable == 1)           // its enabled so record the characters
    {
      if ((Rxchar != 32) && (Rxchar != '@')) //dont save the spaces or @ symbol
      {
        Rxbuf[Rxptr] = Rxchar;
        //Serial.println(Rxchar);
        Rxptr++;
        if (Rxptr > 13) 
        {
          Rxenable = 0;
        }//end rxptr
      }//end rxchar
      if (Rxchar == 13) 
      {
        Rxenable = 0;
        Cmdcomplete = 1;
      }//end rxchar
    }//end rxenable

  }// end serial available

  if (Cmdcomplete == 1)
  {
    Cmdcomplete = 0;
    cmdbuf[0] = toupper(Rxbuf[1]); //copy and convert to upper case
    cmdbuf[1] = toupper(Rxbuf[2]); //copy and convert to upper case
    cmdbuf[2] = 0; //null terminate        Command = Chr(rxbuf(3)) + Chr(rxbuf(4))
    valbuf[0] = Rxbuf[3]; 
    R = Rxptr - 1;
      for (i = 4 ; i <= R ; i++)//For I = 6 To R
      {
          valbuf[i-3] = Rxbuf[i]; //Mystr = Mystr + Chr(rxbuf(i))
      }
     valbuf[R+1] = 0; //null terminate
     Param = atoi(valbuf);//   Param = Val(mystr)
    if (strcmp(cmdbuf,"NS")==0)       //NumSensors
    {
          //'Print "command was ON"
          if ((Param <= 8) && (Param > 0)) 
          {
            NumSensors = Param;                   
          }
          
    }
    if (strcmp(cmdbuf,"UD")==0)       //UpdateDelay
    {
          //'Print "command was ON"
          if ((Param <= 60) && (Param >= 0)) 
          {
            UpdateDelay = Param;                   
          }
          
    }
    if (strcmp(cmdbuf,"SV")==0)       //Save
    {
          EEPROM.write(0,NumSensors);
          EEPROM.write(1,UpdateDelay);
          EEPROM.write(511,1);
    }
  }
}

void PublishSerialThermocoupleData() {
  
  for (int i=0; i<8; i++){
    Serial.print("T ");  
    Serial.print(FloatTemp[i], 2);
    Serial.print(" ");
  }
  Serial.println("");
}