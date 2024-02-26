import sys
import subprocess
import os
from docx import Document
from openai import OpenAI, RateLimitError
from docx.shared import Pt
import argparse
from config import API, COVERLETTERS, JOBDESCRIPTION, WORKEXPERIENCE, EDUCATION

## HOW TO SET UP

## Create 3 files, 1 to store the job description, 1 to store your education, and 1 to store your work experience, 
## save them locally in the same directory

## Create a directory to store the saved Cover Letters

## Grab an api key from OpenAi.com




key = API ## API key to interact with OpenAI
outputdir = COVERLETTERS ## Directory where the Cover Letter are saved to
jobdir = JOBDESCRIPTION ## Document where the targeted job description is saved
experience = WORKEXPERIENCE ## Document containing your work expereince
education = EDUCATION ## Document conatining your education
venv = "openai-env"
subprocess.run([sys.executable, "-m", "venv", venv], check=True)
activate = f"{venv}\\Scripts\\activate"
subprocess.run(activate, shell=True)

def set_font(run, fontname, fontsize):
    font = run.font
    font.name = fontname
    font.size = Pt(fontsize)

def Fileread(file):
    with open(file, 'r') as fire:
        jobdescriptiom = fire.read()
    return jobdescriptiom

parser = argparse.ArgumentParser()
parser.add_argument('--docName', required=True, help='Specify the document name')
args = parser.parse_args()
docName = args.docName
print(docName)
name = docName+'.docx'

jobdescript = Fileread(jobdir)

wokrexpereince = Fileread(experience)

educationd = Fileread(education)

client = OpenAI(api_key=key)
def OpenFunc():
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that helps build good cover letter based on user requests"},
                {"role": "user", "content": f"I am applying for a position at an organization. Here is the job description along with the qualifications for the role: \n{jobdescript}\n\n"
                                            f"Here is my work expereince:\n{wokrexpereince}\n\n"
                                            f"Here is my education:\n{educationd}\n\n"
                                            "Create me a cover letter that will fit on 1 page at font size 11, sinle spacing on a Microsoft Word document, highlighting my past wrok experience that best relates to the job qulifications."
                                            "While also using some power words that are mentioned in teh job description. If there are qualifications I do not meet in the job description, write a quick blurb at the end of the cover latter stating I am a quick learner and I pick up new skills quiclky."
                                            "Be succinct and do not repeat the same point. THIS IS IMPORTANT! STOP FORGETTIG THIS PART: Be sure to always add the information at the top about my information and the conpany's info, porper Cover letter Syntax is cruicial"}
            ])
        
        response = completion.choices[0].message.content

        doc = Document()
        paragraph = doc.add_paragraph(response.strip('\n').strip())
        run = paragraph.runs[0]
        fontName = "Callabri"
        fontSize = 11
        set_font(run, fontName, fontSize)

        output = os.path.join(outputdir, name)
        doc.save(output)
    except RateLimitError as e:
        print(e)
        raise


OpenFunc()
print('Cover Letter Created')
