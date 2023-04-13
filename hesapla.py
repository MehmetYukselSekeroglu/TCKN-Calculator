#!/usr/bin/env python3
import sys
import argparse
from colorama import *

DEV_BY="PRIME"

def title():
    print(f"{blue}[Powered By {DEV_BY}]{reset}")

def help_menu():
    print(f"""|----------------------------|
|By {DEV_BY} @ 24.11.2022 | v1.0 |
|----------------------------|
-Kullanım: python3 {sys.argv[0]} --tc 12345678901 --adet 10
    --tc    : Hesaplanacak Tc numarası
    --adet  : Hesaplama adeti
    
-Not: --adet en az 1 olmalıdır!
""")


try:
    if sys.argv[1] == "--help":
        help_menu()
        exit(0)
except Exception:
    pass

ArgumanParser = argparse.ArgumentParser()
ArgumanParser.add_argument("--tc", required=True, help="Hesaplanacak tc numarası")
ArgumanParser.add_argument("--adet",required=True, help="Hesaplama adeti")
Arg_all = vars(ArgumanParser.parse_args())

TcNumber_is = Arg_all["tc"]
HesaplamaAdet =  Arg_all["adet"]
olustuma_adedi = HesaplamaAdet



def gecerlilik_kontrol(tc):

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
    
def index_oto(indis):
    alfa = len(indis) - 1
    return alfa

def kontrol_basamakları(ilk_9_indis):
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
def tc_retici(uretilecek_tc):
    ilk_9indis = uretilecek_tc[0:9]
    ilk_9indis = int(ilk_9indis)

    geriye_donuk = ilk_9indis
    ileri_donuk = ilk_9indis
    print("|------------------")
    print("[?] Geriye dönük: ")
    a = 0
    while (a <= int(olustuma_adedi)):
        geriye_donuk = geriye_donuk - 29999
        dondurulecek_deger = f"{geriye_donuk}{kontrol_basamakları(geriye_donuk)}"
        if gecerlilik_kontrol(dondurulecek_deger):
            print(f"[-{a}] {dondurulecek_deger}")
            a= a+1 
        

    #else:
        #    print(f"[-] {dondurulecek_deger} - GEÇERSİZ ")
    print("|------------------")
    print("[?] İleriye dönük: ")
    b = 0
    while (b <= int(olustuma_adedi)):
        ileri_donuk = ileri_donuk + 29999
        dondurulecek_deger = str(ileri_donuk)+str(kontrol_basamakları(ileri_donuk))
        if gecerlilik_kontrol(dondurulecek_deger):
            print(f"[{b}] {dondurulecek_deger}")
            b=b+1
    print("|------------------\n")


red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
reset = Fore.RESET



if len(TcNumber_is) < 11 or len(TcNumber_is) > 11:
    title()
    print(f"{red}[-] Geçersiz Tc uzunluğu: {len(TcNumber_is)}{reset}")
    exit(1)

if gecerlilik_kontrol(TcNumber_is):
    title()
    print(f"{blue}[+] Tc geçerlidir | Tc: {TcNumber_is}{reset}")
    tc_retici(str(TcNumber_is))
    exit(0)

else:
    title()
    print(f"{red}[-] Tc Geçersizdir! {reset}")
    exit(0)


try:
    tc_numarası = sys.argv[1]
    olustuma_adedi = sys.argv[2]
    if len(tc_numarası) > 11:
        print("uzun tc numarası!")
        exit()
    elif len(tc_numarası) < 11:
        print("kısa tc numarası!")
        exit()

except Exception:
    help_menu()

else:
    if gecerlilik_kontrol(tc_numarası):
        print("By Only @ 24.11.2022 | v1.0\n")
        print(f"[+] TC GEÇERLİDİR ! | TC: {tc_numarası}")
        tc_retici(str(tc_numarası))
    else:
        print("[-] TC GEÇERSİZ !")
        print("By Only @ 24.11.2022 | v1.0")


