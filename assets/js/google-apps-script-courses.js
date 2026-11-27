/**
 * GOOGLE APPS SCRIPT - HỆ THỐNG GHI DANH KHÓA HỌC NGẮN HẠN (MLAB - THẦY ĐƯỜNG KHÁNH SƠN)
 * --------------------------------------------------------------------------------------
 * TÍNH NĂNG ĐẦY ĐỦ:
 * 1. Tự động lưu ảnh chụp biên lai chuyển khoản của học viên vào thư mục "Bien_Lai_Hoc_Vien_MLAB" trong Google Drive.
 * 2. Tự động điền thông tin học viên + tạo Link bấm xem ảnh biên lai ngay ở cột 12 trong Google Sheets.
 * 3. Tự động gửi Email thông báo cho Giảng viên (hiển thị ảnh trực tiếp trong Email + đính kèm file ảnh gốc + link mở trên Drive).
 */

const NOTIFY_EMAIL = "sonduongkhanh@gmail.com";
const DRIVE_FOLDER_NAME = "Bien_Lai_Hoc_Vien_MLAB";

function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Tạo dòng tiêu đề 12 cột nếu trang tính đang trống
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
        "Lịch trống & Ghi chú",
        "Link Ảnh Biên Lai (Google Drive)"
      ]);
      sheet.getRange(1, 1, 1, 12).setFontWeight("bold").setBackground("#076b33").setFontColor("#ffffff");
    } else if (sheet.getRange(1, 12).getValue() === "") {
      // Nếu bảng cũ mới có 11 cột, tự động thêm tiêu đề cột 12 "Link Ảnh Biên Lai (Google Drive)"
      sheet.getRange(1, 12)
        .setValue("Link Ảnh Biên Lai (Google Drive)")
        .setFontWeight("bold")
        .setBackground("#076b33")
        .setFontColor("#ffffff");
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
    const courseName = data.courseName || "";
    const learningMode = data.learningMode || "";
    const fee = data.fee || "";
    const paymentStatus = data.paymentStatus || "";
    const note = data.note || "";
    const receiptImage = data.receiptImage || "";

    // Xử lý ảnh biên lai: Lưu vào Google Drive + Tạo link trong Google Sheets + Đính kèm Email
    let inlineImages = {};
    let attachments = [];
    let receiptHtmlSection = "";
    let driveFileUrl = "";

    if (receiptImage && receiptImage.indexOf("base64,") !== -1) {
      try {
        const base64Data = receiptImage.split("base64,")[1];
        const decoded = Utilities.base64Decode(base64Data);
        const timeTag = Utilities.formatDate(new Date(), "GMT+7", "yyyyMMdd_HHmmss");
        const safeFileName = "Bien_Lai_" + orderCode.replace(/[^a-zA-Z0-9]/g, "_") + "_" + timeTag + ".jpg";
        const blob = Utilities.newBlob(decoded, "image/jpeg", safeFileName);

        // 1. Đính kèm vào Email
        inlineImages["receiptImg"] = blob;
        attachments.push(blob);

        // 2. Lưu vào thư mục Google Drive "Bien_Lai_Hoc_Vien_MLAB"
        try {
          const folders = DriveApp.getFoldersByName(DRIVE_FOLDER_NAME);
          const folder = folders.hasNext() ? folders.next() : DriveApp.createFolder(DRIVE_FOLDER_NAME);
          const file = folder.createFile(blob);
          file.setDescription("Biên lai học phí của: " + fullName + " (" + phone + ") - Khóa: " + courseName);
          driveFileUrl = file.getUrl();
        } catch (driveErr) {
          driveFileUrl = "Lỗi quyền Drive: " + driveErr.toString();
        }

        receiptHtmlSection = `
          <div style="margin-top: 16px; padding: 14px; background: #f2fbf6; border: 1.5px solid #0b8a42; border-radius: 10px; text-align: center;">
            <p style="margin: 0 0 10px 0; font-weight: bold; color: #076b33; font-size: 14px;">📷 Ảnh chụp biên lai chuyển khoản của học viên:</p>
            <img src="cid:receiptImg" style="max-width: 420px; width: 100%; border-radius: 8px; border: 1px solid #cbd5e1;" />
            ${driveFileUrl.indexOf("http") === 0 ? `<p style="margin: 10px 0 0 0; font-size: 13px;"><a href="${driveFileUrl}" target="_blank" style="display:inline-block; background:#0b8a42; color:#ffffff; text-decoration:none; padding:8px 14px; border-radius:6px; font-weight:bold;">🔗 Xem ảnh biên lai trên Google Drive</a></p>` : ""}
          </div>
        `;
      } catch (imgErr) {
        receiptHtmlSection = `<p style="color:#b91c1c;">Lỗi giải mã ảnh: ${imgErr.toString()}</p>`;
      }
    }

    // Ghi dòng dữ liệu mới vào Google Sheets
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
      note,
      driveFileUrl || "Không đính kèm ảnh (Xác thực bằng mã GD)"
    ]);

    // Nếu có link Google Drive hợp lệ, chuyển ô cột 12 thành nút bấm Hyperlink rõ ràng trong Google Sheets
    const lastRow = sheet.getLastRow();
    if (driveFileUrl && driveFileUrl.indexOf("http") === 0) {
      const linkCell = sheet.getRange(lastRow, 12);
      const richText = SpreadsheetApp.newRichTextValue()
        .setText("🖼️ Xem Ảnh Biên Lai (" + fullName + ")")
        .setLinkUrl(driveFileUrl)
        .build();
      linkCell.setRichTextValue(richText).setFontColor("#0b8a42").setFontWeight("bold");
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
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Lịch trống & Xác thực:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${note || "Không có"}</td></tr>
            <tr><td style="padding: 8px; border-bottom: 1px solid #eee; font-weight: bold;">Link Google Drive:</td><td style="padding: 8px; border-bottom: 1px solid #eee;">${driveFileUrl.indexOf("http") === 0 ? `<a href="${driveFileUrl}" target="_blank" style="color:#0b8a42;font-weight:bold;">Mở ảnh biên lai trên Drive</a>` : "Không có ảnh"}</td></tr>
          </table>
          ${receiptHtmlSection}
          <p style="font-size: 13px; color: #6b7280; margin-top: 14px;">Dữ liệu và link ảnh biên lai cũng đã được lưu tự động vào Google Sheets của Thầy.</p>
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
      mailOptions.attachments = attachments;
    }

    MailApp.sendEmail(mailOptions);

    return ContentService
      .createTextOutput(JSON.stringify({ status: "success", driveUrl: driveFileUrl }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: "error", message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * HÀM CẤP QUYỀN NHANH (Chạy thử 1 lần trong Apps Script để cấp quyền Google Drive + Sheets + Mail)
 */
function authorizePermissions() {
  const folders = DriveApp.getFoldersByName(DRIVE_FOLDER_NAME);
  const folder = folders.hasNext() ? folders.next() : DriveApp.createFolder(DRIVE_FOLDER_NAME);
  Logger.log("Đã sẵn sàng thư mục lưu biên lai trên Google Drive: " + folder.getUrl());
}
