import array as arr
import numpy as np
import io, re
import matplotlib.pyplot as plt
import  math

from numpy.random import random


# def loop_char(name):
#     for c in name:
#         print(c)
#
# def print_odd():
#     sum = 0
#     totalSum = 0
#     a = int(input(f"Nhập khoảng cách đầu: "))
#     b = int(input(f"Nhập khoảng cách cuối: "))
#     for x in range(a, b):
#         totalSum +=x
#         if x % 2 != 0:
#             print(x)
#             sum+=x
#     print(f'Tổng các số lẻ là: {sum}')
#     print(f'Tổng các số là: {totalSum}')
#
#     n = 6
#     i = n * (n+1) // 2
#     print(f"Tổng các số từ 1 đến 6 là: {i}")


# def array():
#     a = int(input(f'Nhập giá trị của "a": '))
#     b = int(input(f'Nhập giá trị của "b": '))
#     c = int(input(f'Nhập giá trị của "c": '))
#     d = int(input(f'Nhập giá trị của "d": '))
#     n = [
#         {
#             "a": a,
#             "b": b,
#             "c": c,
#             "d": d
#         }
#     ]
#     for x in n:
#         print(f"Giá trị của mảng: {x}")
#
#     for x in n:
#         print(f"Giá trị value: {x.keys()}")
#
#     for x in n:
#         print(f"Giá trị value: {x.values()}")

# def courses():
#     courses = [131, 141, 142, 212]
#     names =["Maths","Physics","Chem","Bio"]
#     zipped = zip(courses,names)
#     for i in zipped:
#         print(i)


# def findVowels():
#     vowels = "{u,e,o,a,i}"
#     charr = "jabbawocky"
#     sum = 0
#     for x in charr:
#         if x.lower() not in vowels:
#             sum +=1
#     print(f"Các từ phụ âm là: {sum}")
#
# def findVowels2():
#     vowels = "{u,e,o,a,i}"
#     charr = "jabbawocky"
#     sum = 0
#     for x in charr:
#         if x.lower() not in vowels:
#             continue
#     print(f"Các từ phụ âm dùng continue là: {sum}")


# def english():
#     print("Chào mừng bạn đến lớp học Tiếng Anh")
#     choice = {
#         1 :"Tìm kiếm phụ âm cách trực tiếp không dùng continue",
#         2 :"Tìm kiếm phụ âm bằng continue",
#         3 :"Thoát!!!"
#     }
#     for i in choice.keys():
#         print(f'{i} - {choice[i]}')
#     print("-----------------------------------------------------------")
#     pls = int(input(f"Làm ơn chọn câu: "))
#     c = choice.get(pls ,-1)
#     while c == -1:
#         print(f"Chọn sai làm ơn chọn lại dùm!!!\n")
#         english()
#     else:
#         print(f"Bạn đã chọn câu: {c}")
#         if c == 1:
#             findVowels()
#         else:
#             if c == 2:
#                 findVowels2()
#         if c == 3:
#             print("3")
#
# def findVowels():
#     vowels = "{u,e,o,a,i}"
#     charr = "jabbawocky"
#     sum = 0
#     for x in charr:
#         if x.lower() not in vowels:
#             sum + =1
#     print(f"Các từ phụ âm là: {sum}")
#
# def findVowels2():
#     vowels = "{u,e,o,a,i}"
#     charr = "jabbawocky"
#     summ = 0
#     for x in charr:
#         if x.lower() not in vowels:
#             continue
#         summ + =1
#     print(f"Các từ phụ âm dùng continue là: {summ}")

def bai7():
    print(f'a từ -2 <= a < 3')
    while True:
        n = int(input(f"Nhập giá trị a: "))
        if -2 <= n < 3:
            try:
                kq = 10 / n
                print(f'Kết quả của 10 / {n} = {kq}')
            except ZeroDivisionError:
                print("Không thể chia hết cho 0")
            break
        else:
            print("Nhập sai!!!!")


def lambDa():
    ages = [23, 10, 80]
    names = ["Hoa", "Lam", "Nam"]
    zipped = zip(ages, names)
    print(sorted(zipped, key=lambda x: x[0]))


def docFile():
    f = open("dssinhvien", mode='r', encoding='utf-8')
    f.close()
    with open('dssinhvien', 'r', encoding='utf-8') as f:
        array = f.readlines()
        for item in array:
            print(item)


def calcTotal():
    a = int(input("Nhập giá trị a: "))
    b = int(input("Nhập giá trị b: "))
    print(f"Tổng của {a} + {b} = {a + b}")


def maTrix():
    ar = np.zeros((3, 3), dtype=int)  # khởi tạo ma trận 3x3 chứa toàn số 0
    arr2 = np.full((3, 3), 3, dtype=int)  # khởi tạo ma trận 3x3 chứa toàn số 3
    arr3 = np.random.randint(-10, 10, size=(3, 3))  #khởi tạo ma trận 3x3 chưa toàn số 0 và sử dụng random
    arr4 = np.eye(3,3, dtype=int) #Ma trận đơn vị với đường chéo từ góc trái đến góc phải dưới bằng 1
    arr5 = np.random.randint(1, 10, size=(3, 3))  #khởi tạo ma trận 3x3 chưa toàn số 0 và sử dụng random
    # for i in range(3):
    #     for j in range(3):
    #         ar[i][j] = int(input(f"Nhập giá trị của ma trận ar[{i}][{j}]: "))
    #
    # for a in range(3):
    #     for b in range(3):
    #         arr2[a][b] = arr2[a][b]
    #
    # vec = np.zeros(4)
    # for v in range(4):
    #     vec[v] = int(input(f'Nhập giá trị vector vector[{v}]: '))

    #Tính đường chéo theo For
    sum = 0
    for i, row in enumerate(arr5):
        for j, col in enumerate(row):
            if i == j:
                sum += arr5[i][j]


    for i in enumerate(ar):
        ar = np.diag([1, 2, 3])


    #Tính định thức
    dinhthuc = np.linalg.det(arr3)




    # print("Vector sau khi nhập\n")
    # print("Rank của vector:", np.ndim(vec))
    # print("Hình dạng của vector:", vec.shape)
    # print(vec)
    # print("-----------------------")
    # print("Ma trận sau khi nhập:\n")
    # print("Rank của ma trận:", np.ndim(ar))
    # print("Hình dạng của ma trận:", ar.shape)
    # print(ar)
    # print("-----------------------")
    # print('Ma trận sau khi phần tử cộng thêm 3\n')
    # print(arr2 + ar)
    # print("-----------------------")
    # print("Ma trận chuyển vị")
    # print(np.transpose(ar))
    # print("Vector chuyển vị")
    # print(np.transpose(vec))
    # print("-----------------------")
    # print(f'Ma trận ngẫu nhiên')
    # print(arr3)
    # print("-----------------------")
    # print(f'Ma trận đơn vị là\n')
    # print(arr4)
    # print("-----------------------")
    # print(arr5)
    # print(f"Tính vết của ma trận đường chéo là: {np.trace(arr5)}")
    # print("-----------------------")
    # print(arr5)
    # print(f'Tổng vết của ma trận đường chéo là: {sum}')
    # print("-----------------------")
    # print(f"Ma trận đường chéo 1,2,3 là\n")
    # print(ar)
    print("-----------------------")
    print(arr3)
    print(f'Tính định thức ma trận: {dinhthuc}')



def norm():
    x = [2, 7]
    dinhMuc = np.linalg.norm(x)
    print(f"Định mức của vector x là: {dinhMuc}")

    chuanHoa = x / dinhMuc  # chuẩn hóa là = 1
    print(f"Vector chuẩn hóa của x: {chuanHoa}")


def calc():
    a = np.array([10, 15])
    b = np.array([8, 2])
    c = np.array([1, 2, 3])

    tichvohuong = (a[0] * b[0]) + (a[1] * b[1])


    #bài16
    x = np.linspace(0,32,5)
    print(f'Bài 16: {x}')

    # print(f"Tích vô hướng của a và b là: {tichvohuong}")
    #
    # print(f'a + b = {a + b},'
    #       f'a - b = {a - b},'
    #       f'a - c = {a - c[:2]}')


def handleArr():
    a = np.array([[2, 4, 9], [3, 6, 7]])
    # n = int(input("Nhập giá trị cần tìm trong mảng: "))
    # for i, row in enumerate(a):
    #     for x, value in enumerate(row):
    #         if value == n:
    #             print(f'So {n} cần tìm nằm ở vị trí hàng {i} và cột {x}')
    #
    # print(f"Mức rank của mảng a là : {np.ndim(a)},\n"
    #       f"Hình dạng của mảng a là: {np.shape(a)}")
    # m = int(input("Nhập giá trị cột: "))
    # for i, row in enumerate(a):
    #     for j, col in enumerate(row):
    #         if j == m:
    #             print(col)


    #Nối ma trận theo cột
    a1 = [1, -2, -5]
    a2 = [2, 5, 6]
    print(f"Ma trận sau khi xử lý\n")
    print(np.column_stack((a1,a2)))



def DoThiBinhPhuong():
    # y = np.array([-5,6], dtype=int)
    # y1 = np.array([-5,10], dtype=int)
    # y_binhphuong = y**2
    # y1_binhphuong = y1**2
    # #Vẽ đồ thị của bình phương y
    # plt.plot(y, y_binhphuong, y1, y1_binhphuong, marker='o', linestyle='-')
    # plt.title("Bình phương của giá trị y, y1")
    # plt.xlabel('y,y1')
    # plt.ylabel('Bình phương của y, y1')
    # plt.grid(True)
    # plt.show()


    x = np.linspace(-5,5, 50)
    x_binhphuong = x**2
    #Vẽ đồ thị của bình phương x
    plt.plot(x, x_binhphuong, marker='o', linestyle='-')
    plt.title("Bình phuong của giá trị x")
    plt.xlabel('x')
    plt.ylabel('Bình phương của x')
    plt.grid(True)
    plt.show()


def DoThi():
    # y = np.linspace(-5,5, 10)
    # y_exp = np.exp(y)
    # #vẽ đồ thị cuủa bình phương y
    # plt.plot(y, y_exp, marker='o', linestyle='-')
    # plt.title("Hàm mũ của giá trị y")
    # plt.xlabel('y')
    # plt.ylabel('Hàm mũ của y')
    # plt.grid(True)
    # plt.show()

    # y = np.linspace(0.1, 5, 10)
    # y_exp = np.log(y)
    # #vẽ đồ thị cuủa bình phương y
    # plt.plot(y, y_exp, marker='o', linestyle='-')
    # plt.title("Hàm log của giá trị y")
    # plt.xlabel('y')
    # plt.ylabel('Hàm log của y')
    # plt.grid(True)
    # plt.show()


    #Bài 20
    y = np.linspace(0.1, 5, 50)

    y1= np.exp(y)
    y2 = np.exp(2*y)
    y3 = np.log(y)
    y4 = np.log(2*y)

    #Vẽ 2 đồ thị trên cùng 1 đồ thị
    plt.figure(figsize=(10,5))

    plt.subplot(1 ,2, 1) #dòng 1, cột 2, đồ thị 1
    plt.plot(y, y1, label='y1 = exp(y)')
    plt.plot(y, y2, label='y2 = exp(2*y)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Hai đồ thị y1 = exp(y) và y2 = exp(2*y)")
    plt.legend()


    #Vẽ 2 đồ thị trong 2 đồ thị con
    plt.subplot(1, 2, 2) #dòng 1, cột 2, đồ thị 2
    plt.plot(y, y3, label='y3 = log(y)')
    plt.plot(y, y4, label='y4 = log(2*y)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Hai đồ thị y3 = log(y) và y4 = log(2*y)')
    plt.legend()

    #Hiển thị

    plt.tight_layout()
    plt.show()






if __name__ == "__main__":
    # loop_char("abc")
    print("-----------------------------------------------")
    # print_odd()
    print("-----------------------------------------------")
    # array()
    print("-----------------------------------------------")
    # courses()
    print("-----------------------------------------------")
    # english()
    # findVowels()
    # findVowels2()
    print("-----------------------------------------------")
    # bai7()
    print("-----------------------------------------------")
    # lambDa()
    print("-----------------------------------------------")
    # docFile()
    print("-----------------------------------------------")
    # calcTotal()
    print("-----------------------------------------------")
    # maTrix()
    print("-----------------------------------------------")
    # norm()
    print("-----------------------------------------------")
    # calc()
    print("-----------------------------------------------")
    # handleArr()
    print("-----------------------------------------------")
    # DoThiBinhPhuong()
    print("-----------------------------------------------")
    DoThi()

