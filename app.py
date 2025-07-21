import streamlit as st
from PIL import Image
from model import generate_base_caption, stylize_caption

st.set_page_config(page_title="Visual Caption Generator", layout="centered")
st.title("🖼️ AI-Powered Image Caption Generator")
st.caption("Upload an image, generate a smart caption, then stylize it your way")

# --- Session State ---
if "base_caption" not in st.session_state:
    st.session_state.base_caption = None
if "styled_caption" not in st.session_state:
    st.session_state.styled_caption = None

st.markdown("---")

image_file = st.file_uploader("📷 **Upload your image**", type=["jpg", "jpeg", "png"])

if image_file:
    if "last_image" not in st.session_state:
        st.session_state.last_image = None

    # If a new image is uploaded, reset previous captions
    if st.session_state.last_image != image_file:
        st.session_state.last_image = image_file
        st.session_state.base_caption = None
        st.session_state.styled_caption = None

    image = Image.open(image_file)
    st.image(image, caption="Uploaded Image", width = 300)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Generate Caption"):
            with st.spinner("Generating caption..."):
                st.session_state.base_caption = generate_base_caption(image)
                st.session_state.styled_caption = None  # Reset on re-caption

    if st.session_state.base_caption:
        st.markdown("### Base Caption:")
        st.markdown(f"> {st.session_state.base_caption}")
        st.markdown("")

        col1, col2 = st.columns([3, 1])
        with col1:
            style = st.selectbox("Choose a style:", [
                "funny", "aesthetic", "poetic", "emotional", "sarcastic"
            ])
        with col2:
            if st.button("✨ Stylize Caption"):
                with st.spinner("Stylizing..."):
                    st.session_state.styled_caption = stylize_caption(
                        st.session_state.base_caption, style
                    )

    if st.session_state.styled_caption:
        st.markdown("### Stylized Caption:")
        st.markdown(f"<div style='padding: 12px; background-color: #f0f4ff; border-left: 5px solid #1f77b4; font-size: 1.1rem; font-style: italic;'>"
                    f"{st.session_state.styled_caption}"
                    f"</div>",
                    unsafe_allow_html=True)
        st.success("Done! You can try another style or re-upload an image.")
