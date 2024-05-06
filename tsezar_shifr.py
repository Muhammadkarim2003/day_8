alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']



def ceaser(start_text, shift_amout, ciper_directon):
    end_text = ""
    if ciper_directon == 'decode':
          shift_amout *= -1
    for char in start_text:
      if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amout
        end_text += alphabet[new_position]
      else:
          end_text += char

      
    print(f"{ciper_directon}, Decode {end_text}")




from art import logo
print(logo)


should_countue = True
while should_countue:
    direction = input("Shifrlash uchun 'encode' deb yozing,\n shifrdan ochish uchun esa 'decode': ")
    text = input("Xabaringizni yozing: ").lower()
    shift = int(input("Siljish raqamini kiriting: "))


ceaser(start_text=text, shift_amout=shift, ciper_directon=direction)

result = input("Davom etish uchun 'yesy\nTo'xtash uchun 'no'\n")
if result == 'no':
    should_countue = False
    print("Goodbye")
    






# def encrypt(plain_text, shift_amout):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amout
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"Sizning shaifringiz {cipher_text}")


# def dicrypt(cipher_text, shift_amout):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amout
#         plain_text += alphabet[new_position]
#     print(f"Decodlangan xabar {plain_text}")



# if direction == 'encode':
#     encrypt(plain_text=text, shift_amout=shift)
# elif direction == 'decode':
#     dicrypt(cipher_text=text, shift_amout=shift)

