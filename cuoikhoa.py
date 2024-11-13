"""
Xây dựng chương trình quản lý người dùng và ghi lại nhật ký hoạt động
Mục tiêu:
Viết một chương trình Python có chức năng quản lý thông tin người dùng bao gồm:

Thêm người dùng mới.
Cập nhật thông tin người dùng.
Xóa người dùng.
Tìm kiếm người dùng.
Ngoài ra, chương trình sẽ ghi lại tất cả các thao tác (hoạt động) vào một file nhật ký activity.txt,
Nếu có lỗi thì ghi vào file error.txt

Nhập tên, tuổi và email của người dùng.
Ghi lại thông tin vào file users.txt.
Ghi nhật ký hoạt động vào file activity.txt.

Gợi ý

+ Tạo ra 1 hàm ghi vào file activity.text
+ tạo ra 1 hàm ghi vào file error.text

+ tao 4 hàm tương ứng CRUD với 1 user
    + Create -> lưu vào file list_user.txt
    + Read -> doc tu file list_user.txt
    + Update -> cap nhật user trong list_user.txt
    + Delete -> xóa user trong list_user.txt
Ghi vào file nhật ký activity.txt
nếu có lỗi sử dụng try except để ghi lỗi vào error.txt

Mẫu file list_user.txt:
Tên: Tuấn Phát - Tuổi: 15 - Email: phatgpt@gmail.com
Tên: Đức Khang - Tuôi: 15 - Email: khang@gmail.com
Tên: Trường - Tuổi: 15 - Email: truong@gmail.com
#thêm user

Mẫu file activity.txt:
[2024-11-06 12:00:00] - bắt đầu tạo mới user
[2024-11-06 12:05:00] - Tạo mới user thành công

Mẫu file error.txt
[2024-11-06 12:00:00] - Lỗi khi cập nhật user
[2024-11-06 12:05:00] - Lỗi khi xoá user
"""