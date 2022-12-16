print("Hesap makinesine hoş geldiniz!")

# Kullanıcıdan ilk sayıyı alıyoruz
sayi1 = float(input("Lütfen ilk sayıyı girin: "))

# Kullanıcıdan işlem türünü alıyoruz
islem = input("Lütfen bir işlem türü girin (+, -, *, /): ")

# Kullanıcıdan ikinci sayıyı alıyoruz
sayi2 = float(input("Lütfen ikinci sayıyı girin: "))

# Kullanıcının girdiği işlem türüne göre hesaplama yapıyoruz
if islem == "+":
  sonuc = sayi1 + sayi2
  print(sayi1, "+", sayi2, "=", sonuc)
elif islem == "-":
  sonuc = sayi1 - sayi2
  print(sayi1, "-", sayi2, "=", sonuc)
elif islem == "*":
  sonuc = sayi1 * sayi2
  print(sayi1, "*", sayi2, "=", sonuc)
elif islem == "/":
  sonuc = sayi1 / sayi2
  print(sayi1, "/", sayi2, "=", sonuc)
else:
  print("Geçersiz işlem türü!")