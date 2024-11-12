import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    # Kullanılacak karakterleri belirleme
    character_pool = ""
    if use_upper:
        character_pool += string.ascii_uppercase  # Büyük harfler
    if use_lower:
        character_pool += string.ascii_lowercase  # Küçük harfler
    if use_digits:
        character_pool += string.digits           # Sayılar
    if use_special:
        character_pool += string.punctuation      # Özel karakterler

    # Havuz boşsa hata mesajı verelim
    if not character_pool:
        return "Lütfen en az bir karakter türü seçin."

    # Şifreyi karakter havuzundan rastgele seçimlerle oluşturma
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# Kullanıcıdan bilgi alma
length = int(input("Şifrenin uzunluğunu girin: "))
use_upper = input("Büyük harf kullanılsın mı? (E/H): ").lower() == 'e'
use_lower = input("Küçük harf kullanılsın mı? (E/H): ").lower() == 'e'
use_digits = input("Sayı kullanılsın mı? (E/H): ").lower() == 'e'
use_special = input("Özel karakter kullanılsın mı? (E/H): ").lower() == 'e'

# Şifre oluşturma ve ekrana yazdırma
password = generate_password(length, use_upper, use_lower, use_digits, use_special)
print("Oluşturulan şifre:", password)
