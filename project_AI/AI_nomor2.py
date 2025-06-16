import cv2
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

def ekstrak_fitur_rata_rata_warna(image):
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rata_rata = img_rgb.mean(axis=0).mean(axis=0)
    return rata_rata

def load_dataset(folder_dataset):
    X = []
    y = []
    kelas = os.listdir(folder_dataset)
    print("Kelas ditemukan:", kelas)
    for label in kelas:
        folder_kelas = os.path.join(folder_dataset, label)
        if not os.path.isdir(folder_kelas):
            continue
        for file in os.listdir(folder_kelas):
            file_path = os.path.join(folder_kelas, file)
            img = cv2.imread(file_path)
            if img is None:
                print(f"Gagal baca gambar {file_path}")
                continue
            fitur = ekstrak_fitur_rata_rata_warna(img)
            X.append(fitur)
            y.append(label)
    return np.array(X), np.array(y)

folder_dataset = 'D:/Downloads/project_AI/dataset'

print("Loading dataset dan ekstrak fitur...")
X_train, y_train = load_dataset(folder_dataset)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
print("Model k-NN berhasil dilatih.")

path_input = input("Masukkan path file gambar buah untuk diprediksi: ")
if not os.path.isfile(path_input):
    print("File tidak ditemukan!")
    exit()

img_input = cv2.imread(path_input)
if img_input is None:
    print("Gagal membaca gambar input.")
    exit()

fitur_input = ekstrak_fitur_rata_rata_warna(img_input).reshape(1, -1)
prediksi = model.predict(fitur_input)[0]

plt.imshow(cv2.cvtColor(img_input, cv2.COLOR_BGR2RGB))
plt.title(f"Prediksi: {prediksi}", fontsize=14)
plt.axis('off')
plt.show()