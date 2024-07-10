
# json数据类型的转换
# import json
# data = [{"name": "王大锤", "age": 11}, {"name": "张大山", "age": 13}]
# data2 = [{"name": "王大锤", "age": 11}, {"name": "张大山", "age": 13}]
# print(f"{data}的数据类型为{type(data)}")
# json_str = json.dumps(data, ensure_ascii=False)
# print(f"{data2}使用json转换格式之后变成{json_str},它的数据类型为{type(json_str)}")

# data = [{"name": "王大锤", "age": 11}, {"name": "张大山", "age": 13}]
# data_str = str(data)
# print(f"{data_str}的数据类型为{type(data_str)}")
 

# 简单柱状图的示例1
for r in range(10):
    # 控制开关(想用就注释一下下面的break)
    # break
    # 基础折线图的构建
    # 导入包
    # 选择图例
    dec = input("请输入想要的图表类型(折线图/ 柱状图):")
    if dec == '柱状图':
        from pyecharts.charts import Bar
        line = Bar()
    else:
        from pyecharts.charts import Line
        line = Line()
    # import全局配置功能
    from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts

    # 给折线图对象添加x轴坐标
    x = set(input("输入横坐标(逗号隔开每一个数据):").split(","))
    print(f'你输入了{len(x)}个横坐标值')
    line.add_xaxis(xaxis_data=x)
    # 添加y轴坐标
    y = input("输入纵坐标(逗号隔开每一个数据):").split(",")
    line.add_yaxis(series_name="/GDP", y_axis=y)

    # 全局配置项的配置
    line.set_global_opts(
        title_opts=TitleOpts(title="个人图表展示"),
        legend_opts=LegendOpts(is_show=True),
        toolbox_opts=ToolboxOpts(is_show=True))

    # render html file
    try:
        line.render("mycharts.html")
    except Exception as e:
        print(f"错误为:{e}")
    break





