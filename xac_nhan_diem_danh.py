import tkinter as tk
from tkinter import messagebox # Thêm thư viện để dùng Popup
from datetime import datetime    # Thêm thư viện để lấy thời gian

def xu_ly_du_lieu():
    # 1. Lấy dữ liệu
    mssv = o_nhap_ma_sv.get().strip()
    ho_ten = o_nhap_ho_ten.get().strip()
    
    # 2. Ràng buộc dữ liệu: Kiểm tra MSSV có phải là số không
    if not mssv.isdigit():
        messagebox.showerror("Lỗi đầu vào", "MSSV phải là chữ số, vui lòng nhập lại!")
        return # Dừng hàm tại đây, không xử lý tiếp bên dưới

    # 3. Kiểm tra trống thông tin
    if ho_ten != "" and mssv != "":
        # Cập nhật Label kết quả
        nhan_ket_qua.config(text=f"Chào sinh viên: {ho_ten} ({mssv})", fg="blue")
        
        # Tương tác Terminal: In kèm thời gian hiện tại
        thoi_gian = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
        print(f"[{thoi_gian}] Đã điểm danh: {ho_ten} - {mssv}")
        
        # 4. Xóa trắng các ô nhập liệu sau khi thành công
        o_nhap_ma_sv.delete(0, tk.END)
        o_nhap_ho_ten.delete(0, tk.END)
    else:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ MSSV và Họ tên!")

# --- PHẦN GIAO DIỆN GIỮ NGUYÊN ---
root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x350")
root.columnconfigure(1, weight=1)

tk.Label(root, text="Mã sinh viên:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv = tk.Entry(root)
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Họ và tên:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten = tk.Entry(root)
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

nut_xac_nhan = tk.Button(root, text="Xác nhận điểm danh", command=xu_ly_du_lieu, bg="#28a745", fg="white")
nut_xac_nhan.grid(row=2, column=0, columnspan=2, pady=10)

nhan_ket_qua = tk.Label(root, text="Chờ dữ liệu...", font=("Arial", 10, "italic"))
nhan_ket_qua.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
