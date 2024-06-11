import streamlit as st
from PIL import Image
from rembg import remove
import io

st.title("Image Background Removal App")

# Allow user to upload an image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    
    # Display the original image
    st.image(image, caption='Original Image', use_column_width=True)
    
    # Button to remove the background
    if st.button('Remove Background'):
        # Remove the background
        output_image = remove(image)
        
        # Display the image with the background removed
        st.image(output_image, caption='Image with Background Removed', use_column_width=True)
        
        # Convert the output image to bytes
        buffered = io.BytesIO()
        output_image.save(buffered, format="PNG")
        buffered.seek(0)
        
        # Provide an option to download the result
        st.download_button(
            label="Download Image",
            data=buffered,
            file_name="image_no_bg.png",
            mime="image/png"
        )
# Footer
st.write("Developed by Naveen Kumar.")
