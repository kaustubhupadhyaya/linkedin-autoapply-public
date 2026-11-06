'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html

GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''


###################################################### APPLICATION INPUTS ######################################################

# Copy this file to config/questions.py and replace the placeholders. The real
# file is git-ignored. The bot will not start until config/questions.py exists.

# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Relative path to your default resume. If the file is missing, the bot keeps
# the resume already uploaded to LinkedIn.
default_resume_path = "all resumes/default/resume.pdf"

# What to answer when an application asks how many years of experience you have.
years_of_experience = "0"          # A number in quotes, for example "0", "1", "2"

# Do you need visa sponsorship now or in future?
require_visa = "No"                # "Yes" or "No"

# Portfolio or personal website. Leave empty to skip the question.
website = ""

# LinkedIn profile URL. Leave empty to skip the question.
linkedIn = ""

# Do you already have permission to work in the country you are applying to?
legally_authorized = "Yes"         # "Yes" or "No"

# Citizenship status. Leave empty to skip the question.
us_citizenship = "Other"           # "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident", "Other"


## Common application questions

# Expected salary / CTC. Use numbers only.
desired_salary = 0                 # Do NOT use quotes

# Current salary / CTC. Use numbers only.
current_ctc = 0                    # Do NOT use quotes

# Notice period in days.
notice_period = 0                  # Any number >= 0 without quotes

# LinkedIn headline.
linkedin_headline = ""

# LinkedIn summary. Use \n for line breaks.
linkedin_summary = ""

# Cover letter. Use \n for line breaks.
cover_letter = ""

# Free-form information the AI may use when answering application questions.
# Include only facts you are willing to send to an employer.
user_information_all = ""

# Name of your most recent employer.
recent_employer = ""

# Answer for "on a scale of 1-10" experience questions.
confidence_level = "5"             # "1" through "10", in quotes
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

# Pause before every submission so you can review the form.
pause_before_submit = True         # True or False

# Pause when the bot cannot answer a question.
pause_at_failed_question = True    # True or False

# Overwrite answers LinkedIn has saved from previous applications.
overwrite_previous_answers = False # True or False


############################################################################################################
'''
Upstream project: https://github.com/GodsScion/Auto_job_applier_linkedIn
License: GNU Affero General Public License v3.0
'''
############################################################################################################
