# Animated GIF Generator

## Overview
This project demonstrates the creation of an animated GIF generator that combines state-of-the-art AI technologies with a user-friendly interface. By integrating **Streamlit** for interactivity, **LangChain** for workflow orchestration, GPT-powered language models for text generation, and **DALL-E** for image creation, the system enables users to effortlessly transform text prompts into animated visual stories.

## Key Components
- **Streamlit**: Provides a user-friendly interface for generating GIFs based on user input.
- **LangChain**: Orchestrates the overall workflow, managing the flow of data between different stages of the process.
- **GPT-4 (via LangChain)**: Generates detailed descriptions, plots, and image prompts based on the initial user query.
- **DALL-E 3**: Creates high-quality images based on the generated prompts.
- **Python Imaging Library (PIL)**: Assembles the individual images into a GIF animation.
- **Asynchronous Programming**: Utilizes `asyncio` to optimize image generation and retrieval.

## Methodology
1. **Interactive Input via Streamlit**: Users input a text prompt directly through the Streamlit interface.
2. **Character and Scene Description**: The system generates a detailed description of the main character or scene.
3. **Storyboarding**: A multi-step plot is created to outline the animation progression.
4. **Image Prompt Creation**: DALL-E prompts are crafted for each storyboard step.
5. **Image Generation**: DALL-E generates high-quality images for each plot step.
6. **GIF Assembly**: The generated frames are combined into a GIF using PIL.
7. **Visualization in Streamlit**: The final GIF is displayed directly in the Streamlit app for preview and download.

## Applications
- **Storytelling**: Create visually captivating stories in GIF format.
- **Education**: Explain concepts or processes with dynamic, animated visuals.
- **Content Creation**: Quickly produce unique animations for blogs, presentations, or social media.

## Conclusion
The Animated GIF Generator bridges the gap between advanced AI capabilities and user accessibility. By combining text-based input, AI-powered generation, and an intuitive interface, this tool unlocks new possibilities for creative storytelling, education, and content creation.


## Setup
1. Clone the repository:
   ```
   git clone <https://github.com/Mythreshneerugattu/GIF-generation-with-DALL-E-and-Lang-Graph.git>
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY='your_api_key_here'
   ```

## Running the Application
To run the Streamlit application, use the following command:
```
streamlit run app.py
```

## Usage
- Enter your prompt in the input box and click "Generate GIF".
- The generated GIF will be displayed below the input box.

## Generated GIF

![Screenshot](Screenshot1.png)
![Screenshot](Screenshot2.png)
![Screenshot](Screenshot3.png)
![GIF Animation](generated_animation.gif)


## License
This project is licensed under the MIT License.
