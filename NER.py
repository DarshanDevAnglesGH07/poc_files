import streamlit as st
import spacy
from google.cloud import storage
import os

bucket_name = "ner-spacy-model"
model_folder = "model-best"

mount_point = "mounted-folder"
os.system(f"gcloud storage mount {bucket_name} {mount_point}")

nlp = spacy.load(os.path.join(mount_point, model_folder))

st.header("Use of Customly created NER model", divider=True)
text_input = st.text_input("Enter text for Brand/Product/Model Detection: ")

if text_input:
    doc = nlp(text_input)
    st.subheader("Recognized Brands/Products/Model:")
    for ent in doc.ents:
        st.write(f"  {ent.text} ({ent.label_})")
