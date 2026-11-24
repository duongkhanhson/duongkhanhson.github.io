---
title: "Hướng Dẫn & Knowledge (Tutorials) "
permalink: /tutorials/
layout: single
author_profile: true
---

<style>
  /* Course Section Styling - CNS Scientific Palette (Primary Green #0b8a42, Steel Blue #3b6ca8, Ochre Orange #d47a17, Crimson #9d0c4c, Teal #179083) */
  .mlab-course-section {
    margin-bottom: 2.5rem;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }
  .mlab-section-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, #076b33, #0b8a42);
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
    border: 1px solid #d1e7dd;
    border-radius: 16px;
    box-shadow: 0 10px 25px -5px rgba(11, 138, 66, 0.1), 0 4px 10px -2px rgba(11, 138, 66, 0.05);
    overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    margin-bottom: 28px;
  }
  .mlab-gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(195px, 1fr));
    gap: 12px;
    margin-top: 10px;
  }
  .mlab-gallery-item {
    background: #ffffff;
    border: 1px solid #d1e7dd;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    display: flex;
    flex-direction: column;
  }
  .mlab-gallery-item img {
    width: 100%;
    height: 135px;
    object-fit: cover;
    display: block;
    border-bottom: 1px solid #eef8f2;
  }
  .mlab-gallery-caption {
    padding: 8px 10px;
    font-size: 0.78rem;
    font-weight: 600;
    color: #063d1e;
    text-align: center;
    background: #f8faf9;
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .mlab-tier-selector {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 12px;
    margin: 14px 0 20px 0;
  }
  .mlab-tier-btn {
    background: #f8faf9;
    border: 2px solid #cbd5e1;
    border-radius: 12px;
    padding: 14px 16px;
    text-align: left;
    cursor: pointer;
    transition: all 0.2s ease;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .mlab-tier-btn:hover {
    border-color: #0b8a42;
    background: #f2fbf6;
    transform: translateY(-2px);
  }
  .mlab-tier-btn.active {
    background: #eef8f2;
    border-color: #0b8a42;
    box-shadow: 0 6px 16px rgba(11, 138, 66, 0.16);
  }
  .mlab-tier-badge {
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 800;
    text-transform: uppercase;
    padding: 3px 9px;
    border-radius: 99px;
    margin-bottom: 8px;
    width: fit-content;
    color: #ffffff;
  }
  .mlab-tier-title {
    font-size: 0.93rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 5px;
    line-height: 1.35;
  }
  .mlab-tier-desc {
    font-size: 0.79rem;
    color: #475569;
    margin-bottom: 10px;
    line-height: 1.4;
  }
  .mlab-tier-price {
    font-size: 1.2rem;
    font-weight: 800;
    color: #0b8a42;
  }
  .mlab-proof-box {
    background: #fffbeb;
    border: 1.5px solid #f59e0b;
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 14px;
  }
  .mlab-upload-area {
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 6px;
  }
  .mlab-upload-label {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #ffffff;
    border: 1.5px dashed #0b8a42;
    color: #076b33;
    font-weight: 700;
    font-size: 0.83rem;
    padding: 8px 14px;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.2s;
  }
  .mlab-upload-label:hover {
    background: #eef8f2;
  }
  .mlab-receipt-preview {
    display: none;
    margin-top: 10px;
    align-items: center;
    gap: 10px;
    background: #ffffff;
    padding: 8px 10px;
    border-radius: 8px;
    border: 1px solid #d1e7dd;
  }
  .mlab-receipt-preview img {
    width: 54px;
    height: 54px;
    object-fit: cover;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
  }
  .mlab-course-header {
    background: linear-gradient(135deg, #063d1e 0%, #076b33 55%, #0b8a42 100%);
    color: #ffffff;
    padding: 24px 26px;
    position: relative;
  }
  .mlab-course-tag-row {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    margin-bottom: 10px;
  }
  .mlab-badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 5px 11px;
    border-radius: 6px;
    font-size: 0.76rem;
    font-weight: 700;
  }
  .mlab-badge-mode {
    background: #3b6ca8;
    color: #ffffff;
    border: 1px solid rgba(255, 255, 255, 0.25);
  }
  .mlab-badge-discount {
    background: #9d0c4c;
    color: #ffffff;
    border: 1px solid rgba(255, 255, 255, 0.25);
  }
  .mlab-badge-cert {
    background: #179083;
    color: #ffffff;
    border: 1px solid rgba(255, 255, 255, 0.25);
  }
  .mlab-btn-enroll-top {
    background: linear-gradient(135deg, #d47a17, #c25e00);
    color: #ffffff !important;
    font-weight: 700;
    font-size: 0.78rem;
    padding: 6px 14px;
    border: 1px solid rgba(255, 255, 255, 0.35);
    border-radius: 7px;
    cursor: pointer;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.22);
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .mlab-btn-enroll-top:hover {
    transform: translateY(-1px);
    background: linear-gradient(135deg, #e0851d, #d47a17);
    box-shadow: 0 5px 14px rgba(0, 0, 0, 0.3);
  }
  .mlab-course-title {
    margin: 6px 0 8px 0 !important;
    font-size: 1.55rem !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    line-height: 1.3 !important;
  }
  .mlab-course-subtitle {
    margin: 0;
    font-size: 0.95rem;
    color: #e2f5ea;
    font-weight: 500;
  }
  .mlab-course-meta-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    margin-top: 16px;
    padding-top: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.18);
    font-size: 0.83rem;
    color: #f0fdf4;
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
    background: #f2fbf6;
    border-left: 4px solid #0b8a42;
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
    background: #f8faf9;
    border: 1px solid #d1e7dd;
    border-radius: 12px;
    padding: 16px;
  }
  .mlab-info-box h4 {
    margin: 0 0 10px 0 !important;
    font-size: 0.98rem !important;
    color: #076b33 !important;
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
    border: 1px solid #bcd9c8;
    border-radius: 10px;
    margin-bottom: 22px;
    overflow: hidden;
  }
  .mlab-curriculum-details summary {
    padding: 14px 18px;
    background: #eef8f2;
    font-weight: 700;
    color: #063d1e;
    cursor: pointer;
    user-select: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.92rem;
  }
  .mlab-curriculum-details summary:hover {
    background: #dff2e7;
  }
  .mlab-curriculum-content {
    padding: 16px 20px;
    font-size: 0.86rem;
    max-height: 360px;
    overflow-y: auto;
    border-top: 1px solid #d1e7dd;
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
    color: #0b8a42;
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
    background: linear-gradient(135deg, #d47a17, #c25e00);
    color: #ffffff !important;
    font-weight: 700;
    font-size: 0.95rem;
    padding: 12px 24px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    box-shadow: 0 4px 14px rgba(212, 122, 23, 0.35);
    transition: all 0.2s ease;
    text-decoration: none !important;
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }
  .mlab-btn-enroll:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(212, 122, 23, 0.45);
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
    background: linear-gradient(135deg, #063d1e, #0b8a42);
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
    background: #e2f5ea;
    color: #076b33;
    border: 1px solid #75c696;
  }
  .mlab-step-pill.done {
    background: #dcfce7;
    color: #0b8a42;
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
    background: linear-gradient(135deg, #0b8a42, #076b33);
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
    background: linear-gradient(135deg, #0b8a42, #065f2c);
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

  <!-- ==================== KHÓA HỌC 1 (ĐẦU TRANG): THIẾT KẾ CƠ KHÍ BẰNG AUTODESK INVENTOR ==================== -->
  <div class="mlab-course-card">
    <div class="mlab-course-header">
      <div class="mlab-course-tag-row">
        <span class="mlab-badge mlab-badge-mode">🌐 Học Online & Offline tại MLAB</span>
        <span class="mlab-badge mlab-badge-discount">🔥 Học 1 Khóa – Hỗ Trợ Trọn Đời</span>
      </div>
      <div class="mlab-course-tag-row">
        <span class="mlab-badge mlab-badge-cert">🎓 Lịch học linh hoạt theo học viên</span>
        <button type="button" class="mlab-btn-enroll-top" onclick="openMlabEnrollModal(selectedInventorTierKey)">
          ✍️ Ghi Danh & Thanh Toán QR
        </button>
      </div>
      <h2 class="mlab-course-title">THIẾT KẾ CƠ KHÍ & MÔ PHỎNG 3D BẰNG AUTODESK INVENTOR</h2>
      <p class="mlab-course-subtitle">⚙️ Đào tạo từ Khóa Cơ Bản &rarr; Khóa Nâng Cao CAM, CNC &rarr; Khóa Chuyên Sâu Khuôn Mẫu & Sản Phẩm Nhựa</p>
      <div class="mlab-course-meta-bar">
        <span>👨‍🏫 <strong>Giảng viên:</strong> ThS. Đường Khánh Sơn (MLAB)</span>
        <span>📞 <strong>Hotline / Zalo:</strong> 0946.469.720</span>
        <span>🛠️ <strong>Hình thức:</strong> Vừa học vừa thực hành 100% trên máy</span>
        <span>♾️ <strong>Quyền lợi:</strong> Hỗ trợ cài đặt & đồng hành trọn đời</span>
      </div>
    </div>

    <div class="mlab-course-body">
      <div class="mlab-course-intro">
        <strong>Bạn đang gặp phải những trăn trở này?</strong>
        <ul style="margin: 8px 0 12px 0; padding-left: 20px; color: #334155;">
          <li>👨‍🎓 Sắp tốt nghiệp đại học nhưng vẫn <strong>chưa thành thạo phần mềm thiết kế 3D</strong>, chưa đọc hiểu bản vẽ kỹ thuật hay tự thiết kế được sản phẩm hoàn chỉnh?</li>
          <li>📌 Sắp báo cáo đồ án chuyên ngành, đồ án thiết kế máy, luận văn tốt nghiệp nhưng vẫn chưa dựng và mô phỏng được mô hình cơ khí trên máy tính?</li>
          <li>💼 Kỹ năng vẽ và thiết kế 3D còn yếu khiến hiệu suất công việc chưa cao, mất nhiều cơ hội thăng tiến?</li>
          <li>✏️ Muốn học <strong>VẼ & THIẾT KẾ CƠ KHÍ 3D</strong> bài bản nhưng không biết bắt đầu từ đâu và học như thế nào cho hiệu quả?</li>
        </ul>
        👉 <strong>Các khóa học Thiết kế Cơ khí trên phần mềm Autodesk Inventor tại MLAB</strong> sẽ giúp bạn giải quyết triệt để tất cả các vấn đề đó với bài giảng chi tiết, trực quan, dễ hiểu – vừa học vừa thực hành trực tiếp trên máy tính, nâng cao kỹ năng ngay sau từng buổi học!
      </div>

      <div class="mlab-project-tags">
        <strong>💡 Điểm khác biệt của khóa học Inventor tại MLAB:</strong><br>
        Nhận học viên mỗi ngày – Lịch học sắp xếp linh hoạt theo thời gian của học viên (Sáng / Chiều / Tối, Online hoặc Offline). Lộ trình đào tạo toàn diện từ <em>Thiết kế chi tiết 3D, Lắp ráp cơ cấu máy, Kim loại tấm, Khung dầm, Đường ống & Dây dẫn, Thiết kế khuôn nhựa, Phân tích sức bền hữu hạn (FEA/Nastran), Gia công CNC (HSM Inventor) đến xuất mô hình sang MATLAB/Simscape để mô phỏng động lực học và thiết kế bộ điều khiển Robot!</em>
      </div>

      <div class="mlab-grid-2">
        <div class="mlab-info-box">
          <h4>🎯 Sau khóa học bạn sẽ làm chủ 13 kỹ năng:</h4>
          <ul>
            <li>Đọc hiểu và phân tích thành thạo bản vẽ kỹ thuật 2D/3D.</li>
            <li>Xây dựng chi tiết (Part Modeling) và mô hình 3D phức tạp.</li>
            <li>Mô phỏng lắp ráp (Assembly) các chi tiết thành cơ cấu, máy hoàn chỉnh.</li>
            <li>Khai thác thư viện chi tiết máy tiêu chuẩn đồ sộ (Content Center & Design Accelerator: bánh răng, trục, ổ lăn, đai, xích...).</li>
            <li>Mô phỏng động học và động lực học cơ cấu – máy (Dynamic Simulation).</li>
            <li>Phân tích sức bền (Stress Analysis / Nastran CAE), tối ưu hóa kết cấu sản phẩm.</li>
            <li>Thành thạo tính toán, thiết kế và trải phẳng chi tiết kim loại tấm (Sheet Metal).</li>
          </ul>
        </div>
        <div class="mlab-info-box">
          <h4>🚀 Kỹ năng Chuyên sâu & Tích hợp Cơ điện tử:</h4>
          <ul>
            <li>Thành thạo thiết kế hệ thống đường ống và dây dẫn điện (Tube & Pipe, Cable & Harness).</li>
            <li>Thành thạo thiết kế sản phẩm nhựa và tách khuôn ép nhựa (Mold Design).</li>
            <li>Render hình ảnh thực tế (Inventor Studio) và tạo video trình diễn nguyên lý hoạt động của máy móc, dây chuyền sản xuất.</li>
            <li><strong>Đặc biệt:</strong> Xuất mô hình 3D liên kết trực tiếp với <strong>MATLAB / Simulink (Simscape Multibody)</strong> để mô phỏng và thiết kế bộ điều khiển tự động, Robot.</li>
            <li>Liên kết đa nền tảng CAD/CAM/CAE, lập trình gia công CNC với <strong>Inventor HSM / CAM</strong>.</li>
            <li>Xuất file chuẩn in 3D (.STL/.OBJ), tạo mẫu nhanh và gia công thực tế trên máy CNC.</li>
          </ul>
        </div>
      </div>

      <details class="mlab-curriculum-details" open>
        <summary>
          <span>🖼️ Thư viện Mô hình 3D, Mô phỏng CAE/Simscape & Sản phẩm thực tế của Khóa học Inventor</span>
          <span style="color: #0b8a42; font-size: 0.82rem;">Nhấn để thu gọn / mở rộng ▼</span>
        </summary>
        <div class="mlab-curriculum-content" style="max-height: none;">
          <div class="mlab-gallery-grid">
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/he-thong-dong-nap-chai-ctut.png" alt="Mô hình 3D hệ thống đóng nắp chai tự động CTUT">
              <div class="mlab-gallery-caption">Thiết kế 3D Hệ thống băng tải & đóng nắp chai tự động hoàn chỉnh</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/he-thong-dong-nap-chai-3d.jpg" alt="Bản vẽ lắp ráp chi tiết máy đóng nắp chai">
              <div class="mlab-gallery-caption">Bố trí cụm cơ cấu máy & đánh số bản vẽ lắp ráp kỹ thuật</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/scara-parallel-system-3d.png" alt="Mô hình 3D hệ thống SCARA Parallel Robot MLAB">
              <div class="mlab-gallery-caption">Thiết kế 3D hệ thống Robot SCARA song song kết hợp băng tải MLAB</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/scara-phan-loai-mau-sac.png" alt="Thực nghiệm Robot SCARA phân loại sản phẩm theo màu sắc">
              <div class="mlab-gallery-caption">Sản phẩm thực tế: Robot SCARA phân loại màu sắc qua xử lý ảnh</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/scara-phan-loai-hinh-dang.jpg" alt="Thực nghiệm Robot SCARA phân loại hình dạng sản phẩm">
              <div class="mlab-gallery-caption">Sản phẩm thực tế: Robot SCARA nhận diện & phân loại hình dạng</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/xe-may-tu-can-bang-3d.jpg" alt="Thiết kế 3D các cụm chi tiết xe máy tự cân bằng bằng bánh đà">
              <div class="mlab-gallery-caption">Thiết kế 3D cụm bánh đà phản ứng & hệ truyền động xe tự cân bằng</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/xe-may-tu-can-bang-thuc-te.jpg" alt="Sản phẩm thực tế mô hình xe máy tự cân bằng MLAB in 3D và gia công CNC">
              <div class="mlab-gallery-caption">Sản phẩm thực tế: Mô hình Xe máy tự cân bằng MLAB (In 3D & CNC)</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/xe-may-tu-can-bang-leo-doc.jpg" alt="Thử nghiệm xe máy tự cân bằng trên mặt phẳng nghiêng">
              <div class="mlab-gallery-caption">Thực nghiệm kiểm chứng khả năng tự cân bằng trên mặt dốc nghiêng</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/dog-robot-simscape.png" alt="Xuất mô hình Robot 4 chân từ Inventor sang MATLAB Simscape Multibody">
              <div class="mlab-gallery-caption">Liên kết mô hình 3D Inventor sang MATLAB Simscape Multibody</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/dog-robot-gui-ik.png" alt="Giao diện điều khiển động học thuận nghịch Dog Robot trên MATLAB">
              <div class="mlab-gallery-caption">Mô phỏng Động học thuận/nghịch & Điều khiển Robot 4 chân (Dog Robot)</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/inventor-gearbox.jpg" alt="Thiết kế hộp giảm tốc và chi tiết máy">
              <div class="mlab-gallery-caption">Thiết kế Hộp giảm tốc & Thư viện chi tiết máy tiêu chuẩn</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/inventor-mold.jpg" alt="Thiết kế sản phẩm nhựa và làm khuôn">
              <div class="mlab-gallery-caption">Thiết kế sản phẩm nhựa & Tách khuôn ép nhựa (Mold Design)</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/inventor-cae.jpg" alt="Phân tích sức bền và mô phỏng CAE">
              <div class="mlab-gallery-caption">Phân tích ứng suất, biến dạng, tần số & nhiệt (CAE / Nastran)</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/inventor-conveyor.jpg" alt="Thiết kế hệ thống băng tải tự động">
              <div class="mlab-gallery-caption">Thiết kế máy & Hệ thống băng tải tự động hóa công nghiệp</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/inventor-robot-scara.jpg" alt="Thiết kế Robot song song liên kết MATLAB">
              <div class="mlab-gallery-caption">Thiết kế cơ khí Robot song song 2 bậc tự do trên Inventor</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/inventor-robot-omni.jpg" alt="Thiết kế Robot di động đa hướng Omni">
              <div class="mlab-gallery-caption">Thiết kế mô hình Mobile Robot đa hướng phục vụ Đồ án & NCKH</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/inventor-car-render.jpg" alt="Thiết kế Surface nâng cao và Render Inventor Studio">
              <div class="mlab-gallery-caption">Thiết kế bề mặt phức tạp (Surfacing) & Render Inventor Studio</div>
            </div>
            <div class="mlab-gallery-item">
              <img src="{{ site.baseurl }}/assets/images/inventor/inventor-overview.jpg" alt="Hệ sinh thái thiết kế Autodesk Inventor">
              <div class="mlab-gallery-caption">Hệ sinh thái Thiết kế CAD/CAM/CAE toàn diện trên Autodesk Inventor</div>
            </div>
          </div>
        </div>
      </details>

      <details class="mlab-curriculum-details" open>
        <summary>
          <span>📋 Xem chi tiết Nội dung 3 Khóa học Đào tạo (Khóa Cơ Bản &rarr; Khóa Nâng Cao CAM, CNC &rarr; Khóa Chuyên Sâu Khuôn Mẫu)</span>
          <span style="color: #0b8a42; font-size: 0.82rem;">Nhấn để thu gọn / mở rộng ▼</span>
        </summary>
        <div class="mlab-curriculum-content" style="max-height: none;">
          <ol style="margin-bottom: 0; padding-left: 20px;">
            <li style="margin-bottom: 12px;">
              <strong style="color: #0b8a42;">Khóa 1 – Khóa Cơ Bản: Thiết Kế & Lắp Ráp 3D Inventor (Học phí: 1.500.000đ):</strong>
              <ul style="margin-top: 4px; padding-left: 18px;">
                <li>Làm chủ giao diện Autodesk Inventor, phương pháp đọc hiểu bản vẽ kỹ thuật 2D/3D và tư duy dựng hình tham số (Parametric Modeling).</li>
                <li>Thiết lập ràng buộc hình học (Geometric Constraints) và kích thước chuẩn trong phác thảo 2D Sketch.</li>
                <li><strong>Thành thạo dựng hình, vẽ chi tiết 3D, mô tả sản phẩm từ ý tưởng đến bản vẽ lắp:</strong> Thực hành đầy đủ các lệnh dựng khối 3D chi tiết máy (Extrude, Revolve, Sweep, Loft, Coil, Rib, Shell, Hole, Fillet, Chamfer, Pattern, Mirror...).</li>
                <li>Lắp ráp các chi tiết thành cụm cơ cấu và máy hoàn chỉnh (Assembly Constraints & Joints), kiểm tra va chạm (Interference).</li>
                <li><strong>Xuất video mô phỏng lắp ráp, hoạt động của cụm chi tiết, máy móc, robot...</strong> bằng môi trường Presentation & Inventor Studio trực quan.</li>
                <li><strong>Xuất bản vẽ 2D cho gia công, chế tạo (Laser, CNC...):</strong> Trình bày bản vẽ kỹ thuật tiêu chuẩn TCVN/ISO (Drawing: hình chiếu, mặt cắt, hình trích, dung sai, độ nhám, bảng kê vật tư BOM tự động) và xuất file DXF/DWG/PDF đưa vào xưởng sản xuất.</li>
              </ul>
            </li>
            <li style="margin-bottom: 12px;">
              <strong style="color: #3b6ca8;">Khóa 2 – Khóa Nâng Cao: Gia Công CAM, CNC & Mô Phỏng Kỹ Thuật (Học phí: 2.500.000đ):</strong>
              <ul style="margin-top: 4px; padding-left: 18px;">
                <li><strong>Thiết kế các cơ cấu máy, tính toán và thiết kế các bộ truyền động đai, xích, bánh răng...</strong> tự động theo tiêu chuẩn kỹ thuật với Design Accelerator (Trục, ổ lăn, bánh răng trụ/côn/trục vít, bộ truyền đai, xích, cam, lò xo, mối ghép bu lông...).</li>
                <li>Thiết kế và tính toán chi tiết kim loại tấm (Sheet Metal), trải phẳng phôi (Flat Pattern) phục vụ cắt Laser/Chấn CNC; Thiết kế hệ thống khung giàn thép định hình (Frame Generator) và kết cấu hàn (Weldments).</li>
                <li>Mô phỏng động học & động lực học cơ cấu máy (Dynamic Simulation), phân tích bền phần tử hữu hạn (Stress Analysis / Nastran CAE: ứng suất, biến dạng, tần số dao động riêng, tải nhiệt).</li>
                <li><strong>Lập trình và xuất chương trình NC cho máy CNC (Inventor CAM / HSM):</strong> Thiết lập gốc tọa độ phôi, chọn dao, lập trình đường chạy dao Phay CNC 2.5D/3D và Tiện CNC, mô phỏng kiểm tra va chạm dao trên máy tính.</li>
                <li><strong>Thành thạo tập lệnh G-code, vận hành máy Phay, Tiện CNC:</strong> Đọc hiểu, hiệu chỉnh cấu trúc mã lệnh G-code / M-code, kỹ thuật gá đặt phôi, xét gốc dao và vận hành gia công thực tế trên máy Phay/Tiện CNC & In 3D tạo mẫu nhanh.</li>
              </ul>
            </li>
            <li>
              <strong style="color: #9d0c4c;">Khóa 3 – Inventor Chuyên Sâu Theo Yêu Cầu Học Viên (Khuôn mẫu, Sản phẩm, AI trong thiết kế...) (Học phí: 4.500.000đ):</strong>
              <ul style="margin-top: 4px; padding-left: 18px;">
                <li>Dựng hình bề mặt cong phức tạp và kiểu dáng công nghiệp (Advanced Surfacing, Freeform Modeling & Multi-body Part) cho các sản phẩm nhựa kỹ thuật và tiêu dùng.</li>
                <li>Thiết kế đặc thù cho sản phẩm nhựa (Plastic Part Features: gân tăng cứng, vấu lẫy Snap-fit, vấu bắt vít Boss, lưới thoát nhiệt Grill, góc thoát khuôn Draft Analysis).</li>
                <li><strong>Quy trình thiết kế và tách khuôn ép nhựa hoàn chỉnh (Inventor Mold Design):</strong> Thiết lập độ co rút vật liệu nhựa, xác định mặt phân khuôn (Parting Surface), tách Lõi và Lòng khuôn (Core & Cavity), thiết kế kênh dẫn nhựa (Runner), cổng phun (Gate), hệ thống làm mát, chốt đẩy (Ejector Pins) và lắp ráp bộ đế khuôn tiêu chuẩn (Mold Base), mô phỏng dòng chảy nhựa (Moldflow).</li>
                <li><strong>Ứng dụng AI trong thiết kế cơ khí & tối ưu hóa (Generative Design / Topology Optimization / Tự động hóa iLogic & VBA):</strong> Tối ưu hóa hình học chi tiết máy theo tải trọng bằng AI, tự động hóa thiết kế tham số hàng loạt.</li>
                <li>Thiết kế hệ thống đường ống và dây dẫn phức tạp (Tube & Pipe, Cable & Harness); Render hình ảnh sản phẩm & xuất video diễn hoạt dây chuyền sản xuất (Inventor Studio).</li>
                <li><strong>Tích hợp hệ thống Cơ điện tử & Robot:</strong> Xuất mô hình 3D cơ khí và thông số quán tính từ Inventor sang <strong>MATLAB / Simulink (Simscape Multibody)</strong> để mô phỏng động học/động lực học và thiết kế bộ điều khiển tự động cho đồ án, luận văn và dự án nghiên cứu.</li>
              </ul>
            </li>
          </ol>
        </div>
      </details>

      <div class="mlab-course-footer">
        <div style="width: 100%; margin-bottom: 6px;">
          <div style="font-size: 0.85rem; color: #063d1e; font-weight: 800; text-transform: uppercase; margin-bottom: 4px;">
            👇 CHỌN KHÓA HỌC INVENTOR BẠN MUỐN ĐĂNG KÝ (Nhấn chọn khóa học trước khi bấm Ghi danh):
          </div>
          <div class="mlab-tier-selector">
            <button type="button" id="tierBtn_INV_BASIC" class="mlab-tier-btn active" onclick="selectInventorTier('INV_BASIC')">
              <div>
                <span class="mlab-tier-badge" style="background: #0b8a42;">Khóa 1 • Căn Bản</span>
                <div class="mlab-tier-title">Inventor Căn Bản</div>
                <div class="mlab-tier-desc">Thành thạo vẽ 3D từ ý tưởng đến bản vẽ lắp, xuất bản vẽ 2D gia công (Laser, CNC...), xuất video mô phỏng lắp ráp & hoạt động máy móc, robot.</div>
              </div>
              <div class="mlab-tier-price">1.500.000đ</div>
            </button>

            <button type="button" id="tierBtn_INV_CAM" class="mlab-tier-btn" onclick="selectInventorTier('INV_CAM')">
              <div>
                <span class="mlab-tier-badge" style="background: #3b6ca8;">Khóa 2 • Nâng Cao</span>
                <div class="mlab-tier-title">Inventor Nâng Cao CAM, CNC</div>
                <div class="mlab-tier-desc">Thiết kế cơ cấu máy, tính toán truyền động (đai, xích, bánh răng...), mô phỏng CAE, thành thạo G-code, lập trình xuất NC & vận hành Phay/Tiện CNC.</div>
              </div>
              <div class="mlab-tier-price">2.500.000đ</div>
            </button>

            <button type="button" id="tierBtn_INV_MOLD" class="mlab-tier-btn" onclick="selectInventorTier('INV_MOLD')">
              <div>
                <span class="mlab-tier-badge" style="background: #9d0c4c;">Khóa 3 • Chuyên Sâu</span>
                <div class="mlab-tier-title">Inventor Chuyên Sâu Theo Yêu Cầu Học Viên (Khuôn mẫu, sản phẩm, AI trong thiết kế...)</div>
                <div class="mlab-tier-desc">Thiết kế khuôn mẫu & sản phẩm nhựa, Surface nâng cao, ứng dụng AI trong thiết kế cơ khí & liên kết mô phỏng điều khiển MATLAB.</div>
              </div>
              <div class="mlab-tier-price">4.500.000đ</div>
            </button>
          </div>
        </div>

        <div>
          <div id="inventorSelectedLabel" style="font-size: 0.8rem; color: #076b33; font-weight: 700; text-transform: uppercase;">
            Đang chọn: Inventor Căn Bản
          </div>
          <div class="mlab-price-box">
            <span id="inventorSelectedPrice" class="mlab-price-current">1.500.000đ</span>
            <span style="font-size: 0.82rem; color: #0b8a42; font-weight: 700;">(Học 1 khóa – Hỗ trợ trọn đời)</span>
          </div>
        </div>
        <div class="mlab-action-group">
          <a href="tel:0946469720" class="mlab-btn-outline">
            📞 Tư vấn: 0946.469.720
          </a>
          <button type="button" class="mlab-btn-enroll" onclick="openMlabEnrollModal(selectedInventorTierKey)">
            ✍️ Ghi Danh & Thanh Toán QR
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ==================== KHÓA HỌC 2: IoT CHO SINH VIÊN KỸ THUẬT ==================== -->
  <div class="mlab-course-card">
    <div class="mlab-course-header">
      <div class="mlab-course-tag-row">
        <span class="mlab-badge mlab-badge-mode">🌐 Học Online & Offline tại MLAB</span>
        <span class="mlab-badge mlab-badge-discount">🔥 Ưu đãi Giảm 57%</span>
      </div>
      <div class="mlab-course-tag-row">
        <span class="mlab-badge mlab-badge-cert">🎓 Cấp chứng nhận hoàn thành</span>
        <button type="button" class="mlab-btn-enroll-top" onclick="openMlabEnrollModal('IOT')">
          ✍️ Ghi Danh & Thanh Toán QR
        </button>
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
          <span style="color: #0b8a42; font-size: 0.82rem;">Nhấn để mở rộng ▼</span>
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
            <span style="font-size: 0.8rem; color: #0b8a42; font-weight: 700;">(Tiết kiệm 57%)</span>
          </div>
        </div>
        <div class="mlab-action-group">
          <a href="https://emechatronix.edubit.vn/iot-cho-sinh-vien-ky-thuat" target="_blank" rel="noopener" class="mlab-btn-outline">
            🔗 Xem trên Edubit
          </a>
          <button type="button" class="mlab-btn-enroll" onclick="openMlabEnrollModal('IOT')">
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
      <h3 id="mlabModalTitle">🎓 Ghi Danh Khóa Học Ngắn Hạn - MLAB</h3>
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
            <label for="mlabCourseSelect">Khóa học đăng ký <span style="color:#dc2626">*</span></label>
            <select id="mlabCourseSelect" class="mlab-form-control" onchange="updateCourseSelectionUI()" required>
              <option value="INV_BASIC">Inventor căn bản (Học phí: 1.500.000đ)</option>
              <option value="INV_CAM">Inventor nâng cao CAM , CNC (Học phí: 2.500.000đ)</option>
              <option value="INV_MOLD">Inventor chuyên sâu theo yêu cầu học viên (khuôn mẫu, sản phẩm, AI trong thiết kế...) (Học phí: 4.500.000đ)</option>
              <option value="IOT">IoT cho sinh viên kỹ thuật (Học phí: 1.500.000đ)</option>
            </select>
          </div>

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
                <option value="Học online">Học online</option>
                <option value="Học offline">Học offline</option>
              </select>
            </div>
          </div>

          <div class="mlab-form-group">
            <label for="mlabNote">Lịch trống có thể sắp xếp học :</label>
            <input type="text" id="mlabNote" class="mlab-form-control" placeholder="Ví dụ: sáng hoặc chiều thứ :...">
          </div>

          <button type="submit" id="mlabProceedQrBtn" class="mlab-btn-primary">
            Tiếp tục: Tạo mã QR Thanh toán Học phí &rarr;
          </button>
        </form>
      </div>

      <!-- BƯỚC 2: HIỂN THỊ MÃ VIETQR ĐỘNG & XÁC NHẬN -->
      <div id="mlabStep2" style="display: none;">
        <div class="mlab-qr-box">
          <div style="font-weight: 700; color: #076b33; font-size: 0.88rem; margin-bottom: 8px;">
            📱 Mở App Ngân hàng bất kỳ để quét mã VietQR tự động
          </div>
          <img id="mlabVietQrImg" src="" alt="Mã VietQR Thanh toán học phí" />
          <div style="font-size: 0.78rem; color: #475569;">
            (Mã QR đã tích hợp sẵn số tiền <strong id="mlabQrAmountNote">1.500.000 VNĐ</strong> và nội dung chuyển khoản tự động)
          </div>

          <div class="mlab-bank-details">
            <div><span>Ngân hàng thụ hưởng:</span> <strong>VietinBank (NH Công Thương VN)</strong></div>
            <div><span>Số tài khoản:</span> <strong style="color:#076b33;">107005679531</strong></div>
            <div><span>Chủ tài khoản:</span> <strong>DUONG KHANH SON</strong></div>
            <div><span>Số tiền học phí:</span> <strong id="mlabBankFeeDisplay" style="color:#9d0c4c;">1.500.000 VNĐ</strong></div>
            <div><span>Nội dung chuyển khoản:</span> <strong id="mlabOrderCodeDisplay" style="background:#fef3c7; padding: 1px 6px; border-radius: 4px; font-family: monospace;">IOT</strong></div>
          </div>
        </div>

        <div class="mlab-proof-box">
          <div style="font-weight: 800; color: #92400e; font-size: 0.85rem; margin-bottom: 8px;">
            🔒 XÁC THỰC THANH TOÁN (Vui lòng tải ảnh chụp biên lai CK HOẶC nhập mã giao dịch ngân hàng để mở nút Gửi thông báo):
          </div>

          <div class="mlab-form-group" style="margin-bottom: 10px;">
            <label style="color: #1e293b;">Cách 1: Tải lên ảnh chụp màn hình chuyển khoản thành công</label>
            <div class="mlab-upload-area">
              <label for="mlabReceiptFile" class="mlab-upload-label">
                📷 Chọn ảnh biên lai chuyển khoản
              </label>
              <input type="file" id="mlabReceiptFile" accept="image/*" style="display: none;" onchange="handleReceiptUpload(event)">
              <span id="mlabReceiptFileName" style="font-size: 0.78rem; color: #475569;">Chưa chọn ảnh nào</span>
            </div>
            <div id="mlabReceiptPreviewBox" class="mlab-receipt-preview">
              <img id="mlabReceiptPreviewImg" src="" alt="Ảnh biên lai" />
              <div style="flex: 1; font-size: 0.78rem; color: #076b33; font-weight: 700;">
                ✅ Đã đính kèm ảnh biên lai chuyển khoản
              </div>
              <button type="button" onclick="clearReceiptUpload()" style="background: #fee2e2; color: #b91c1c; border: none; border-radius: 6px; padding: 4px 8px; font-size: 0.75rem; font-weight: 700; cursor: pointer;">Xóa ảnh</button>
            </div>
          </div>

          <div class="mlab-form-group" style="margin-bottom: 0;">
            <label for="mlabTxRef" style="color: #1e293b;">Cách 2: Hoặc nhập Mã giao dịch ngân hàng / Thời gian chuyển khoản (Tối thiểu 4 ký tự):</label>
            <input type="text" id="mlabTxRef" class="mlab-form-control" placeholder="Ví dụ: FT2432891023 hoặc Đã CK lúc 20:30 từ VCB..." oninput="checkPaymentVerification()">
          </div>
        </div>

        <div id="mlabVerifyHint" style="text-align: center; padding: 10px 12px; border-radius: 8px; background: #f1f5f9; color: #64748b; font-size: 0.82rem; font-weight: 600; margin-bottom: 6px;">
          ⚠️ Nút <strong>"Tôi đã thanh toán – Gửi thông báo ghi danh"</strong> sẽ tự động hiển thị ngay khi bạn tải ảnh biên lai hoặc nhập mã giao dịch ở trên.
        </div>

        <button type="button" id="mlabSubmitBtn" class="mlab-btn-success" style="display: none;" onclick="submitEnrollmentNotification()">
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
  // Cấu hình danh sách khóa học & thông tin thanh toán VietQR động
  const MLAB_COURSES = {
    IOT: {
      code: "IOT",
      name: "IoT cho sinh viên kỹ thuật",
      shortLabel: "IoT cho sinh viên kỹ thuật",
      amount: 1500000,
      feeText: "1.500.000 VNĐ",
      priceDisplay: "1.500.000đ",
      notePlaceholder: "Ví dụ: sáng hoặc chiều thứ :...",
      modes: [
        "Học online",
        "Học offline"
      ]
    },
    INV_BASIC: {
      code: "INVCB",
      name: "Inventor căn bản",
      shortLabel: "Inventor căn bản",
      amount: 1500000,
      feeText: "1.500.000 VNĐ",
      priceDisplay: "1.500.000đ",
      notePlaceholder: "Ví dụ: sáng hoặc chiều thứ :...",
      modes: [
        "Học online",
        "Học offline"
      ]
    },
    INV_CAM: {
      code: "INVCAM",
      name: "Inventor nâng cao CAM , CNC",
      shortLabel: "Inventor nâng cao CAM , CNC",
      amount: 2500000,
      feeText: "2.500.000 VNĐ",
      priceDisplay: "2.500.000đ",
      notePlaceholder: "Ví dụ: sáng hoặc chiều thứ :...",
      modes: [
        "Học online",
        "Học offline"
      ]
    },
    INV_MOLD: {
      code: "INVCS",
      name: "Inventor chuyên sâu theo yêu cầu học viên (khuôn mẫu, sản phẩm, AI trong thiết kế...)",
      shortLabel: "Inventor chuyên sâu theo yêu cầu học viên (khuôn mẫu, sản phẩm, AI trong thiết kế...)",
      amount: 4500000,
      feeText: "4.500.000 VNĐ",
      priceDisplay: "4.500.000đ",
      notePlaceholder: "Ví dụ: sáng hoặc chiều thứ :...",
      modes: [
        "Học online",
        "Học offline"
      ]
    }
  };

  let selectedInventorTierKey = "INV_BASIC";
  let uploadedReceiptBase64 = "";
  let uploadedReceiptFileName = "";

  const MLAB_PAYMENT_CONFIG = {
    bankId: "ICB", // Mã ngân hàng VietinBank chuẩn Napas VietQR
    accountNo: "107005679531",
    accountName: "DUONG KHANH SON",
    notifyEmail: "sonduongkhanh@gmail.com",
    // URL Web App của Google Apps Script để tự động ghi vào Google Sheets
    googleScriptUrl: "https://script.google.com/macros/s/AKfycbzT-V4IbA9lEHcce9cTtjPFRhoMcJ9NJDoZn_tmJVcCNpATbHXEKT5QtS5tUvHNbSjBWw/exec"
  };

  let currentEnrollmentData = {};

  function selectInventorTier(tierKey) {
    if (!MLAB_COURSES[tierKey]) return;
    selectedInventorTierKey = tierKey;
    const course = MLAB_COURSES[tierKey];

    ["INV_BASIC", "INV_CAM", "INV_MOLD"].forEach(function(k) {
      const btn = document.getElementById("tierBtn_" + k);
      if (btn) {
        btn.className = (k === tierKey) ? "mlab-tier-btn active" : "mlab-tier-btn";
      }
    });

    const labelEl = document.getElementById("inventorSelectedLabel");
    const priceEl = document.getElementById("inventorSelectedPrice");
    if (labelEl) labelEl.textContent = "Đang chọn: " + course.shortLabel;
    if (priceEl) priceEl.textContent = course.priceDisplay;
  }

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

  function updateCourseSelectionUI() {
    const courseKey = document.getElementById("mlabCourseSelect").value || "IOT";
    const course = MLAB_COURSES[courseKey] || MLAB_COURSES.IOT;

    document.getElementById("mlabModalTitle").textContent = "🎓 Ghi Danh: " + course.name;
    document.getElementById("mlabNote").placeholder = course.notePlaceholder;
    document.getElementById("mlabProceedQrBtn").innerHTML = `Tiếp tục: Tạo mã QR Thanh toán Học phí (${course.priceDisplay}) &rarr;`;

    const modeSelect = document.getElementById("mlabMode");
    modeSelect.innerHTML = "";
    course.modes.forEach(function(m) {
      const opt = document.createElement("option");
      opt.value = m;
      opt.textContent = m;
      modeSelect.appendChild(opt);
    });
  }

  function openMlabEnrollModal(courseKey) {
    const selectEl = document.getElementById("mlabCourseSelect");
    const targetKey = (courseKey === "INVENTOR") ? selectedInventorTierKey : (courseKey || "IOT");
    if (targetKey && MLAB_COURSES[targetKey]) {
      selectEl.value = targetKey;
    }
    updateCourseSelectionUI();
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

  function checkPaymentVerification() {
    const txRef = document.getElementById("mlabTxRef").value.trim();
    const hasReceiptImage = Boolean(uploadedReceiptBase64);
    const hasValidTxRef = txRef.length >= 4;
    const isVerified = hasReceiptImage || hasValidTxRef;

    const submitBtn = document.getElementById("mlabSubmitBtn");
    const hintBox = document.getElementById("mlabVerifyHint");

    if (isVerified) {
      submitBtn.style.display = "block";
      hintBox.style.display = "none";
    } else {
      submitBtn.style.display = "none";
      hintBox.style.display = "block";
    }
  }

  function handleReceiptUpload(event) {
    const file = event.target.files && event.target.files[0];
    if (!file) {
      clearReceiptUpload();
      return;
    }

    uploadedReceiptFileName = file.name;
    document.getElementById("mlabReceiptFileName").textContent = file.name;

    // Nén ảnh biên lai xuống kích thước vừa phải để gửi nhanh qua Google Sheets / Email
    const reader = new FileReader();
    reader.onload = function(e) {
      const img = new Image();
      img.onload = function() {
        const canvas = document.createElement("canvas");
        const maxDim = 900;
        let w = img.width;
        let h = img.height;
        if (w > maxDim || h > maxDim) {
          if (w > h) {
            h = Math.round((h * maxDim) / w);
            w = maxDim;
          } else {
            w = Math.round((w * maxDim) / h);
            h = maxDim;
          }
        }
        canvas.width = w;
        canvas.height = h;
        const ctx = canvas.getContext("2d");
        ctx.drawImage(img, 0, 0, w, h);
        uploadedReceiptBase64 = canvas.toDataURL("image/jpeg", 0.75);

        document.getElementById("mlabReceiptPreviewImg").src = uploadedReceiptBase64;
        document.getElementById("mlabReceiptPreviewBox").style.display = "flex";
        checkPaymentVerification();
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }

  function clearReceiptUpload() {
    uploadedReceiptBase64 = "";
    uploadedReceiptFileName = "";
    const fileInput = document.getElementById("mlabReceiptFile");
    if (fileInput) fileInput.value = "";
    document.getElementById("mlabReceiptFileName").textContent = "Chưa chọn ảnh nào";
    document.getElementById("mlabReceiptPreviewBox").style.display = "none";
    document.getElementById("mlabReceiptPreviewImg").src = "";
    checkPaymentVerification();
  }

  function proceedToVietQR(event) {
    event.preventDefault();
    const courseKey = document.getElementById("mlabCourseSelect").value || "IOT";
    const course = MLAB_COURSES[courseKey] || MLAB_COURSES.IOT;

    const fullName = document.getElementById("mlabFullName").value.trim();
    const phone = document.getElementById("mlabPhone").value.replace(/\s+/g, "");
    const email = document.getElementById("mlabEmail").value.trim();
    const org = document.getElementById("mlabOrg").value.trim();
    const learningMode = document.getElementById("mlabMode").value;
    const note = document.getElementById("mlabNote").value.trim();

    // Tạo mã nội dung chuyển khoản ngắn gọn, không dấu
    const cleanName = removeVietnameseTones(fullName).split(/\s+/).slice(-2).join(" ");
    const orderCode = (course.code + " " + phone + " " + cleanName).substring(0, 45);

    currentEnrollmentData = {
      orderCode: orderCode,
      fullName: fullName,
      phone: phone,
      email: email,
      organization: org || "Không ghi",
      courseName: course.name,
      learningMode: learningMode,
      fee: course.feeText,
      amount: course.amount,
      note: note
    };

    // Tạo URL ảnh VietQR động chuẩn Napas
    const qrUrl = `https://img.vietqr.io/image/${MLAB_PAYMENT_CONFIG.bankId}-${MLAB_PAYMENT_CONFIG.accountNo}-compact2.png?amount=${course.amount}&addInfo=${encodeURIComponent(orderCode)}&accountName=${encodeURIComponent(MLAB_PAYMENT_CONFIG.accountName)}`;

    document.getElementById("mlabVietQrImg").src = qrUrl;
    document.getElementById("mlabQrAmountNote").textContent = course.feeText;
    document.getElementById("mlabBankFeeDisplay").textContent = course.feeText;
    document.getElementById("mlabOrderCodeDisplay").textContent = orderCode;

    // Reset trạng thái xác thực ở Bước 2 để bắt buộc người dùng tải ảnh hoặc nhập mã GD
    document.getElementById("mlabTxRef").value = "";
    clearReceiptUpload();
    checkPaymentVerification();

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
    if (!uploadedReceiptBase64 && txRef.length < 4) {
      alert("Vui lòng tải ảnh biên lai chuyển khoản hoặc nhập Mã giao dịch ngân hàng trước khi gửi thông báo!");
      return;
    }

    const proofMethod = uploadedReceiptBase64
      ? (txRef ? `Đã đính kèm ảnh biên lai (${uploadedReceiptFileName}) + Mã GD: ${txRef}` : `Đã đính kèm ảnh biên lai (${uploadedReceiptFileName})`)
      : `Mã giao dịch CK: ${txRef}`;

    const combinedNote = [currentEnrollmentData.note, proofMethod].filter(Boolean).join(" | ");

    submitBtn.disabled = true;
    submitBtn.textContent = "⏳ Đang gửi thông tin & biên lai ghi danh cho Thầy Sơn...";

    const payload = {
      ...currentEnrollmentData,
      note: combinedNote,
      txRef: txRef || "Không nhập",
      receiptFileName: uploadedReceiptFileName || "",
      receiptImage: uploadedReceiptBase64 || "",
      paymentStatus: `Đã xác thực thanh toán (${proofMethod}) - Học phí: ${currentEnrollmentData.fee}`
    };

    try {
      // 1. Gửi thẳng vào Google Sheets + Gmail Apps Script
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
          _subject: `[MLAB - Ghi danh] ${payload.fullName} - ${payload.phone} (${payload.courseName})`,
          _template: "table",
          "Khóa học": payload.courseName,
          "Mã đối soát CK (VietQR)": payload.orderCode,
          "Họ và tên học viên": payload.fullName,
          "Số điện thoại / Zalo": payload.phone,
          "Email học viên": payload.email,
          "Trường / Đơn vị": payload.organization,
          "Hình thức học": payload.learningMode,
          "Học phí": payload.fee,
          "Xác thực thanh toán": proofMethod,
          "Ghi chú học viên": currentEnrollmentData.note || "Không có"
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
