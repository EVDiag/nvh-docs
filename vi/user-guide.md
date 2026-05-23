# NVH Source Locator — Hướng dẫn người dùng

NVH Source Locator là một công cụ đo lường để định vị các nguồn tiếng ồn và rung động sử dụng TDOA (Time Difference of Arrival) từ các tín hiệu gia tốc kế được ghi lại trên máy hiện sóng hoặc hệ thống đo lường.

Hướng dẫn này bao quát tất cả các tính năng. Để có một tóm lược nhanh, xem **Tham khảo nhanh**.

---

## Mục lục

1. [Cách hoạt động](#how-it-works)
2. [Trước khi bắt đầu](#before-you-start)
3. [Các tab chính](#the-main-tabs)
4. [Chế độ 2-Sensor](#2-sensor-mode)
5. [Chế độ 3-Sensor](#3-sensor-mode)
6. [Chế độ Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Tab Materials](#the-materials-tab)
8. [Bù nhiệt độ](#temperature-compensation)
9. [Chú thích ảnh](#photo-annotation)
10. [Báo cáo](#reports)
11. [Sao lưu và khôi phục](#backup-and-restore)
12. [Cài đặt](#settings)
13. [Tính năng Pro](#pro-features)
14. [Tab Help và hướng dẫn](#help-tab-and-tutorials)
15. [Khắc phục sự cố](#troubleshooting)

---

## Cách hoạt động {#how-it-works}

Khi một nguồn tiếng ồn phát ra âm thanh hoặc rung động, sóng truyền qua vật liệu với tốc độ đã biết. Nếu bạn đặt hai hoặc nhiều gia tốc kế trên vật liệu và đo thời điểm sóng đến mỗi cảm biến, sự khác biệt thời gian sẽ cho bạn biết nguồn ở đâu.

NVH Source Locator nhận:

- **Hiệu chuẩn**: khoảng cách giữa các cảm biến và thời gian sóng cần để đi quãng đường đó (được sử dụng để tính tốc độ âm thanh của vật liệu)
- **Sự kiện**: sự khác biệt thời gian giữa các cảm biến phát hiện sự kiện tiếng ồn/rung động

Sau đó, nó tính toán vị trí nguồn trên cấu trúc.

Bạn càng sử dụng nhiều cảm biến, bạn càng có thể xác định nguồn chính xác hơn:

- **2 cảm biến** → khoảng cách dọc theo một đường thẳng
- **3 cảm biến** → vị trí trên bề mặt 2D (X, Y)
- **4 cảm biến** → vị trí trong không gian 3D (X, Y, Z)

---

## Trước khi bắt đầu {#before-you-start}

Bạn sẽ cần:

- **Máy hiện sóng hoặc hệ thống đo lường** có thể hiển thị sự khác biệt thời gian giữa các kênh gia tốc kế tính bằng micro giây (µs)
- **Ít nhất 2 gia tốc kế** được gắn vật lý vào cấu trúc (càng nhiều cảm biến = độ chính xác càng cao)
- **Cách đo khoảng cách** giữa các cảm biến (thước dây, thước cặp)
- **Cách kích hoạt sóng** tại vị trí đã biết để hiệu chuẩn (va đập búa đã hiệu chuẩn, gõ tua vít, hoặc tín hiệu đã biết khác)

![Màn hình chính với tab 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Các tab chính {#the-main-tabs}

Ứng dụng có các tab ở trên cùng:

![Thanh tab](../screenshots/02-tab-bar.png)

| Tab | Chức năng | Khi sử dụng |
|---|---|---|
| **2-Sensor** | Định vị nguồn 1D dọc theo đường thẳng giữa 2 cảm biến | Kiểm tra nhanh, cấu trúc giống thanh dầm. **Hoàn toàn miễn phí.** |
| **3-Sensor** | Định vị nguồn 2D sử dụng 3 cảm biến trong tam giác | Sử dụng chung nhất, tấm và bề mặt |
| **3-Sen+** | 3-Sensor với bộ giải bình phương tối thiểu xác định thừa | Đo lường yêu cầu khắt khe hơn, kháng nhiễu |
| **4-Sensor** | Định vị 2D sử dụng hai cặp (A-B + C-D) | Bố trí cảm biến hình chữ nhật, kiểm tra chéo |
| **4-Sen+** | Chế độ 2D nâng cao, 4 cảm biến ở bất kỳ vị trí nào | Hình học không phải hình chữ nhật, LSQ đầy đủ |
| **3D** | Định vị nguồn 3D sử dụng 4 cảm biến với tọa độ XYZ | Cấu trúc phức tạp trong không gian 3D |
| **3D+** | 3D với tối đa 6 cảm biến, LSQ xác định thừa | Hình học rất phức tạp, độ chính xác tối đa |
| **Materials** | Thư viện tốc độ âm thanh + vật liệu tùy chỉnh | Chọn một lần cho mỗi phiên đo |
| **Help** | Hướng dẫn trong ứng dụng và tham khảo | Khi bạn cần một sự tóm lược nhanh |

> **Miễn phí vs Pro**: Tab 2-Sensor hoàn toàn miễn phí. Các tab khác có thể truy cập nhưng có các trường nhập cụ thể bị khóa cho người dùng Pro (được đánh dấu bằng huy hiệu khóa vàng). Chạm vào trường bị khóa sẽ hiển thị paywall Pro.

Cài đặt được truy cập thông qua biểu tượng bánh răng ⚙ ở góc trên bên phải (không phải tab).

---

## Chế độ 2-Sensor {#2-sensor-mode}

Đo lường đơn giản nhất: định vị nguồn dọc theo đường thẳng giữa hai gia tốc kế.

![Tab 2-Sensor](../screenshots/01b-home-2sensor.png)

### Bước 1: Áp dụng một vật liệu

Chạm vào tab Materials. Chọn vật liệu mà cấu trúc của bạn được làm từ (ví dụ: "Nhôm", "Thép, Mild (1020)"). Ứng dụng sử dụng tốc độ âm thanh đã biết của vật liệu để tự động điền trường thời gian hiệu chuẩn.

Nếu vật liệu của cấu trúc của bạn không có trong danh sách, bạn có thể tạm thời chọn "Không khí" và ghi đè thời gian hiệu chuẩn thủ công trong bước 2.

### Bước 2: Nhập dữ liệu hiệu chuẩn

Trên tab 2-Sensor, bạn sẽ thấy hai phần cặp: **Cặp A–B** và **Cặp A–C** (chỉ yêu cầu A–B nếu bạn chỉ có 2 cảm biến).

Cho mỗi cặp, bạn điền:

- **Khoảng cách cảm biến** (`d`): khoảng cách vật lý giữa các cảm biến, tính bằng cm hoặc inch (được đặt trong Cài đặt)
- **Trễ thời gian hiệu chuẩn** (`tCal`): thời gian để sóng đi giữa các cảm biến ở tốc độ âm thanh của vật liệu — được điền tự động khi bạn chọn vật liệu, nhưng bạn có thể ghi đè

### Bước 3: Nhập thời gian sự kiện

- **Trễ thời gian sự kiện** (`tEvent`): sự khác biệt thời gian giữa các cảm biến phát hiện sự kiện tiếng ồn, tính bằng micro giây
- **Cảm biến đầu tiên**: cảm biến nào nghe sự kiện đầu tiên (A hoặc B)

### Bước 4: Đọc kết quả

Ứng dụng hiển thị vị trí nguồn là khoảng cách từ cảm biến A:
- Kết quả = 0: nguồn ở cảm biến A
- Kết quả = khoảng cách: nguồn ở cảm biến B
- Kết quả ở giữa: nguồn ở giữa chúng
- Kết quả ở ngoài: nguồn ở ngoài một trong các cảm biến (toast sẽ cảnh báo)

Thẻ kết quả hiển thị cả hai khoảng cách (từ A, từ B) và cho biết cảm biến nào gần hơn.

### Bước 5 (tùy chọn): Chú thích ảnh

Chạm vào **📷 Chú thích ảnh** để chụp ảnh thiết lập của bạn. Ứng dụng phủ các điểm đánh dấu cho cảm biến A, B và nguồn. Hữu ích cho báo cáo.

---

## Chế độ 3-Sensor {#3-sensor-mode}

Định vị một nguồn trên mặt phẳng 2D sử dụng ba cảm biến được sắp xếp thành tam giác.

![Tab 3-Sensor](../screenshots/03-3sensor-tab.png)

### Thiết lập

Đặt ba cảm biến trên cấu trúc của bạn tạo thành tam giác. Đều, vuông, hoặc thường — ứng dụng xử lý tất cả các hình học.

### Nhập dữ liệu

Trong phần **Độ dài các cạnh tam giác**, nhập khoảng cách vật lý cho cả ba cạnh (A–B, A–C, B–C).

Cho mỗi cặp (A–B và A–C), nhập:
- **tCal**: thời gian hiệu chuẩn (tự động điền từ vật liệu)
- **tEvent**: sự khác biệt thời gian đo được cho sự kiện tiếng ồn
- **Cảm biến đầu tiên**: cảm biến nào nghe đầu tiên

### Đọc kết quả

Ứng dụng hiển thị vị trí nguồn là tọa độ X, Y so với cảm biến A (cảm biến A tại gốc, cảm biến B trên trục X). Hình ảnh hiển thị tất cả ba cảm biến và vị trí nguồn.

![Kết quả tam giác](../screenshots/04-triangle-result.png)

---

## Chế độ Pro+ {#pro-modes}

Một số tab nâng cao cung cấp bộ giải xác định thừa và chiều cao hơn:

### 3-Sen+ (Pro)

Cùng thiết lập tam giác như 3-Sensor, nhưng hiệu chuẩn VÀ đo cả ba cặp (A–B, A–C, B–C). Bộ giải sử dụng cả 3 TDOA trong khớp bình phương tối thiểu — bền vững hơn với nhiễu đo lường và vật liệu dị hướng. Các phần dư trên mỗi cặp được báo cáo để bạn có thể phát hiện các phép đo không nhất quán.

### 4-Sensor

Đặt bốn cảm biến quanh khu vực:
- **A–B** = cặp ngang (phía trái/phải)
- **C–D** = cặp dọc (phía trên/dưới)

Chạy cặp A–B trước (ngang), sau đó cặp C–D (dọc). Bản đồ 2D hiển thị giao điểm. Mỗi cặp được hiệu chuẩn riêng — hữu ích khi vật liệu thay đổi qua cấu trúc.

### 4-Sen+ (2D Nâng cao)

Bốn cảm biến ở bất kỳ vị trí nào (không bắt buộc hình chữ nhật). Ghép A với mỗi B, C, D và hiệu chuẩn riêng. Bộ giải bình phương tối thiểu xác định thừa trung bình hóa nhiễu đo lường trên mỗi cặp và báo cáo các phần dư trên mỗi cặp.

### 3D

Đo 3D đầy đủ với 4 cảm biến được đặt trong không gian 3D. Nhập tọa độ (X, Y, Z) của mỗi cảm biến, cùng với thời gian hiệu chuẩn và sự kiện cho mỗi cặp (A–B, A–C, A–D).

### 3D+ (Pro)

Giống như 3D nhưng hỗ trợ tối đa **6 cảm biến** (A đến F) với LSQ xác định thừa. Độ chính xác tối đa cho hình học 3D phức tạp.

---

## Tab Materials {#the-materials-tab}

Thư viện vật liệu kỹ thuật phổ biến với tốc độ âm thanh đã biết ở 20 °C.

![Tab Materials](../screenshots/05-materials-tab.png)

### Danh sách vật liệu

Danh sách bao gồm không khí, chất lỏng, cao su, polyme, gỗ, kính và kim loại. Tốc độ dao động từ ~340 m/s (không khí) đến ~13.000 m/s (một số kim loại ở nhiệt độ phòng).

### Vật liệu tích hợp với bù nhiệt độ

14 kim loại thường được sử dụng bao gồm dữ liệu hệ số nhiệt độ. Khi Nhiệt độ tham chiếu trong Cài đặt khác 20 °C, ứng dụng tự động điều chỉnh tốc độ của các vật liệu này:

- Nhôm
- Thép, Mild (1020)
- Thép không gỉ (304)
- Sắt (đúc)
- Sắt
- Đồng
- Đồng thau
- Đồng đỏ
- Titan
- Magie
- Chì
- Kẽm
- Niken
- Wolfram

Vật liệu có bù hiển thị hai giá trị trong bộ chọn: **tốc độ đã bù** (lớn, nổi bật) và **tốc độ tham chiếu ở 20 °C** (nhỏ, xám bên dưới).

Vật liệu không có bù hiển thị **"ref only"** in nghiêng — tốc độ được liệt kê của chúng được sử dụng nguyên trạng bất kể nhiệt độ.

### Vật liệu tùy chỉnh

Nếu bạn đo hiệu chuẩn trên tab 2-Sensor, bạn có thể lưu kết quả như một vật liệu tùy chỉnh. Sau khi đo 2-sensor thành công, tìm tùy chọn để lưu tốc độ được dẫn xuất dưới tên bạn chọn.

Vật liệu tùy chỉnh lưu trữ tốc độ đo tại chỗ; chúng không bao giờ áp dụng bù nhiệt độ (tốc độ đã được đo ở nhiệt độ thử nghiệm).

### Yêu thích

Chạm vào ngôi sao bên cạnh bất kỳ vật liệu nào để đánh dấu là yêu thích. Các yêu thích xuất hiện ở đầu danh sách để truy cập nhanh.

### Tìm kiếm

Sử dụng thanh tìm kiếm ở trên cùng để lọc vật liệu theo tên. Tìm kiếm khớp với cả tên chính thống tiếng Anh và tên hiển thị đã dịch.

---

## Bù nhiệt độ {#temperature-compensation}

Tốc độ âm thanh trong vật liệu thay đổi theo nhiệt độ. Trong thử nghiệm NVH ô tô, điều này quan trọng: khoang động cơ ở 80 °C, cabin lạnh ở -10 °C, hoặc khu vực ống xả ở 200 °C tất cả đều hoạt động khác với điều kiện phòng thí nghiệm ở nhiệt độ phòng.

### Đặt nhiệt độ

Mở Cài đặt (biểu tượng ⚙) → Nhiệt độ tham chiếu. Nhập nhiệt độ môi trường thử nghiệm của bạn bằng °C (phạm vi -40 đến +200).

![Bảng cài đặt](../screenshots/06-settings.png)

### Điều gì xảy ra khi nhiệt độ ≠ 20 °C

- Các trường thời gian hiệu chuẩn tự động điền với tốc độ điều chỉnh theo nhiệt độ
- Bộ chọn Materials hiển thị nổi bật tốc độ điều chỉnh
- Một toast xác nhận: *"Nhôm đã áp dụng (6.284 m/s @ 60 °C) — đã cập nhật N cặp"*
- Gợi ý "Vật liệu gần nhất" so sánh với tốc độ điều chỉnh theo nhiệt độ
- Các mục lịch sử đã lưu ghi lại nhiệt độ hoạt động
- Báo cáo bao gồm một dòng chân trang: *"Nhiệt độ tham chiếu: 60 °C, đã áp dụng bù"*

### Đặt lại khi khởi động ứng dụng

Nhiệt độ tham chiếu **luôn đặt lại về 20 °C** khi bạn khởi động ứng dụng. Điều này ngăn các cài đặt cũ từ phiên đo trước đây ảnh hưởng âm thầm đến công việc hôm nay. Một ghi chú in nghiêng nhỏ trong Cài đặt nhắc bạn về hành vi này.

Nếu bạn muốn phát lại một phép đo lịch sử ở nhiệt độ gốc, chỉ cần chạm vào mục — nhiệt độ được khôi phục tự động.

### Vật liệu không có bù

Hầu hết các vật liệu phi kim không có hệ số nhiệt độ đáng tin cậy được công bố. Ứng dụng hiển thị huy hiệu **"ref only"** cho những loại này — tốc độ được liệt kê của chúng được sử dụng bất kể cài đặt nhiệt độ. Nếu bạn cần các phép đo chính xác ở nhiệt độ không phải phòng cho các vật liệu này, thực hiện hiệu chuẩn tại chỗ và lưu kết quả như một vật liệu tùy chỉnh.

---

## Chú thích ảnh {#photo-annotation}

Sau khi tính toán thành công, chạm vào nút **📷 Chú thích ảnh** để phủ các điểm đánh dấu cảm biến và nguồn trên một ảnh thiết lập của bạn.

![Chú thích ảnh](../screenshots/08-photo-annotation.png)

### Luồng

1. Chạm vào **Chú thích ảnh** — máy ảnh hệ thống mở ra
2. Chụp ảnh vị trí cảm biến của bạn
3. Ứng dụng tải ảnh vào lớp chú thích
4. Các điểm đánh dấu cảm biến (A, B, C, D, E, F khi áp dụng — tối đa 6 cảm biến) và điểm đánh dấu nguồn tự động được đặt dựa trên tính toán của bạn
5. Kéo bất kỳ điểm đánh dấu nào để tinh chỉnh vị trí. Khi bạn điều chỉnh, vị trí nguồn được tính lại từ các vị trí cảm biến đã sửa
6. Chạm vào **Lưu** để giữ, hoặc **Chụp lại** để thử lại

Ảnh có chú thích được tự động bao gồm trong báo cáo PDF.

---

## Báo cáo {#reports}

Chạm vào nút **In kết quả** trên bất kỳ màn hình kết quả nào để tạo báo cáo được định dạng.

![Báo cáo PDF](../screenshots/09-pdf-report.png)

### Nội dung báo cáo

- Tiêu đề (có thể tùy chỉnh trong Cài đặt → Tiêu đề báo cáo)
- Tiêu đề phép đo và dấu thời gian
- Tất cả các giá trị đầu vào trong một bảng sạch sẽ
- Kết quả tính toán
- Văn bản kết luận
- Hình ảnh (biểu đồ hình học)
- Ảnh có chú thích (nếu bạn đã chụp)
- Dòng chân trang nhiệt độ (nếu bù đang hoạt động)
- Số trang và dòng tín dụng

### Định dạng đầu ra

- **Android**: tạo PDF gốc, lưu vào điện thoại hoặc chia sẻ
- **iOS**: hộp thoại in của hệ thống → lưu dưới dạng PDF, AirPrint, hoặc chia sẻ

### Tùy chỉnh tiêu đề

Cài đặt → Tiêu đề báo cáo. Nhập tên công ty của bạn, tên phòng thí nghiệm, thông tin dự án, hoặc bất cứ điều gì bạn muốn ở trên cùng của mỗi báo cáo.

---

## Sao lưu và khôi phục {#backup-and-restore}

Lưu tất cả các vật liệu tùy chỉnh, yêu thích, cài đặt và lịch sử của bạn vào một tệp duy nhất. Chuyển giữa các thiết bị.

### Sao lưu

Cài đặt → **Sao lưu** → chạm "Lưu tệp sao lưu". Ứng dụng tạo tệp JSON và mở bảng chia sẻ của điện thoại bạn. Lưu vào ổ đám mây của bạn (Google Drive, iCloud, OneDrive), gửi email cho bản thân, hoặc chuyển bằng bất kỳ cách nào bạn thích.

### Khôi phục

Cài đặt → **Khôi phục** → chọn tệp sao lưu từ bộ nhớ điện thoại của bạn. Ứng dụng nhập vật liệu tùy chỉnh, yêu thích, lịch sử và cài đặt.

⚠️ **Khôi phục thay thế dữ liệu hiện tại của bạn.** Nếu bạn có các phép đo quan trọng trên thiết bị hiện tại, hãy sao lưu chúng trước khi khôi phục từ một bản sao lưu khác.

---

## Cài đặt {#settings}

Truy cập qua biểu tượng bánh răng ⚙ ở góc trên bên phải. Cài đặt là một modal, không phải tab.

![Cài đặt](../screenshots/06-settings.png)

| Cài đặt | Kiểm soát điều gì |
|---|---|
| **Nâng cấp lên Pro** | Mua hoặc tìm hiểu về các tính năng Pro ($19,99) |
| **Ngôn ngữ** | Ngôn ngữ hiển thị ứng dụng (hỗ trợ 30) |
| **Chủ đề** | Sáng, Tối, hoặc Tự động (theo hệ thống) |
| **Đơn vị khoảng cách** | cm hoặc inch |
| **Nhiệt độ tham chiếu** | Nhiệt độ hoạt động cho bù, -40 đến +200 °C |
| **Tiêu đề báo cáo** | Văn bản tùy chỉnh ở đầu báo cáo được tạo |
| **Sao lưu** | Xuất tất cả dữ liệu vào một tệp |
| **Khôi phục** | Nhập dữ liệu từ tệp sao lưu |
| **Khôi phục mua hàng** | Tái mua Pro trên thiết bị mới |

---

## Tính năng Pro {#pro-features}

NVH Source Locator sử dụng **mô hình freemium khóa theo tính năng**:

- **Miễn phí**: Tab 2-Sensor hoàn toàn chức năng không giới hạn
- **Pro**: Tất cả các tab khác có các trường nhập cụ thể bị khóa. Paywall xuất hiện khi người dùng miễn phí chạm vào trường bị khóa

### Những gì bị khóa

Các trường yêu cầu Pro được phân tán trên:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Chế độ 3D và 3D+
- Sao lưu và Khôi phục
- Báo cáo PDF
- Vật liệu tùy chỉnh
- Chú thích ảnh

Người dùng miễn phí có thể MỞ bất kỳ tab nào và XEM giao diện. Họ chỉ không thể nhập giá trị vào các trường nhập bị khóa Pro.

![Trường bị khóa Pro](../screenshots/11-pro-locked-field.png)

### Paywall

![Paywall](../screenshots/07-paywall.png)

Khi người dùng miễn phí chạm vào trường bị khóa, paywall trượt vào hiển thị:
- Biểu tượng ứng dụng với huy hiệu PRO
- Danh sách tính năng
- Nút mở khóa với giá ($19,99 mặc định; có thể thay đổi theo khu vực)
- Đổi mã khuyến mãi (chỉ Android — iOS sử dụng luồng Offer Code riêng của Apple)
- Liên kết khuyến mãi tùy chọn đến các kênh cộng đồng

### Mua Pro

Chạm vào bất kỳ trường bị khóa nào, hoặc chạm vào **Nâng cấp lên Pro** trong Cài đặt. Sử dụng hệ thống thanh toán chính thức của nền tảng của bạn (Google Play trên Android, Apple App Store trên iOS).

### Khôi phục Pro trên thiết bị mới

Nếu bạn đã mua trên một thiết bị và muốn Pro trên thiết bị khác (cùng tài khoản):

1. Đăng nhập vào **cùng** tài khoản Google (Android) hoặc Apple ID (iOS) bạn đã sử dụng để mua
2. Mở NVH Source Locator trên thiết bị mới
3. Đi đến Cài đặt → **Khôi phục mua hàng**
4. Ứng dụng xác minh với hồ sơ mua hàng của nền tảng và mở khóa Pro

### Tự động khôi phục khi khởi động

Nếu bạn đổi mã khuyến mãi trong Google Play Store hoặc App Store trong khi NVH Source Locator đang chạy ở chế độ nền, việc quay lại ứng dụng tự động phát hiện việc mua mới và mở khóa Pro — không cần Khôi phục thủ công.

### Đổi mã khuyến mãi

**Android**: nút "Có mã khuyến mãi Google Play?" trong paywall mở luồng đổi Google Play với mã của bạn được điền sẵn.

**iOS**: Chính sách App Store 3.1.1 yêu cầu đổi qua luồng "Đổi mã" chính thức của Apple. Nút Google Play bị ẩn trên iOS. Hãy tìm "Đổi mã App Store" trong Cài đặt thay thế.

---

## Tab Help và hướng dẫn {#help-tab-and-tutorials}

Tab **Help** bao gồm hướng dẫn trong ứng dụng, hướng dẫn thực hành tốt nhất và thông tin tham khảo.

![Tab Help](../screenshots/10-help-tab.png)

Các chủ đề được bao quát:
- Thiết bị bạn cần
- Cách đặt cảm biến để có độ chính xác tốt nhất
- Mẹo hiệu chuẩn
- Các kịch bản đo phổ biến
- Mẹo cho phép tam giác và vị trí 3D
- Đi dây cáp và chất lượng tín hiệu

---

## Khắc phục sự cố {#troubleshooting}

### Kết quả tính toán sai hoặc không có ý nghĩa

1. Kiểm tra hiệu chuẩn của bạn. `tCal` tự động điền giả định tốc độ vật liệu được công bố — các vật liệu thực tế khác nhau. Hiệu chuẩn chính xác nhất là tại chỗ: chạm vào vị trí đã biết và để ứng dụng dẫn xuất tốc độ thực tế.
2. Kiểm tra cài đặt **Cảm biến đầu tiên** — cảm biến nào nghe sự kiện trước có ý nghĩa cho toán học.
3. Xác minh các phép đo khoảng cách của bạn. Lỗi vài mm sẽ lan truyền.

### Toast nói "Kết quả ngoài phạm vi"

Toán học nói nguồn không nằm giữa các cảm biến của bạn. Nguyên nhân có thể:
- Nguồn thực sự ở ngoài đường/mặt phẳng cảm biến
- Một trong các đầu vào của bạn sai
- Tốc độ hiệu chuẩn quá xa với thực tế

### Gợi ý tốc độ tính toán hiển thị màu cảnh báo

Tốc độ âm thanh ngụ ý từ đầu vào của bạn xa với bất kỳ vật liệu phổ biến nào (dưới 50 m/s hoặc trên 20.000 m/s). Kiểm tra đầu vào — có khả năng là lỗi gõ trong tCal hoặc khoảng cách.

### Bộ chọn Materials hiển thị tốc độ khác với mong đợi

Kiểm tra Nhiệt độ tham chiếu trong Cài đặt. Nếu không phải 20 °C, các tốc độ hiển thị phản ánh bù nhiệt độ. Ứng dụng hiển thị "ref X @ 20°C" bên dưới các tốc độ đã bù để bạn có thể xác minh.

### Mục lịch sử phát lại với kết quả khác

Các mục lịch sử cũ được tạo trước phiên bản ứng dụng 1.75 có thể không lưu trữ nhiệt độ. Nếu bạn đã đo ở nhiệt độ không phải 20 °C, phát lại sẽ sử dụng cài đặt hiện tại. Đặt nhiệt độ thủ công trong Cài đặt trước khi phát lại, HOẶC đo lại.

### Các điểm đánh dấu chú thích ảnh không ở vị trí tôi mong đợi

Các điểm đánh dấu được đặt tự động dựa trên hình học đầu vào. Kéo chúng để điều chỉnh. Điều chỉnh các điểm đánh dấu cập nhật vị trí nguồn trong lớp phủ ảnh — nhưng KHÔNG thay đổi kết quả tính toán cơ bản.

### Sao lưu/Khôi phục thất bại

Đảm bảo rằng bạn đang sử dụng tệp sao lưu được tạo bởi cùng phiên bản hoặc phiên bản mới hơn của ứng dụng. Các tệp sao lưu cũ hơn có thể thiếu các trường dữ liệu hiện tại.

### Khôi phục mua hàng nói "không tìm thấy mua hàng"

1. Xác minh bạn đã đăng nhập vào cùng tài khoản cửa hàng mà bạn đã sử dụng để mua
2. Xác minh việc mua không được hoàn lại hoặc đã hết hạn
3. Thử gỡ cài đặt và cài đặt lại ứng dụng (việc mua được liên kết với tài khoản cửa hàng của bạn, không phải cài đặt ứng dụng)
4. Liên hệ support@evdiag.net nếu tiếp tục

### Đầu vào số nhảy về 0 bất ngờ

Theo thiết kế: khi bạn rời khỏi trường số (chạm vào nơi khác), nếu nó trống, âm, hoặc chứa văn bản không phải số, nó nhảy về 0. Ngăn chặn các phép tính bị hỏng âm thầm từ các đầu vào bị xóa ngẫu nhiên. Đầu vào nhiệt độ được miễn (thay vào đó giới hạn ở -40/+200).

### Cần thêm trợ giúp

Liên hệ `support@evdiag.net` với:
- Kiểu thiết bị và phiên bản OS của bạn
- Phiên bản ứng dụng (Cài đặt → cuối trang)
- Mô tả những gì bạn đã thử
- Ảnh chụp màn hình nếu có thể

---

*NVH Source Locator được phát triển bởi EVDiag. Truy cập https://evdiag.net để cập nhật và tài nguyên.*
