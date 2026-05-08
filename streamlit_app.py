import streamlit as st
from pathlib import Path

base_path = Path(__file__).parent

st.title("🎈 Madlen and Nils Go for a Run")
st.write(
    "Welcome to a bright story about Madlen, the pink elephant who wants to go running with her friend Nils."
)

st.header("Meet Madlen")
st.write(
    "Madlen is excited for a run across the meadow with Nils, her blue giraffe friend. She is not worried about the Hafengeburtstag event later that day, "
    "because she knows her friends will still be there when she joins them afterward."
)

pink_elephant = base_path / "pink_elephant_plot.png"
if pink_elephant.exists():
    st.image(str(pink_elephant), caption="Madlen and Nils getting ready for their run.", use_column_width=True)
else:
    st.warning("Madlen picture not found. Generate `pink_elephant_plot.png` first.")

st.header("A Sunny Run")
st.write(
    "One sunny morning, Madlen and Nils lace up their shoes and run through the meadow together. "
    "They smile at the flowers and enjoy the breeze, knowing the Hafengeburtstag celebration will wait for them later."
)

meadow_image = base_path / "madlen_meadow.png"
if meadow_image.exists():
    st.image(str(meadow_image), caption="Madlen and Nils running together under a rainbow.", use_column_width=True)
else:
    st.warning("Meadow picture not found. Generate `madlen_meadow.png` first.")

st.header("Friends Still Waiting")
st.write(
    "After their run, Madlen and Nils head toward the Hafengeburtstag celebration. "
    "They are happy knowing their friends will still be there when they arrive, ready to share music, laughter, and treats."
)

friend_image = base_path / "madlen_friend.png"
if friend_image.exists():
    st.image(str(friend_image), caption="Madlen and Nils arriving at Hafengeburtstag together.", use_column_width=True)
else:
    st.warning("Friend picture not found. Generate `madlen_friend.png` first.")

st.write("**The end.** Thank you for visiting Madlen and Nils on their joyful run!")
