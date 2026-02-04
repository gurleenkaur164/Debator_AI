from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
#python-dotenv loads the .env file from the OS environment
load_dotenv()

llm= ChatGroq(
    model="llama3-8b-8192",
    temperature= 0.3

)

debate_text= """ 
  Speaker A: Social media reduces our attention spans.
  Speaker B: Social media keeps us connected with the world.
"""

prompt= f"""

You are a professional debate judge. Given the following debate between two speakers, provide:
1. A summary of points made by speaker A.
2. A summary of the points made by speaker B.
3. Your decision on who won the debate and why.
Debate:{debate_text}
"""

response= llm.invoke(prompt)
print("The debate analysis is shown here")
print(response)