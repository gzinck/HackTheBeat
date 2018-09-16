//possible addition: reset/delay every spike

#include <Filters.h>
int soundSensor = A0;  
float HfilterFrequency = 0.155;
float LfilterFrequency = 0.295;// filters out changes faster that 0.3 Hz.
FilterOnePole lowpassFilter( LOWPASS, LfilterFrequency );   // create a one pole (RC) lowpass filter
FilterOnePole highpassFilter( HIGHPASS, HfilterFrequency );
float LowfilterOutput = 0;
float Bandpass = 0;

void setup() {
  Serial.begin(115200);
  pinMode(soundSensor,INPUT);

}

void loop() {
  LowfilterOutput = lowpassFilter.input( analogRead( soundSensor ) );
  Bandpass = highpassFilter.input( LowfilterOutput );
  Serial.println(Bandpass);
  delay (25);
}
