#include <PID_v1.h>

// --- Cấu hình chân kết nối ---
const int encoderPinA = 2;
const int encoderPinB = 3;
const int motorPWM = 9;
const int motorDir1 = 8;
const int motorDir2 = 10;

// --- Thông số hiệu chuẩn ---
const double pulsesPerRev = 8418;

volatile long encoderPos = 0;
double targetPos = 0;
double currentPos = 0;
double motorOutput = 0;

double Kp = 0.7, Ki = 1.3, Kd = 0.441;
PID myPID(&currentPos, &motorOutput, &targetPos, Kp, Ki, Kd, DIRECT);

void setup() {
  Serial.begin(115200);

  pinMode(encoderPinA, INPUT_PULLUP);
  pinMode(encoderPinB, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(encoderPinA), readEncoder, CHANGE);
  attachInterrupt(digitalPinToInterrupt(encoderPinB), readEncoder, CHANGE);

  pinMode(motorPWM, OUTPUT);
  pinMode(motorDir1, OUTPUT);
  pinMode(motorDir2, OUTPUT);

  myPID.SetMode(AUTOMATIC);
  myPID.SetOutputLimits(-200, 200);
  myPID.SetSampleTime(10);

  Serial.println("--- HE THONG DA SAN SANG ---");
  Serial.println("Nhap goc quay (do) vao Serial (VD: 90, -180, 360):");
}

void loop() {
  if (Serial.available() > 0) {
    String request = Serial.readStringUntil('\n');
    request.trim();

    if (request.length() > 0) {
      if (request.equalsIgnoreCase("HOME")) {
        targetPos = 0;
        Serial.println("HOME");
      } else {
        float angle = request.toFloat();
        targetPos = (angle / 360.0) * pulsesPerRev;
        Serial.print("Target: ");
        Serial.print(angle);
        Serial.println(" deg");
      }
    }
    while (Serial.available()) Serial.read();
  }

  currentPos = (double)encoderPos;
  myPID.Compute();
  controlMotor(motorOutput);

  static unsigned long lastPrint = 0;
  if (millis() - lastPrint > 100) {
    Serial.print("Target_Pulses:");
    Serial.print(targetPos);
    Serial.print(",Current_Pulses:");
    Serial.print(currentPos);
    Serial.print(",Target_Degrees:");
    Serial.print((targetPos / pulsesPerRev) * 360.0);
    Serial.print(",Current_Degrees:");
    Serial.println((currentPos / pulsesPerRev) * 360.0);
    lastPrint = millis();
  }
}

void readEncoder() {
  byte portState = PIND;
  boolean sA = bitRead(portState, 2);
  boolean sB = bitRead(portState, 3);
  static boolean lastA = LOW;
  static boolean lastB = LOW;

  if (sA != lastA) {
    if (sA == sB) encoderPos++;
    else encoderPos--;
  } else {
    if (sA == sB) encoderPos--;
    else encoderPos++;
  }

  lastA = sA;
  lastB = sB;
}

void controlMotor(double output) {
  double error = abs(targetPos - currentPos);

  if (error < 15) {
    digitalWrite(motorDir1, LOW);
    digitalWrite(motorDir2, LOW);
    analogWrite(motorPWM, 0);
    return;
  }

  int speed = abs(output);
  int minPWM = (error < 200) ? 35 : 55;
  speed = constrain(speed, minPWM, 200);

  if (output > 0) {
    digitalWrite(motorDir1, HIGH);
    digitalWrite(motorDir2, LOW);
    analogWrite(motorPWM, speed);
  } else {
    digitalWrite(motorDir1, LOW);
    digitalWrite(motorDir2, HIGH);
    analogWrite(motorPWM, speed);
  }
}
