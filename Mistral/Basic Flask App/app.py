from flask import Flask, render_template, request, jsonify
from huggingface_hub import InferenceClient
import json

app = Flask(__name__)

def format_prompt(message, history):
    prompt = ""
    for user_prompt, bot_response in history:
        prompt += f"[INST] {user_prompt} [/INST]"
        prompt += f" {bot_response} "
    prompt += f"[INST] {message} [/INST]"
    return prompt

def generate(prompt, history, temperature=0.9, max_new_tokens=256, top_p=0.95, repetition_penalty=1.0):
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=42,
    )

    formatted_prompt = format_prompt(prompt, history)

    client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1")
    stream = client.text_generation(formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    output = ""

    for response in stream:
        output += response.token.text
        # yield output
    return output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    history = request.form.get('history', [])
    history = json.loads(history) # Convert the history from JSON string to list
    response = generate(user_input, history)
    history.append((user_input, response))
    return jsonify({'response': response, 'history': json.dumps(history)})

if __name__ == '__main__':
    app.run(debug=True)