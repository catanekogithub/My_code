print("""说明：这是一个股价计算小程序
需要输入基本股价，增长率和增长天数
计算公式：基本股价x增长率的<增长天数>次方""")
# 公司基本信息
company = "<ANASAZI>"
stock_code = "003023"
# 基本股价
stock_price = float(input("请输入基本股价："))
#stock_price = 114
# 股票每日增长系数
stock_price_daily_growth_factor = float(input("请输入每日增长系数："))
# 增长天数
growth_day = float(input("请输入增长的天数："))
# 最终股价
finally_stock_price = stock_price*stock_price_daily_growth_factor**growth_day
# 输出
print(f"股票公司{company}-股票代码{stock_code}")
print("""目前股价:%.2s，股票增长率:%.1f，增长天数:%d，
增长后最终股价为%s""" % (stock_price, stock_price_daily_growth_factor, growth_day,finally_stock_price))
# print("增长后最终股价")
# 将存有类型为float数据的变量finally_stock_price通过int()语句转为int类型并输出其类型信息
# print(type(int(finally_stock_price)))
print(f"最终股价的数据类型为：{type(finally_stock_price)}")
