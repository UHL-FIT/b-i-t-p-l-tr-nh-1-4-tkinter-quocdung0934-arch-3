import tkinter as tk

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x250")

# 1. Tạo các thành phần (nhưng chưa hiện lên)
nhan_ma_sv = tk.Label(root, text="Mã sinh viên:")
o_nhap_ma_sv = tk.Entry(root)

nhan_ho_ten = tk.Label(root, text="Họ và tên:")
o_nhap_ho_ten = tk.Entry(root)

# Hàng 0 với căn lề trái (sticky="w") và khoảng cách (padx, pady)
nhan_ma_sv.grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10)

# Hàng 1
nhan_ho_ten.grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10)

root.columnconfigure(0, weight=1)
root.mainloop()



