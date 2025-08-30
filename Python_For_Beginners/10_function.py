# 计算扇形面积
def calculate_area(central_angle, radius):
    sector_area = central_angle / 360 * 3.14 * radius ** 2
   # print(f"此扇形的面积为: {sector_area:.2f}")
    return sector_area

sector_area_1 = calculate_area(160, 30)
sector_area_2 = calculate_area(60, 15)
print(type(sector_area_1))
print(sector_area_1)
print(sector_area_2)