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
    if (remoteSignal=="e144827d"){
      Serial.println("POWER");
    }
    else if (remoteSignal=="e144a25d"){
      Serial.println("AUTO");
    }
    else if (remoteSignal=="e144629d"){
      Serial.println("MANUAL");
    }
    irrecv.resume(); // Receive the next value
  }
  if (digitalRead(passivePin)==LOW){
    Serial.println("MOTION");
  }
  delay(100);
}
