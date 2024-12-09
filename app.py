
from flask import Flask, jsonify
from flask_cors import CORS
import groq
import re
import os

app = Flask(__name__)
CORS(app)

groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)  


myth_fact_prompt = (
    "Provide a common myth related to nutrition and its corresponding fact that debunks it. "
    "Write the myth first, labeled 'Myth:', and the fact immediately after, labeled 'Fact:'. "
    "Make sure the myth sounds believable but is false, and the fact is accurate and debunks the myth. "
    "Both the myth and fact should be short, 1-2 sentences each."
)


def clean_myth_fact(text):
    """Extract and clean the myth and fact from the model response"""
    
    myth_match = re.search(r"Myth:(.*?)(Fact:|$)", text, re.DOTALL)
    fact_match = re.search(r"Fact:(.*)", text, re.DOTALL)

   
    myth = myth_match.group(1).strip() if myth_match else "Myth not found."
    fact = fact_match.group(1).strip() if fact_match else "Fact not found."

    return myth, fact

def generate_myth_fact_pair(prompt):
    """ Generate a pair of myth and fact from the model """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192", 
    )

    
    processed_text = chat_completion.choices[0].message.content

   
    myth, fact = clean_myth_fact(processed_text)


    return {"myth": myth, "fact": fact}

@app.route('/generate-myths-facts', methods=['GET'])
def generate_myths_facts():
    myths_facts = []

    
    while len(myths_facts) < 1:
        myth_fact = generate_myth_fact_pair(myth_fact_prompt)
        myths_facts.append(myth_fact)

    return jsonify({"myths_facts": myths_facts})

if __name__ == '__main__':
    app.run(debug=True)
