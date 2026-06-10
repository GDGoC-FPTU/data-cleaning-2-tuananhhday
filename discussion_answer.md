# Câu hỏi thảo luận

## Vì sao dùng ETL để che PII thay vì ELT?

Chúng ta dùng ETL vì dữ liệu nhạy cảm nên được làm sạch trước khi lưu trữ.

Nếu dùng ELT, dữ liệu thô sẽ được đưa vào nơi lưu trữ trước. Điều đó có nghĩa
là tên thật và email thật đã tồn tại trong database, vector store hoặc data
warehouse trước khi được làm sạch. Việc này tạo ra rủi ro về quyền riêng tư và
bảo mật dữ liệu.

Với ETL, chúng ta xóa tên và che email trước khi lưu trữ, nên hệ thống AI chỉ
nhận dữ liệu đã được làm sạch.
