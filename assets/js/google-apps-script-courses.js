/**
 * GOOGLE APPS SCRIPT - HỆ THỐNG GHI DANH KHÓA HỌC NGẮN HẠN (MLAB - THẦY ĐƯỜNG KHÁNH SƠN)
 * --------------------------------------------------------------------------------------
 * HƯỚNG DẪN CÀI ĐẶT TRONG 1 PHÚT:
 * 1. Mở Google Sheets mới tại: https://sheets.new (đăng nhập bằng sonduongkhanh@gmail.com)
 * 2. Đặt tên file tùy ý (ví dụ: "Danh sách Học viên Đăng ký Khóa học MLAB").
 * 3. Trên thanh menu, chọn: Tiện ích mở rộng (Extensions) -> Apps Script.
 * 4. Xóa toàn bộ mã mặc định trong khung soạn thảo và DÁN toàn bộ mã này vào.
 * 5. Nhấn biểu tượng Đĩa mềm (Lưu) -> Nhấn nút "Triển khai" (Deploy) ở góc phải trên cùng -> Chọn "Triển khai mới" (New deployment).
 * 6. Ở mục "Chọn loại" (bánh răng), chọn "Ứng dụng web" (Web app):
 *    - Thực thi dưới dạng (Execute as): Tôi (sonduongkhanh@gmail.com)
 *    - Ai có quyền truy cập (Who has access): Bất kỳ ai (Anyone)  <-- QUAN TRỌNG!
 * 7. Nhấn "Triển khai" (Deploy), cấp quyền (Authorize access -> Advanced -> Go to project), rồi copy đường link "URL ứng dụng web" (Web app URL) dán vào biến GOOGLE_SCRIPT_URL trong _pages/tutorials.md (hoặc gửi cho AI cập nhật).
 */

const NOTIFY_EMAIL = "sonduongkhanh@gmail.com";

function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Tạo dòng tiêu đề nếu trang tính đang trống
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        "Thời gian đăng ký",
        "Mã đơn / Nội dung CK",
        "Họ và tên",
        "Số điện thoại / Zalo",
        "Email học viên",
        "Trường / Đơn vị",
        "Khóa học",
        "Hình thức học",
        "Học phí (VNĐ)",
        "Trạng thái báo CK",
        "Ghi chú / Mã GD"
      ]);
      sheet.getRange(1, 1, 1, 11).setFontWeight("bold").setBackground("#1e3a8a").setFontColor("#ffffff");
    }

    let data = {};
    if (e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (err) {
        data = e.parameter || {};
      }
    } else {
      data = e.parameter || {};
    }

    const timestamp = Utilities.formatDate(new Date(), "GMT+7", "dd/MM/yyyy HH:mm:ss");
    const orderCode = data.orderCode || "";
    const fullName = data.fullName || "";
    const phone = data.phone || "";
    const email = data.email || "";
    const org = data.organization || "";
    const courseName = data.courseName || "IoT CHO SINH VIÊN KỸ THUẬT";
    const learningMode = data.learningMode || "Online / Offline";
    const fee = data.fee || "1.500.000 VNĐ";
    const paymentStatus = data.paymentStatus || "Học viên xác nhận đã chuyển khoản QR";
    const note = data.note || "";

    // Ghi vào dòng mới trong Google Sheets
    sheet.appendRow([
      timestamp,
      orderCode,
      fullName,
      "'" + phone,
      email,
      org,
      courseName,
      learningMode,
      fee,
      paymentStatus,
      note
    ]);

    // Gửi email thông báo cho giảng viên
    const subject = "[MLAB - Đăng ký khóa học] " + fullName + " - " + phone + " (" + courseName + ")";
    const htmlBody = `
      <div style="font-family: Arial, sans-serif; max-width: 600px; border: 1px solid #e5e7eb; border-radius: 10px; overflow: hidden;">
        <div style="background: #1e3a8a; color: #ffffff; padding: 16px 20px;">
          <h2 style="margin: 0; font-size: 18px;">🎓 Thông báo Học viên Đăng ký Khóa học Mới</h2>
        </div>
        <div style="padding: 20px; color: #1f2937; line-height: 1.6;">
          <p>Xin chào Thầy <strong>Đường Khánh Sơn</strong>,</p>
          <p>Hệ thống trên trang <strong>duongkhanhson.github.io/tutorials/</strong> vừa ghi nhận một học viên đăng ký và xác nhận thanh toán học phí:</p>
          <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold; width: 40%;">Thời gian:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${timestamp}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Khóa học:</td><td style="padding: 8px; border-bottom: 1px solid #eee; color: #1d4ed8; font-weight: bold;">${courseName}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Hình thức đăng ký:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${learningMode}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Họ và tên:</td><td style="padding: 8px; border-bottom: 1px solid #eee;"><strong>${fullName}</strong></td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Số điện thoại / Zalo:</td><td style="padding: 8px; border-bottom: 1px solid #eee;"><strong>${phone}</strong></td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Email học viên:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${email}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Trường / Đơn vị:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${org}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Học phí:</td><td style="padding: 8px; border-bottom: 1px solid #eee; color: #b91c1c; font-weight: bold;">${fee}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Nội dung CK (Mã QR):</td><td style="padding: 8px; border-bottom: 1px solid #eee; font-family: monospace; background: #fef3c7;">${orderCode}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Ghi chú / Mã GD:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${note || "Không có"}</td></tr>
          </table>
          <p style="font-size: 13px; color: #6b7280;">Dữ liệu cũng đã được lưu tự động vào Google Sheets của Thầy.</p>
        </div>
      </div>
    `;

    MailApp.sendEmail({
      to: NOTIFY_EMAIL,
      subject: subject,
      htmlBody: htmlBody,
      replyTo: email || NOTIFY_EMAIL
    });

    return ContentService
      .createTextOutput(JSON.stringify({ status: "success", message: "Recorded and emailed" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: "error", message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
