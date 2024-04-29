#!/usr/bin/env python3
import argparse
import sys


import tckn_calculator


def printTitle() -> None:
    print(f"-> Powered By {tckn_calculator.__AUTHOR__}")
    print()



ArgumanParser = argparse.ArgumentParser(add_help=True)
ArgumanParser.add_argument("--tc", required=True,type=str   ,help="-> Target TCKN Number, example:\t--tc 11122233300")
ArgumanParser.add_argument("--count",required=True,type=int, help="-> Calculating Count, example :\t--count 10")
Arg_all = vars(ArgumanParser.parse_args())

target_tckn = Arg_all["tc"]
calculating_count =  Arg_all["count"]





printTitle()


validationStatus = tckn_calculator.validation_check(tc_number=target_tckn)

if not validationStatus:
    print(f"[-] This TCKN Not Valid!    : {target_tckn}")
    sys.exit()
    
    

print(f"[+] Calculating TCKN... Please wait.")
generatedList = tckn_calculator.tckn_generator(tc_number=target_tckn,pcs=calculating_count)

if not generatedList[0]:
    print(f"[-] Calculation Failed:\t{generatedList[1]}")

print(f"[+] OK... Calculation success.")


print()


geriyeDonuk = generatedList[1]
ileriDonuk = generatedList[2]


print(f"Geriye Dönük:")
print("-"*50)

for single_tc in geriyeDonuk:
    print(single_tc)
    
    
print("-"*50)
print()

print(f"İleriye Dönük:")
print("-"*50)

for single_tc in ileriDonuk:
    print(single_tc)




print("-"*50)
print()

print(f"[+] Proccess successfuly.")




