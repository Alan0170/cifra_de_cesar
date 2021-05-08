alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 2

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:

    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Aqui está o resultado: {end_text}")


from art import logo
print(logo)


should_end = False
while not should_end:

  direction = input("Digite 'encode' para criptografar, ou digite 'decode' para descriptografar:\n")
  text = input("Digite sua mensagem:\n").lower()
  shift = int(input("Digite o número do turno:\n"))
 
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Digite 'sim' se quiser utilizar novamente. Caso contrário, digite 'nao'.\n").lower()
  if restart == "nao":
    should_end = True
    print("Programa Finalizado!")
    


