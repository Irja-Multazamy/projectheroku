import streamlit as st

st.title("Web Datamining")
st.write("""
# Klasifikasi Student Performance in Exams Dataset
Applikasi Berbasis Web untuk Mengklasifikasi Kinerja Siswa dalam Ujian
""")

algoritma = st.sidebar.selectbox(
    "Pilih Algoritma",
    ("KNN", "Naive Bayes", "Random Forest")
)
st.subheader("Parameter Inputan")

addres = st.text_input("Masukkan Addres :")
file = st.text_input("Masukkan File :")
english = st.number_input("Masukkan Nilai English :")
math = st.number_input("Masukkan Nilai Math :")
sciences = st.number_input("Masukkan Nilai Sciences :")
language = st.number_input("Masukkan Nilai Language :")
hasil = st.button("Cek Klasifikasi")
