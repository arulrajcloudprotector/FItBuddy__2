import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL_NAME = "gemini-3.8-flash"


async def stream_workout_gemini(goal, intensity):
    """Async generator yielding 3-day workout plan chunks."""
    prompt = f"""You are a professional fitness trainer. Create a personalized 3-day workout plan.

Fitness goal: {goal}
Preferred intensity: {intensity}

For each day include:
- Warm-up (5-10 mins)
- Main workout (exercises with sets and reps)
- Cooldown

Format:
Day 1:
Warm-up: ...
Main Workout: ...
Cooldown: ...
(Repeat for Day 2 and Day 3)

Keep the plan concise and clear."""
    try:
        stream = client.models.generate_content_stream(
            model=MODEL_NAME,
            contents=prompt
        )
        for chunk in stream:
            if chunk.text:
                yield chunk.text
    except Exception as e:
        yield f"API Error: {str(e)}"


async def update_workout_plan(original_plan, feedback):
    """Regenerate the plan based on user feedback."""
    prompt = f"""You are a professional fitness trainer.
Here is the original 3-day workout plan:
{original_plan}

The user has given this feedback: "{feedback}"

Revise the plan based on this feedback. Keep the same 3-day format and change only what's needed."""
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"API Error: {str(e)}"