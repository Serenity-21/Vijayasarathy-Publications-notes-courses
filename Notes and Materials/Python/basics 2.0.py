#and needs both the comparisons to be either true or false, if one is true and another is false then the result will be false
from colorsys import hls_to_rgb

print('h'=='h' and 9==8)
#using or means even if one of the statement is true then the answer will be true
print('h'=='h' or 9==8)
#not results in the opposite of what the true result is, if the original result would be true then using not will result as false
print(not 99==99)
#if,else and elif are used for control the flow of the statements giving conditions to give out certain results if the conditions are met
if 'valo'=='valo' or 0==1:
    print('True')
else:
    print('nope')
hungry = False
if hungry:
    print('feedme')
else :
    print('eatshit')
vijay = "must be an idiot"
if vijay=="loves aadhi":
    print('heee')
elif vijay== 'loves vijay':
    print('i know')
elif vijay== 'must be an idiot':
    print('i know right')
else:
    print('koo')
#for is used to iterate the iterables like list, dict
my_likes=['food','sex','game']
for vijay_likes in my_likes:
  vijay= 'sexy'
if vijay=='hot':
    print('sex')
elif vijay=='sexy':
    print('food')
else:
    print('game')
#tuple unpacking where the tuples in the list are unpacked using for loop
number=[(1,2),(3,4),(5,6),(7,8)]
for a,b in number:
   print(a)
   print(b)
   print(a,b)
for _ in number:
    print(_)
d={'key':'value','key2':'value2','key3':'value3'}
for key,value in d.items():
 print(value)








