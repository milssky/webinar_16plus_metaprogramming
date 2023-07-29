class MetaClass(type):
    """
    Описание принимаемых параметров:

    mcs – объект метакласса, например <__main__.MetaClass>
    name – строка, имя класса, для которого используется 
      данный метакласс, например "User"
    bases – кортеж из классов-родителей, например (SomeMixin, AbstractUser)
    attrs – dict-like объект, хранит в себе значения атрибутов и методов класса
    cls – созданный класс, например <__main__.User>
    extra_kwargs – дополнительные keyword-аргументы переданные в сигнатуру класса
    args и kwargs – аргументы переданные в конструктор класса 
      при создании нового экземпляра
    """
    def __new__(mcs, name, bases, attrs, **extra_kwargs):
        print("Meta new")
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs, **extra_kwargs):
        print("Meta init")
        super().__init__(cls)  

    @classmethod  
    def __prepare__(mcs, cls, bases, **extra_kwargs):
        print("Meta prepare")
        return super().__prepare__(mcs, cls, bases, **extra_kwargs)

    def __call__(cls, *args, **kwargs):
        print("Meta call")
        return super().__call__(*args, **kwargs)


class User(metaclass=MetaClass):

    def __new__(cls, name):  
        return super().__new__(cls)  

    def __init__(self, name):  
        self.name = name

user = User(name='Vanya')

print(user.name)

