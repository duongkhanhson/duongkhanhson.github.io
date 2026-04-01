// Servo Motor SG90 Control via Serial
#include <Servo.h>

Servo myServo;          // Tạo object servo
const int servoPin = 9; // Pin PWM cho servo (Arduino Uno)
int angle = 90;         // Góc ban đầu (90 độ)

void setup() {
  Serial.begin(9600);   // Khởi tạo serial communication ở 9600 baud
  myServo.attach(servoPin); // Gắn servo vào pin 9
  myServo.write(angle); // Đặt góc ban đầu
  
  Serial.println("Servo Control Ready!");
  Serial.println("Send angle (0-180) or commands: MIN, MID, MAX");
}

void loop() {
  // Kiểm tra xem có dữ liệu từ serial không
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim(); // Xóa khoảng trắng
    
    // Xử lý lệnh
    if (command == "MIN") {
      angle = 0;
      Serial.println("Set to MIN (0 degrees)");
    } 
    else if (command == "MID" || command == "CENTER") {
      angle = 90;
      Serial.println("Set to MID (90 degrees)");
    } 
    else if (command == "MAX") {
      angle = 180;
      Serial.println("Set to MAX (180 degrees)");
    } 
    else {
      // Cố gắng chuyển đổi thành số
      int newAngle = command.toInt();
      if (newAngle >= 0 && newAngle <= 180) {
        angle = newAngle;
        Serial.print("Set angle to: ");
        Serial.println(angle);
      } else {
        Serial.println("Invalid angle! Please enter 0-180");
      }
    }
    
    // Cập nhật vị trí servo
    myServo.write(angle);
    delay(15); // Chờ servo cập nhật vị trí
  }
}
