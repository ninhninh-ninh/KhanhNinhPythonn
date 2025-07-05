import json
import os


def doc_file(ten_file):
    """Đọc dữ liệu từ file JSON, nếu không có thì khởi tạo dữ liệu trống."""
    if not os.path.exists(ten_file):
        return {"mon_an": {}, "thuc_don": {}}
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            du_lieu = json.load(f)
            
            if "mon_an" not in du_lieu:
                du_lieu["mon_an"] = {}
            if "thuc_don" not in du_lieu:
                du_lieu["thuc_don"] = {}
            return du_lieu
    except:
        return {"mon_an": {}, "thuc_don": {}}


def ghi_file(ten_file, du_lieu):
    """Ghi dữ liệu vào file JSON."""
    with open(ten_file, 'w', encoding='utf-8') as f:
        json.dump(du_lieu, f, indent=4, ensure_ascii=False)


def them_mon_an(data):
    """Thêm một món ăn mới."""
    print("\n THÊM MÓN ĂN")
    ma = input("Mã món (VD: MA001): ").strip().upper()
    if ma in data["mon_an"]:
        print(" Món đã tồn tại.")
        return
    ten = input("Tên món: ").strip()
    calo = int(input("Lượng calo: "))
    loai = input("Loại món (Đạm/Tinh bột/Rau/...): ").strip()
    data["mon_an"][ma] = {"Ten": ten, "Calo": calo, "Loai": loai}
    print(" Đã thêm món ăn.")

def xem_mon_an(data):
    """Hiển thị danh sách món ăn."""
    print("\n DANH SÁCH MÓN ĂN")
    if not data["mon_an"]:
        print("Chưa có món ăn nào.")
        return
    for ma, mon in data["mon_an"].items():
        print(f"- {ma}: {mon['Ten']} | {mon['Calo']} calo | Loại: {mon['Loai']}")

def sua_mon_an(data):
    """Sửa thông tin món ăn."""
    ma = input("Mã món cần sửa: ").strip().upper()
    if ma not in data["mon_an"]:
        print(" Không tìm thấy món.")
        return
    ten = input("Tên mới: ").strip()
    calo = int(input("Calo mới: "))
    loai = input("Loại mới: ").strip()
    data["mon_an"][ma] = {"Ten": ten, "Calo": calo, "Loai": loai}
    print(" Đã sửa món.")

def xoa_mon_an(data):
    """Xoá một món ăn."""
    ma = input("Mã món cần xoá: ").strip().upper()
    if ma in data["mon_an"]:
        del data["mon_an"][ma]
        print(" Đã xoá món.")
    else:
        print(" Không tìm thấy món.")

def tim_mon_theo_ten(data):
    """Tìm món theo tên."""
    tu_khoa = input("Nhập tên món cần tìm: ").strip().lower()
    ket_qua = [mon for mon in data["mon_an"].values() if tu_khoa in mon["Ten"].lower()]
    if not ket_qua:
        print(" Không tìm thấy món nào.")
    else:
        for mon in ket_qua:
            print(f" {mon['Ten']} | {mon['Calo']} calo | {mon['Loai']}")

def tim_mon_theo_loai(data):
    """Tìm món theo loại."""
    loai = input("Nhập loại món: ").strip().lower()
    ket_qua = [mon for mon in data["mon_an"].values() if loai == mon["Loai"].lower()]
    if not ket_qua:
        print(" Không có món nào thuộc loại này.")
    else:
        for mon in ket_qua:
            print(f" {mon['Ten']} | {mon['Calo']} calo")

def mon_it_calo_nhat(data):
    """Tìm món ăn có calo thấp nhất."""
    if not data["mon_an"]:
        print(" Không có món.")
        return
    mon_nhe = min(data["mon_an"].values(), key=lambda m: m["Calo"])
    print(f" Món ít calo nhất: {mon_nhe['Ten']} ({mon_nhe['Calo']} calo)")


def them_thuc_don(data):
    """Thêm một thực đơn mới."""
    print("\n THÊM THỰC ĐƠN")
    ma = input("Mã thực đơn: ").strip().upper()
    if ma in data["thuc_don"]:
        print(" Thực đơn đã tồn tại.")
        return
    ten = input("Tên thực đơn: ").strip()
    danh_sach = input("Nhập danh sách mã món (cách nhau bằng dấu phẩy): ").split(',')
    danh_sach = [m.strip().upper() for m in danh_sach]
    tong_calo = sum(data["mon_an"].get(m, {"Calo": 0})["Calo"] for m in danh_sach)
    data["thuc_don"][ma] = {"Ten_thuc_don": ten, "Danh_sach_mon": danh_sach, "Tong_calo": tong_calo}
    print(" Đã thêm thực đơn.")

def xem_thuc_don(data):
    """Xem tất cả thực đơn."""
    print("\n DANH SÁCH THỰC ĐƠN")
    for ma, td in data["thuc_don"].items():
        print(f"{ma}: {td['Ten_thuc_don']} ({td['Tong_calo']} calo)")
        for ma_mon in td["Danh_sach_mon"]:
            mon = data["mon_an"].get(ma_mon, {"Ten": "Không rõ", "Calo": 0})
            print(f"   • {ma_mon} - {mon['Ten']} ({mon['Calo']} calo)")

def sua_thuc_don(data):
    """Sửa thông tin thực đơn."""
    ma = input("Mã thực đơn cần sửa: ").strip().upper()
    if ma not in data["thuc_don"]:
        print(" Không tìm thấy thực đơn.")
        return
    ten = input("Tên mới: ").strip()
    danh_sach = input("Danh sách món mới: ").split(',')
    danh_sach = [m.strip().upper() for m in danh_sach]
    tong_calo = sum(data["mon_an"].get(m, {"Calo": 0})["Calo"] for m in danh_sach)
    data["thuc_don"][ma] = {"Ten_thuc_don": ten, "Danh_sach_mon": danh_sach, "Tong_calo": tong_calo}
    print(" Đã sửa thực đơn.")

def xoa_thuc_don(data):
    """Xoá một thực đơn."""
    ma = input("Mã thực đơn cần xoá: ").strip().upper()
    if ma in data["thuc_don"]:
        del data["thuc_don"][ma]
        print(" Đã xoá thực đơn.")
    else:
        print(" Không tìm thấy.")

def tim_thuc_don_theo_ten(data):
    """Tìm thực đơn theo tên."""
    tu_khoa = input("Nhập tên thực đơn: ").strip().lower()
    for td in data["thuc_don"].values():
        if tu_khoa in td["Ten_thuc_don"].lower():
            print(f" {td['Ten_thuc_don']} ({td['Tong_calo']} calo)")

def xem_tong_calo(data):
    """Xem tổng calo của một thực đơn."""
    ma = input("Mã thực đơn: ").strip().upper()
    if ma in data["thuc_don"]:
        print(f"Tổng calo: {data['thuc_don'][ma]['Tong_calo']} calo")
    else:
        print(" Không tìm thấy.")

def mon_calo_cao(data):
    """Hiển thị món có calo lớn hơn 500"""
    print("\n📍 MÓN ĂN NHIỀU CALO (>500)")
    cao = [mon for mon in data["mon_an"].values() if mon["Calo"] > 500]
    if not cao:
        print("Không có món nào calo cao.")
    else:
        for mon in cao:
            print(f"🍖 {mon['Ten']} - {mon['Calo']} calo | {mon['Loai']}")


def thong_ke_loai_mon(data):
    """Thống kê số lượng món theo từng loại"""
    print("\n📊 THỐNG KÊ MÓN ĂN THEO LOẠI")
    thong_ke = {}
    for mon in data["mon_an"].values():
        loai = mon["Loai"]
        thong_ke[loai] = thong_ke.get(loai, 0) + 1
    for loai, so_luong in thong_ke.items():
        print(f"• {loai}: {so_luong} món")


def thuc_don_nhieu_calo(data):
    """Hiển thị thực đơn có nhiều calo nhất"""
    if not data["thuc_don"]:
        print("Không có thực đơn.")
        return
    td_max = max(data["thuc_don"].values(), key=lambda td: td["Tong_calo"])
    print(f"\n🔥 Thực đơn nhiều calo nhất: {td_max['Ten_thuc_don']} ({td_max['Tong_calo']} calo)")
    for ma in td_max["Danh_sach_mon"]:
        mon = data["mon_an"].get(ma, {"Ten": "Không rõ", "Calo": 0})
        print(f"   • {ma} - {mon['Ten']} ({mon['Calo']} calo)")


def dem_tong_mon_an(data):
    """Đếm tổng số lượng món ăn hiện có"""
    print(f"\n🧮 Tổng số món ăn đã lưu: {len(data['mon_an'])} món")


def xuat_file_txt(data):
    """Xuất dữ liệu ra file txt dễ đọc"""
    with open("xuat_du_lieu.txt", "w", encoding="utf-8") as f:
        f.write("====== DANH SÁCH MÓN ĂN ======\n")
        for ma, mon in data["mon_an"].items():
            f.write(f"{ma}: {mon['Ten']} | {mon['Calo']} calo | {mon['Loai']}\n")

        f.write("\n====== DANH SÁCH THỰC ĐƠN ======\n")
        for ma, td in data["thuc_don"].items():
            f.write(f"{ma}: {td['Ten_thuc_don']} ({td['Tong_calo']} calo)\n")
            for ma_mon in td["Danh_sach_mon"]:
                mon = data["mon_an"].get(ma_mon, {"Ten": "Không rõ", "Calo": 0})
                f.write(f"   • {ma_mon} - {mon['Ten']} ({mon['Calo']} calo)\n")

    print("📄 Đã xuất ra file 'xuat_du_lieu.txt'")


def menu():
    ten_file = "du_lieu.json"
    data = doc_file(ten_file)

    while True:
        print("1. Thêm món ăn")
        print("2. Xem danh sách món ăn")
        print("3. Sửa món ăn")
        print("4. Xoá món ăn")
        print("5. Tìm món ăn theo tên")
        print("6. Tìm món ăn theo loại")
        print("7. Món ăn ít calo nhất")
        print("8. Thêm thực đơn")
        print("9. Xem danh sách thực đơn")
        print("10. Sửa thực đơn")
        print("11. Xoá thực đơn")
        print("12. Tìm thực đơn theo tên")
        print("13. Xem tổng calo thực đơn")
        print("14. Lưu dữ liệu")
        print("15. Thoát")
        print("16. Món ăn nhiều calo (>500)")             
        print("17. Thống kê món ăn theo loại")            
        print("18. Thực đơn nhiều calo nhất")            
        print("19. Đếm tổng số món ăn")                 
        print("20. Xuất ra file TXT")                     

        chon = input(" Chọn chức năng (1-20): ").strip()

        if chon == '1': them_mon_an(data)
        elif chon == '2': xem_mon_an(data)
        elif chon == '3': sua_mon_an(data)
        elif chon == '4': xoa_mon_an(data)
        elif chon == '5': tim_mon_theo_ten(data)
        elif chon == '6': tim_mon_theo_loai(data)
        elif chon == '7': mon_it_calo_nhat(data)
        elif chon == '8': them_thuc_don(data)
        elif chon == '9': xem_thuc_don(data)
        elif chon == '10': sua_thuc_don(data)
        elif chon == '11': xoa_thuc_don(data)
        elif chon == '12': tim_thuc_don_theo_ten(data)
        elif chon == '13': xem_tong_calo(data)
        elif chon == '14': ghi_file(ten_file, data); print("💾 Đã lưu.")
        elif chon == '16': mon_calo_cao(data)
        elif chon == '17': thong_ke_loai_mon(data)
        elif chon == '18': thuc_don_nhieu_calo(data)
        elif chon == '19': dem_tong_mon_an(data)
        elif chon == '20': xuat_file_txt(data)
        elif chon == '15': 
            ghi_file(ten_file, data)
            print(" Đã thoát chương trình.")
            break
        else:
            print(" Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    menu()