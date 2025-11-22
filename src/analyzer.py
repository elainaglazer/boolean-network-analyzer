import itertools

def generate_stg(rules): # <--- NHẬN BIẾN RULES Ở ĐÂY
    """
    Input: Biến 'rules' từ parser.py
    Output: List các cạnh chuyển đổi trạng thái (stg_edges)
    """
    stg_edges = []
    nodes = sorted(rules.keys()) # Lấy danh sách tên các nút
    
    # TODO: Viết logic tạo STG
    # 1. Tạo tất cả trạng thái nhị phân (000, 001, ..., 111)
    # 2. Với mỗi trạng thái, dùng eval() trên các công thức trong 'rules'
    # 3. Lưu kết quả vào stg_edges. VD: stg_edges.append(('000', '001'))
    
    return stg_edges

def find_attractors(stg_edges):
    """
    Input: stg_edges từ hàm trên
    Output: List các attractor
    """
    attractors = []
    # TODO: Tìm chu trình hoặc điểm cố định
    return attractors
