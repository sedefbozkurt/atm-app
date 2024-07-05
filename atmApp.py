# Bankamatik Uygulaması

def showMenu():
  print("\nBankamatik")
  print("1. Bakiyeni Kontrol Et")
  print("2. Para Yatır")
  print("3. Para Çek")
  print("4. Hesap Geçmişi")
  print("5. Çıkış")

def CheckBalance(balance):
  print(f"Mevcut bakiyeniz: {balance:.2f} ₺")

def depositMoney(balance, history):
    while True:
        try:
            amount = float(input("Yatırılacak tutarı girin: "))
            if amount > 0: 
                balance += amount
                history.append(f"{amount} ₺ yatırıldı.")
                print(f"{amount} ₺ yatırıldı.")
                break
            else:
                print("Tutar pozitif olmalıdır.")
        except ValueError:
            print("Geçersiz giriş. Lütfen sayısal bir değer giriniz.")
    return balance

def withdrawMoney(balance, history):
    while True:
        try:
            amount = float(input("Çekilecek tutarı girin: "))
            if amount > 0:
                if balance >= amount:
                    balance -= amount
                    history.append(f"{amount} ₺ çekildi.")
                    print(f"{amount:.2f} ₺ çekildi")
                    break
                else:
                    print("Yetersiz bakiye.")
            else:
                print("Tutar pozitif olmalıdır.")
        except ValueError:
            print("Geçersiz giriş. Lütfen sayısal bir değer girin.")
    return balance

def showHistory(history):
    print("\nHesap Geçmişi:")
    for record in history:
        print(record)
          
def main():
    balance = 0.0 # İlk bakiye
    history = []

    while True:
        showMenu()
        choice = input("Yapmak istediğiniz işlemi seçiniz (1-5): ")

        if choice == '1': 
            CheckBalance(balance)
        elif choice == '2':
            balance = depositMoney(balance, history)
        elif choice == '3':
            balance = withdrawMoney(balance, history)
        elif choice == '4':
            showHistory(history)
        elif choice == '5':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçeneki lütfen tekrar deneyin")
            
if __name__ == "__main__":
    main()