Bộ phân tích Boolean Network
        




Bộ phân tích Boolean Network


1. Overview
Mục tiêu của dự án:
1. Xây dựng một tool (Boolean Network Analyzer) để hỗ trợ việc phân tích và trực quan hóa Boolean networks.
2. Kết hợp giữa học lý thuyết (hiểu các khái niệm cơ bản: influence graph, update scheme, state transition graph, attractor) và thực hành triển khai (công cụ phân tích).
3. Giúp sinh viên hiểu, biểu diễn, cập nhật và phân tích động lực học trong các mạng Boolean, từ đó áp dụng vào lĩnh vực sinh học hệ thống hoặc các hệ thống phức tạp khác.
Kiến thức đạt được sau khi hoàn thành dự án
1. Hiểu rõ các khái niệm quan trọng trong mô hình hóa Boolean networks: influence graph, synchronous/asynchronous update, state transition graph, attractors.
2. Kỹ năng xử lý và phân tích dữ liệu Boolean network từ file .bnet
3. Kỹ năng sử dụng thư viện hỗ trợ phân tích Boolean network (PyBoolNet).
4. Kinh nghiệm lập trình trực quan hóa dữ liệu bằng Python (networkx, matplotlib, graphviz, v.v.).
5. Kỹ năng làm việc nhóm, chia task (lý thuyết, code parser, visualize, tìm attractors, viết báo cáo).
2. Chức năng
Công cụ “Boolean Network Analyzer” sẽ có các chức năng chính:
1. Nhập boolean network từ file .bnet.
2. Trực quan hóa Influence Graph.
3. Xây dựng State Transition Graph.
4. Tinh các Attractors.
5. Xuất output và trực quan hóa.
3. Yêu cầu phi chức năng 
Ngoài các chức năng chính, công cụ cần đảm bảo các tiêu chí hiệu suất sau:
1. Xử lý mạng Boolean quy mô 10–20 nodes trong thời gian ngắn (dưới 2 giây cho 10–15 nodes, dưới 10 giây cho 20 nodes), đảm bảo không bị treo hoặc chậm đáng kể.
2. Input file .bnet, output ra hình ảnh + log. 
3. Kết quả hiển thị (graph, attractor) phải rõ ràng, dễ đọc và dễ hiểu.
4. Chương trình có khả năng xử lý input sai (báo lỗi hợp lý, không bị crash).
4. Công cụ dự kiến áp dụng
Ngôn ngữ lập trình chính: Python.
Các thư viện dự kiến:
* Numpy, Pandas, PyBoolNet để xử lý dữ liệu.
* Matplotlib để vẽ biểu đồ.
* GitHub để quản lý code và viết báo cáo chung. (insert link)
5. Kết quả đầu ra (Outcome – Final Report)
        Công cụ có thể đọc file .bnet, hiển thị được quan hệ giữa các nút (influence graph) và quan hệ giữa các trạng thái của toàn hệ thống (state transition graph), đồng thời tìm attractors. Chạy được với ví dụ mạng nhỏ và có kèm kết quả minh họa.
Final report sẽ có các nội dung sau: 
1. Giới thiệu: Trình bày mục tiêu dự án và các khái niệm chính của Boolean Network (influence graph, state transition graph, attractor).
2. Sơ đồ hệ thống (Diagram): Mô tả kiến trúc trong hệ thống, vẽ đồ thị và tìm attractor, cách hiện thực và trực quan hóa qua các thư viện python.
3. Đánh giá: Chạy thử với mạng nhỏ, thu được influence graph, state transition graph và attractor minh họa.
4. Kết luận và bài học rút ra.
