import requests , time , os , random
from bs4 import BeautifulSoup



BK = '\033[0;30m' #black
BL = '\033[0;34m' #blue
GN = '\033[0;32m' #green
CY = '\033[0;36m' #cyan
R = '\033[0;31m' #Red
PE = '\033[0;35m' #purple
BW = '\033[0;33m' #brown
LG = '\033[0;37m' #lightgreen
DG = '\033[1;30m' #darkgrey
LB = '\033[1;34m' #lightblue
LGN = '\033[1;32m' #lightgreen
LC = '\033[1;36m' #lightcyan
LR = '\033[1;31m' #lightred
LP = '\033[1;35m' #lightpurple
Y = '\033[1;33m' #yellow
W = '\033[1;37m' #white
MN = '\033[101m' #Latar Merah
MS = '\033[0m' # Latar Biasa





# MENU




def menu () :
      print (LGN+"["+W+"01"+LGN+"]"+Y+" install Metaxploit [300Mb+]")
      print (LGN+"["+W+"02"+LGN+"]"+Y+" install Ngrok")
      print (LGN+"["+W+"03"+LGN+"]"+Y+" install Lazymux")
      print (LGN+"["+W+"04"+LGN+"]"+Y+" install A-Rat")
      print (LGN+"["+W+"05"+LGN+"]"+Y+" install Bughunter")
      print (" ")
      print (" ")


      print (LGN+"["+W+"00"+LGN+"]"+Y+" Exit")



# METAXPLOIT


def metaxsploit () :
    os.system ("clear")
    os.system ("figlet -f slant  Metaxploit | lolcat")
    print (LC+"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print (" ")
    print (MN+W+":: Peringatan : Siapakan Kesabaran Dan Paketan ::"+MS+" ")
    print (" ")
    print (LGN+"["+W+"01"+LGN+"]"+Y+" install Bahan-Bahan")
    print (LGN+"["+W+"02"+LGN+"]"+Y+" install Metaxploit")
    print (" ")
    print (LGN+"["+W+"00"+LGN+"]"+Y+" Kembali")
    print (" ")
    print (" ")
    pilih = input(W+"Masukan Pilihan Agan : ")
    if pilih == '1' or pilih == '01':
       os.system ('clear')
       os.system ('figlet -f slant Sabar | lolcat')
       print (LGN+" ")
       os.system ('apt update && apt upgrade && apt install curl && apt install git && pkg install ruby && pkg install root-repo && pkg install unstable-repo && pkg install x11-repo')
       os.system ("figlet -f slant Done | lolcat")
       os.system ("clear")
       os.system ("python xtoolsx.py")
    elif pilih == '2' or pilih == '02':
       os.system ("clear")
       os.system ("figlet -f Sabar | lolcat")
       print (LGN+" ")
       os.system ('pkg install metaxploit')
       os.system ("figlet -f slant Done | lolcat")
       os.system ("clear")
       os.system ("python xtoolsx.py")
    elif pilih == '0' or pilih == '00':
       os.system ('exit')
       os.system ('python xtoolsx.py')
    else:
       print ('Salah Ketik Lu Gann')
       os.system ("clear")
       os.system ("python xtoolsx.py")

# NGROK



def ngrok () :
       os.system ("clear")
       os.system ("figlet -f slant Sabar | lolcat")
       print (LGN+" ")
       os.system ('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip')
       os.system ('unzip ngrok-stable-linux-arm.zip')
       os.system ("figlet -f slant Done | lolcat")
       os.system ("clear")
       os.system ("python xtoolsx.py")






# LAZYMUX

def lazymux () :
    os.system ('clear')
    os.system ("figlet -f slant Sabar | lolcat ")
    print (LGN+" ")
    os.system ('git clone https://github.com/Gameye98/Lazymux')
    os.system ("figlet -f slant Done | lolcat ")
    os.system ("clear")
    os.system ("python xtoolsx.py")


# A-rat

def arat () :
    os.system ('clear')
    os.system ("figlet -f slant Sabar | lolcat")
    print (LGN+" ")
    os.system ('git clone https://github.com/Xi4u7/A-Rat.git')
    os.system ("figlet -f slant Done | lolcat")
    os.system ("clear")
    os.system ("python xtoolsx.py")



#BugHunter

def bughunter () :
    os.system ("clear")
    print (LGN+" ")
    os.system ("figlet -f slant Sabar | lolcat")
    os.system ('git clone https://github.com/thehackingsage/bughunter.git')
    os.system ("figlet -f slant Done | lolcat")
    os.system ("clear")
    os.system ("python xtoolsx.py")












# Tampilan Awal




os.system ("clear")
os.system ("figlet -f slant xTOOLSx | lolcat")
print (LB+"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print (Y+"        .:.:."+W+" Code By : Mr.iVx7 "+Y+".:.:.          ")
print (" ")
print (MN+W+":: Peringatan : Dilarang Menyalahgunakan   ::"+MS+" ")
print (MN+W+":: Tools ini Atau Diperjual Belikan Trims. ::"+MS+" ")
print (" ")
print (" ")
menu()
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")



oe = input (W+'Masukan Pilihan Agan : ')
if oe == '1' or oe == '01':
     metaxsploit()
elif oe == '2' or oe == '02':
       ngrok()
elif oe == '3' or oe == '03':
       lazymux()
elif oe == '4' or oe == '04':
       arat()
elif oe == '5' or oe == '05':
       bughunter()
elif oe == '0' or oe == '00':
       os.system ("clear")
       print (LB+" [*] Terimakasih Telah Menggunakan Tools Ini")
       print (LGN+" [*] Terimakasih Juga Yang Telah Mensupport Tools ini")
       print (Y+" [*] Mr.iVx7 Mengucapkan Terimakasih")
       print (LR+" [*] Byeee..")
       os.system ("figlet -f slant xTOOLSx | lolcat")
       os.system ("exit")
else:
       print("Salah Ketik Lu Gayynn")
       os.system ("python xtoolsx.py")



