
# 定义一个类
class personal_property:
    def __init__(self, name, age, tel):
        self.name = name  # 传入的同时直接创建了成员变量, 不需要在上面特别定义
        self.age = age
        self.tel = tel

    def speak(self):
        print(f'{self.name}说了一句话')
    def poop(self):
        print(f'{self.name}拉了坨大的')

class teacher(personal_property):
    def teach(self):
        print(f'{self.name}教了我一堂课')

lingo = personal_property("椎名林檎", 18, 1414123123)
mayu = teacher('樱岛麻衣',17,114514)

print(mayu.name, mayu.age, mayu.tel)
# print(zhou.speak)  # 直接print所创建的对象输出的是其内存地址(开发过程中无需关心)
print(f'{lingo.name}是天使')
mayu.speak()
mayu.teach()