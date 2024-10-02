# from flask import Flask, jsonify
# from flask_cors import CORS
# import gc
# import groq
# import re

# app = Flask(__name__)
# CORS(app)

# # Initialize Groq client (replace with actual initialization)
# client = groq.Client(api_key="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")  # Replace with your actual API key

# # Single concise and clear prompt for the LLM
# single_prompt = (
#     "Provide a short, humorous, and simple nutritional fact in 1-2 sentences. "
#     "Avoid using introductory phrases like 'Here's a fact' or 'Did you know'. "
#     "Make it easy to understand and engaging."
# )

# def clean_fact(fact):
#     """ Remove introductory phrases and keep it concise """
#     # Regular expression to remove introductory phrases like "Here's a fact..."
#     fact = re.sub(r"^(here|did you know|what's|give me|tell me|provide|let's|here's|probiotics are|antioxidants are|vitamin c is).*?:?\s*", "", fact, flags=re.IGNORECASE)
#     # Remove leading/trailing whitespace and ensure only 1-2 sentences
#     fact = fact.strip()
#     return fact

# def generate_fact(prompt):
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt,
#             }
#         ],
#         model="llama3-8b-8192",
#     )

#     # Get the processed text from the response
#     processed_text = chat_completion.choices[0].message.content

#     # Clean and truncate the response to 1-2 sentences
#     sentences = processed_text.split('. ')
#     processed_text = '. '.join(sentences[:2]) + ('.' if len(sentences) > 1 else '')

#     # Apply additional cleaning
#     processed_text = clean_fact(processed_text)

#     # Force garbage collection to free memory
#     gc.collect()

#     return processed_text

# @app.route('/generate-facts', methods=['GET'])
# def generate_facts():
#     facts = []

#     while len(facts) < 5:
#         fact = generate_fact(single_prompt)
#         facts.append(fact)

#     return jsonify({"facts": facts})

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, jsonify
from flask_cors import CORS
import gc
import groq
import re

app = Flask(__name__)
CORS(app)

# Initialize Groq client (replace with actual initialization)
client = groq.Client(api_key="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")  # Replace with your actual API key

# Prompt to generate both myth and fact together
myth_fact_prompt = (
    "Provide a common myth related to nutrition and its corresponding fact that debunks it. "
    "Write the myth first, labeled 'Myth:', and the fact immediately after, labeled 'Fact:'. "
    "Make sure the myth sounds believable but is false, and the fact is accurate and debunks the myth. "
    "Both the myth and fact should be short, 1-2 sentences each."
)


def clean_myth_fact(text):
    """Extract and clean the myth and fact from the model response"""
    # Use regex to capture the myth and fact based on their labels
    myth_match = re.search(r"Myth:(.*?)(Fact:|$)", text, re.DOTALL)
    fact_match = re.search(r"Fact:(.*)", text, re.DOTALL)

    # Extract and clean the myth and fact
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
        model="llama3-8b-8192",  # Replace with the correct model
    )

    # Get the processed text from the response
    processed_text = chat_completion.choices[0].message.content

    # Apply additional cleaning
    myth, fact = clean_myth_fact(processed_text)

    # # Split the result into myth and fact by the first sentence break
    # myth, fact = processed_text.split('. ', 1)
    # myth = myth.strip() + '.'
    # fact = fact.strip() + '.'

    # # Force garbage collection to free memory
    # gc.collect()

    return {"myth": myth, "fact": fact}

@app.route('/generate-myths-facts', methods=['GET'])
def generate_myths_facts():
    myths_facts = []

    # Generate 2 myth-fact pairs
    while len(myths_facts) < 1:
        myth_fact = generate_myth_fact_pair(myth_fact_prompt)
        myths_facts.append(myth_fact)

    return jsonify({"myths_facts": myths_facts})

if __name__ == '__main__':
    app.run(debug=True)
