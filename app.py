# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
"""Thêm một công việc mới vào danh sách."""
tasks.append(task_name)
 print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
print("Chào mừng đến với ứng dụng To-Do List!")
add_task("Học bài Git và GitHub")
add_task("Làm bài tập thực hành ở nhà")
def show_tasks():
    """Hien thi tat ca cong viec hien co trong danh sach."""
    print("\nDanh sach cong viec hien tai:")
    if not tasks:
	print( "chua co cong viec nao!")
    else:
	for i, task in enumerate( tasks, start=1):
	    print(f"{i}. {tasks}")
if __name__ == "__main__ ":
    print("chao mung ban den voi ung dung To-Do List!")
    add_task("Hoc baI Git va GitHub")
    add_task("Lam bai tap thuc hanh o nha")
    show_tasks()
# Danh sách để lưu các công việc
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")

def view_tasks():
    """Hiển thị tất cả công việc trong danh sách."""
    if not tasks:
        print("Danh sách công việc trống.")
        return

    print("\n--- Danh sách công việc ---")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
    print("---------------------------\n")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

    view_tasks() # Thêm lệnh gọi hàm mới