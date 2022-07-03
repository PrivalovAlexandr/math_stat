from decimal import *
from pprint import pprint
from math import sqrt

def int_r(num):
    #   округление до тысячных
    number = Decimal(num).quantize(Decimal('1.000'))
    return number.__float__()



#   //  задание без интервалов


#   примеры number_list
#
#   number_list = [3.2, 3.4, 3.3, 3.5, 3.6, 3.7, 3.4, 3.3, 3.4, 3.7, 3.2]
#   number_list = [23, 24, 16, 21, 18, 17, 20, 23, 18, 16, 19, 22, 18, 24, 19, 17, 22, 19, 15, 23]

number_list = []

def normal_quest6(number_list:list):
    number_list.sort()

    range_list = {}
    for i in number_list:
        if i not in range_list:
            count = 0
            for j in number_list:
                if j == i:
                    count += 1
            range_list[i] = [count, int_r(count/len(number_list))]

    print('Вариационный ряд вида [count, p*]:')
    pprint(range_list)
    print(f'Общее количество значений: {len(number_list)}\n--------------------')

    sum = 0
    for i in range_list:
        sum += i
    v_sr = sum/len(number_list)
    print(f"Сумма: {sum}")
    print(f"Выборочное среднее: \n{int_r(v_sr)}\n--------------------")

    sum2 = 0
    for i in range_list:
        sum2 += (i-v_sr)**2
    v_ds = sum2/len(number_list)
    print(f"Сумма: {sum2}")
    print(f"Выборочная дисперсия: \n{int_r(v_ds)}\n--------------------")

    v_sr_sqrt = sqrt(v_ds)
    print(f"Выборочное среднее квадратическое отклонение: \n{int_r(v_sr_sqrt)}\n--------------------")





#   //  задание с интервалами




#
#   //  примеры необходимых переменных  //
#

#   интервального ряда
#inter = [
#[161, 165],
#[165, 169],
#[169, 173],
#[173, 177],
#[177, 181]]

#   вероятность каждого интервала    
#p_list = [
#    0.06,
#    0.19,
#    0.47,
#    0.19,
#    0.09]

inter = []
p_list = []

def inter_quest6 (inter, p_list):
    sr_inter = []
    for i in inter:
        sr_inter.append((i[0]+i[1])/2)
    step = sr_inter[1]-sr_inter[0]
    print(f"Интервальный шаг: {step}")
    print(f"Середины интервалов: \n{sr_inter}\n--------------------")
    

    x_on_p = []
    for i in range (0, len(sr_inter)):
        x_on_p.append(int_r(sr_inter[i]*p_list[i]))
    
    sum = 0
    for i in x_on_p:
        sum+=i
    print(f"x*p:\n{x_on_p}")
    print(f"Выборочное среднее:\n{sum}\n--------------------")

    sr_on_p = []
    for i in range (0, len(sr_inter)):
        sr_on_p.append(int_r(((Decimal(sr_inter[i])-Decimal(sum))**2)*Decimal(p_list[i])))
    
    sum2 = 0
    for i in sr_on_p:
        sum2+=i
    print(f"sr_inter*p:\n{sr_on_p}")
    print(f"Выборочная дисперсия: {sum2}\n--------------------")
    
    v_sr_sqrt = int_r(sqrt(sum2))
    print(f"Выборочное среднее квадратическое отклонение: \n{v_sr_sqrt}\n--------------------")

    f_dict = {}
    count=0
    for i in p_list:
        count+=1
        f_dict[f'f{count}'] = int_r(i/step)
    print("Высоты ступенчетой гистограммы:")
    pprint(f_dict)
    print('--------------------')




if __name__ == "__main__":
    choice = input(
'''Выберите тип ряда:
    1 - без интервалов
    2 - с интервалами

''')
    match choice:
        case '1':
            if number_list:
                normal_quest6(number_list)
            else:
                print('Вы оставили number_list пустым. Введите значения и попробуйте ещё раз')
        case '2':
            if (inter != []) & (p_list != []):
                inter_quest6(inter, p_list)
            else:
                if (not inter) & (not p_list):
                    error = 'inter и p_list'
                elif not inter:
                    error = 'inter' 
                else:
                    error = 'p_list'
                print(f'Вы оставили {error} пустым. Введите значения и попробуйте ещё раз')