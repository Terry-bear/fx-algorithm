from collections import Counter
from statistics import mean

import xlrd
import matplotlib.pyplot as plt

# 计算市级风险值分布
def cal_city_area_fx(city_arr, fx_arr):
    area_project_count_dict = dict(Counter(city_arr))
    area_project_fx_dict = {}
    for (key, value) in area_project_count_dict.items():
        area_project_fx_dict[key] = 0
    for (key, value) in area_project_fx_dict.items():
        city_idx_arr = [i for i in range(0, len(city_arr)) if key == city_arr[i]]
        # 地区项目风险值
        city_project_arr = [fx_arr[city_idx_arr[i]] for i in range(0, len(city_idx_arr))]
        area_project_fx_dict[key] = mean(city_project_arr)
    return area_project_count_dict, area_project_fx_dict


# 计算地州风险值分布
def cal_country_area_fx(country_arr, fx_arr):
    area_project_count = Counter(country_arr)
    return area_project_count


if __name__ == '__main__':
    data = xlrd.open_workbook("./地区风险值.xlsx")
    table = data.sheet_by_index(0)
    assert table.row_len(0) == 9, "数据格式不符合标准"
    print(table.row_values(0), table.row_len(0))
    # 获取行数
    nrows = table.nrows
    # 获取列数
    ncols = table.ncols
    # 定义分层变量
    province_arr = []
    city_arr = []
    country_arr = []
    project_arr = []
    part_arr = []
    fx_arr = []
    for row in range(1, nrows):
        for col in range(ncols):
            if col == 1:
                # 省级
                province_arr.append(table.cell(row, 1).value)
            if col == 2:
                # 市级
                city_arr.append(table.cell(row, 2).value)
            if col == 3:
                # 地州
                country_arr.append(table.cell(row, 3).value)
            if col == 4:
                # 项目名
                project_arr.append(table.cell(row, 4).value)
            if col == 5:
                # 主管部门
                part_arr.append(table.cell(row, 5).value)
            if col == 6:
                # 风险值
                fx_arr.append(table.cell(row, 6).value)
    # 项目风险值分布情况
    # plt.scatter(fx_arr, country_arr)
    # plt.show()
    area_project_count_dict, area_project_fx_dict = cal_city_area_fx(city_arr, fx_arr)
    print("地区总量", area_project_count_dict)
    print("地区平均风险值", area_project_fx_dict)
