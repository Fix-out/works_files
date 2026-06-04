with open("resource/secret.txt", "w", encoding="utf-8") as file:
    file.write("Это сообщение должно быть зашифровано и расшифровано")
with open("resource/secret.txt", "r", encoding="utf-8") as file:
    words = file.read()
result = ''
encrypted_text = ''
for char in words:
    if char.isalpha():
        encrypted_text += chr(ord(char) + 3)
    else:
        encrypted_text += char
with open('resource/encrypted.txt', 'w', encoding="utf-8") as file:
    file.write(encrypted_text)
with open('resource/encrypted.txt', 'r', encoding="utf-8") as file:
    encrypted_data = file.read()
for char in encrypted_data:
    if char.isalpha():
        result += chr(ord(char) - 3)
    else:
        result += char
with open('resource/decrypted.txt', 'w', encoding="utf-8") as file:
    file.write(result)
