import openai
import os

# Set up your OpenAI API key (ensure it's set in your environment or use dotenv)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure you have your key set in your environment

def get_openai_response(prompt, max_tokens=100):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or use GPT-4 if available
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"
