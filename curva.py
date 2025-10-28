# ===========================================================
# Visualisasi Hasil Pelatihan CNN pada Dataset MNIST
# ===========================================================
import matplotlib.pyplot as plt
import numpy as np

# Simulasi data akurasi (bisa diganti dengan history.history dari model.fit)
epochs = np.arange(1, 6)
train_acc = np.array([0.965, 0.982, 0.991, 0.994, 0.996])
val_acc = np.array([0.960, 0.980, 0.987, 0.990, 0.992])

# Plot grafik
plt.figure(figsize=(8,5))
plt.plot(epochs, train_acc * 100, marker='o', label='Training Accuracy', color='royalblue')
plt.plot(epochs, val_acc * 100, marker='s', label='Validation Accuracy', color='darkorange')
plt.title('Kurva Pelatihan CNN pada Dataset MNIST', fontsize=13)
plt.xlabel('Epoch')
plt.ylabel('Akurasi (%)')
plt.xticks(epochs)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# Simpan hasil
plt.savefig("Images/mnist_cnn_training_curve.png", dpi=150)
plt.show()
