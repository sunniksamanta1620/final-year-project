import streamlit as st
import tensorflow as tf
import streamlit as st


@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('"C:\Users\sunni\potato\training-20230325T150010Z-001\training\my_model.hdf5"')
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()

st.write("""
         # potato Classification
         """
         )

file = st.file_uploader("Please upload an file", type=["jpg", "png"])
