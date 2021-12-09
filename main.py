import boto3
from tkinter import *
from tkinter import messagebox

def convert(language):
    session = boto3.session.Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_ACCESS_KEY)
    client = session.client(service_name="polly")
    # Getting the text from the text entry field
    text = text_entry.get()
    # This will start the text to speach and push the mp3 file to a S3 bucket
    response = client.start_speech_synthesis_task(
        Engine='standard',
        LanguageCode=language,
        OutputFormat='mp3',
        OutputS3BucketName='texttospeachstefanitarosculet',
        SampleRate='8000',
        Text=text,
        TextType='text',
        VoiceId="Brian"
    )
    response_message = f"Your response status is:{response['ResponseMetadata']['HTTPStatusCode']}.\nYour text is: {text}"
    messagebox.showinfo(title="Information", message=response_message)
    text_entry.delete(0, END)

def text_to_speach():
    if len(text_entry.get()) < 10:
        messagebox.showinfo(title = "Error", message="Please enter a longer text in order to benefit of this functionality!")
    else:
        convert('en-GB')

# Creating the GUI using Tkinter
window = Tk()
window.title("Text to Speach AWS Polly")
window.config(padx=50, pady=50)

canvas = Canvas(width = 200, height = 200)
tts_image = PhotoImage(file = "text_to_speach.png")
canvas.create_image(100, 100, image =tts_image)
canvas.grid(column=0, row =0)

text_label = Label(text="Text to Speach: ", fg="dark blue",font=("Verdana",20))
text_label.grid(column=0, row=1)

text_entry = Entry(width = 40, font=('Verdana',20))
text_entry.focus()
text_entry.grid(column=1, row=1)

text_to_speach_button = Button(window,text = "TextToSpeach",width =12,height=2,fg='orange',font = ("Verdana",20),command=text_to_speach)
text_to_speach_button.grid(column=1, row=0)

window.mainloop()
