import streamlit as st
import spacy
import os
import shutil

def load_model(mount_folder):
    # Define the source and destination paths
    source_model_dir = os.path.join(mount_folder, "model-best")
    local_model_dir = "model-best"

    # Check if the source model directory exists
    if not os.path.exists(source_model_dir):
        st.error(f"Source model directory '{source_model_dir}' does not exist.")
        return None

    # If the local model directory already exists, delete it
    if os.path.exists(local_model_dir):
        shutil.rmtree(local_model_dir)

    # Copy the model from the mounted folder to the local directory
    shutil.copytree(source_model_dir, local_model_dir)

    # Load the spaCy model from the local directory
    nlp = spacy.load(local_model_dir)
    return nlp

# Set the path to the mounted folder
mount_folder = "mounted-folder"  # Path to the mounted folder

nlp = load_model(mount_folder)

st.header("Use of Customly created NER model", divider=True)
text_input = st.text_input("Enter text for Brand/Product/Model Detection: ")

if text_input:
    doc = nlp(text_input)
    st.subheader("Recognized Brands/Products/Model:")
    for ent in doc.ents:
        st.write(f"  {ent.text} ({ent.label_})")
