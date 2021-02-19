from string import ascii_uppercase,ascii_lowercase
russian_lowercase="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
russian_uppercase="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
def load_file(filename:str)->str:
 text=""
 try:
  with open(filename,"r")as file:
   text=file.read()
  print(text)
 except BaseException as exception:
  print(exception)
 return text
def save_to_file(text:str,filename:str)->None:
 try:
  with open(filename,"w")as file:
   file.write(text)
  print(text)
 except Exception as exception:
  print(exception)
def choose_sequence(symbol:str)->tuple:
 if symbol in ascii_uppercase or symbol in ascii_lowercase:
  return ascii_lowercase,ascii_uppercase
 else:
  return russian_lowercase,russian_uppercase
def caesar_encrypt(text:str,cipher_step:int)->str:
 text=list(text)
 for index,symbol in enumerate(text):
  lower_letters,upper_letters=choose_sequence(symbol)
  if symbol.islower():
   text[index]=lower_letters[(lower_letters.index(symbol)-cipher_step)%len(lower_letters)]
  elif symbol.isupper():
   text[index]=upper_letters[(upper_letters.index(symbol)-cipher_step)%len(upper_letters)]
 return "".join(text)
def caesar_decrypt(text:str,cipher_step:int)->str:
 text=list(text)
 for index,symbol in enumerate(text):
  lower_letters,upper_letters=choose_sequence(symbol)
  if symbol.islower():
   text[index]=lower_letters[(lower_letters.index(symbol)+cipher_step)%len(lower_letters)]
  elif symbol.isupper():
   text[index]=upper_letters[(upper_letters.index(symbol)+cipher_step)%len(upper_letters)]
 return "".join(text)
def vigener_cipher(text:str,secret_key:str,*,encrypt:bool=True)->str:
 if encrypt:
  operation=lambda x,y:x+y
 else:
  operation=lambda x,y:x-y
 text,key_len=list(text),len(secret_key)
 for index,symbol in enumerate(text):
  lower_letters,upper_letters=choose_sequence(symbol)
  additional_value=(index%key_len)
  if symbol.islower():
   text[index]=lower_letters[operation(lower_letters.index(symbol),lower_letters.index(secret_key[additional_value]))%len(lower_letters)]
  elif symbol.isupper():
   text[index]=upper_letters[operation(upper_letters.index(symbol),upper_letters.index(secret_key[additional_value]))%len(upper_letters)]
 return "".join(text)
if __name__=='__main__':
 data=caesar_encrypt("HELLO",5)
# Created by pyminifier (https://github.com/liftoff/pyminifier)

