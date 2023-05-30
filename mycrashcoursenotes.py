# Değişkenler, Değişkenlerde string atamak için "" int,float atamak içinse direk yazıyoruz
# Örnek
#Int Integer demek yani tam sayı bu sebeple 1.5 yazarsanız 1 olarak okur


f = float(1.9)
x = int(1.5)
g = bool(True)
z = "Dünyaya"
y = complex(10+7j+6j+3)


# Inputlar  

f = float(input("Ondalıklı Sayı Gir : "))
z = str(input("Merhaba : "))
y = complex(input("Karmaşık Sayı Gir : "))
x = int(input("Tam Sayı Gir : "))
g = bool(input("True yada False sayı gir : "))


# If Else Elif Modülleri

print("BotDatNet Sys3.0")


f = input("Username : ")
g = input("Password : ")
x = "archy"
y = "123"

# Elif Kullanmak Hayatı Kolaylaştırır 

if(f == x and g == y) :
    print("Giriş Başarılı")   
elif not f.strip() and not g.strip():
    print("Kullanıcı Adı Ve Parola Alanı Boş Bırakılmaz")
elif not f.strip():
    print("Kullanıcı Adı Alanı Boş Bırakılmaz")
elif not g.strip():
    print("Parola Alanı Boş Bırakılmaz")
else:
    print("Hatalı Parola yada Kullanıcı Adı")



# Listlerle Çalışmak Saçma Ama Data Scienceda Işe Yarar
invitation_list = [
    "Zenci Göt",
    "ARCHY",
    "Graham Chapman",
    "John Cleese",
    "Terry Gilliam",
    "Eric Idle",
    "Terry Jones",
    "Michael Palin",
]


name = input("Adınızı Girin : ")

if name in invitation_list :
    print("Girebilirsin")
#elif name not in invitation_list:
    print("Davetiye Almayı Dene")
else:
    print("Giremezsiiz")


#List Methotları ( leetcode çözerken en fazla çıkanlar)
print("len()")
print(len(list_laptop))
# sum()
print("sum()")
print(numbers)
print("sum:", sum(numbers))






#print(z,y,x,g,f)




