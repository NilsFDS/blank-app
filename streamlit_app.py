import streamlit as st
from pathlib import Path

base_path = Path(__file__).parent

st.title("🎈 Madlen the Pink Elephant")
st.write(
    "Welcome to a gentle story about Madlen, a bright pink elephant with a big heart."
)

st.header("Meet Madlen")
st.write(
    "Madlen is a kind little elephant who loves to explore the meadow, share smiles, and paint the sky with her imagination. "
    "Every day feels like a happy adventure when she is around."
)

pink_elephant = base_path / "pink_elephant_plot.png"
if pink_elephant.exists():
    st.image(str(pink_elephant), caption="Madlen the pink elephant.", use_column_width=True)
else:
    st.warning("Madlen picture not found. Generate `pink_elephant_plot.png` first.")

st.header("A Rainbow Morning")
st.write(
    "One morning, Madlen wakes under cotton candy clouds and finds a rainbow stretching across the meadow. "
    "She dances through the flowers, humming a happy tune as bright colors follow her path."
)

meadow_image = base_path / "madlen_meadow.png"
if meadow_image.exists():
    st.image(str(meadow_image), caption="Madlen dances under a rainbow.", use_column_width=True)
else:
    st.warning("Meadow picture not found. Generate `madlen_meadow.png` first.")

st.header("A Friend for Madlen")
st.write(
    "Madlen meets a little bird who chirps, ‘Let’s play together!’ They share stories and watch the sun sparkle. "
    "With every smile, the world feels a little softer and brighter."
)

friend_image = base_path / "madlen_friend.png"
if friend_image.exists():
    st.image(str(friend_image), caption="Madlen and her bird friend.", use_column_width=True)
else:
    st.warning("Friend picture not found. Generate `madlen_friend.png` first.")

st.write("**The end.** Thank you for visiting Madlen on her happy day!")
