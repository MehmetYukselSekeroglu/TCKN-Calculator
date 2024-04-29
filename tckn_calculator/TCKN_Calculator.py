#!/usr/bin/env python3


"""
Project Start Date  :   01.12.2022 
Name                :   TcKn Calculator
Version             :   1.0.0
Language            :   Python3.x
Project Page        :   https://github.com/MehmetYukselSekeroglu/tc-hesaplayici.git
License             :   Mit
"""



VERSION =   "1.0.0"
AUTHOR  =   "Prime Security"




def validation_check(tc_number:str) -> bool:
    
    
    # TcKn Numarasının olması gereken uzunlugu ve nümerik olup olmadıgını kontrol eder
    if len(tc_number) != 11 or not tc_number.isnumeric():
        return False
    
    tc = tc_number

    step_1 = int(tc[0]) + int(tc[2]) + int(tc[4]) + int(tc[6]) + int(tc[8])
    step_1 = step_1 * 7

    step_2 = int(tc[1]) + int(tc[3]) + int(tc[5]) + int(tc[7])
    step_2 = step_2 * 9

    final_indis_10 = step_1 + step_2
    final_indis_10 = final_indis_10 % 10
    final_indis_11 = 0

    for z in range(10):    
        final_indis_11 = final_indis_11 + int(tc[z])

    final_indis_10 = str(final_indis_10)
    final_indis_11=final_indis_11%10
    final_indis_11 = str(final_indis_11)


    if final_indis_10 == tc[9] and final_indis_11 == tc[10]:
        return True
    else:
        return False
    
    
def make_control_index(ilk_9_indis) -> str:
    tc = str(ilk_9_indis)
    step_1 = int(tc[0]) + int(tc[2]) + int(tc[4]) + int(tc[6]) + int(tc[8])
    step_1 = step_1 * 7

    step_2 = int(tc[1]) + int(tc[3]) + int(tc[5]) + int(tc[7])
    step_2 = step_2 * 9

    final_indis_10 = step_1 + step_2
    final_indis_10 = final_indis_10 % 10 
    final_indis_11 = 0
    tc=f"{tc}{final_indis_10}"
    for i in range(10):
        final_indis_11 = final_indis_11 + int(tc[i])

    
    final_indis_10 = str(final_indis_10)
    final_indis_11 = final_indis_11 % 10
    final_indis_11 = str(final_indis_11)
    
    final= final_indis_10+final_indis_11
    return final



def tckn_generator(tc_number:str,pcs:int) -> list:
    
    # TcKn Numarasının olması gereken uzunlugu ve nümerik olup olmadıgını kontrol eder
    if len(tc_number) != 11 or not tc_number.isnumeric():
        return [False, "TCKN length or type is invalid."]
    
    if pcs < 1:
        return [False, "pcs parameters is invalid"]
    
    
    uretilecek_tc = tc_number
    olustuma_adedi = pcs
    
    olustuma_adedi = int(olustuma_adedi)
    ilk_9indis = uretilecek_tc[0:9]
    ilk_9indis = int(ilk_9indis)

    geriye_donuk = ilk_9indis
    ileri_donuk = ilk_9indis

    ileri_donuk_liste=[]
    geriye_donuk_liste=[]


    a = 0
    while (a <= int(olustuma_adedi)):
        geriye_donuk = geriye_donuk - 29999
        dondurulecek_deger = f"{geriye_donuk}{make_control_index(geriye_donuk)}"
        if validation_check(dondurulecek_deger):
            #print(f"[-{a}] {dondurulecek_deger}")
            geriye_donuk_liste.append(dondurulecek_deger)
            a= a+1 


    b = 0
    while (b <= int(olustuma_adedi)):
        ileri_donuk = ileri_donuk + 29999
        dondurulecek_deger = str(ileri_donuk)+str(make_control_index(ileri_donuk))
        if validation_check(dondurulecek_deger):
            #print(f"[{b}] {dondurulecek_deger}")
            ileri_donuk_liste.append(dondurulecek_deger)
            b=b+1
    return [True, geriye_donuk_liste, ileri_donuk_liste]

