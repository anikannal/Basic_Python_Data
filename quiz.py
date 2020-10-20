from ipywidgets import widgets, Layout, Box, GridspecLayout
import pandas
import numpy as np

##Basic mcq

def create_mcq(description, options, correct_answer, hint):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        layout={'width': 'max-content'},
        disabled = False,
        indent = False,
        align = 'center',
    )
    
    description_out = widgets.Output(layout=Layout(width='auto'))
    
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(float(alternativ.value))
        if a==correct_answer_index:
            s = '\x1b[6;30;42m' + "correct" + '\x1b[0m' +"\n"
        else:
            s = '\x1b[5;30;41m' + "try again" + '\x1b[0m' +"\n"
        with feedback_out:
            feedback_out.clear_output()
            print(s)
        return
    
    check = widgets.Button(description="check")
    check.on_click(check_selection)
    
#    hint_out = widgets.Output()
    
#     def hint_selection(b):
#         with hint_out:
#             print(hint)
            
#         with feedback_out:
#             feedback_out.clear_output()
#             print(hint)
    
    #hintbutton = widgets.Button(description="hint")
    #hintbutton.on_click(hint_selection)
    
    return widgets.VBox([description_out, 
                         alternativ, 
                         widgets.HBox([check]), feedback_out], 
                        layout=Layout(display='flex',
                                     flex_flow='column',
                                     align_items='stretch',
                                     width='auto')) 



def quiz_me(filename):
    #print(__file__)
    df = pandas.read_excel("./data/quizzes/"+filename, sheet_name='Sheet1')
    
    questions = []

    for i in range(len(df)):
        questions.append(create_mcq(str(i+1)+ ". " + df.iloc[i,0], [df.iloc[i,1], df.iloc[i,2], df.iloc[i,3], df.iloc[i,4]], df.iloc[i,5] ,''))

    for i in range(len(questions)):
        display(questions[i])