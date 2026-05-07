import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


def generate_ai_checklists(goal_name, duration_hours):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemma-4-26b-a4b-it"

    prompt = f"""
    You are a neurodivergent-friendly DevOps buddy.
    Goal: "{goal_name}"
    Available Time: {duration_hours} hours.

    Task: Slice this into 2-hour "deep work" chunks.
    Format: Monday.com compatible markdown.
    - Use '🔹 **SESSION X: [Focus]**' for headers.
    - Use '[]' for checkboxes.
    - Start each with a '5-min Grounding' step.
    - End each with 'Update Obsidian & Monday.com'.
    """

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.5,
            ),
        )
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⏳ The AI is taking a mandatory 60-second break (Rate Limit). Please try again in a minute!"
        return f"❌ Error: {str(e)}"
