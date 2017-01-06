/*  Arduino Sensor
 *  
 *  Does the sensing component of my universal remote
 *  
 *  Author: Andy Tracy <adtme11@gmail.com>
 */

#include <IRremote.h>

int remotePin = 11;
int passivePin = 10;
String remoteSignal;

IRrecv irrecv(remotePin);

decode_results results;

void setup()
{
  Serial.begin(9600);
  pinMode(passivePin, INPUT);
  irrecv.enableIRIn(); // Start the receiver
}

void loop() {
  if (irrecv.decode(&results)) {
    remoteSignal=String(results.value, HEX);
    if (remoteSignal=="61a09d62"){ // 'Home' Button
      Serial.println("HOME");
    }
    else if (remoteSignal=="61a000ff"){ // '1' Button
      Serial.println("ONE");
    }
    else if (remoteSignal=="61a0807f"){ // '2' Button
      Serial.println("TWO");
    }
    else if (remoteSignal=="61a040bf"){ // '3' Button
      Serial.println("THREE");
    }
    else if (remoteSignal=="61a0c03f"){ // '4' Button
      Serial.println("FOUR");
    }
    irrecv.resume(); // Receive the next value
  }
  if (digitalRead(passivePin)==LOW){
    Serial.println("MOTION");
  }
  delay(100);
}
