#include <Servo.h>

Servo servo1;
Servo servo2;

void setup() {
  Serial.begin(115200);
  servo1.attach(9);
  servo2.attach(10);
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    input.trim();
    int commaIndex = input.indexOf(',');
    if (commaIndex > 0) {
      int val1 = input.substring(0, commaIndex).toInt();
      int val2 = input.substring(commaIndex + 1).toInt();
      val1 = constrain(val1, 0, 180);
      val2 = constrain(val2, 0, 180);
      servo1.write(val1);
      servo2.write(val2);
    }
  }
}
