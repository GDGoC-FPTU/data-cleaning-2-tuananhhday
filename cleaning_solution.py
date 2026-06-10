import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def mask_email(email):
    """
    Che địa chỉ email bằng cách giữ ký tự đầu tiên của username
    và thêm '***' trước phần domain.
    Ví dụ: vana@gmail.com -> v***@gmail.com
    """
    if not email or '@' not in email:
        return email
    parts = email.split('@')
    return parts[0][0] + "***@" + parts[1]

def clean_data(input_file, output_file):
    # Đọc dữ liệu thô từ file JSON
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {input_file}.")
        return
    except json.JSONDecodeError:
        print(f"Lỗi: Không thể đọc dữ liệu JSON từ {input_file}.")
        return

    seen_ids = set()
    sanitized_data = []

    for item in data:
        # 1. Xóa bản ghi trùng: mỗi id chỉ được xuất hiện một lần
        item_id = item.get('id')
        if item_id in seen_ids:
            continue
        
        # 2. Kiểm tra outlier: loại bỏ sản phẩm có giá lớn hơn 5,000
        price = item.get('price')
        if price is not None and price > 5000:
            continue
            
        # 3. Kiểm tra dữ liệu không hợp lệ: loại bỏ sản phẩm có giá âm
        if price is not None and price < 0:
            continue

        # 4. Che thông tin cá nhân: xóa tên và che email
        
        # Xóa trường 'name' khỏi bản ghi
        if 'name' in item:
            del item['name']
            
        # Che trường 'email' bằng hàm mask_email
        if 'email' in item:
            item['email'] = mask_email(item['email'])
            
        sanitized_data.append(item)
        seen_ids.add(item_id)

    # Lưu dữ liệu đã làm sạch ra file JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sanitized_data, f, indent=4)
    
    print(f"Đã làm sạch dữ liệu thành công. Kết quả được lưu vào {output_file}")
    print(f"Số bản ghi ban đầu: {len(data)}")
    print(f"Số bản ghi sau khi làm sạch: {len(sanitized_data)}")

if __name__ == "__main__":
    INPUT_PATH = "toxic_sample.json"
    OUTPUT_PATH = "sanitized_sample.json"
    clean_data(INPUT_PATH, OUTPUT_PATH)
