#include <Servo.h>

// TB6612 pins
const int AIN1 = 7;
const int AIN2 = 6;
const int PWMA = 5;
const int BIN1 = 9;
const int BIN2 = 8;
const int PWMB = 10;

// Servo pin
Servo mouthServo;
const int SERVO_PIN = 3;

String input = "";

void setup() {
  Serial.begin(115200);

  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  pinMode(PWMB, OUTPUT);

  // motor speed
  analogWrite(PWMA, 255);
  analogWrite(PWMB, 255);

  // motor direction
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);

  mouthServo.attach(SERVO_PIN);
  mouthServo.write(90);
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      if (input == "OPEN") {
        mouthServo.write(180);
      } else if (input == "CLOSE") {
        mouthServo.write(100);
      }
      input = "";
    } else {
      input += c;
    }
  }
}
