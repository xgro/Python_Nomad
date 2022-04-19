# a = 2
# b = 3
# print(a+b)


# 자료형 연습 1
# a = 'like this' 
# b = 3
# c = True
# print(c)

# 자료형 연습 2
a_string = "like this"
a_number = 3
a_float = 3.12
a_boolean = False
a_none = None

print(type(a_none))

#Python content Type : Snake_


# https://docs.python.org/3/library/ 파이썬 참조 공식 문서
# 1-0 자료형 연습 list
days = ["Mon","Tue","Wed","Thur","Fri"]

print(days)
print(type(days)) 
print("Mon" in days)
print(days[3])
print(len(days))


# 1-1 자료형 연습 tuples Immutable variables
days = ("Mon","Tue","Wed","Thur","Fri")

print(days)
print(type(days)) 
print("Mon" in days)
print(len(days))




# 1-2 자료형 연습 dict 
xgro = {
    "name" : "chan",
    "age" : "20",
    "korean" : True,
    "fav_food" : ["kimchi","sashimi"]
}
    

print(xgro)
xgro["handsome"] = True
print(xgro)