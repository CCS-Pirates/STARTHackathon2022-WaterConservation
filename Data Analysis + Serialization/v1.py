import random, os
'''
      jan  feb   mar   apr   may   jun   jul   aug  sep  octo   nov   dec
'''

new_arr = []

def yr1():
    mr = [0, 0.06, 0.09, 0.07, 0.08, 0, 0, 0.08, 0.09, 0, 0.04, 0.15]
    res_arr1 = []
    cubic_mt_per_yr = float(input("Year 1: "))

    for i in range(4):
        num = round(random.uniform(0.04,0.08), 2)
        mr.pop(0)
        mr.pop(5)
        mr.pop(6)
        #mr.pop(8)
        #mr.append(0.15)
    
        mr.insert(0, num)
        mr.insert(5, num)
        mr.insert(6, num)
        #mr.insert(8, num)
    
    mr = [i for i in mr if i != 0]
    #mr.append(0.15)
    _abs = abs(sum(mr)-1.0)
    print(mr)
    mr.insert(8,_abs)
    print(sum(mr))
    
    for i in mr:
        res = i*cubic_mt_per_yr
    #    print(res)
        res_arr1.append(res)
    print("---------------------")
    print("\tYEAR 1")
    print("---------------------")
    print(res_arr1)
    print("-------------------\n")    

def yr2():
    mr = [0, 0.06, 0.09, 0.07, 0.08, 0, 0, 0.08, 0.09, 0, 0.04, 0.15]
    res_arr2 = []
    cubic_mt_per_yr = float(input("Year 2: "))

    for i in range(4):
        num = round(random.uniform(0.04,0.08), 2)
        mr.pop(0)
        mr.pop(5)
        mr.pop(6)
        #mr.pop(8)
        #mr.append(0.15)
    
        mr.insert(0, num)
        mr.insert(5, num)
        mr.insert(6, num)
        #mr.insert(8, num)
    
    mr = [i for i in mr if i != 0]
    #mr.append(0.15)
    _abs = abs(sum(mr)-1.0)
    print(mr)
    mr.insert(8,_abs)
    print(sum(mr))
    
    for i in mr:
        res = i*cubic_mt_per_yr
    #    print(res)
        res_arr2.append(res)

    print("---------------------")
    print("\tYEAR 2")
    print("---------------------")
    print(res_arr2)
    print("-------------------\n")

def yr3():
    mr = [0, 0.06, 0.09, 0.07, 0.08, 0, 0, 0.08, 0.09, 0, 0.04, 0.15]
    res_arr3 = []
    cubic_mt_per_yr = float(input("Year 3: "))

    for i in range(4):
        num = round(random.uniform(0.04,0.08), 2)
        mr.pop(0)
        mr.pop(5)
        mr.pop(6)
        #mr.pop(8)
        #mr.append(0.15)
    
        mr.insert(0, num)
        mr.insert(5, num)
        mr.insert(6, num)
        #mr.insert(8, num)
    
    mr = [i for i in mr if i != 0]
    #mr.append(0.15)
    _abs = abs(sum(mr)-1.0)
    print(mr)
    mr.insert(8,_abs)
    print(sum(mr))
    
    for i in mr:
        res = i*cubic_mt_per_yr
    #    print(res)
        res_arr3.append(res)
    print("---------------------")
    print("\tYEAR 3")
    print("---------------------")
    print(res_arr3)
    print("-------------------\n")

def yr4():
    mr = [0, 0.06, 0.09, 0.07, 0.08, 0, 0, 0.08, 0.09, 0, 0.04, 0.15]
    res_arr4 = []
    cubic_mt_per_yr = float(input("Year 4: "))

    for i in range(4):
        num = round(random.uniform(0.04,0.08), 2)
        mr.pop(0)
        mr.pop(5)
        mr.pop(6)
        #mr.pop(8)
        #mr.append(0.15)
    
        mr.insert(0, num)
        mr.insert(5, num)
        mr.insert(6, num)
        #mr.insert(8, num)
    
    mr = [i for i in mr if i != 0]
    #mr.append(0.15)
    _abs = abs(sum(mr)-1.0)
    print(mr)
    mr.insert(8,_abs)
    print(sum(mr))
    
    for i in mr:
        res = i*cubic_mt_per_yr
    #    print(res)
        res_arr4.append(res)
    print("---------------------")
    print("\tYEAR 4")
    print("---------------------")
    print(res_arr4)
    print("-------------------\n")
    
def yr5():
    mr = [0, 0.06, 0.09, 0.07, 0.08, 0, 0, 0.08, 0.09, 0, 0.04, 0.15]
    res_arr5 = []
    cubic_mt_per_yr = float(input("Year 5: "))

    for i in range(4):
        num = round(random.uniform(0.04,0.08), 2)
        mr.pop(0)
        mr.pop(5)
        mr.pop(6)
        #mr.pop(8)
        #mr.append(0.15)
    
        mr.insert(0, num)
        mr.insert(5, num)
        mr.insert(6, num)
        #mr.insert(8, num)
    
    mr = [i for i in mr if i != 0]
    #mr.append(0.15)
    _abs = abs(sum(mr)-1.0)
    print(mr)
    mr.insert(8,_abs)
    print(sum(mr))
    
    for i in mr:
        res = i*cubic_mt_per_yr
    #    print(res)
        res_arr5.append(res)
    print("---------------------")
    print("\tYEAR 5")
    print("---------------------")
    print(res_arr5)
    print("-------------------\n")
                
def main():
    yr1()
    yr2()
    yr3()
    yr4()
    yr5()
    
if __name__=="__main__":
    os.system("clear")
    main()
