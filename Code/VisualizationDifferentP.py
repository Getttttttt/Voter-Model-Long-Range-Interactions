import matplotlib.pyplot as plt
import pandas as pd

# 文件路径和对应的标签
file_paths = [
    "./data/pchange_N10000/p_0_N_10000.txt",
    "./data/pchange_N10000/p_0.0001_N_10000.txt",
    "./data/pchange_N10000/p_0.0002_N_10000.txt",
    "./data/pchange_N10000/p_0.0005_N_10000.txt",
    "./data/pchange_N10000/p_0.001_N_10000.txt",
]
labels = [
    "p=0.0000, N=10000",
    "p=0.0001, N=10000",
    "p=0.0002, N=10000",
    "p=0.0005, N=10000",
    "p=0.0010, N=10000",
]

# 颜色和标记
colors = ['blue', 'green', 'red', 'purple', 'orange']
markers = ['o', '^', 's', 'x', '*']  


# 绘图设置
plt.figure(figsize=(10, 8))
plt.title('Voter Model: n_a(t) Evolution for Different p (N = 10000)')
plt.xlabel('Time Steps')
plt.ylabel('n_a(t)')
plt.xscale('log')  # 设置横轴为对数尺度

# 读取和绘制数据
for file_path, label, color, marker in zip(file_paths, labels, colors, markers):
    # 读取数据时指定列名
    data = pd.read_csv(file_path, delim_whitespace=True, header=None, names=['step', 'na'])
    plt.plot(data['step'], data['na'], label=label, color=color, marker=marker, linestyle='-', markersize=6, linewidth=1, markevery=0.0001)

plt.legend()
plt.show()
