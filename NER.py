import streamlit as st
import spacy
import os

def load_model(mount_folder):
    local_model_dir = os.path.join(mount_folder, "model-best")

    # Check if the model directory exists
    if not os.path.exists(local_model_dir):
        st.error(f"Model directory '{local_model_dir}' does not exist.")
        return None

    # Load the spaCy model
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
