import os

def load_bnet(file_path):
    """
    Đọc file .bnet và trả về một dictionary chứa các quy tắc Boolean.
    
    Args:
        file_path (str): Đường dẫn đến file .bnet
        
    Returns:
        dict: Dạng {'GeneA': 'GeneB or GeneC', 'GeneB': '!GeneA'}
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")
    
    rules = {}
    # TODO: Implement logic đọc file ở đây
    # 1. Mở file
    # 2. Đọc từng dòng, bỏ qua comment
    # 3. Tách tên biến và hàm logic
    
    return rules
