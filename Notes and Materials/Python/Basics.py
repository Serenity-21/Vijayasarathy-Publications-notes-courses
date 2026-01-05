print('Naandhandaleo')
me='Naandhandaleo'
print(me)
print(me[2:9:3])
print("Hi da \nbyeda")
me='1'
you='2'
print(me+you)
my_list=['podapunda',100,2.69]
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[0:2])
print(my_list[::-1])
print(my_list[0:2:2])
another_list=['hida',2,69.69,'yesda']
print(another_list)
print(my_list+another_list)
print(my_list[0] + another_list[0])
my_list[1]=200
print(my_list)
another_list[1]=4
print(my_list[1]+another_list[1])
my_list.append('vikram')
print(my_list[3])
my_list.remove('vikram')
print(my_list)
new_list=my_list+another_list
print(new_list)
new_list.pop()
print(new_list)
new_list.append('yesda')
print(new_list)
num_list=[1,3,5,7,2,4,0]
num_list.sort()
print(num_list)
vijay_varigal=[1,2,3,78,90]
#dict is flexible compared to list, you cant perform slice or index in dict as it is unordered
my_dick={'k1':5,'k2':6,'k3':7,'k4':8}
print(my_dick['k1'])
new_dick={'k1':0,'k2':[1,2,3,],'k3':{'vijay':7}}
print(new_dick['k3']['vijay'])
print(new_dick['k2'][2])
print(new_dick.items())
print(new_dick.keys())
print(new_dick.values())
new_dick['k1']='sexy'
print(new_dick['k1'].upper())
t=(1,1,5,6,)
print(t.count(1))
print(t.index(5))
#set cant add same values, it gotta be unique
set=set()
set.add(1)
set.add('dick')
print(set)
list=(1,1,1,1,1,1)
set.add(list)
print(set)
#Booleans are operators that allow you to convey True or False statements
a=1
b=1
a=True
b=False
print(a+b)
print(bool(a))
print(bool(b))
print(bool(a+b))
#creating file
content='Vijay is an idiot'
file_path= "vijay.txt"
with open(file_path,'w')as file:
    file.write(content)
    print(f"File {file_path} has been created")
my_file= open('vijay.txt')
print(my_file.read())
print(my_file.read())
print(my_file.read())
my_file.seek(0)
print(my_file.read())
content=my_file.read()
print(content)
new_file= open("D:\\valo.txt")
cont=new_file.read()
with open("D:\\valo.txt", "a") as file:
    newcontent= '\nbrim gotta booty'
    file.write(newcontent)










