import openai
import re
from api_key import API_KEY
from flask import Flask


openai.api_key = API_KEY
def aianswer(question):
        
    # Set the model to use
    model_engine = "text-davinci-003"
    
    # Set the prompt to generate text for
    #text = input("What topic you want to write about: ")
    text = "Get me details of the city "+question
    prompt = text
    
    print("The AI BOT is trying now to generate a new text for you...")
    # Generate text using the GPT-3 model
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Print the generated text
    generated_text = completions.choices[0].text
    return generated_text
'''
# Save the text in a file
with open("generated_text.txt", "w") as file:
    file.write(generated_text.strip())


<img src="https://unsplash.com/photos/S5UZ_pC7rC8.jpg" alt="Example Image">

print("The Text Has Been Generated Successfully!")

print(generated_text)
@app.route("/")
def index():
    return "Congratulations, it's a web app!"


<input type="email" id="email" name="email" required>
<label for="message">Message:</label>


        <form action="" method="get">
                Enter city: <input type="text" name="celsius">
                <input type="submit" value="Ask me">
            </form>"""
        + "Answer: "
        + fahrenheit`

'''


from flask import Flask
from flask import request
fahrenheit = ""
celsius = ""
app = Flask(__name__)

@app.route("/")
def index():
    fahrenheit = ""
    celsius = ""
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = aianswer(celsius)  #fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """
        
        
        <!DOCTYPE html>
<html>
  <head>
    <title>User Input Screen</title>
    <style>
      body {
        background-image: url("https://images.unsplash.com/photo-1677856216846-596a3d6d869e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80");
        background-repeat: no-repeat;
        background-size: cover;
      }
      form {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 20px;
        width: 50%;
        margin: auto;
        margin-top: 10%;
      }
      label {
        display: block;
        margin-bottom: 10px;
        font-size: 18px;
        font-weight: bold;
      }
      input[type="text"],
      input[type="email"],
      textarea {
        width: 100%;
        padding: 10px;
        font-size: 16px;
        border-radius: 5px;
        border: none;
        margin-bottom: 20px;
      }
      input[type="submit"] {
        background-color: #4caf50;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <form>
      <label for="name">Enter city:</label>
      <input type="text" id="name" name="celsius" required>
      <label for="email">Email:</label>
      <textarea id="message" name="message" rows="5" required> """+ fahrenheit+ """</textarea>
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
     """
        
        
        
        
        
        
        
        
        
        
        
        
    )


def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
app = Flask(__name__)

