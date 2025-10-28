import matplotlib.pyplot as plt
import networkx as nx
from pathlib import Path

# Membuat graf hubungan antar dataset
G = nx.DiGraph()

nodes = {
    "MNIST\n(1998)": (0, 0),
    "EMNIST\n(2017)": (-2, -2),
    "Fashion-MNIST\n(2017)": (2, -2),
    "KMNIST\n(2018)": (-2, -4),
    "QMNIST\n(2019)": (2, -4),
    "CIFAR-10\n(2009)": (-1, -6),
    "ImageNet\n(2012)": (1, -6)
}

# Menambahkan node dan edges
for n, pos in nodes.items():
    G.add_node(n, pos=pos)

edges = [
    ("MNIST\n(1998)", "EMNIST\n(2017)"),
    ("MNIST\n(1998)", "Fashion-MNIST\n(2017)"),
    ("MNIST\n(1998)", "KMNIST\n(2018)"),
    ("MNIST\n(1998)", "QMNIST\n(2019)"),
    ("EMNIST\n(2017)", "CIFAR-10\n(2009)"),
    ("Fashion-MNIST\n(2017)", "ImageNet\n(2012)")
]
G.add_edges_from(edges)

# Plot graf
pos = nx.get_node_attributes(G, 'pos')
plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=2500, edgecolors='black', linewidths=1.5)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=15, edge_color='gray', width=2)
plt.title("Evolusi dan Keterkaitan Dataset MNIST dan Turunannya", fontsize=12, fontweight='bold', pad=15)
plt.axis('off')
plt.tight_layout()

# Simpan gambar
plt.savefig("Images/mnist_dataset_evolution.png", dpi=150)
plt.show()