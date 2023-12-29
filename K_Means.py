#use colab for execution
#K-MEAN 
from sklearn.cluster import KMeans
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

original_image = Image.open("/content/elon musk.jpg")
original_data = np.array(original_image)

original_pixels = original_data.reshape((-1, 3))

K = 16

kmeans = KMeans(n_clusters=K, n_init=10, random_state=0)
kmeans.fit(original_pixels)
compressed_pixels = kmeans.cluster_centers_[kmeans.labels_]

compressed_data = compressed_pixels.reshape(original_data.shape).astype(np.uint8)
compressed_image = Image.fromarray(compressed_data)
fig, axes = plt.subplots(1, 2, figsize=(5, 5))
axes[0].imshow(original_data)
axes[0].set_title("Original Image")
axes[0].axis('off')

axes[1].imshow(compressed_data)
axes[1].set_title(f"Compressed Image (K={K})")
axes[1].axis('off')
plt.tight_layout()
plt.show()
compressed_image.save(f"compressed_image_K{K}.jpg")
