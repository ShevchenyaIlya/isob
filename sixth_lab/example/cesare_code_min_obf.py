from string import ascii_uppercase,ascii_lowercase
g=str
O=open
V=file
e=print
q=BaseException
v=None
a=Exception
z=tuple
J=int
u=list
G=enumerate
D=len
c=True
M="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
t="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
def C(filename:g)->g:
 S=""
 try:
  with O(filename,"r")as V:
   S=V.read()
  e(S)
 except q as exception:
  e(exception)
 return S
def R(S:g,filename:g)->v:
 try:
  with O(filename,"w")as V:
   V.write(S)
  e(S)
 except a as exception:
  e(exception)
def U(symbol:g)->z:
 if symbol in ascii_uppercase or symbol in ascii_lowercase:
  return ascii_lowercase,ascii_uppercase
 else:
  return M,t
def W(S:g,cipher_step:J)->g:
 S=u(S)
 for B,symbol in G(S):
  j,E=U(symbol)
  if symbol.islower():
   S[B]=j[(j.index(symbol)-cipher_step)%D(j)]
  elif symbol.isupper():
   S[B]=E[(E.index(symbol)-cipher_step)%D(E)]
 return "".join(S)
def r(S:g,cipher_step:J)->g:
 S=u(S)
 for B,symbol in G(S):
  j,E=U(symbol)
  if symbol.islower():
   S[B]=j[(j.index(symbol)+cipher_step)%D(j)]
  elif symbol.isupper():
   S[B]=E[(E.index(symbol)+cipher_step)%D(E)]
 return "".join(S)
def m(S:g,secret_key:g,*,encrypt:bool=c)->g:
 if encrypt:
  N=lambda x,y:x+y
 else:
  N=lambda x,y:x-y
 S,K=u(S),D(secret_key)
 for B,symbol in G(S):
  j,E=U(symbol)
  Y=(B%K)
  if symbol.islower():
   S[B]=j[N(j.index(symbol),j.index(secret_key[Y]))%D(j)]
  elif symbol.isupper():
   S[B]=E[N(E.index(symbol),E.index(secret_key[Y]))%D(E)]
 return "".join(S)
if __name__=='__main__':
 F=W("HELLO",5)
# Created by pyminifier (https://github.com/liftoff/pyminifier)

