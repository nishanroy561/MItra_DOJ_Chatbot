from fastapi import FastAPI, Request
from groq import Groq
import os

# Initialize FastAPI
app = FastAPI()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Define route
@app.post("/chat")
async def chat_with_groq(request: Request):
    # Parse user input from the request
    req_data = await request.json()
    user_message = req_data.get("message", "")

    if not user_message:
        return {"error": "Message is required."}

    try:
        # Interact with Groq
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": user_message}],
            model="llama3-8b-8192",
        )
        groq_response = chat_completion.choices[0].message.content

        # Return Groq's response
        return {"response": groq_response}
    except Exception as e:
        return {"error": str(e)}
