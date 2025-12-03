# Bộ phân tích Boolean network

Công cụ hỗ trợ phân tích và trực quan hóa **Boolean networks** sử dụng phương pháp **Binary Decision Diagrams**.

- Đọc Boolean network từ file `.bnet`.
- Hiển thị Influence Graph (Mạng lưới tương tác).
- Xây dựng State Transition Graph (STG) (cho mạng nhỏ).
- Tìm và hiển thị các Attractors (Fixed Points & Limit Cycles) với độ chính xác 100%.

# Hiệu suất
- **Công nghệ:** Sử dụng Binary Decision Diagrams (BDDs) thông qua thư viện `PyBoolNet`.
- **Tốc độ:**
    - Mạng < 20 nodes: Xử lý tức thì (< 0.5s).
    - Mạng 30 nodes: Tìm Attractors trong vài giây.
- **Lưu ý:** Vẽ STG chỉ khả dụng cho mạng <= 12 nodes.

# Công cụ sử dụng
- Python 3.9+
- **PyBoolNet** (Core Engine)
- NetworkX, Matplotlib (Visualization)

# Cấu trúc thư mục
```
src/
│
├── input_data/test_cases/  # Chứa các file mẫu .bnet
│
├── main.py                 # Chương trình chính (Entry point)
├── pyboolnet_analyzer.py   # Wrapper cho PyBoolNet (Formal Verification)
├── visualizer.py           # Vẽ đồ thị (Influence Graph, STG)
├── bnet_parser.py          # Parser tùy chỉnh (cho Visualization)
├── benchmark_accuracy.py   # Kiểm chứng độ chính xác (vs Brute Force)
├── benchmark_time.py       # Đo thời gian thực thi
└── benchmark_utils.py      # Các hàm hỗ trợ benchmark
```

# Chi tiết Module

1.  **Logic & Phân tích (`pyboolnet_analyzer.py`)**:
    -   Sử dụng `PyBoolNet` để chuyển đổi file `.bnet` sang định dạng Primes.
    -   Tính toán Attractors bằng thuật toán tượng trưng (Symbolic Algorithms).
    -   Tự động bỏ qua vẽ STG nếu mạng quá lớn (>12 nodes).

2.  **Trực quan hóa (`visualizer.py`)**:
    -   Vẽ **Influence Graph**: Quan hệ giữa các gen.
    -   Vẽ **STG**: Các trạng thái và chuyển đổi (nếu mạng nhỏ).

3.  **Giao diện (`main.py`)**:
    -   Nhận đầu vào từ dòng lệnh.
    -   Điều phối luồng chạy: Parser -> Analyzer -> Visualizer.
    -   Xuất kết quả ra màn hình và lưu vào thư mục `output/`.

# Note: Biến `rules` là gì?

* **Về mặt ý nghĩa:** Nó đại diện cho **cấu trúc mạng lưới** (Network Topology). Nó quy định nút nào điều khiển nút nào.
* **Về mặt luồng dữ liệu (Data Flow):**
    1.  **File .bnet** (Input thô) chứa quy tắc viết cho người đọc (VD: `A, B | !C`).
    2.  **Parser** chuyển hóa nó thành **`rules`** (VD: `'A': 'B or not C'`) để Python có thể hiểu và tính toán được.
    3.  **Analyzer** dùng `rules` để tính toán xem hệ thống sẽ chuyển sang trạng thái nào tiếp theo (Sinh ra State Transition Graph).
    4.  **Visualizer** dùng `rules` để vẽ sơ đồ quan hệ cha-con (Influence Graph).

ví dụ file .bnet gốc
```
targets, factors
GeneA,   GeneB | !GeneC
GeneB,   GeneA
GeneC,   GeneA & GeneB
```
sau khi xử lí
```
rules = {
    "GeneA": "GeneB or not GeneC",
    "GeneB": "GeneA",
    "GeneC": "GeneA and GeneB"
}
```

# Cài đặt & Chạy

1. **Clone dự án**
```bash
git clone https://github.com/elainaglazer/boolean-network-analyzer.git
cd boolean-network-analyzer
```

2. **Cài đặt thư viện**
```bash
pip install -r requirements.txt
```

3. **Chạy chương trình**
- **Chạy với Test Case có sẵn:**
```bash
  python src/main.py <test case name> <test case name #2> 
```
  hoặc 
  ```bash
  python src/main.py "path/to/your/file.bnet"
  ```
  usage:
   ```bash
  python src/main.py tc_1 tc_2
  ```

4. **Chạy Benchmark**
- **Kiểm tra độ chính xác:**
  So sánh kết quả giữa PyBoolNet và thuật toán vét cạn
  ```bash
  python src/benchmark_accuracy.py 5   # Test với mạng ngẫu nhiên 5 nodes
  python src/benchmark_accuracy.py 8   # Test với mạng ngẫu nhiên 8 nodes
  ```

- **Đo thời gian thực thi (Time):**
  Vẽ biểu đồ hiệu năng từ 1 đến 30 nodes
  ```bash
  python src/benchmark_time.py
  ```
  Kết quả biểu đồ sẽ được lưu tại `output/benchmark_execution_time.png`.
