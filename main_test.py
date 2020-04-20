from stats.descriptive_stats import std, mean


def fx(data):
    yita = 0.25
    B = 100

    return mean(data) + std(data) / mean(data)*B*0.2


if __name__ == '__main__':
    # 高离散数据组
    data3 = [70, 6, 99, 13, 50, 20, 80, 89, 90, 21]
    # 聚合型数据组
    data4 = [60, 66, 69, 73, 69, 60, 68, 69, 80, 71]
    print("地区风险值:", fx(data3), std(data3) / mean(data3))
    print("地区风险值:", fx(data4), std(data4) / mean(data4))
