# calculator_class.py

# 클래스 생성
class Calc:
    def __init__(self):  # 생성자 메서드
        self.a = 0       # 멤버 변수 생성 및 초기화  
        self.b = 0       # 멤버 변수 생성 및 초기화  
        self.c = 0       # 멤버 변수 생성 및 초기화  
        
    def add(self,a,b):   # 인스턴스 메서드
        self.a = a
        self.b = b
        self.c = self.a + self.b
        return self.c

    def subtract(self,a,b):
        self.a = a
        self.b = b
        self.c = self.a - self.b
        return self.c

    def multiply(self,a,b):
        self.a = a
        self.b = b
        self.c = self.a * self.b
        return self.c

    def divide(self,a,b):
        self.a = a
        self.b = b
        self.c = self.a / self.b
        return self.c

if __name__ == '__main__':
    
    c1 = Calc()      # 인스턴스 객체의 생성
    ret = c1.add(10,20)
    print(ret)

    ret = c1.subtract(50,30)
    print(ret)
    
    print(c1.a,c1.b,c1.c)

