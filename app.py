import streamlit as st
import os
import asyncio
from gif import run_workflow  # Import the function from gif.py

# Set the title of the app
st.title("GIF Animation Generator")

# Input box for user prompt
user_query = st.text_input("Enter your prompt for GIF generation:")

# Button to generate GIF
if st.button("Generate GIF"):
    if user_query:
        try:
            # Run the workflow to generate the GIF
            result = asyncio.run(run_workflow(user_query))
            if result and result["gif_data"]:
                # Save the GIF data to a file
                gif_path = "generated_animation.gif"
                with open(gif_path, "wb") as f:
                    f.write(result["gif_data"])
                
                # Display the GIF
                st.image(gif_path, caption="Generated GIF", use_column_width=True)
            else:
                st.error("Failed to generate GIF.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a prompt.")
