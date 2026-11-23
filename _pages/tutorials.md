---
title: "Hướng Dẫn & Knowledge (Tutorials) "
permalink: /tutorials/
layout: single
author_profile: true
---

<style>
  /* Course Section Styling */
  .mlab-course-section {
    margin-bottom: 2.5rem;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }
  .mlab-section-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, #1e3a8a, #2563eb);
    color: #fff;
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    padding: 5px 12px;
    border-radius: 999px;
    margin-bottom: 10px;
  }
  .mlab-course-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.08), 0 4px 10px -2px rgba(15, 23, 42, 0.04);
    overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .mlab-course-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #1d4ed8 100%);
    color: #ffffff;
    padding: 24px 26px;
    position: relative;
  }
  .mlab-course-tag-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 12px;
  }
  .mlab-badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 700;
  }
  .mlab-badge-mode {
    background: rgba(56, 189, 248, 0.2);
    color: #7dd3fc;
    border: 1px solid rgba(125, 211, 252, 0.35);
  }
  .mlab-badge-discount {
    background: #ef4444;
    color: #ffffff;
  }
  .mlab-badge-cert {
    background: rgba(34, 197, 94, 0.2);
    color: #86efac;
    border: 1px solid rgba(134, 239, 172, 0.35);
  }
  .mlab-course-title {
    margin: 0 0 8px 0 !important;
    font-size: 1.55rem !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    line-height: 1.3 !important;
  }
  .mlab-course-subtitle {
    margin: 0;
    font-size: 0.95rem;
    color: #cbd5e1;
    font-weight: 500;
  }
  .mlab-course-meta-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    margin-top: 16px;
    padding-top: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.14);
    font-size: 0.83rem;
    color: #e2e8f0;
  }
  .mlab-course-body {
    padding: 24px 26px;
    color: #1e293b;
    font-size: 0.92rem;
    line-height: 1.65;
  }
  .mlab-course-intro {
    margin-bottom: 18px;
    color: #334155;
  }
  .mlab-project-tags {
    background: #f8fafc;
    border-left: 4px solid #2563eb;
    padding: 12px 16px;
    border-radius: 0 8px 8px 0;
    margin-bottom: 20px;
    font-size: 0.88rem;
    color: #1e293b;
  }
  .mlab-grid-2 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 18px;
    margin-bottom: 20px;
  }
  .mlab-info-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 16px;
  }
  .mlab-info-box h4 {
    margin: 0 0 10px 0 !important;
    font-size: 0.98rem !important;
    color: #0f172a !important;
  }
  .mlab-info-box ul {
    margin: 0;
    padding-left: 18px;
    font-size: 0.86rem;
    color: #334155;
  }
  .mlab-info-box ul li {
    margin-bottom: 6px;
  }
  .mlab-curriculum-details {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    margin-bottom: 22px;
    overflow: hidden;
  }
  .mlab-curriculum-details summary {
    padding: 14px 18px;
    background: #f1f5f9;
    font-weight: 700;
    color: #0f172a;
    cursor: pointer;
    user-select: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.92rem;
  }
  .mlab-curriculum-details summary:hover {
    background: #e2e8f0;
  }
  .mlab-curriculum-content {
    padding: 16px 20px;
    font-size: 0.86rem;
    max-height: 360px;
    overflow-y: auto;
    border-top: 1px solid #e2e8f0;
  }
  .mlab-course-footer {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding-top: 18px;
    border-top: 1px solid #e2e8f0;
  }
  .mlab-price-box {
    display: flex;
    align-items: baseline;
    gap: 10px;
    flex-wrap: wrap;
  }
  .mlab-price-current {
    font-size: 1.65rem;
    font-weight: 800;
    color: #dc2626;
  }
  .mlab-price-old {
    font-size: 0.95rem;
    color: #94a3b8;
    text-decoration: line-through;
  }
  .mlab-action-group {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
  .mlab-btn-enroll {
    background: linear-gradient(135deg, #ea580c, #dc2626);
    color: #ffffff !important;
    font-weight: 700;
    font-size: 0.95rem;
    padding: 12px 24px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    box-shadow: 0 4px 14px rgba(220, 38, 38, 0.35);
    transition: all 0.2s ease;
    text-decoration: none !important;
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }
  .mlab-btn-enroll:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(220, 38, 38, 0.45);
  }
  .mlab-btn-outline {
    background: #f1f5f9;
    color: #1e293b !important;
    font-weight: 600;
    font-size: 0.88rem;
    padding: 12px 16px;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    text-decoration: none !important;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .mlab-btn-outline:hover {
    background: #e2e8f0;
  }

  /* Registration & VietQR Modal */
  .mlab-modal-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(15, 23, 42, 0.72);
    backdrop-filter: blur(4px);
    z-index: 9999;
    align-items: center;
    justify-content: center;
    padding: 16px;
    overflow-y: auto;
  }
  .mlab-modal-overlay.active {
    display: flex;
  }
  .mlab-modal {
    background: #ffffff;
    width: 100%;
    max-width: 560px;
    border-radius: 16px;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35);
    overflow: hidden;
    max-height: 92vh;
    display: flex;
    flex-direction: column;
    animation: mlabModalIn 0.22s ease-out;
  }
  @keyframes mlabModalIn {
    from { opacity: 0; transform: translateY(15px) scale(0.98); }
    to { opacity: 1; transform: translateY(0) scale(1); }
  }
  .mlab-modal-header {
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    color: #ffffff;
    padding: 18px 22px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .mlab-modal-header h3 {
    margin: 0 !important;
    font-size: 1.12rem !important;
    color: #ffffff !important;
  }
  .mlab-modal-close {
    background: rgba(255, 255, 255, 0.15);
    border: none;
    color: #ffffff;
    width: 32px;
    height: 32px;
    border-radius: 8px;
    font-size: 1.2rem;
    cursor: pointer;
    line-height: 1;
  }
  .mlab-modal-body {
    padding: 20px 22px;
    overflow-y: auto;
    color: #1e293b;
    font-size: 0.9rem;
  }
  .mlab-step-indicator {
    display: flex;
    gap: 8px;
    margin-bottom: 18px;
  }
  .mlab-step-pill {
    flex: 1;
    text-align: center;
    padding: 7px 10px;
    border-radius: 8px;
    font-size: 0.78rem;
    font-weight: 700;
    background: #f1f5f9;
    color: #64748b;
  }
  .mlab-step-pill.active {
    background: #dbeafe;
    color: #1d4ed8;
    border: 1px solid #93c5fd;
  }
  .mlab-step-pill.done {
    background: #dcfce7;
    color: #15803d;
  }
  .mlab-form-group {
    margin-bottom: 13px;
  }
  .mlab-form-group label {
    display: block;
    font-weight: 700;
    font-size: 0.83rem;
    margin-bottom: 5px;
    color: #334155;
  }
  .mlab-form-control {
    width: 100%;
    padding: 10px 12px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-size: 0.9rem;
    box-sizing: border-box;
    background: #fff;
    color: #0f172a;
  }
  .mlab-form-control:focus {
    outline: none;
    border-color: #2563eb;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
  }
  .mlab-form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }
  @media (max-width: 520px) {
    .mlab-form-row {
      grid-template-columns: 1fr;
    }
  }
  .mlab-qr-box {
    text-align: center;
    background: #f8fafc;
    border: 2px dashed #93c5fd;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 14px;
  }
  .mlab-qr-box img {
    max-width: 250px;
    width: 100%;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    margin: 0 auto 10px auto;
    display: block;
    background: #fff;
  }
  .mlab-bank-details {
    text-align: left;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 0.83rem;
    margin-top: 10px;
  }
  .mlab-bank-details div {
    padding: 4px 0;
    border-bottom: 1px dashed #f1f5f9;
    display: flex;
    justify-content: space-between;
    gap: 8px;
  }
  .mlab-bank-details div:last-child {
    border-bottom: none;
  }
  .mlab-btn-primary {
    width: 100%;
    background: linear-gradient(135deg, #1d4ed8, #1e40af);
    color: #ffffff;
    border: none;
    padding: 12px 18px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 0.95rem;
    cursor: pointer;
    transition: opacity 0.2s;
  }
  .mlab-btn-primary:hover {
    opacity: 0.94;
  }
  .mlab-btn-success {
    width: 100%;
    background: linear-gradient(135deg, #16a34a, #15803d);
    color: #ffffff;
    border: none;
    padding: 13px 18px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 0.95rem;
    cursor: pointer;
  }
  .mlab-btn-back {
    background: transparent;
    border: 1px solid #cbd5e1;
    color: #475569;
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
    margin-top: 8px;
    width: 100%;
  }
  .mlab-success-box {
    text-align: center;
    padding: 16px 8px;
  }
</style>

<!-- ==================== MODULE ĐĂNG KÝ KHÓA HỌC NGẮN HẠN ==================== -->
<div class="mlab-course-section">
  <div class="mlab-section-badge">
    <span>🚀 KHÓA HỌC NGẮN HẠN & ĐÀO TẠO THỰC CHIẾN - MLAB</span>
  </div>

  <div class="mlab-course-card">
    <div class="mlab-course-header">
      <div class="mlab-course-tag-row">
        <span class="mlab-badge mlab-badge-mode">🌐 Học Online & Offline tại MLAB</span>
        <span class="mlab-badge mlab-badge-discount">🔥 Ưu đãi Giảm 57%</span>
        <span class="mlab-badge mlab-badge-cert">🎓 Cấp chứng nhận hoàn thành</span>
      </div>
      <h2 class="mlab-course-title">IoT CHO SINH VIÊN KỸ THUẬT</h2>
      <p class="mlab-course-subtitle">🎓 Không cần giỏi lập trình – Học từ cơ bản đến thực hành & xây dựng đồ án thực tế!</p>
      <div class="mlab-course-meta-bar">
        <span>👨‍🏫 <strong>Giảng viên:</strong> ThS. Đường Khánh Sơn (MLAB)</span>
        <span>📚 <strong>Giáo trình:</strong> 17 Chương / 22 Bài học</span>
        <span>⭐ <strong>Đánh giá:</strong> 5.0/5.0</span>
        <span>🛠️ <strong>Thực hành:</strong> Arduino, ESP32, Blynk, Cloud</span>
      </div>
    </div>

    <div class="mlab-course-body">
      <div class="mlab-course-intro">
        Khóa học giúp bạn bước vào thế giới <strong>Internet of Things (IoT)</strong> – nơi mọi thiết bị đều có thể giao tiếp và điều khiển từ xa. Dành riêng cho sinh viên kỹ thuật, khóa học trang bị kiến thức nền tảng về cảm biến, vi điều khiển (Arduino, ESP32), truyền dữ liệu không dây và ứng dụng thực tế. Học xong có thể áp dụng ngay cho học tập, đồ án, nghiên cứu khoa học hoặc phát triển sản phẩm cá nhân.
      </div>

      <div class="mlab-project-tags">
        <strong>💡 Đặc biệt – Hướng dẫn chi tiết xây dựng các đồ án IoT ứng dụng thực tế:</strong><br>
        Mô hình nhà thông minh (Smart Home), vườn thông minh, giám sát nhà yến thông minh, giám sát chất lượng nước, cảnh báo cháy nổ và chữa cháy tự động, trạm thời tiết & chất lượng không khí (BME680), camera thông minh, khóa cửa bảo mật vân tay / nhận diện khuôn mặt, chấm công, robot, xử lý nước thải, điều khiển từ xa qua App điện thoại với <em>Blynk, Arduino Cloud, ThingSpeak, Firebase, Telegram...</em>
      </div>

      <div class="mlab-grid-2">
        <div class="mlab-info-box">
          <h4>🎯 Bạn sẽ học được gì?</h4>
          <ul>
            <li>Nguyên lý hoạt động của hệ thống IoT toàn diện.</li>
            <li>Làm chủ Arduino, ESP32 và các cảm biến thông dụng (I2C, ADC, ngắt ngoài).</li>
            <li>Kết nối mạng Wi-Fi, giao thức TCP/IP và đẩy dữ liệu lên Internet.</li>
            <li>Điều khiển thiết bị từ xa bằng Smartphone theo thời gian thực.</li>
            <li>Tạo Dashboard giám sát trực quan (Blynk, Arduino Cloud, ThingSpeak, Firebase, MQTT).</li>
            <li>Tự tay hoàn thiện các dự án & đồ án IoT thực tế.</li>
          </ul>
        </div>
        <div class="mlab-info-box">
          <h4>👨‍🔧 Khóa học phù hợp với ai?</h4>
          <ul>
            <li>Sinh viên các ngành: Kỹ thuật, Điện – Điện tử, Cơ điện tử, CNTT, Tự động hóa, Robotics...</li>
            <li>Người mới bắt đầu muốn học bài bản về lập trình nhúng và IoT từ cơ bản.</li>
            <li>Sinh viên đang chuẩn bị làm đồ án môn học, đồ án tốt nghiệp, nghiên cứu khoa học hoặc thi kỹ thuật.</li>
            <li>Người yêu thích công nghệ muốn tự chế tạo hệ thống Smart Home / Smart Farm.</li>
          </ul>
        </div>
      </div>

      <details class="mlab-curriculum-details">
        <summary>
          <span>📋 Xem chi tiết Đề cương khóa học (10 Chuyên đề & 22 Bài học thực chiến)</span>
          <span style="color: #2563eb; font-size: 0.82rem;">Nhấn để mở rộng ▼</span>
        </summary>
        <div class="mlab-curriculum-content">
          <p style="margin-top:0;"><strong>🧱 Phần A – 10 Chuyên đề cốt lõi:</strong></p>
          <ol style="margin-bottom: 14px; padding-left: 20px;">
            <li><strong>Giới thiệu IoT:</strong> Khái niệm, kiến trúc và ứng dụng thực tế.</li>
            <li><strong>Làm quen Arduino & ESP32:</strong> Cài đặt IDE, cấu hình board và nạp code đầu tiên.</li>
            <li><strong>Cảm biến cơ bản:</strong> Đọc dữ liệu DHT11 (nhiệt độ - độ ẩm), PIR (chuyển động)...</li>
            <li><strong>Điều khiển thiết bị:</strong> Điều khiển LED, Relay đóng ngắt bằng nút nhấn và code.</li>
            <li><strong>Kết nối Wi-Fi:</strong> Cấu hình ESP32 kết nối mạng và xử lý mất kết nối.</li>
            <li><strong>Gửi dữ liệu lên Internet:</strong> Đẩy dữ liệu cảm biến lên Firebase / ThingSpeak.</li>
            <li><strong>Điều khiển từ xa qua App:</strong> Sử dụng Blynk / Telegram bật tắt thiết bị từ điện thoại.</li>
            <li><strong>Tạo Dashboard giám sát:</strong> Hiển thị biểu đồ và thông số online qua Web/App.</li>
            <li><strong>Xây dựng dự án IoT mẫu:</strong> Hệ thống giám sát và cảnh báo nhiệt độ online.</li>
            <li><strong>Tổng kết & Định hướng nâng cao:</strong> Node-RED, MQTT, AIoT thực chiến.</li>
          </ol>
          <p><strong>📚 Phần B – Chi tiết 17 Chương / 22 Bài học & Đồ án thực tế:</strong></p>
          <ul style="margin-bottom: 0; padding-left: 20px;">
            <li><strong>Chương 1 – 5 (Lý thuyết nền tảng):</strong> Bài 1: Giới thiệu môn học IoT | Bài 2: Tổng quan về IoT | Bài 3: Lập trình cho thiết bị IoT | Bài 4: Internet và TCP/IP | Bài 5: An toàn và bảo mật IoT.</li>
            <li><strong>Chương 6 (Thực hành dự án nhỏ trên ESP32):</strong> Bài 6: Điều khiển LED đơn | Bài 7: Input, Output và Ngắt ngoài trên ESP32 | Bài 8: Giao tiếp I2C, ADC với các cảm biến thông dụng | Bài 9: Nền tảng Blynk với ESP32 | Bài 10: Arduino Cloud với ESP32 | Bài 11: ThingSpeak với ESP32.</li>
            <li><strong>Chương 7 – 17 (Xây dựng 11 Đồ án IoT thực tế - Bài 12 đến Bài 22):</strong>
              <ul>
                <li>Mô hình Nhà thông minh (Smart Home)</li>
                <li>Mô hình Giám sát mực nước trong bồn và điều khiển bơm từ xa</li>
                <li>Mô hình Cảnh báo cháy nổ và chữa cháy tự động</li>
                <li>Mô hình Giám sát chất lượng nước</li>
                <li>Mô hình Trạm giám sát chất lượng không khí trong nhà dùng cảm biến BME680</li>
                <li>Mô hình Vườn thông minh (Smart Garden)</li>
                <li>Mô hình Khóa cửa thông minh mở bằng vân tay / Smartphone</li>
                <li>Mô hình Giám sát nhà yến thông minh</li>
                <li>Mô hình Hệ thống khóa cửa nhận dạng bằng khuôn mặt (Face ID)</li>
                <li>Mô hình Cửa nhà xe thông minh</li>
              </ul>
            </li>
          </ul>
        </div>
      </details>

      <div class="mlab-course-footer">
        <div>
          <div style="font-size: 0.78rem; color: #64748b; font-weight: 600; text-transform: uppercase;">Học phí trọn khóa (Online & Offline)</div>
          <div class="mlab-price-box">
            <span class="mlab-price-current">1.500.000đ</span>
            <span class="mlab-price-old">3.500.000đ</span>
            <span style="font-size: 0.8rem; color: #16a34a; font-weight: 700;">(Tiết kiệm 57%)</span>
          </div>
        </div>
        <div class="mlab-action-group">
          <a href="https://emechatronix.edubit.vn/iot-cho-sinh-vien-ky-thuat" target="_blank" rel="noopener" class="mlab-btn-outline">
            🔗 Xem trên Edubit
          </a>
          <button type="button" class="mlab-btn-enroll" onclick="openMlabEnrollModal()">
            ✍️ Ghi Danh & Thanh Toán QR
          </button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ==================== MODAL GHI DANH & MÃ VIETQR ĐỘNG ==================== -->
<div id="mlabEnrollModal" class="mlab-modal-overlay" onclick="if(event.target===this) closeMlabEnrollModal()">
  <div class="mlab-modal">
    <div class="mlab-modal-header">
      <h3>🎓 Ghi Danh: IoT Cho Sinh Viên Kỹ Thuật</h3>
      <button type="button" class="mlab-modal-close" onclick="closeMlabEnrollModal()" aria-label="Đóng">&times;</button>
    </div>

    <div class="mlab-modal-body">
      <div class="mlab-step-indicator">
        <div id="mlabStepPill1" class="mlab-step-pill active">1. Thông tin học viên</div>
        <div id="mlabStepPill2" class="mlab-step-pill">2. Quét mã QR học phí</div>
        <div id="mlabStepPill3" class="mlab-step-pill">3. Hoàn tất</div>
      </div>

      <!-- BƯỚC 1: ĐIỀN THÔNG TIN -->
      <div id="mlabStep1">
        <form id="mlabInfoForm" onsubmit="proceedToVietQR(event)">
          <div class="mlab-form-group">
            <label for="mlabFullName">Họ và tên học viên <span style="color:#dc2626">*</span></label>
            <input type="text" id="mlabFullName" class="mlab-form-control" placeholder="Ví dụ: Nguyễn Văn A" required>
          </div>

          <div class="mlab-form-row">
            <div class="mlab-form-group">
              <label for="mlabPhone">Số điện thoại / Zalo <span style="color:#dc2626">*</span></label>
              <input type="tel" id="mlabPhone" class="mlab-form-control" placeholder="Ví dụ: 0912345678" pattern="[0-9+ ]{9,13}" required>
            </div>
            <div class="mlab-form-group">
              <label for="mlabEmail">Email nhận tài liệu & kích hoạt <span style="color:#dc2626">*</span></label>
              <input type="email" id="mlabEmail" class="mlab-form-control" placeholder="sinhvien@gmail.com" required>
            </div>
          </div>

          <div class="mlab-form-row">
            <div class="mlab-form-group">
              <label for="mlabOrg">Trường / Đơn vị / Ngành học</label>
              <input type="text" id="mlabOrg" class="mlab-form-control" placeholder="Ví dụ: CTUT - Cơ điện tử K10">
            </div>
            <div class="mlab-form-group">
              <label for="mlabMode">Hình thức đăng ký học <span style="color:#dc2626">*</span></label>
              <select id="mlabMode" class="mlab-form-control" required>
                <option value="Kết hợp Online & Offline (1.500.000đ)">Kết hợp Online & Offline (1.500.000đ)</option>
                <option value="Học Online qua hệ thống (1.500.000đ)">Học Online qua hệ thống (1.500.000đ)</option>
                <option value="Học Offline thực hành tại MLAB (1.500.000đ)">Học Offline thực hành tại MLAB (1.500.000đ)</option>
              </select>
            </div>
          </div>

          <div class="mlab-form-group">
            <label for="mlabNote">Ghi chú thêm cho Giảng viên (Lịch học mong muốn / Đồ án quan tâm)</label>
            <input type="text" id="mlabNote" class="mlab-form-control" placeholder="Ví dụ: Em muốn làm đồ án Nhà thông minh ESP32...">
          </div>

          <button type="submit" class="mlab-btn-primary">
            Tiếp tục: Tạo mã QR Thanh toán Học phí (1.500.000đ) &rarr;
          </button>
        </form>
      </div>

      <!-- BƯỚC 2: HIỂN THỊ MÃ VIETQR ĐỘNG & XÁC NHẬN -->
      <div id="mlabStep2" style="display: none;">
        <div class="mlab-qr-box">
          <div style="font-weight: 700; color: #1e3a8a; font-size: 0.88rem; margin-bottom: 8px;">
            📱 Mở App Ngân hàng bất kỳ để quét mã VietQR tự động
          </div>
          <img id="mlabVietQrImg" src="" alt="Mã VietQR Thanh toán học phí" />
          <div style="font-size: 0.78rem; color: #475569;">
            (Mã QR đã tích hợp sẵn số tiền <strong>1.500.000 VNĐ</strong> và nội dung chuyển khoản tự động)
          </div>

          <div class="mlab-bank-details">
            <div><span>Ngân hàng thụ hưởng:</span> <strong>VietinBank (NH Công Thương VN)</strong></div>
            <div><span>Số tài khoản:</span> <strong style="color:#1d4ed8;">107005679531</strong></div>
            <div><span>Chủ tài khoản:</span> <strong>DUONG KHANH SON</strong></div>
            <div><span>Số tiền học phí:</span> <strong style="color:#dc2626;">1.500.000 VNĐ</strong></div>
            <div><span>Nội dung chuyển khoản:</span> <strong id="mlabOrderCodeDisplay" style="background:#fef3c7; padding: 1px 6px; border-radius: 4px; font-family: monospace;">IOT</strong></div>
          </div>
        </div>

        <div class="mlab-form-group">
          <label for="mlabTxRef">Mã giao dịch ngân hàng hoặc thời gian chuyển khoản (Tùy chọn để đối soát nhanh):</label>
          <input type="text" id="mlabTxRef" class="mlab-form-control" placeholder="Ví dụ: Đã chuyển khoản lúc 18:30 từ VCB...">
        </div>

        <button type="button" id="mlabSubmitBtn" class="mlab-btn-success" onclick="submitEnrollmentNotification()">
          ✅ Tôi đã thanh toán – Gửi thông báo ghi danh cho Thầy Sơn
        </button>
        <button type="button" class="mlab-btn-back" onclick="backToStep1()">
          &larr; Quay lại chỉnh sửa thông tin
        </button>
      </div>

      <!-- BƯỚC 3: THÔNG BÁO THÀNH CÔNG -->
      <div id="mlabStep3" style="display: none;">
        <div class="mlab-success-box">
          <div style="font-size: 3.2rem; margin-bottom: 8px;">🎉</div>
          <h4 style="margin: 0 0 8px 0; color: #15803d; font-size: 1.2rem;">Đăng ký & Báo thanh toán thành công!</h4>
          <p style="color: #334155; font-size: 0.9rem; margin-bottom: 14px;">
            Hệ thống đã gửi thông báo ghi danh của bạn kèm mã đối soát <strong id="mlabSuccessOrderCode" style="color:#1d4ed8;"></strong> đến Email và danh sách quản lý lớp học của <strong>Thầy Đường Khánh Sơn</strong>.
          </p>
          <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 12px; font-size: 0.84rem; color: #166534; text-align: left; margin-bottom: 16px;">
            <strong>📌 Bước tiếp theo:</strong>
            <ul style="margin: 6px 0 0 0; padding-left: 18px;">
              <li>Giảng viên sẽ kiểm tra giao dịch và liên hệ qua Số điện thoại / Zalo hoặc Email của bạn trong vòng 1–2 giờ để cấp quyền truy cập khóa học và xếp lịch thực hành tại MLAB.</li>
              <li>Mọi thắc mắc cần hỗ trợ gấp, vui lòng liên hệ trực tiếp Email: <strong>sonduongkhanh@gmail.com</strong>.</li>
            </ul>
          </div>
          <button type="button" class="mlab-btn-primary" onclick="closeMlabEnrollModal()">
            Đóng cửa sổ
          </button>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
  // Cấu hình thông tin thanh toán VietQR động & Email nhận thông báo
  const MLAB_PAYMENT_CONFIG = {
    bankId: "ICB", // Mã ngân hàng VietinBank chuẩn Napas VietQR
    accountNo: "107005679531",
    accountName: "DUONG KHANH SON",
    amount: 1500000,
    courseName: "IoT CHO SINH VIÊN KỸ THUẬT",
    notifyEmail: "sonduongkhanh@gmail.com",
    // URL Web App của Google Apps Script để tự động ghi vào Google Sheets (nếu đã dán URL)
    googleScriptUrl: ""
  };

  let currentEnrollmentData = {};

  function removeVietnameseTones(str) {
    return str
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/đ/g, "d")
      .replace(/Đ/g, "D")
      .replace(/[^a-zA-Z0-9 ]/g, "")
      .trim()
      .toUpperCase();
  }

  function openMlabEnrollModal() {
    document.getElementById("mlabEnrollModal").classList.add("active");
    backToStep1();
  }

  function closeMlabEnrollModal() {
    document.getElementById("mlabEnrollModal").classList.remove("active");
  }

  function backToStep1() {
    document.getElementById("mlabStep1").style.display = "block";
    document.getElementById("mlabStep2").style.display = "none";
    document.getElementById("mlabStep3").style.display = "none";

    document.getElementById("mlabStepPill1").className = "mlab-step-pill active";
    document.getElementById("mlabStepPill2").className = "mlab-step-pill";
    document.getElementById("mlabStepPill3").className = "mlab-step-pill";
  }

  function proceedToVietQR(event) {
    event.preventDefault();
    const fullName = document.getElementById("mlabFullName").value.trim();
    const phone = document.getElementById("mlabPhone").value.replace(/\s+/g, "");
    const email = document.getElementById("mlabEmail").value.trim();
    const org = document.getElementById("mlabOrg").value.trim();
    const learningMode = document.getElementById("mlabMode").value;
    const note = document.getElementById("mlabNote").value.trim();

    // Tạo mã nội dung chuyển khoản ngắn gọn, không dấu: IOT <SĐT> <TÊN>
    const cleanName = removeVietnameseTones(fullName).split(/\s+/).slice(-2).join(" ");
    const orderCode = ("IOT " + phone + " " + cleanName).substring(0, 45);

    currentEnrollmentData = {
      orderCode: orderCode,
      fullName: fullName,
      phone: phone,
      email: email,
      organization: org || "Không ghi",
      courseName: MLAB_PAYMENT_CONFIG.courseName,
      learningMode: learningMode,
      fee: "1.500.000 VNĐ",
      note: note
    };

    // Tạo URL ảnh VietQR động chuẩn Napas (tự động điền sẵn số tiền 1.500.000đ và nội dung CK)
    const qrUrl = `https://img.vietqr.io/image/${MLAB_PAYMENT_CONFIG.bankId}-${MLAB_PAYMENT_CONFIG.accountNo}-compact2.png?amount=${MLAB_PAYMENT_CONFIG.amount}&addInfo=${encodeURIComponent(orderCode)}&accountName=${encodeURIComponent(MLAB_PAYMENT_CONFIG.accountName)}`;

    document.getElementById("mlabVietQrImg").src = qrUrl;
    document.getElementById("mlabOrderCodeDisplay").textContent = orderCode;

    document.getElementById("mlabStep1").style.display = "none";
    document.getElementById("mlabStep2").style.display = "block";
    document.getElementById("mlabStep3").style.display = "none";

    document.getElementById("mlabStepPill1").className = "mlab-step-pill done";
    document.getElementById("mlabStepPill2").className = "mlab-step-pill active";
    document.getElementById("mlabStepPill3").className = "mlab-step-pill";
  }

  async function submitEnrollmentNotification() {
    const submitBtn = document.getElementById("mlabSubmitBtn");
    const txRef = document.getElementById("mlabTxRef").value.trim();
    const combinedNote = [currentEnrollmentData.note, txRef ? ("GD: " + txRef) : ""].filter(Boolean).join(" | ");

    submitBtn.disabled = true;
    submitBtn.textContent = "⏳ Đang gửi thông tin ghi danh cho Giảng viên...";

    const payload = {
      ...currentEnrollmentData,
      note: combinedNote,
      paymentStatus: "Học viên đã xác nhận quét mã VietQR (1.500.000 VNĐ)"
    };

    try {
      // 1. Nếu đã cấu hình Google Apps Script URL -> Gửi thẳng vào Google Sheets + Gmail Apps Script
      if (MLAB_PAYMENT_CONFIG.googleScriptUrl && MLAB_PAYMENT_CONFIG.googleScriptUrl.startsWith("https://")) {
        await fetch(MLAB_PAYMENT_CONFIG.googleScriptUrl, {
          method: "POST",
          mode: "no-cors",
          headers: { "Content-Type": "text/plain;charset=utf-8" },
          body: JSON.stringify(payload)
        });
      }

      // 2. Đồng thời gửi thông báo trực tiếp tới email sonduongkhanh@gmail.com qua FormSubmit AJAX
      await fetch(`https://formsubmit.co/ajax/${MLAB_PAYMENT_CONFIG.notifyEmail}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify({
          _subject: `[MLAB - Ghi danh IoT] ${payload.fullName} - ${payload.phone}`,
          _template: "table",
          "Khóa học": payload.courseName,
          "Mã đối soát CK (VietQR)": payload.orderCode,
          "Họ và tên học viên": payload.fullName,
          "Số điện thoại / Zalo": payload.phone,
          "Email học viên": payload.email,
          "Trường / Đơn vị": payload.organization,
          "Hình thức học": payload.learningMode,
          "Học phí": payload.fee,
          "Trạng thái": payload.paymentStatus,
          "Ghi chú / Mã giao dịch": payload.note || "Không có"
        })
      });
    } catch (err) {
      console.warn("Notification fallback triggered:", err);
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = "✅ Tôi đã thanh toán – Gửi thông báo ghi danh cho Thầy Sơn";

      document.getElementById("mlabSuccessOrderCode").textContent = payload.orderCode;
      document.getElementById("mlabStep1").style.display = "none";
      document.getElementById("mlabStep2").style.display = "none";
      document.getElementById("mlabStep3").style.display = "block";

      document.getElementById("mlabStepPill1").className = "mlab-step-pill done";
      document.getElementById("mlabStepPill2").className = "mlab-step-pill done";
      document.getElementById("mlabStepPill3").className = "mlab-step-pill active";
    }
  }
</script>
<!-- ==================== KẾT THÚC MODULE ĐĂNG KÝ KHÓA HỌC ==================== -->

<hr style="margin: 2rem 0;">

<h2>Tiếng Việt</h2>
<p>Chào mừng đến với danh mục Hướng dẫn & Phân tích chuyên sâu về lộ trình Kỹ thuật Cơ điện tử 4.0.</p>
<h2>English</h2>
<p>Welcome to the Tutorials section, featuring in‑depth guides and analyses on the Mechatronics 4.0 curriculum.</p>

<div class="entries-list">
  {% for post in site.categories.Tutorials %}
      <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
        <h2 class="archive__item-title" itemprop="headline">
          <a href="{{ post.url | relative_url }}" rel="permalink">{{ post.title }}</a>
        </h2>
        <p class="page__meta">
          <i class="far fa-calendar-alt" aria-hidden="true"></i> {{ post.date | date: "%d/%m/%Y" }}
        </p>
        <p class="archive__item-excerpt" itemprop="description">{{ post.content | strip_html | truncate: 250 }}</p>
      </article>
  {% endfor %}
</div>
