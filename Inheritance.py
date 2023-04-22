'''Inheritance.py module'''
class Base:

    '''init'''
    def __init__(self):
        self.value = "Base.value"
        self._value = "Base._value"
        self.__value = "Base.__value"

    def method(self):
        print("Base.method")

    def _method(self):
        print("Base._method")

    def __method(self):
        print("Base.__method")

    def base(self):
        print('base():')
        print(self.value)
        print(self._value)
        print(self.__value)  # サブクラスと名前衝突しても自分のを使う
        self.method()
        self._method()
        self.__method()  # サブクラスと名前衝突しても自分のを使う


class Sub(Base):

    def __init__(self):
        super().__init__()
        self.value = "Sub.value"
        self._value = "Sub._value"
        self.__value = "Sub.__value"

    def method(self):
        print("Sub.method")

    def _method(self):
        print("Sub._method")

    def __method(self):
        print("Sub.__method")

    def sub(self):
        print('sub():')
        print(self.value)
        print(self._value)
        print(self.__value)  # サブクラスと名前衝突しても自分のを使う
        self.method()
        self._method()
        self.__method()  # サブクラスと名前衝突しても自分のを使う


class SubSub(Sub):

    def __init__(self):
        super().__init__()
        self.value = "SubSub.value"
        self._value = "SubSub._value"
        self.__value = "SubSub.__value"

    def method(self):
        print("SubSub.method")

    def _method(self):
        print("SubSub._method")

    def __method(self):
        print("SubSub.__method")

    def subsub(self):
        print('subsub():')
        print(self.value)
        print(self._value)
        print(self.__value)  # サブクラスと名前衝突しても自分のを使う
        self.method()
        self._method()
        self.__method()  # サブクラスと名前衝突しても自分のを使う


subsub = SubSub() # subsub = SubSub()
subsub.base()
print()
subsub.sub()
print()
subsub.subsub()

# message
subsub._Sub__method()
subsub._SubSub__method()

