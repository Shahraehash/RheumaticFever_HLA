#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:02:20 2019

@author: Raehash
"""

import matplotlib.pyplot as plt



IFNy = "MKYTSYILAFQLCIVLGSLGCYCQDPYVKEAENLKKYFNAGHSDVADNGTLFLGILKNWKEESDRKIMQSQIVSFYFKLFKNFKDDQSIQKSVETIKEDMNVKFFNSNKKKRDDFEKLTNYSVTDLNVQRKAIHELIQVMAELSPAAKTGKRKRSQMLFRGRRASQ"
IL6 = "MNSFSTSAFGPVAFSLGLLLVLPAAFPAPVPPGEDSKDVAAPHRQPLTSSERIDKQIRYILDGISALRKETCNKSNMCESSKEALAENNLNLPKMAEKDGCFQSGFNEETCLVKIITGLLEFEVYLEYLQNRFESSEEQARAVQMSTKVLIQFLQKKAKNLDAITTPDPTTNASLLTKLQAQNQWLQDMTTHLILRSFKEFLQSSLRALRQM"
IL17 ="MTPGKTSLVSLLLLLSLEAIVKAGITIPRNPGCPNSEDKNFPRTVMVNLNIHNRNTNTNPKRSSDYYNRSTSPWNLHRNEDPERYPSVIWEAKCRHLGCINADGNVDYHMNSVPIQQEILVLRREPPHCPNSFRLEKILVSVGCTCVTPIVHHVA"
Streptolysin = "MSNKKTFKKYSRVAGLLTAALIIGNLVTANAESNKQNTASTETTTTNEQPKPESSELTTEKAGQKTDDMLNSNDMIKLAPKEMPLESAEKEEKKSEDKKKSEEDHTEEINDKIYSLNYNELEVLAKNGETIENFVPKEGVKKADKFIVIERKKKNINTTPVDISIIDSVTDRTYPAALQLANKGFTENKPDAVVTKRNPQKIHIDLPGMGDKATVEVNDPTYANVSTAIDNLVNQWHDNYSGGNTLPARTQYTESMVYSKSQIEAALNVNSKILDGTLGIDFKSISKGEKKVMIAAYKQIFYTVSANLPNNPADVFDKSVTFKELQRKGVSNEAPPLFVSNVAYGRTVFVKLETSSKSNDVEAAFSAALKGTDVKTNGKYSDILENSSFTAVVLGGDAAEHNKVVTKDFDVIRNVIKDNATFSRKNPAYPISYTSVFLKNNKIAGVNNRTEYVETTSTEYTSGKINLSHQGAYVAQYEILWDEINYDDKGKEVITKRRWDNNWYSKTSPFSTVIPLGANSRNIRIMARECTGLAWEWWRKVIDERDVKLSKEINVNISGSTLSPYGSITYK"

a = len(IFNy)
b = len(IL6)
c = len(IL17)
d = len(Streptolysin)

if (a >= b) and (a>=c) and (a>=d):
    largest = a
elif (b>=a) and (b>=c) and (b>=d):
    largest = b
elif (c>=a) and (c>=b) and (c>=d):
    largest = c
else:
    largest = d

length = largest + 1

digitsequenceNo = list(range(0,length))  #[0, len(IFNy)]

Amplitude1 = [-46] * length #list(range(0,len(IL6))) #[0,len(IFNy)]

j=0
x=1
i=0
while i<len(IFNy):
    Amplitude1[0]= 0
    if IFNy [j] == "F" or IFNy[j] == "L" or IFNy[j] == "I" or IFNy[j] == "Y" or IFNy[j]== "W":
        Amplitude1[x] = 2 + Amplitude1[(x-1)]
        i += 1
        j+=1
        x += 1
    elif IFNy[j]== "M" or IFNy[j] == "V" or IFNy[j]== "A" or IFNy[j] == "P" or IFNy[j]== "C":
        Amplitude1[x] = 1 + Amplitude1[(x-1)]
        i+=1
        j+=1
        x += 1 
    elif IFNy[j] == "T" or IFNy[j] == "H" or IFNy[j]== "Q" or IFNy[j] == "E" or IFNy[j] == "G":
        Amplitude1[x] = -1 + Amplitude1[(x-1)]
        i+=1
        j+=1
        x+= 1
    elif IFNy[j]== "S" or IFNy[j] == "N" or IFNy[j] == "K" or IFNy[j] == "D" or IFNy[j] == "R":
        Amplitude1[x] = -2 + Amplitude1[(x-1)]
        i+=1
        j+=1
        x+=1
    else:
        Amplitude1[x] = 0 + Amplitude1[(x-1)]
        x+=1
        i+=1
        
print(Amplitude1)        
        
Amplitude2 = [-23] * length #[0,len(IFNy)]

j=0
x=1
i=0
while i<len(IL6):
    Amplitude2[0]= 0
    if IL6 [j] == "F" or IL6[j] == "L" or IL6[j] == "I" or IL6[j] == "Y" or IL6[j]== "W":
        Amplitude2[x] = 2 + Amplitude2[(x-1)]
        i += 1
        j+=1
        x += 1
    elif IL6[j]== "M" or IL6[j] == "V" or IL6[j]== "A" or IL6[j] == "P" or IL6[j]== "C":
        Amplitude2[x] = 1 + Amplitude2[(x-1)]
        i+=1
        j+=1
        x += 1 
    elif IL6[j] == "T" or IL6[j] == "H" or IL6[j]== "Q" or IL6[j] == "E" or IL6[j] == "G":
        Amplitude2[x] = -1 + Amplitude2[(x-1)]
        i+=1
        j+=1
        x+= 1
    elif IL6[j]== "S" or IL6[j] == "N" or IL6[j] == "K" or IL6[j] == "D" or IL6[j] == "R":
        Amplitude2[x] = -2 + Amplitude2[(x-1)]
        i+=1
        j+=1
        x+=1
    else:
        Amplitude2[x] = 0 + Amplitude2[(x-1)]
        x+=1
        i+=1
print (Amplitude2)

Amplitude3 = [-27] * length

j=0
x=1
i=0
while i<len(IL17):
    Amplitude3[0]=0
    if IL17 [j] == "F" or IL17[j] == "L" or IL17[j] == "I" or IL17[j] == "Y" or IL17[j]== "W":
        Amplitude3[x] = 2 + Amplitude3[(x-1)]
        i += 1
        j+=1
        x += 1
    elif IL17[j]== "M" or IL17[j] == "V" or IL17[j]== "A" or IL17[j] == "P" or IL17[j]== "C":
        Amplitude3[x] = 1 + Amplitude3[(x-1)]
        i+=1
        j+=1
        x += 1 
    elif IL17[j] == "T" or IL17[j] == "H" or IL17[j]== "Q" or IL17[j] == "E" or IL17[j] == "G":
        Amplitude3[x] = -1 + Amplitude3[(x-1)]
        i+=1
        j+=1
        x+= 1
    elif IL17[j]== "S" or IL17[j] == "N" or IL17[j] == "K" or IL17[j] == "D" or IL17[j] == "R":
        Amplitude3[x] = -2 + Amplitude3[(x-1)]
        i+=1
        j+=1
        x+=1
    else:
        Amplitude3[x] = 0
        x+=1
        i+=1
print(Amplitude3)

Amplitude4 = [-46] * length #list(range(0,len(IL6))) #[0,len(Streptolysin)]

j=0
x=1
i=0
while i<len(Streptolysin):
    Amplitude4[0]= 0
    if Streptolysin [j] == "F" or Streptolysin[j] == "L" or Streptolysin[j] == "I" or Streptolysin[j] == "Y" or Streptolysin[j]== "W":
        Amplitude4[x] = 2 + Amplitude4[(x-1)]
        i += 1
        j+=1
        x += 1
    elif Streptolysin[j]== "M" or Streptolysin[j] == "V" or Streptolysin[j]== "A" or Streptolysin[j] == "P" or Streptolysin[j]== "C":
        Amplitude4[x] = 1 + Amplitude4[(x-1)]
        i+=1
        j+=1
        x += 1 
    elif Streptolysin[j] == "T" or Streptolysin[j] == "H" or Streptolysin[j]== "Q" or Streptolysin[j] == "E" or Streptolysin[j] == "G":
        Amplitude4[x] = -1 + Amplitude4[(x-1)]
        i+=1
        j+=1
        x+= 1
    elif Streptolysin[j]== "S" or Streptolysin[j] == "N" or Streptolysin[j] == "K" or Streptolysin[j] == "D" or Streptolysin[j] == "R":
        Amplitude4[x] = -2 + Amplitude4[(x-1)]
        i+=1
        j+=1
        x+=1
    else:
        Amplitude4[x] = 0 + Amplitude4[(x-1)]
        x+=1
        i+=1
        
print(Amplitude4)      


plt.plot(digitsequenceNo,Amplitude1, label = 'IFN-y')
plt.plot(digitsequenceNo,Amplitude2, label = 'IL-6')
plt.plot(digitsequenceNo,Amplitude3, label = 'IL-17A')
plt.plot(digitsequenceNo,Amplitude4, label = 'Streptolysin')
plt.xlabel('Digit Sequence Number')
plt.ylabel('Amplitude')
plt.title('Variance in Cytokines based on Polarity')
plt.legend()
plt.show()