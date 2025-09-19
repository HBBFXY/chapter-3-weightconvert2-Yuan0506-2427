initial_weight = 50  
for year in range(1, 11):
    earth_weight = initial_weight + 0.5 * year
    moon_weight = earth_weight * 0.165
    print(f"第{year}年，地球体重：{earth_weight:.2f}公斤，月球体重：{moon_weight:.2f}公斤")
