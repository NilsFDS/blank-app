import streamlit as st
from pathlib import Path

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("This is a NOT a text!")

image_path = Path(__file__).parent / "pink_elephant_plot.png"
if image_path.exists():
    st.image(str(image_path), caption="Pink Elephant Outline", use_column_width=True)
else:
    st.warning("Pink elephant image not found. Please generate `pink_elephant_plot.png` in the app directory.")
