def add(n1, n2):
    #pass
    return n1 + n2;

#print(add(1, 3))
#print(type(add))
#ctrl+shift+f10 : 실행


add2 = lambda n1, n2 : n1 + n2
#print(add2(100, 200))
#print(type(add2))


# class 선언
class User() :
    # 생성자 선언
    def __init__(self, name):
        self.name = name

    # toString()
    def __str__(self):
        return self.name


# class instance 생성
user = User("파이썬")
print(user) #자동으로 __str__함수 호출

'''주석
파이썬 모듈 안에는 함수와 클래스를 선언할 수 있다.
block comment
'''