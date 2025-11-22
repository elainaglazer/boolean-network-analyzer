# Bộ phân tích Boolean network

Công cụ hỗ trợ phân tích và trực quan hóa **Boolean networks**.

- Đọc Boolean network từ file `.bnet`.
- Hiển thị Influence Graph.
- Xây dựng State Transition Graph.
- Tìm và hiển thị các Attractors.

# Hiệu suất (phi chức năng)
- Xử lý mạng 10–15 nodes: < 2 giây.
- Xử lý mạng 20 nodes: < 10 giây.
- Báo lỗi nếu input không hợp lệ.

# Công cụ sử dụng
- Python, Numpy, Pandas
- PyBoolNet
- Matplotlib
- GitHub để quản lý mã nguồn

src/
│
├── input_data/             # Chứa các file mẫu .bnet để test
│   ├── example1.bnet
│   └── ...
│
├── parser.py               # Đọc và xử lý file .bnet
├── analyzer.py             # Xử lý logic: Tính toán trạng thái, tìm Attractors
├── visualizer.py           # Vẽ đồ thị: Influence Graph, STG
├── main.py                 # Chương trình chính: Gọi các hàm từ các file trên
└── utils.py(?)             # Các hàm phụ trợ (them nếu cần)

Chia việc:
A: Xử lý Logic (Backend)
Phụ trách các file: parser.py, analyzer.py

    [ ] Task 1 (parser.py): Viết hàm đọc file .bnet. Yêu cầu: Trả về dictionary quy tắc (rules). Xử lý lỗi nếu file sai định dạng.

    [ ] Task 2 (analyzer.py): Viết hàm tạo STG (State Transition Graph). Đầu vào là rules, đầu ra là danh sách các cạnh (edges) giữa các trạng thái.

    [ ] Task 3 (analyzer.py): Viết hàm tìm Attractors từ STG đã tạo.

B: Trực quan hóa & Tích hợp (Frontend/Main)
Phụ trách các file: visualizer.py, main.py

    [ ] Task 1 (visualizer.py): Dùng networkx và matplotlib để vẽ Influence Graph từ rules.

    [ ] Task 2 (visualizer.py): Vẽ State Transition Graph (STG) từ dữ liệu nodes/edges mà bên Logic cung cấp.

    [ ] Task 3 (main.py): Viết luồng chạy chính: Nhập file -> Gọi Parser -> Gọi Analyzer -> Gọi Visualizer -> Xuất kết quả.

    [ ] Task 4: Đảm bảo chương trình chạy dưới 10s với mạng 20 nodes.



Clone dự án
```bash
# 1. Clone dự án
git clone [https://github.com/elainaglazer/boolean-network-analyzer.git](https://github.com/elainaglazer/boolean-network-analyzer.git)
cd boolean-network-analyzer

# 2. Cài thư viện cần thiết
pip install numpy pandas matplotlib networkx pyboolnet

# 3. Chạy chương trình
python src/main.py
