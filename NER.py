import streamlit as st
import spacy
from google.cloud import storage
import os

@st.cache_resource
def load_model(bucket_name, model_folder):
    storage_client = storage.Client() 
    bucket = storage_client.get_bucket(bucket_name)

    # Set the local model directory to "mounted-folder"
    local_model_dir = "mounted-folder/model-best"
    if not os.path.exists(local_model_dir):
        os.makedirs(local_model_dir)

    # Download the model files from the GCS bucket
    blobs = bucket.list_blobs(prefix=model_folder + '/')
    for blob in blobs:
        file_path = os.path.join(local_model_dir, os.path.relpath(blob.name, model_folder))
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        blob.download_to_filename(file_path)

    # Load the NER model from the mounted folder
    nlp = spacy.load(local_model_dir)
    return nlp

# Define the bucket name and model folder
bucket_name = "ner-spacy-model"
model_folder = "model-best"

# Load the NER model
nlp = load_model(bucket_name, model_folder)

# Streamlit app layout
st.header("Use of Customly Created NER Model", divider=True)
text_input = st.text_input("Enter text for Brand/Product/Model Detection:")

if text_input:
    doc = nlp(text_input)
    st.subheader("Recognized Brands/Products/Models:")
    for ent in doc.ents:
        st.write(f"  {ent.text} ({ent.label_})")
