import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("stress_model.pkl", "rb"))

st.set_page_config(
    page_title="Prediksi Tingkat Stres Mahasiswa",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Prediksi Tingkat Stres Mahasiswa")
st.write(
    "Aplikasi ini memprediksi tingkat stres mahasiswa "
    "berdasarkan pola aktivitas harian dan performa akademik."
)

st.divider()

# Input User
study_hours = st.slider(
    "Jam Belajar per Hari",
    min_value=0.0,
    max_value=12.0,
    value=4.0,
    step=0.5
)

extracurricular_hours = st.slider(
    "Jam Kegiatan Ekstrakurikuler per Hari",
    min_value=0.0,
    max_value=10.0,
    value=2.0,
    step=0.5
)

sleep_hours = st.slider(
    "Jam Tidur per Hari",
    min_value=3.0,
    max_value=12.0,
    value=7.0,
    step=0.5
)

social_hours = st.slider(
    "Jam Bersosialisasi per Hari",
    min_value=0.0,
    max_value=10.0,
    value=2.0,
    step=0.5
)

physical_hours = st.slider(
    "Jam Aktivitas Fisik per Hari",
    min_value=0.0,
    max_value=6.0,
    value=1.0,
    step=0.5
)

gpa = st.slider(
    "GPA / IPK",
    min_value=0.0,
    max_value=4.0,
    value=3.0,
    step=0.01
)

# Prediksi
if st.button("Prediksi Tingkat Stres"):

    input_data = pd.DataFrame({
        "Study_Hours_Per_Day": [study_hours],
        "Extracurricular_Hours_Per_Day": [extracurricular_hours],
        "Sleep_Hours_Per_Day": [sleep_hours],
        "Social_Hours_Per_Day": [social_hours],
        "Physical_Activity_Hours_Per_Day": [physical_hours],
        "GPA": [gpa]
    })

    prediction = model.predict(input_data)[0]

    # Sesuaikan dengan hasil LabelEncoder
    label_map = {
        0: "High",
        1: "Low",
        2: "Moderate"
    }

    result = label_map.get(prediction, prediction)

    st.subheader("Hasil Prediksi")

    if result == "High":
        st.error("🔴 Tingkat Stres Tinggi")
    elif result == "Moderate":
        st.warning("🟡 Tingkat Stres Sedang")
    else:
        st.success("🟢 Tingkat Stres Rendah")

    st.write(f"**Prediksi Model:** {result}")

st.divider()

st.caption(
    "Proyek Machine Learning - Prediksi Tingkat Stres Mahasiswa "
    "menggunakan Random Forest dan XGBoost"
)