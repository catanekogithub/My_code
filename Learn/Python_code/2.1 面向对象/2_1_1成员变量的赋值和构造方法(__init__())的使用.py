
# 定义一个类
class personal_info:
    name = None  # 可以省略
    age = None  # 可以省略
    tel = None  # 可以省略
    def __init__(self, name, age, tel):
        self.name = name  # 传入的同时直接创建了成员变量, 不需要在上面特别定义
        self.age = age
        self.tel = tel

    def speak(self):
        print(f'{self.name}正在说话')

zhou = personal_info("周杰伦", 18, 1414123123)
huang = personal_info('黄桃',1,'无')

print(zhou.name, zhou.age, zhou.tel)
zhou.speak()
print(zhou.speak())  # 直接print所创建的对象输出的是其内存地址(开发过程中无需关心)
print(huang.name)