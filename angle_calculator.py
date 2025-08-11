import math
import re

def normalize_angle(radians):
    """
    将弧度转换为归一化角度（0~180度）
    步骤:
      1. 弧度转角度
      2. 规范到[0, 360)区间
      3. 映射到[0, 180]区间
    """
    # 弧度转角度
    degrees = radians * 180 / math.pi
    
    # 规范到[0, 360)区间
    degrees %= 360
    if degrees < 0:
        degrees += 360
    
    # 映射到[0, 180]区间
    if degrees > 180:
        degrees = 360 - degrees
    
    return degrees

def process_input(user_input):
    """处理输入：支持逗号/空格分隔的多个数值"""
    # 替换中文逗号，分割所有数字
    cleaned = user_input.replace('，', ',')
    numbers = re.split(r'[,\s]+', cleaned)
    
    # 过滤空值并转换为浮点数
    return [float(num) for num in numbers if num]

def main():
    print("角度计算工具 (输入'exit'退出)")
    print("-----------------------------------")
    
    while True:
        # 第一组输入
        input1 = input("输入弧度值(多个用空格/逗号分隔): ").strip()
        if input1.lower() == 'exit':
            break
            
        try:
            rad_list1 = process_input(input1)
            deg_list1 = [normalize_angle(rad) for rad in rad_list1]
            
            # 单一模式：仅输出归一化角度
            if len(deg_list1) >= 1:
                formatted_degrees = [f"{deg:.6f}" for deg in deg_list1]
                print("归一化角度:", ", ".join(formatted_degrees))
            
            # 双参数模式：计算角度差
            if len(deg_list1) == 2:
                angle_diff = abs(deg_list1[0] - deg_list1[1])
                over_limit = angle_diff > 5
                print(f"角度差: {angle_diff:.6f}°, 是否超过±5°: {over_limit}")
                continue
                
            # 第二组输入（多参数模式）
            input2 = input("第二组弧度值(与第一组数量相同): ").strip()
            rad_list2 = process_input(input2)
            
            if len(rad_list1) != len(rad_list2):
                print("错误：两组数据数量不匹配")
                continue
                
            deg_list2 = [normalize_angle(rad) for rad in rad_list2]
            diffs = [abs(d1 - d2) for d1, d2 in zip(deg_list1, deg_list2)]
            
            # 输出结果
            print("\n计算结果:")
            print(f"第一组角度: [{', '.join(f'{d:.6f}' for d in deg_list1)}]")
            print(f"第二组角度: [{', '.join(f'{d:.6f}' for d in deg_list2)}]")
            print(f"角度差异: [{', '.join(f'{d:.6f}' for d in diffs)}]")
            
            # 检查超过5°的值
            over_limit_indices = [i for i, diff in enumerate(diffs) if diff > 1]
            if over_limit_indices:
                print("警告：以下位置角度差超过±1°:", ", ".join(map(str, over_limit_indices)))
            else:
                print("所有角度差均在±1°范围内")
                
        except Exception as e:
            print(f"输入错误: {e}")
        
        print("-" * 40)

if __name__ == "__main__":
    main()