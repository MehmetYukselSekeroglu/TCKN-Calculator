

"""
01.12.2022 PRIME İÇİN ÜRETİLEN TC NUMARASI DORULAMA VE HESAPLAMA KÜTÜPHANESİDİR 
TC ALGORİTMASINI KULLANARAK OTOMATİK OLARAK İŞLEM YAPAR 



"""





#girilen tc numarası matematiksel olarak geçerlimi kontrol eder 

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



def tc_uretici(uretilecek_tc,olustuma_adedi):
    olustuma_adedi = int(olustuma_adedi)
    ilk_9indis = uretilecek_tc[0:9]
    ilk_9indis = int(ilk_9indis)

    geriye_donuk = ilk_9indis
    ileri_donuk = ilk_9indis


    ileri_donuk_liste=[]
    geriye_donuk_liste=[]
    #print("|------------------")
    #print("[?] Geriye dönük: ")
    a = 0
    while (a <= int(olustuma_adedi)):
        geriye_donuk = geriye_donuk - 29999
        dondurulecek_deger = f"{geriye_donuk}{kontrol_basamakları(geriye_donuk)}"
        if gecerlilik_kontrol(dondurulecek_deger):
            #print(f"[-{a}] {dondurulecek_deger}")
            geriye_donuk_liste.append(dondurulecek_deger)
            a= a+1 
    #print("[?] İleriye dönük: ")
    b = 0
    while (b <= int(olustuma_adedi)):
        ileri_donuk = ileri_donuk + 29999
        dondurulecek_deger = str(ileri_donuk)+str(kontrol_basamakları(ileri_donuk))
        if gecerlilik_kontrol(dondurulecek_deger):
            #print(f"[{b}] {dondurulecek_deger}")
            ileri_donuk_liste.append(dondurulecek_deger)
            b=b+1
    return ileri_donuk_liste,geriye_donuk_liste

