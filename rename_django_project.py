import os
import sys


def rename_project(old_name, new_name):
    base_dir = os.getcwd()

    # Đổi tên thư mục project
    old_path = os.path.join(base_dir, old_name)
    new_path = os.path.join(base_dir, new_name)

    if not os.path.exists(old_path):
        print(f"Không tìm thấy thư mục '{old_name}'")
        return

    os.rename(old_path, new_path)
    print(f"Đã đổi tên thư mục: {old_name} -> {new_name}")

    # Danh sách các file cần cập nhật nội dung
    files_to_update = [
        'manage.py',
        os.path.join(new_name, 'wsgi.py'),
        os.path.join(new_name, 'asgi.py'),
        os.path.join(new_name, 'settings.py'),
    ]

    # Tìm và thay thế tên project cũ trong các file
    for file_path in files_to_update:
        with open(file_path, 'r') as f:
            content = f.read()

        content = content.replace(old_name, new_name)

        with open(file_path, 'w') as f:
            f.write(content)

        print(f"✔ Đã cập nhật file: {file_path}")

    print("\n✅ Đã đổi tên project thành công!")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Cách dùng: python rename_django_project.py old_name new_name")
    else:
        old_name = sys.argv[1]
        new_name = sys.argv[2]
        rename_project(old_name, new_name)
