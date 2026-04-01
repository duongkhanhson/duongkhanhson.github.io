#include <Arduino.h>

// Chọn mô-đun ESP32-CAM AI Thinker
#define CAMERA_MODEL_AI_THINKER

#include "esp_camera.h"
#include <WiFi.h>
#include <WebServer.h>
#include <esp32-hal-ledc.h>
#include <driver/ledc.h>

// Thay bằng thông tin WiFi của bạn
const char* ssid = "Mlab";
const char* password = "0946469720";

#include "camera_pins.h"

WebServer server(80);

// Servo control với LEDC PWM
const int SERVO_PIN = 13;        // Pin chân servo, có thể đổi nếu cần
const int SERVO_CHANNEL = LEDC_CHANNEL_1;     // Dùng kênh khác với camera XCLK
const int SERVO_TIMER = LEDC_TIMER_1;       // Dùng timer khác với camera XCLK
const int SERVO_FREQ = 50;       // 50 Hz cho servo
const int SERVO_RES = 16;        // 16-bit resolution
int currentAngle = 90;

// Hàm hỗ trợ thuật toán PWM servo
uint32_t servoDutyFromAngle(int angle) {
  angle = constrain(angle, 0, 180);
  const int minUs = 600;
  const int maxUs = 2400;
  int pulseUs = minUs + ((maxUs - minUs) * angle) / 180;
  return (uint32_t)((uint64_t)pulseUs * ((1ULL << SERVO_RES) - 1) / 20000ULL);
}

void servoWrite(int angle) {
  currentAngle = constrain(angle, 0, 180);
  uint32_t duty = servoDutyFromAngle(currentAngle);
  ledcWrite(SERVO_CHANNEL, duty);
}

String getContentType(const String& filename) {
  if (server.hasArg("download"))
    return "application/octet-stream";
  else if (filename.endsWith(".htm"))
    return "text/html";
  else if (filename.endsWith(".html"))
    return "text/html";
  else if (filename.endsWith(".css"))
    return "text/css";
  else if (filename.endsWith(".js"))
    return "application/javascript";
  else if (filename.endsWith(".png"))
    return "image/png";
  else if (filename.endsWith(".jpg"))
    return "image/jpeg";
  else if (filename.endsWith(".gif"))
    return "image/gif";
  return "text/plain";
}

void handleRoot() {
  String html = "<html><head><title>ESP32-CAM Stream</title></head><body>";
  html += "<h2>ESP32-CAM Stream & Control</h2>";
  html += "<p><a href=\"/stream\">Xem stream MJPEG</a></p>";
  html += "<p>Command example: <code>/control?cmd=LEFT</code> or <code>/control?angle=120</code></p>";
  html += "<p>Current servo angle: " + String(currentAngle) + "</p>";
  html += "</body></html>";
  server.send(200, "text/html", html);
}

void handleNotFound() {
  String message = "Không tìm thấy: ";
  message += server.uri();
  message += "\n";
  message += "Method: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
}

void handleControl() {
  String cmd = server.arg("cmd");
  String ang = server.arg("angle");
  String response = "";

  if (cmd.length() > 0) {
    cmd.trim();
    cmd.toUpperCase();
    if (cmd == "LEFT") {
      servoWrite(0);
      response = "OK: LEFT -> angle=0";
    } else if (cmd == "RIGHT") {
      servoWrite(180);
      response = "OK: RIGHT -> angle=180";
    } else if (cmd == "CENTER" || cmd == "MID") {
      servoWrite(90);
      response = "OK: CENTER -> angle=90";
    } else {
      int value = cmd.toInt();
      if (value >= 0 && value <= 180) {
        servoWrite(value);
        response = "OK: cmd angle=" + String(currentAngle);
      } else {
        response = "ERROR: Unknown cmd value: " + cmd;
      }
    }
  } else if (ang.length() > 0) {
    int value = ang.toInt();
    if (value >= 0 && value <= 180) {
      servoWrite(value);
      response = "OK: angle=" + String(currentAngle);
    } else {
      response = "ERROR: angle must be 0-180";
    }
  } else {
    response = "ERROR: Missing cmd or angle parameter";
  }

  server.send(200, "text/plain", response);
}

void handleStream() {
  WiFiClient client = server.client();
  String response = "HTTP/1.1 200 OK\r\n";
  response += "Content-Type: multipart/x-mixed-replace; boundary=frame\r\n";
  response += "Cache-Control: no-cache\r\n";
  response += "Connection: close\r\n\r\n";
  server.sendContent(response);

  while (true) {
    camera_fb_t * fb = esp_camera_fb_get();
    if (!fb) {
      break;
    }

    response = "--frame\r\n";
    response += "Content-Type: image/jpeg\r\n";
    response += "Content-Length: " + String(fb->len) + "\r\n\r\n";

    if (!client.connected()) {
      esp_camera_fb_return(fb);
      break;
    }

    client.write(response.c_str(), response.length());
    client.write(fb->buf, fb->len);
    client.write("\r\n");
    esp_camera_fb_return(fb);
    if (!client.connected()) {
      break;
    }
  }
}

void initCamera() {
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;

  config.frame_size = FRAMESIZE_VGA;
  config.jpeg_quality = 12;
  config.fb_count = 2;

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }
}

void startCameraServer() {
  server.on("/", HTTP_GET, handleRoot);
  server.on("/control", HTTP_GET, handleControl);
  server.on("/stream", HTTP_GET, handleStream);
  server.onNotFound(handleNotFound);
  server.begin();
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  pinMode(SERVO_PIN, OUTPUT);

  ledc_timer_config_t ledc_timer;
  ledc_timer.speed_mode = LEDC_HIGH_SPEED_MODE;
  ledc_timer.duty_resolution = (ledc_timer_bit_t)SERVO_RES;
  ledc_timer.timer_num = (ledc_timer_t)SERVO_TIMER;
  ledc_timer.freq_hz = SERVO_FREQ;
  ledc_timer_config(&ledc_timer);

  ledc_channel_config_t ledc_channel;
  ledc_channel.gpio_num = SERVO_PIN;
  ledc_channel.speed_mode = LEDC_HIGH_SPEED_MODE;
  ledc_channel.channel = (ledc_channel_t)SERVO_CHANNEL;
  ledc_channel.timer_sel = (ledc_timer_t)SERVO_TIMER;
  ledc_channel.intr_type = LEDC_INTR_DISABLE;
  ledc_channel.duty = 0;
  ledc_channel.hpoint = 0;
  ledc_channel_config(&ledc_channel);

  servoWrite(currentAngle);

  WiFi.begin(ssid, password);
  Serial.print("Dang ket noi WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.println("WiFi da ket noi");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());

  initCamera();
  startCameraServer();
}

void loop() {
  server.handleClient();
}
