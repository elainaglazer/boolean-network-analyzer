import os

def load_bnet(file_path):
    """
    Input: Đường dẫn file .bnet
    Output: Biến 'rules' (Dictionary)
    """
    rules = {} # <--- Khởi tạo biến rules

    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return rules

    # TODO: Viết logic đọc file ở đây
    # 1. Mở file, đọc từng dòng
    # 2. Tách tên và công thức (bỏ qua dòng targets, factors)
    # 3. Replace: '!' -> 'not ', '&' -> ' and ', '|' -> ' or '
    
    # Ví dụ giả (Sau khi parse xong sẽ được như này):
    # rules['A'] = 'B or not C'
    
    return rules # <--- TRẢ VỀ BIẾN RULES Ở ĐÂY
