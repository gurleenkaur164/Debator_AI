import gradio as gr
from ai_debate.crew import AIDebate
from dotenv import load_dotenv

load_dotenv()


def run_debate(topic):
    try:
        inputs = {
            "motion": topic
        }

        result = AIDebate().crew().kickoff(inputs=inputs)

        return result

    except Exception as e:
        return f"Error: {str(e)}"


# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown(" Analyse your debates")
    gr.Markdown("Enter a topic and watch AI agents debate!")

    topic_input = gr.Textbox(
        label="Debate Topic",
        placeholder="e.g. AI will replace human jobs"
    )

    run_button = gr.Button("Start Debate ")

    output_box = gr.Textbox(
        label="Debate Output",
        lines=20
    )

    run_button.click(
        fn=run_debate,
        inputs=topic_input,
        outputs=output_box
    )


if __name__ == "__main__":
    demo.launch()