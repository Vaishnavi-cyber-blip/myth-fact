# Nutrition Myths and Facts API
This Flask application generates common nutrition myths and their corresponding facts that debunk them. It uses Groq's LLaMA model(llama3-8b-8192) to generate myth-fact pairs and provides a RESTful API endpoint to access the results.

## Features
  **Flask Backend**: Lightweight web server to handle requests.  
  **CORS Support**: Enables cross-origin requests for secure frontend-backend communication.  
  **AI-Generated Content**: Generates myth-fact pairs using Groq's LLaMA model.  
  **Data Cleaning**: Extracts and formats the output to ensure clean and readable results.

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
Sends the prompt to Groq's LLaMA model.  
Processes the AI response to extract the myth and fact pair.  
Returns the result in a structured format.

## Prompt 
``` myth_fact_prompt = (
    "Provide a common myth related to nutrition and its corresponding fact that debunks it. "
    "Write the myth first, labeled 'Myth:', and the fact immediately after, labeled 'Fact:'. "
    "Both the myth and fact should be short, 1-2 sentences each."
)
```
## Interface

<p align="center">
  <img src="![myy](https://github.com/user-attachments/assets/edc58c88-099f-4e7c-b886-f73c180963c5)" alt="Image Description" width="400"/>
</p>


![myy](https://github.com/user-attachments/assets/edc58c88-099f-4e7c-b886-f73c180963c5)
