# Este programa sirve para ...
def programa_1():
    max_num = input("Introduce un número: ")
    sum_nums = max_num
    for cont in range(9):
        num = input("Introduce otro número: ")
        sum_nums =sum_nums+ num
    if num > max_num:
        max_num = num
    print("The largest number is",max_num)
    print("The average is",sum_nums )
    
programa_1()
