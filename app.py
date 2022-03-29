import numpy as np
import pandas as pd
import streamlit as st
import pickle
import warnings
warnings.filterwarnings("ignore")
model = pickle.load(open("model.pkl","rb")) #loading the created model


st.set_page_config(page_title="CANCER Application") #tab title

#prediction function
def predict_status(radius_mean,perimeter_mean,area_mean,radius_worst,perimeter_worst,area_worst):
    input_data = np.asarray([radius_mean,perimeter_mean,area_mean,radius_worst,perimeter_worst,area_worst])
    input_data = input_data.reshape(1,-1)
    prediction = model.predict(input_data)
    return prediction[0]

def main():

    # titling your page
    st.title("cancer Prediction App")
    st.write("A quick ML app to predict cancer ")

    #getting the input
    radius_mean = st.text_input("Enter your radius_mean")
    perimeter_mean = st.text_input("Enter your perimeter_mean")
    area_mean = st.text_input("Enter your area_mean")
    radius_worst = st.text_input("Enter your radius_worst")
    perimeter_worst = st.text_input("Enter your perimeter_worst")
    area_worst = st.text_input("Enter your area_worst")



    #predict value
    diagnosis = ""

    if st.button("Predict"):
        diagnosis = predict_status(radius_mean,perimeter_mean,area_mean,radius_worst,perimeter_worst,area_worst)
        if diagnosis=="1":
            st.info("You Have an Cancer")
            #st.markdown("![You're like this!](https://i.gifer.com/L6m.gif)")
        elif diagnosis=="0":
                st.info(" not Cancer Something Else")
                #st.markdown("![You're like this!](https://i.gifer.com/L6m.gif)")

        
        else:
                st.error("noooo")

            
        st.subheader("what next? Take Action Towards Better Health")
        st.write("🙋🏼‍♂️ Maintaining a healthy weight is important for your heart health")
        st.write("🙋🏼‍♂️ Don't be like Spongebob or Patrik")
        st.write("Maintain a Healthy Weight: [ check right now!](https://www.nhlbi.nih.gov/heart-truth/maintain-a-healthy-weight)")
        
        
        
        st.write("## Thank you for Visiting \nProject by Suyog H")
        #st.markdown("<h1 style='text-align: right; color: blue; font-size: small;'><a href='https://github.com/suyog56/CANCER'>Looking for Source Code?</a></h1>", unsafe_allow_html=True)
        # st.markdown("<h1 style='text-align: right; color: white; font-size: small'>you can find it on my GitHub</h1>", unsafe_allow_html=True)

    


if __name__=="__main__":
    main()
