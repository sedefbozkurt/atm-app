import json
import getpass
from datetime import datetime

# Bankamatik Uygulaması

def loadUsers():
  try:
    with open("users.json", "r") as file:
      return json.load(file)["users"]
  except FileNotFoundError:
    return []

def saveUsers(users):
  with open("users.json", "w") as file:
    return json.dump({"users": users}, file, indent=3)

def findUser(users, username, password):
  for user in users:
    if user["username"] == username and user["password"] == password:
      return user
  return None

def login(users):
  username = input("Kullanıcı adı: ")
  password = input("Parola: ")
  user = findUser(users, username, password)
  if user:
    return user
  else:
    print("Kullanıcı adı veya parola hatalı") 
    return None

def checkBalance(user):
  print(f"Mevcut bakiyeniz: {user['balance']:.2f} ₺")

def getAmountInput(prompt):
   while True:
    amount = input(prompt)
    try:
      amount = float(amount)
      if amount > 0:
        return amount
      else:
         print("Tutar pozitif olmalıdır")
    except ValueError:
      print("Geçersiz giriş. Lütfen sayısal bir değer girin")

def depositMoney(user):
  amount = getAmountInput("Yatırılacak tutarı girin: ")
  user['balance'] += amount
  user['history'].append({"date": str(datetime.now()), "transaction": f"{amount} ₺ yatırıldı."})
  print(f"{amount} ₺ yatırıldı.")

def withdrawMoney(user):
  amount = getAmountInput("Çekilecek tutarı girin: ")
  if user['balance'] >= amount:
    user['balance'] -= amount
    user['history'].append({"date": str(datetime.now()), "transaction": f"{amount} ₺ çekildi."})
    print(f"{amount} ₺ çekildi.")
  else:
    print("Yetersiz bakiye.")

def showHistory(user):
  print("\nHesap Geçmişi:")
  for record in user['history']:
    print(f"İşlem Tarihi: {record['']}, İşlem: {record['transaction']}")

def changePassword(user):
  currentPassword = getpass.getpass("Mevcut parola: ")
  if currentPassword == user['password']:
    newPassword = getpass.getpass("Yeni parola: ")
    user['password'] = newPassword
    print("Parola başarıyla değiştirildi")
  else:
    print("Mevcut şifre hatalı")

def transferMoney(users, user):
  amount = getAmountInput("Transfer edilecek miktarı girin: ")
  recipientUsername = input("Alıcının kullanıcı adını girin: ")
  recipient = findUser(users, recipientUsername, "")
  if recipient and user['balance'] >= amount:
    user['balance'] -= amount
    user['history'].append({"date": str(datetime.now()), "transaction": f"{amount} ₺ {recipientUsername} hesabına transfer edildi"})
    recipient['balance'] += amount
    user['history'].append({"date": str(datetime.now()), "transaction": f"{amount} ₺ {user['username']} hesabından transfer edildi"})
    print(f"{amount} ₺ {recipientUsername} hesabına transfer edildi")
  else:
    print("Transfer işlemi gerçekleştirilemedi")
          
def main():
  users = loadUsers()
  while True:
    print("\n1.Giriş Yap\n2. Çıkış")
    choice = input("Seçiminiz: ")
    if choice == '1': 
      user = login(users)
      if user:
        while True:
          print("\n1. Bakiyeni Kontrol Et\n2. Para Yatır\n3. Para Çek\n4. Hesap Geçmişi\n5. Şifre Değiştir\n6. Para Transferi\n7. Çıkış")
          choice = input("Seçiminiz: ")
          if choice == '1':
            checkBalance(user)
          elif choice == '2':
            depositMoney(user)
          elif choice == '3':
            withdrawMoney(user)
          elif choice == '4':
            showHistory(user)
          elif choice == '5':
            changePassword(user)
          elif choice == '6':
            transferMoney(users, user)
          elif choice == '7':
            saveUsers(users)
            break
          else:
            print("Geçersiz seçenek lütfen tekrar deneyin")
    elif choice == '2':
      saveUsers(users)        
      break
    else:
      print("Geçersiz seçenek lütfen tekrar deneyin")

if __name__ == "__main__":
    main()