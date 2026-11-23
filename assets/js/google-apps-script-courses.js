/**
 * GOOGLE APPS SCRIPT - HỆ THỐNG GHI DANH KHÓA HỌC NGẮN HẠN (MLAB - THẦY ĐƯỜNG KHÁNH SƠN)
 * --------------------------------------------------------------------------------------
 * Hỗ trợ:
 * - Tự động ghi danh sách học viên vào Google Sheets
 * - Tự động gửi Email thông báo cho Giảng viên (kèm ảnh chụp biên lai chuyển khoản nếu học viên tải ảnh lên)
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
      sheet.getRange(1, 1, 1, 11).setFontWeight("bold").setBackground("#076b33").setFontColor("#ffffff");
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
    const receiptImage = data.receiptImage || "";

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

    // Xử lý ảnh biên lai đính kèm (nếu có)
    let inlineImages = {};
    let receiptHtmlSection = "";
    if (receiptImage && receiptImage.indexOf("base64,") !== -1) {
      try {
        const base64Data = receiptImage.split("base64,")[1];
        const decoded = Utilities.base64Decode(base64Data);
        const blob = Utilities.newBlob(decoded, "image/jpeg", "Bien-Lai-" + orderCode.replace(/\s+/g, "_") + ".jpg");
        inlineImages["receiptImg"] = blob;
        receiptHtmlSection = `
          <div style="margin-top: 16px; padding: 12px; background: #f8faf9; border: 1px solid #d1e7dd; border-radius: 8px; text-align: center;">
            <p style="margin: 0 0 8px 0; font-weight: bold; color: #076b33;">📷 Ảnh chụp biên lai chuyển khoản đính kèm:</p>
            <img src="cid:receiptImg" style="max-width: 360px; width: 100%; border-radius: 8px; border: 1px solid #cbd5e1;" />
          </div>
        `;
      } catch (imgErr) {
        receiptHtmlSection = `<p style="color:#b91c1c;">(Học viên có tải ảnh biên lai nhưng không giải mã được file đính kèm)</p>`;
      }
    }

    // Gửi email thông báo cho giảng viên
    const subject = "[MLAB - Đăng ký khóa học] " + fullName + " - " + phone + " (" + courseName + ")";
    const htmlBody = `
      <div style="font-family: Arial, sans-serif; max-width: 600px; border: 1px solid #d1e7dd; border-radius: 10px; overflow: hidden;">
        <div style="background: #076b33; color: #ffffff; padding: 16px 20px;">
          <h2 style="margin: 0; font-size: 18px;">🎓 Thông báo Học viên Đăng ký Khóa học Mới</h2>
        </div>
        <div style="padding: 20px; color: #1f2937; line-height: 1.6;">
          <p>Xin chào Thầy <strong>Đường Khánh Sơn</strong>,</p>
          <p>Hệ thống trên trang <strong>duongkhanhson.github.io/tutorials/</strong> vừa ghi nhận một học viên đăng ký và xác thực thanh toán học phí:</p>
          <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold; width: 40%;">Thời gian:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${timestamp}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Khóa học:</td><td style="padding: 8px; border-bottom: 1px solid #eee; color: #076b33; font-weight: bold;">${courseName}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Hình thức đăng ký:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${learningMode}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Họ và tên:</td><td style="padding: 8px; border-bottom: 1px solid #eee;"><strong>${fullName}</strong></td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Số điện thoại / Zalo:</td><td style="padding: 8px; border-bottom: 1px solid #eee;"><strong>${phone}</strong></td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Email học viên:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${email}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Trường / Đơn vị:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${org}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Học phí:</td><td style="padding: 8px; border-bottom: 1px solid #eee; color: #9d0c4c; font-weight: bold;">${fee}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Nội dung CK (Mã QR):</td><td style="padding: 8px; border-bottom: 1px solid #eee; font-family: monospace; background: #fef3c7;">${orderCode}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Xác thực & Ghi chú:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${note || "Không có"}</td></tr>
          </table>
          ${receiptHtmlSection}
          <p style="font-size: 13px; color: #6b7280; margin-top: 14px;">Dữ liệu cũng đã được lưu tự động vào Google Sheets của Thầy.</p>
        </div>
      </div>
    `;

    const mailOptions = {
      to: NOTIFY_EMAIL,
      subject: subject,
      htmlBody: htmlBody,
      replyTo: email || NOTIFY_EMAIL
    };
    if (Object.keys(inlineImages).length > 0) {
      mailOptions.inlineImages = inlineImages;
    }

    MailApp.sendEmail(mailOptions);

    return ContentService
      .createTextOutput(JSON.stringify({ status: "success", message: "Recorded and emailed" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: "error", message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
