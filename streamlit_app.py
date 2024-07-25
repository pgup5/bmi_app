import streamlit as st

import streamlit as st

st.title("BMI Calculator")

# Gender selection
gender = st.radio("Gender", ("Male", "Female"))

# Height input
height = st.slider("Height (cm)", 150, 190)

# Weight input
weight = st.slider("Weight (kg)", 40, 120)

# Calculate BMI
bmi = weight / ((height / 100) ** 2)

# Display Result
st.write("## Result")
st.write(f"**BMI:** {bmi:.1f}")

# Interpretation
st.write("## Interpretation")
if bmi < 18.5:
    st.write("Underweight")
elif 18.5 <= bmi < 24.9:
    st.write("Normal weight")
elif 25 <= bmi < 29.9:
    st.write("Overweight")
else:
    st.write("Obesity")

