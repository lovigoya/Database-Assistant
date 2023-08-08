import gradio as gr
import sys

sys.path.append('../')
from backend.main import *

def add_text(history,text):
    agent = main("../backend/config.json")
    output = agent.run(input=text)
    print(f"Output: {output}")
    history = history + [(text,str(output))]
    return history, gr.update(value = "", interactive = False)

with gr.Blocks() as demo:
    gr.Markdown("""
    # <center>Database Assistant</center>
    """)
    
    chatbot = gr.Chatbot([
        ("Hi!", "How can I help you? Ask me anything about your data."),
        ], elem_id="chatbot").style(height=500)
    

    with gr.Row():   
      with gr.Column():
          txt = gr.Textbox(
                show_label=False,
                placeholder="Enter text and press enter",
                ).style(container=False) 
    text_msg = txt.submit(add_text, [chatbot,txt], [chatbot, txt], queue = False).then(
        lambda: gr.update(interactive = True),None,[txt], queue= False
    )

demo.launch()