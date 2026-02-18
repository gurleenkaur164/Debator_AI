from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


class ScoringInput(BaseModel):
    argument: str = Field(
        ...,
        description="This is the argument to be scored by the judge agent"
    )



class ScoringTool(BaseTool):
    name: str = "Scoring Tool"
    description: str = (
        "This tool evaluates the factual accuracy, relevance and convincingness of the arguments presented by the agents. It uses a strict scoring system from 0 to 10 for each category. It also uses the fact check tool for checking the factual accuracy."
    )

   
    args_schema: Type[BaseModel] = ScoringInput

    def _run(self, argument: str) -> str:
    
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        
        evaluation_prompt = f"""
You are an impartial debate judge.

   Evaluate the following argument using STRICT scoring.

   Score based on:
1. Factual Accuracy (0-10)
2. Relevance to the motion (0-10)
3. Convincingness (0-10)

Return ONLY in this format:

Factual Accuracy: <score>
Relevance: <score>
Convincingness: <score>

Explanation:
<brief reasoning>

Argument:
{argument}
"""

        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a strict analytical evaluator. Do not generate new arguments."
                },
                {
                    "role": "user",
                    "content": evaluation_prompt
                }
            ],
            temperature=0.2
        )

        result = response.choices[0].message.content

        return result
