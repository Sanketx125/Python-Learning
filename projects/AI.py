import openai
import os

# Authenticate with OpenAI API
  
# Define the prompt for the GPT-3 model
prompt = (
    "Generate a Python program that does the following:\n"
    "- Takes two numbers as input from the user\n"
    "- Adds the numbers together\n"
    "- Prints the sum of the two numbers\n"
)

# Use the GPT-3 language model to generate Python code
response = openai.Completion.create(
    engine="davinci-codex",
    prompt=prompt,
    temperature=0.5,
    max_tokens=2048,
)

# Extract the generated code from the API response
generated_code = response.choices[0].text.strip()

# Print the generated code
print(generated_code)
