# import the streamlit library
import streamlit as st
from PIL import Image

# title
st.write(""" # BMI Calculator
The **Body Mass Index (BMI) Calculator** can be used to calculate BMI value and corresponding weight status while taking height into consideration.""")

# display image
img = Image.open("image.png")
st.image(img, width=200)

# Set WEIGHT input in kgs
weight = st.number_input("Enter your weight (in kgs)")
if (weight < 1):
    st.error("Please, enter your height")

# radio button to choose HEIGHT format
height_format = st.radio('Select height format: ',
                  ('cms', 'meters', 'feet'))

# compare HEGHT value
if(height_format == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')
     
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter value of height")

elif(height_format == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')
     
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter value of height")

else:
    # take height input in feet
    height = st.number_input('Feet')
     
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter value of height")

if (height < 1):
    st.error("Please, enter your height")


# check if the button is pressed or not
if(st.button('Calculate BMI')):
     
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(round(bmi,3)))
     
    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")       
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")