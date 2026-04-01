// Điều khiển LED Pin 13 dựa vào phát hiện màu xanh từ Python

const int LED_PIN = 13;

void setup() {
  Serial.begin(9600);        // Khởi tạo serial 9600 baud
  pinMode(LED_PIN, OUTPUT);  // Đặt pin 13 là OUTPUT
  digitalWrite(LED_PIN, LOW); // Tắt LED lúc khởi động
  
  Serial.println("LED Control Ready!");
}

void loop() {
  // Kiểm tra xem có dữ liệu từ serial không
  if (Serial.available() > 0) {
    char command = Serial.read();  // Đọc 1 ký tự
    
    if (command == '1') {
      digitalWrite(LED_PIN, HIGH);  // Bật LED
      Serial.println("LED: ON");
    }
    else if (command == '0') {
      digitalWrite(LED_PIN, LOW);   // Tắt LED
      Serial.println("LED: OFF");
    }
  }
}
