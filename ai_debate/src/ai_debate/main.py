from ai_debate.crew import AIDebate

def run():
    motion= input("Enter the topic for debate:")
    inputs={
        "motion": motion
    }
    result= AIDebate().crew.kickoff(inputs=inputs)
    print(result)

if __name__=="__main__":
    run()

