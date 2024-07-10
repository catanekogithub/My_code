
#
# __str__

class personal_info:
    def __init__(self, name, age, tel):
        self.name = name  # 传入的同时直接创建了成员变量, 不需要在上面特别定义
        self.age = age
        self.tel = tel

info_input = personal_info("周杰伦", 18, 1414123123)
print(info_input)  # 直接print所创建的对象输出的是其内存地址(开发过程中无需关心)

# <__main__.personal_info object at 0x00000156F84EFF40>

class personal_info:
    def __init__(self, name, age, tel):
        self.name = name  # 传入的同时直接创建了成员变量, 不需要在上面特别定义
        self.age = age
        self.tel = tel
    def __str__(self):
        return f"返回成为字符串, name={self.name} "
    
info_input = personal_info("周杰伦", 18, 1414123123)
print(info_input)

# 返回成为字符串, name=周杰伦