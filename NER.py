import streamlit as st
import spacy
from google.cloud import storage
import os

# Function to load the model
@st.cache_resource
def load_model(bucket_name, service_account_json, model_folder):
    # Initialize the Google Cloud Storage client
    storage_client = storage.Client.from_service_account_json(service_account_json)
    bucket = storage_client.get_bucket(bucket_name)

    local_model_dir = "model-best"
    if not os.path.exists(local_model_dir):
        os.makedirs(local_model_dir)

    # Download model files from GCS
    blobs = bucket.list_blobs(prefix=model_folder + '/')
    for blob in blobs:
        file_path = os.path.join(local_model_dir, os.path.relpath(blob.name, model_folder))
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        blob.download_to_filename(file_path)

    # Load the Spacy model
    nlp = spacy.load(local_model_dir)
    return nlp

# Set up parameters
bucket_name = "ner-spacy-model"
service_account_json = "dspl-ai-ml-coe-pocs-d5481b27bd85.json"
model_folder = "model-best"

# Load the model using the cached function
nlp = load_model(bucket_name, service_account_json, model_folder)

# Streamlit UI
st.header("Use of Customly created NER model", divider=True)
text_input = st.text_input("Enter text for Brand/Product/Model Detection: ")

if text_input:
    doc = nlp(text_input)
    st.subheader("Recognized Brands/Products/Model:")
    for ent in doc.ents:
        st.write(f"  {ent.text} ({ent.label_})")
