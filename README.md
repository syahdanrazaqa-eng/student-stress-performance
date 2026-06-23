

# Prediksi Tingkat Stres Mahasiswa Menggunakan Perbandingan Random Forest dan XGBoost

## Deskripsi Proyek

Proyek ini bertujuan untuk membangun model Machine Learning yang dapat memprediksi tingkat stres mahasiswa berdasarkan pola aktivitas harian dan performa akademik.

Model yang digunakan dalam penelitian ini adalah:

- Random Forest
- XGBoost

Kedua model dibandingkan untuk menentukan model dengan performa terbaik yang kemudian diimplementasikan dalam aplikasi berbasis Streamlit.

---

# Anggota Kelompok

| Nama | NIM |
|--------|--------|
| M Syahdan Razaqa Yuhanas | 2330511107|


---

# Dataset

Dataset yang digunakan adalah **Student Lifestyle Dataset**.

## Fitur Dataset

| Fitur | Deskripsi |
|---------|---------|
| Study_Hours_Per_Day | Jam belajar per hari |
| Extracurricular_Hours_Per_Day | Jam kegiatan ekstrakurikuler |
| Sleep_Hours_Per_Day | Jam tidur per hari |
| Social_Hours_Per_Day | Jam aktivitas sosial |
| Physical_Activity_Hours_Per_Day | Jam aktivitas fisik |
| GPA | Nilai IPK mahasiswa |
| Stress_Level | Tingkat stres mahasiswa |

Jumlah data: **2000 record**

---

# Metodologi

Proyek ini menggunakan metodologi **CRISP-DM (Cross Industry Standard Process for Data Mining)**.

## 1. Business Understanding

### Latar Belakang

Tingkat stres mahasiswa dapat dipengaruhi oleh berbagai faktor seperti pola belajar, kualitas tidur, aktivitas sosial, aktivitas fisik, dan prestasi akademik.

### Problem Statement

1. Apakah data gaya hidup mahasiswa dapat digunakan untuk memprediksi tingkat stres?
2. Model mana yang memiliki performa lebih baik antara Random Forest dan XGBoost?

### Tujuan

- Membangun model prediksi tingkat stres mahasiswa.
- Membandingkan performa Random Forest dan XGBoost.
- Mengimplementasikan model terbaik ke dalam aplikasi Streamlit.

---

## 2. Data Understanding

Tahapan ini dilakukan untuk memahami karakteristik dataset yang digunakan.

Analisis yang dilakukan:

- Menampilkan informasi dataset
- Statistik deskriptif
- Distribusi tingkat stres
- Korelasi antar fitur

---

## 3. Data Preparation

Tahapan persiapan data:

- Menghapus kolom Student_ID
- Encoding target menggunakan LabelEncoder
- Memisahkan fitur dan target
- Membagi dataset menjadi data training dan testing

Train-Test Split:

- Training : 80%
- Testing : 20%

---

## 4. Modeling

### Random Forest

Parameter:

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

### XGBoost

```python
XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)
```

---

## 5. Evaluation

Metrik evaluasi yang digunakan:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

### Hasil Perbandingan

| Model         | Accuracy | Precision | Recall | F1-Score |
| ------------- | -------- | --------- | ------ | -------- |
| Random Forest | 97.50%   | 97.40%    | 97.50% | 97.40%   |
| XGBoost       | 98.25%   | 98.20%    | 98.30% | 98.20%   |




Model dengan akurasi terbaik dipilih sebagai model final untuk deployment.

---

## 6. Deployment

Model terbaik diimplementasikan menggunakan Streamlit.

### Input Pengguna

- Jam Belajar
- Jam Ekstrakurikuler
- Jam Tidur
- Jam Aktivitas Sosial
- Jam Aktivitas Fisik
- GPA

### Output

- Tingkat Stres Rendah
- Tingkat Stres Sedang
- Tingkat Stres Tinggi

---

# Struktur Repository

```text
prediksi-stres-mahasiswa/
│
├── dataset/
│   └── student_lifestyle_dataset.csv
│
├── notebook/
│   └── student_stress_prediction.ipynb
│
├── model/
│   └── stress_model.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── assets/
```

---

# Menjalankan Aplikasi Secara Lokal

## Install Dependency

```bash
pip install -r requirements.txt
```

## Jalankan Streamlit

```bash
streamlit run app.py
```

---

# Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Streamlit
- Matplotlib
- Seaborn

--- https://student-stress-performance-athavfwqukfubgvtvqkvfu.streamlit.app/

# Kesimpulan

Berdasarkan hasil eksperimen, model Machine Learning mampu memprediksi tingkat stres mahasiswa berdasarkan pola aktivitas dan performa akademik. Perbandingan antara Random Forest dan XGBoost dilakukan untuk menentukan model dengan performa terbaik yang kemudian diimplementasikan ke dalam aplikasi web menggunakan Streamlit.
