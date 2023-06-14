#Aleksander Kant Pizza calculator


#prijzen
SmallHawaiPrijs    = 6.99
MediumHawaiPrijs   = 8.99
LargeHawaiPrijs    = 13.99
XXLHawaiPrijs      = 15.99
ColaPrijs          = 2.25
FantaPrijs         = 2.25
LiptonPrijs        = 2.25
RedBullPrijs       = 3.50
WaterPrijs         = 1.70


#menu
print("____________PRIJSKAART PIZZA Hawai____________")
print("----------------Small, 20 cm----------------")
print("--------------------€6,99--------------------")
print("=================================================")
print("----------------Medium, 25 cm----------------")
print("--------------------€8,99--------------------")
print("=================================================")
print("----------------Large, 35 cm----------------")
print("-------------------€13,99-------------------")
print("=================================================")
print("-----------------XXL, 40 cm-----------------")
print("-------------------€15,99-------------------")
print("+++++++++++++++++++++++++++++++++++++++++++++++++")
print("_________________DRANKJES_________________")
print("--------- Cola, Fanta, Lipton---------")
print("------------------€2,25------------------")
print("=================================================")
print("----------------Red Bull----------------")
print("-----------------€3.50-----------------")
print("=================================================")
print("------------------Water------------------")
print("-----------------€1,70-----------------")




#hoeveelheden
hoeveelSmallHawai  = int(input("Aantal small hawai Pizza's:  "))
hoeveelMediumHawai = int(input("Aantal Medium hawai Pizza's: "))
hoeveelLargeHawai  = int(input("Aantal Large Hawai Pizza's:  "))
hoeveelXXLHawai    = int(input("Aantal Hawai xxl Pizza's:    "))
hoeveelCola        = int(input("Aantal Cola:                 "))
hoeveelFanta       = int(input("Aantal Fanta:                "))
hoeveelLipton      = int(input("Aantal Lipton:               "))
hoeveelRedBull     = int(input("Aantal Red Bull:             "))                      
hoeveelWater       = int(input("Aantal Water:                "))

#prijs en hoeveelheden
TotaalSmallHawai  = (SmallHawaiPrijs  * hoeveelSmallHawai)
TotaalMediumHawai = (MediumHawaiPrijs * hoeveelMediumHawai)
TotaalLargeHawai  = (LargeHawaiPrijs  * hoeveelLargeHawai)
TotaalXXLHawai    = (XXLHawaiPrijs    * hoeveelXXLHawai)
TotaalCola        = (ColaPrijs        * hoeveelCola)
TotaalFanta       = (FantaPrijs       * hoeveelFanta)
TotaalLipton      = (LiptonPrijs      * hoeveelLipton)
TotaalRedBull     = (RedBullPrijs     * hoeveelRedBull)
TotaalWater       = (WaterPrijs       * hoeveelWater)


#alles wat besteld is 
TotaalBestelling = (TotaalSmallHawai + TotaalMediumHawai + TotaalLargeHawai + TotaalXXLHawai + TotaalCola + TotaalFanta + TotaalLipton + TotaalRedBull + TotaalWater)



#afmeting pizza/prijs
print("Totale prijs van Small Hawai Pizza:    " + " €" + str(TotaalSmallHawai))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs Medium Hawai Pizza:   " + " €" + str(TotaalMediumHawai))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van Large Hawai Pizza: " + " €" + str(TotaalLargeHawai))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van XXL Hawai Pizza:   " + " €" + str(TotaalXXLHawai))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van Cola:               " + " €" + str(TotaalCola))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van Fanta:              " + " €" + str(TotaalFanta))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van lipton:            " + " €" + str(TotaalLipton))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijd van Red Bull:           " + " €" + str(TotaalRedBull))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Totale prijs van Water:             " + " €" + str(TotaalWater))
print("==============================================================")







print("--------------------------------")
print("Uw volledige bestelling bestaat uit")
print(f"{hoeveelSmallHawai } SmallHawai pizza's ")
print(f"{hoeveelMediumHawai} MediumHawai pizza's ")
print(f"{hoeveelLargeHawai } LargeHawai pizza's ")
print(f"{hoeveelXXLHawai   } XXLHawai pizza's ")
print(f"{hoeveelCola       } Cola ")
print(f"{hoeveelFanta      } Fanta ")
print(f"{hoeveelLipton     } Lipton ")
print(f"{hoeveelRedBull    } Redbull ")
print(f"{hoeveelWater      } Water ")
print("--------------------------------")






#betaling
print("Totaalprijs te betalen: " + "€" + str(TotaalBestelling))
