import itertools

def generate_stg(rules, mode='synchronous'):
    """
    Tạo đồ thị chuyển đổi trạng thái (STG).
    
    Args:
        rules (dict): Dictionary chứa quy tắc Boolean.
        mode (str): 'synchronous' hoặc 'asynchronous'.
        
    Returns:
        list: Danh sách các cạnh [(state_hien_tai, state_ke_tiep), ...]
    """
    stg_edges = []
    # TODO: Implement logic tạo STG
    # 1. Liệt kê tất cả trạng thái có thể (2^n)
    # 2. Với mỗi trạng thái, áp dụng rules để tìm trạng thái tiếp theo
    
    return stg_edges

def find_attractors(stg_edges):
    """
    Tìm các attractors từ STG.
    
    Returns:
        list: Danh sách các attractor (mỗi attractor là list các state)
    """
    attractors = []
    # TODO: Implement thuật toán tìm chu trình hoặc điểm cố định
    
    return attractors
