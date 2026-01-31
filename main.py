from google import genai
from google.genai import  types

client = genai.Client()

uploaded_file = client.files.upload(file="cat.jpg")

def get_current_weather(location: str) -> str:
    """Returns the current weather in a given location
    
    Args:
      location: the city and state, e.g. San Francisco, CA
    Returns:
      the current temperature and humidity in the given location
    """
    return "snowy"

response = client.models.generate_content(
    model="gemini-flash-latest",
    # contents=["what do you see in this image?", uploaded_file],
    contents="what's the weather like in Seattle, Washington?",
    config=types.GenerateContentConfig(
        # system_instruction="You are a rude teacher"
        tools=[get_current_weather]
    )
)

print(response.text)