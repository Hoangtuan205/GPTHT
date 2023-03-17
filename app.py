from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

openai.api_key = "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"
model_engine = "davinci"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = generate_response(prompt)
        return render_template('index.html', prompt=prompt, response=response)
    else:
        return render_template('index.html')

def generate_response(prompt):
    # Tạo payload cho yêu cầu API của OpenAI
    data = {
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 1024,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    # Gửi yêu cầu đến OpenAI API và nhận kết quả
    response = openai.Completion.create(
        engine=model_engine,
        prompt=data["prompt"],
        max_tokens=data["max_tokens"],
        temperature=data["temperature"],
        top_p=data["top_p"],
        frequency_penalty=data["frequency_penalty"],
        presence_penalty=data["presence_penalty"]
    )
    return response.choices[0].text

if __name__ == '__main__':
    app.run(debug=True)
