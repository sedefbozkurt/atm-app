# Bankamatik Uygulaması

def showMenu():
  print("\nBankamatik")
  print("1. Bakiyeni Kontrol Et")
  print("2. Para Yatır")
  print("3. Para Çek")
  print("4. Çıkış")

def CheckBalance(balance):
  print(f"Mevcut bakiyeniz: {balance:.2f} ₺")

def depositMoney(balance):
    while True:
        try:
            amount = float(input("Yatırılacak tutarı girin: "))
            if amount > 0: 
                balance += amount
                print(f"{amount} ₺ yatırıldı.")
                break
            else:
                print("Tutar pozitif olmalıdır.")
        except ValueError:
            print("Geçersiz giriş. Lütfen sayısal bir değer giriniz.")
    return balance

def withdrawMoney(balance):
    while True:
        try:
            amount = float(input("Çekilecek tutarı girin: "))
            if amount > 0:
                if balance >= amount:
                    balance -= amount
                    print(f"{amount:.2f} ₺ çekildi")
                    break
                else:
                    print("Yetersiz bakiye.")
            else:
                print("Tutar pozitif olmalıdır.")
        except ValueError:
            print("Geçersiz giriş. Lütfen sayısal bir değer girin.")
    return balance
          
def main():
    balance = 0.0 # İlk bakiye

    while True:
        showMenu()
        choice = input("Yapmak istediğiniz işlemi seçiniz (1-4): ")

        if choice == '1': 
            CheckBalance(balance)
        elif choice == '2':
            balance = depositMoney(balance)
        elif choice == '3':
            balance = withdrawMoney(balance)
        elif choice == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçeneki lütfen tekrar deneyin")
            
if __name__ == "__main__":
    main()