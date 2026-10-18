import streamlit as st
import numpy as np
import joblib

# โหลดโมเดลที่บันทึกไว้
model = joblib.load('calories_model.pkl')

st.title("🔥 Calories Burnt Prediction App")
st.write("กรอกข้อมูลการออกกำลังกายของคุณเพื่อทำนายปริมาณแคลอรีที่เผาผลาญ")

# สร้างช่องรับข้อมูลหน้าเว็บ (UI)
gender = st.selectbox("เพศ", ["Male", "Female"])
age = st.slider("อายุ (ปี)", 10, 100, 25)
height = st.number_input("ส่วนสูง (ซม.)", 100.0, 220.0, 170.0)
weight = st.number_input("น้ำหนัก (กก.)", 30.0, 200.0, 65.0)
duration = st.slider("ระยะเวลาออกกำลังกาย (นาที)", 1, 120, 30)
heart_rate = st.slider("อัตราการเต้นของหัวใจ (BPM)", 60, 200, 110)
body_temp = st.number_input("อุณหภูมิร่างกาย (°C)", 35.0, 42.0, 39.5)

# ปุ่มกดทำนาย
if st.button("คำนวณแคลอรี"):
    # แปลงเพศเป็นตัวเลข (Male = 0, Female = 1 ตามที่เทรนโมเดลไว้)
    gender_val = 0 if gender == "Male" else 1
    
    # รวมข้อมูลเป็น Array
    input_data = np.array([[gender_val, age, height, weight, duration, heart_rate, body_temp]])
    
    # ทำนายผล
    prediction = model.predict(input_data)
    
    # แสดงผลลัพธ์
    st.success(f"Estimated Calories Burnt: **{prediction[0]:.2f} kcal**")