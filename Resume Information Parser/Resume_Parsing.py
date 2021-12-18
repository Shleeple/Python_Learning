#!/usr/bin/env python
# coding: utf-8

# In[50]:
import spacy #nlp
import pdfminer #pdf2txt
import re #regex
import os #file manip
import pandas as pd #csv- tabular

# In[8]:
import pdf2txt

# ## Converting pdf to txt
# In[16]:
def convert_pdf(f):
    output_filename = os.path.basename(os.path.splitext(f)[0]) + ".txt" # gets filename with .txt extension
    output_filepath = os.path.join("Output/txt/", output_filename) # gets the desired output path
    pdf2txt.main(args=[f, "--outfile", output_filepath]) # input pdf to txt and save it in the given location
    print(output_filepath + " saved successfully!")
    return open(output_filepath, encoding='utf8').read() # Opens the file, reads it, and returns that

# ## Load Languaje Model
# In[10]:
nlp = spacy.load("en_core_web_sm")

# ## Declare placeholder lists and dictionary
# In[38]:
result_dict = {'name':[], 'phone':[], 'email':[], 'skills':[]}
names = []
phones = []
emails = []
skills = []

# ## Function to actually parse the information
# In[39]:
# source of phone_number regex: 'https://stackoverflow.com/a/3868861'
# In[40]:

def parse_content(text):
    # compiling regex por skillset
    skillset = re.compile("java|sql|css|python|django") 
    
    # compiling regex por phone number
    phone_num = re.compile("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})") 
    
    doc = nlp(text)
    name = [entity.text for entity in doc.ents if entity.label_ == "PERSON"][0] # Grabs the first entity labeled "PERSON"
    print(name)
    email = [word for word in doc if word.like_email == True][0] # Grabs the first email found
    print(email)
    phone = str(re.findall(phone_num, text.lower())) # finds the phone number in text, using the regex 'phone_num'
    skills_list = re.findall(skillset, text.lower()) # finds skills using the regex skillset, using lowercase to avoid issues
    unique_skills_list = str(set(skills_list)) # makes sure a skill is only listed once, even if it's found many times in text
    
    # Append information to placeholder lists
    names.append(name)
    emails.append(email)
    phones.append(phone)
    skills.append(unique_skills_list)
    print(skills[-1])
    
    print("Extraction completed successfully!")

# ## Loop to parse all PDFs
# In[41]:
for file in os.listdir('Resumes/'): # Reads through every file in the 'Resumes' folder
    if file.endswith('.pdf'): # Validates that will only go through PDF files
        print("Reading..... " + file)
        txt = convert_pdf(os.path.join('Resumes/', file)) # Converts the file to txt, opens it and reads it to txt
        parse_content(txt) # Parses the file read to txt
        print('')

# In[48]:
result_dict['name'] = names
result_dict['phone'] = phones
result_dict['skills'] = skills
result_dict['email'] = emails

# In[54]:
result_df = pd.DataFrame(result_dict) # Converts result dictionary into Pandas DataFrame
result_df

# In[56]:
result_df.to_csv('Output/csv/parsed_resumes.csv') # Stores Pandas DataFrame into a csv file in the directory we chose
# ## Now we can download the Jupyter Notebook as a .py file, so that it's usable by others