import datetime
while 1:
    gun1=int(input("Luften 1. Gun Tarihini Giriniz:"))
    ay1=int(input("Lutfen 1. Ay Tarihini Giriniz:"))
    yil1=int(input("Lutfen 1. Yıl tarihini Giriniz:"))
    print(50*"-")
    gun2=int(input("Luften 2. Gun Tarihini Giriniz:"))
    ay2=int(input("Lutfen 2. Ay Tarihini Giriniz:"))
    yil2=int(input("Lutfen 2. Yil Tarihini Giriniz:"))
    print(50*"-")
    try:
        tarih1=datetime.date(day=gun1,month=ay1,year=yil1)
        tarih2=datetime.date(day=gun2,month=ay2,year=yil2)
        print("1. Tarih:{} (YIL/AY/GUN)".format(tarih1))
        print("2. Tarih: {} (YIL/AY/GUN)".format(tarih2))
        if tarih1<tarih2:
            tarihFark=tarih2-tarih1
        else:
            tarihFark=tarih1-tarih2
        print("****************** İki Tarih Arasindaki Fark:{} Gundur ******************".format(tarihFark.days))
        break
    except ValueError:
        print("!!!!!!!!!!!!!!HATA OLUSTU!!!!!!!!!!!!!!\n..."
          ".........Tarihleri Yanlıs Girdiniz............\n............lutfen Tekrar Deneyiniz............")
        print(50*"-")
        continue