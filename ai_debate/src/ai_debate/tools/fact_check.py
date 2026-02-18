from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from crewai_tools import SerperDevTool

class FactCheckInput(BaseModel):
    argument: str= Field(..., description= "The argument to be fact-checked")

class FactCheckTool(BaseTool):
    name= "Fact Check Tool"
    desccription= "Checks the factual accuracy of the argument provided by the agents."

    def _run(self, argument:str):
        search_tool= SerperDevTool()

        search_results= search_tool.run(argument)
        return f"Argument is {argument} and the factual check results are {search_results}"
