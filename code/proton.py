import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

# ===== 解决中文显示问题 =====
try:
    mpl.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Micro Hei', 'DejaVu Sans']
    mpl.rcParams['axes.unicode_minus'] = False
except:
    pass

# ===== 参数设置 =====
L = 1.0
r_center = 0.15
r_outer = 0.12

# ===== 三个夸克环的方向向量（120°对称） =====
dirs = np.array([
    [1, 0, 0],
    [-0.5, np.sqrt(3)/2, 0],
    [-0.5, -np.sqrt(3)/2, 0]
])
dirs = dirs / np.linalg.norm(dirs, axis=1, keepdims=True)

# ===== 外围节点生成 =====
outer_nodes = []
global_ref = np.array([0, 0, 1])

for i, d in enumerate(dirs):
    if np.allclose(np.abs(np.dot(d, global_ref)), 1.0):
        ref = np.array([1, 0, 0])
    else:
        ref = global_ref
    e1 = np.cross(d, ref)
    e1 = e1 / np.linalg.norm(e1)
    e2 = np.cross(d, e1)
    e2 = e2 / np.linalg.norm(e2)
    
    n1 = L * (e1 * 0.7 + e2 * 0.7)
    n2 = L * (e1 * 0.7 - e2 * 0.7)
    
    outer_nodes.append(n1)
    outer_nodes.append(n2)

outer_nodes = np.array(outer_nodes)
center = np.array([0, 0, 0])

# ===== 绘图 =====
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# 中心节点
ax.scatter(*center, color='red', s=200, edgecolors='black', linewidths=2, zorder=10, label='中心节点')

# 外围节点
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for i in range(3):
    idx1 = i*2
    idx2 = i*2 + 1
    ax.scatter(outer_nodes[idx1,0], outer_nodes[idx1,1], outer_nodes[idx1,2], 
               color=colors[i], s=150, edgecolors='black', linewidths=1.5, zorder=5)
    ax.scatter(outer_nodes[idx2,0], outer_nodes[idx2,1], outer_nodes[idx2,2], 
               color=colors[i], s=150, edgecolors='black', linewidths=1.5, zorder=5)

# 夸克环（三角形）
for i in range(3):
    idx1 = i*2
    idx2 = i*2 + 1
    nodes = [center, outer_nodes[idx1], outer_nodes[idx2], center]
    xs = [n[0] for n in nodes]
    ys = [n[1] for n in nodes]
    zs = [n[2] for n in nodes]
    ax.plot(xs, ys, zs, color=colors[i], linewidth=2.5, alpha=0.8, 
            label=f'夸克环 {i+1}')

# 径向边（虚线）
for n in outer_nodes:
    ax.plot([center[0], n[0]], [center[1], n[1]], [center[2], n[2]], 
            color='gray', linestyle=':', linewidth=1.5, alpha=0.6)

# ===== 横向连接（六条虚线，两组对应关系） =====
for i in range(3):
    j = (i + 1) % 3
    # 第一组：环i的第一个节点 → 环j的第一个节点（同侧）
    n1 = outer_nodes[i*2]
    n2 = outer_nodes[j*2]
    ax.plot([n1[0], n2[0]], [n1[1], n2[1]], [n1[2], n2[2]], 
            color='purple', linestyle='--', linewidth=1.5, alpha=0.5)
    # 第二组：环i的第二个节点 → 环j的第二个节点（同侧）
    n1 = outer_nodes[i*2 + 1]
    n2 = outer_nodes[j*2 + 1]
    ax.plot([n1[0], n2[0]], [n1[1], n2[1]], [n1[2], n2[2]], 
            color='purple', linestyle='--', linewidth=1.5, alpha=0.5)

# 坐标轴与视角
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.set_title('质子三维扇叶结构\n(3个夸克环共享中心节点, 非共面分布)', fontsize=14)

ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.view_init(elev=20, azim=60)

ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3)

# 标注节点
ax.text(center[0]-0.15, center[1]-0.15, center[2]-0.15, 'O', color='red', fontsize=12, fontweight='bold')
for i, n in enumerate(outer_nodes):
    label = f'P{i+1}'
    ax.text(n[0]+0.08, n[1]+0.08, n[2]+0.08, label, color='black', fontsize=9)

plt.tight_layout()
plt.savefig('proton_3d_structure_corrected.png', dpi=300, bbox_inches='tight')
plt.show()

print("=" * 50)
print("质子三维扇叶结构 - 节点坐标")
print("=" * 50)
print(f"中心节点 O: ({center[0]:.3f}, {center[1]:.3f}, {center[2]:.3f})")
print("\n外围节点:")
for i, n in enumerate(outer_nodes):
    ring = i // 2 + 1
    print(f"  夸克环{ring} P{i+1}: ({n[0]:.3f}, {n[1]:.3f}, {n[2]:.3f})")
print("=" * 50)