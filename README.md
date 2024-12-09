# Nutrition Myths and Facts API
This Flask application generates common nutrition myths and their corresponding facts that debunk them. It uses Groq's LLaMA model(llama3-8b-8192) to generate myth-fact pairs and provides a RESTful API endpoint to access the results.

## Features
  Flask Backend: Lightweight web server to handle requests.
  CORS Support: Enables cross-origin requests for secure frontend-backend communication.
  AI-Generated Content: Generates myth-fact pairs using Groq's LLaMA model.
  Data Cleaning: Extracts and formats the output to ensure clean and readable results.

 ## Myth-Fact Generation Function
 
``` def generate_myth_fact_pair(prompt):
    """ Generate a pair of myth and fact from the model """
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192"
    )
    processed_text = chat_completion.choices[0].message.content
    myth, fact = clean_myth_fact(processed_text)
    return {"myth": myth, "fact": fact}
 ```
