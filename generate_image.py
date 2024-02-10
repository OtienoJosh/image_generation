import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    try:
        # Send request to OpenAI API to generate image based on the prompt
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=50  # Adjust as needed
        )

        # Get the generated image from the response
        generated_image = response.choices[0].text.strip()
        print("Generated image:", generated_image)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Prompt Copilot with a description of the image you want to generate
    prompt = input("Enter a description of the image you want to generate: ")

    # Generate the image based on the prompt
    generate_image(prompt)
