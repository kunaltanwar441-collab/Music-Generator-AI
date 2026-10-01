import streamlit as st
import subprocess
import os

st.set_page_config(
    page_title="AI Music Generator",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 AI Music Generator")
st.markdown("### Generate Piano Music using Artificial Intelligence")

st.write("""
This application uses a trained LSTM Neural Network to generate
new MIDI music based on your training dataset.
""")

if st.button("🎼 Generate New Music"):

    with st.spinner("Generating Music... Please wait..."):

        subprocess.run(["python", "generate.py"])

    output_file = "generated/output.mid"

    if os.path.exists(output_file):

        st.success("✅ Music Generated Successfully!")

        with open(output_file, "rb") as file:

            st.download_button(
                label="⬇️ Download Generated MIDI",
                data=file,
                file_name="AI_Music.mid",
                mime="audio/midi"
            )

    else:
        st.error("❌ Failed to generate music.")