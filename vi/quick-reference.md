# NVH Source Locator — Tham khảo nhanh

Bản tóm tắt một trang. Để biết chi tiết đầy đủ, xem **Hướng dẫn sử dụng**.

---

## Quy trình chính (2-Sensor, miễn phí)

1. **Chọn vật liệu** — tab Materials → chạm vào vật liệu của bạn
2. **Nhập hiệu chuẩn** ở tab 2-Sensor:
   - Khoảng cách giữa các cảm biến (`d`)
   - Độ trễ thời gian hiệu chuẩn (`tCal`) — tự động điền từ vật liệu
3. **Nhập sự kiện** — `tEvent` và Cảm biến đầu tiên (A hoặc B)
4. **Đọc kết quả** — khoảng cách từ cảm biến A

![Tab 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Tất cả các tab

| Tab | Đầu ra | Trường Pro? |
|---|---|---|
| 2-Sensor | Khoảng cách dọc theo đường | Không (hoàn toàn miễn phí) |
| 3-Sensor | X, Y trên bề mặt | Có |
| 3-Sen+ | X, Y với LSQ qua 3 cặp | Có |
| 4-Sensor | X, Y từ hai cặp (A–B + C–D) | Có |
| 4-Sen+ | X, Y từ 4 cảm biến, vị trí bất kỳ | Có |
| 3D | X, Y, Z từ 4 cảm biến | Có |
| 3D+ | X, Y, Z từ tối đa 6 cảm biến | Có |
| Materials | Bộ chọn tốc độ âm thanh | Không |
| Help | Hướng dẫn | Không |

Cài đặt nằm dưới biểu tượng ⚙ (trên cùng bên phải), không phải là tab.

---

## Bù nhiệt độ

Cài đặt → Nhiệt độ tham chiếu, phạm vi **-40 đến +200 °C**.

- **14 kim loại** có bù tích hợp sẵn (nhôm, các loại thép, đồng, đồng thau, đồng đỏ, titan, magie, chì, kẽm, niken, vonfram, sắt, gang)
- Vật liệu không có bù hiển thị **"ref only"**
- **Đặt lại về 20 °C mỗi khi khởi động ứng dụng** (khởi động an toàn mặc định)
- Phát lại mục lịch sử sẽ khôi phục nhiệt độ ban đầu của nó

---

## Phím tắt

- **Chạm vào vật liệu** → tự động điền vào tất cả các trường `tCal` ở tất cả các tab
- **Giữ +/-** trên các trường số → tăng nhanh
- **Kéo ngang** trên trường số → cuộn qua các giá trị
- **Đầu vào trống/âm/không hợp lệ** → quay về 0 khi mất tiêu điểm (trường nhiệt độ giới hạn ở -40/200)
- **Đánh dấu sao vật liệu** → di chuyển lên đầu bộ chọn

---

## Mô hình Pro

**Freemium khóa tính năng** ($19,99):
- Miễn phí: tab 2-Sensor hoạt động đầy đủ, không giới hạn
- Pro: Các tab khác có thể truy cập nhưng có **các trường có ổ khóa vàng** hiển thị paywall khi chạm

Pro mở khóa: từ 3-Sensor đến 3D+, vật liệu tùy chỉnh, sao lưu/khôi phục, báo cáo PDF, chú thích ảnh.

![Paywall](../screenshots/07-paywall.png)

---

## Báo cáo và sao lưu

Nút **In kết quả** trên bất kỳ màn hình kết quả nào → PDF với tiêu đề, đầu vào, kết quả, hình ảnh, ảnh (nếu đã chụp) và chân trang nhiệt độ (khi bù được kích hoạt).

Tùy chỉnh tiêu đề trong Cài đặt → Tiêu đề báo cáo.

**Sao lưu**: Cài đặt → Sao lưu → chia sẻ vào đám mây/email.  
**Khôi phục**: Cài đặt → Khôi phục → chọn tệp sao lưu.

---

## Khôi phục Pro trên thiết bị mới

Cùng tài khoản Google (Android) hoặc Apple ID (iOS) mà bạn đã mua → Cài đặt → **Khôi phục mua hàng** → mở khóa trong vài giây.

Khôi phục tự động diễn ra âm thầm khi bạn quay lại ứng dụng sau khi đổi mã khuyến mãi bên ngoài.

---

## Khắc phục sự cố nhanh

- **Kết quả ngoài phạm vi?** Kiểm tra dấu `tEvent` / Cảm biến đầu tiên / khoảng cách cảm biến
- **Vật liệu gần nhất sai?** Có thể nhiệt độ tham chiếu đã được đặt vô tình — kiểm tra Cài đặt
- **Khôi phục mua hàng thất bại?** Xác minh cùng tài khoản cửa hàng; cài đặt lại nếu vẫn tiếp tục
- **Trường được đặt thành 0?** Đầu vào trống/âm tự động được đặt khi mất tiêu điểm — nhập lại giá trị
- **Nút stepper biến mất?** Chúng xuất hiện bên cạnh các trường có `data-step` — khởi động lại ứng dụng nếu thiếu
- **Cảnh báo nhiệt độ lỗi thời?** Đặt lại về 20 mỗi khi khởi động — đặt lại cho phiên này

---

Liên hệ `support@evdiag.net` — kèm theo kiểu máy thiết bị, phiên bản ứng dụng (Cài đặt → dưới cùng) và mô tả về những gì bạn đã thử.
