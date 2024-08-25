#import
import os
import time
import threading
from playsound import playsound
from tabulate import tabulate
import json
from termcolor import colored

#json
with open('JSON/voiced_lines.json', 'r', encoding='utf-8') as file:
    voiced_lines = json.load(file)

with open('JSON/variables.json', 'r') as file:
    variables = json.load(file)

with open('JSON/responses.json', 'r') as file:
    responses_data = json.load(file)
    responses = responses_data["responses"]

#global()
def typewriter_effect(text, delay=0.01, newline=True):
    if text is None:
        return

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

    if newline:
        print()

def play_audio(file_path):
    playsound(file_path)

def play_sound_with_text(file_path, text):
    audio_thread = threading.Thread(target=play_audio, args=(file_path,))
    audio_thread.start()
    typewriter_effect(text, delay=0.01, newline=True)
    audio_thread.join()

def format_result(value, normal_range=None, unit=""):
    if value is None:
        return ""

    if normal_range is None:
        return f"{value} {unit}"

    if normal_range and isinstance(normal_range, tuple) and len(normal_range) == 2:
        if normal_range[0] <= value <= normal_range[1]:
            return f"{value} {unit}"
        else:
            return colored(f"{value} {unit}", 'red')
        
    else:
        return f"{value} {unit}"

#voiced_lines
    #narrator
excellent_path = voiced_lines['excellent']['path']
excellent_text = voiced_lines['excellent']['text']

intro_path = voiced_lines['intro']['path']
intro_text = voiced_lines['intro']['text']

history_path = voiced_lines['history']['path']
history_text = voiced_lines['history']['text']

differential_path = voiced_lines['differential']['path']
differential_text = voiced_lines['differential']['text']

physical_path = voiced_lines['physical']['path']
physical_text = voiced_lines['physical']['text']

hint_physical_path = voiced_lines['hint_physical']['path']
hint_physical_text = voiced_lines['hint_physical']['text']

hint_monitoring_path = voiced_lines['hint_monitoring']['path']
hint_monitoring_text = voiced_lines['hint_monitoring']['text']

hint_vasculature_path = voiced_lines['hint_vasculature']['path']
hint_vasculature_text = voiced_lines['hint_vasculature']['text']

lab_path = voiced_lines['lab']['path']
lab_text = voiced_lines['lab']['text']

hint_atb_path = voiced_lines['hint_atb']['path']
hint_atb_text = voiced_lines['hint_atb']['text']

resolution_path = voiced_lines['resolution']['path']
resolution_text = voiced_lines['resolution']['text']

hint_surgery_path = voiced_lines['hint_surgery']['path']
hint_surgery_text = voiced_lines['hint_surgery']['text']

outro_path = voiced_lines['outro']['path']
outro_text = voiced_lines['outro']['text']

    #DC
DC_1_path = voiced_lines['DC_1']['path']
DC_1_text = voiced_lines['DC_1']['text']

DC_2_path = voiced_lines['DC_2']['path']
DC_2_text = voiced_lines['DC_2']['text']

DC_3_path = voiced_lines['DC_3']['path']
DC_3_text = voiced_lines['DC_3']['text']

DC_4_path = voiced_lines['DC_4']['path']
DC_4_text = voiced_lines['DC_4']['text']

DC_5_path = voiced_lines['DC_5']['path']
DC_5_text = voiced_lines['DC_5']['text']

DC_6_path = voiced_lines['DC_6']['path']
DC_6_text = voiced_lines['DC_6']['text']

#interaction_DC
def ask_question(performed_questions):
    questions = {
        "1": "Can you describe the pain?",
        "2": "Have you experienced anything like this before?",
        "3": "Are you experiencing any other symptoms, like fever or nausea?",
        "4": "Have you taken any medications recently?",
        "5": "Have you noticed any changes in appetite, bowel movements, or urinary habits?",
        "6": "Have you been out of the country recently?"
    }

    available_questions = {str(index + 1): q for index, q in enumerate(questions.values()) if str(index + 1) not in performed_questions}

    if not available_questions:
        return True

    print("\nChoose a question to ask the patient (enter numbers separated by commas):")
    for index, question in available_questions.items():
        print(f"{index}. {question}")

    choice = input("\nEnter the numbers of the questions you want to ask (comma-separated): ")

    if choice == "0":
        typewriter_effect("\nYou have decided to end the interaction and proceed with the examination.")
        return True

    selected_questions = choice.split(", ")

    for question_number in selected_questions:
        question_number = question_number.strip()
        if question_number in available_questions:
            if question_number not in performed_questions:
                performed_questions.add(question_number)
                
                # Print the chosen question
                question_text = available_questions[question_number]
                typewriter_effect(f"Q: {question_text}", newline=False)

                # Play sound and get the text response
                if question_number == "1":
                    play_sound_with_text(DC_1_path, DC_1_text)
                elif question_number == "2":
                    play_sound_with_text(DC_2_path, DC_2_text)
                elif question_number == "3":
                    play_sound_with_text(DC_3_path, DC_3_text)
                elif question_number == "4":
                    play_sound_with_text(DC_4_path, DC_4_text)
                elif question_number == "5":
                    play_sound_with_text(DC_5_path, DC_5_text)
                elif question_number == "6":
                    play_sound_with_text(DC_6_path, DC_6_text)
            else:
                typewriter_effect(f"\nQuestion {question_number} has already been asked.")
        else:
            typewriter_effect(f"\nQuestion number {question_number} is not a valid choice.")

    return False

def interactive_conversation():
    performed_questions = set()
    while True:
        end_interaction = ask_question(performed_questions)
        if end_interaction:
            break


#interaction_exams
def perform_exams(performed_exams):
    exams = {
        "1": "AIRWAY",
        "2": "BREATH",
        "3": "CIRC",
        "4": "HEENT",
        "5": "NECK",
        "6": "CARD",
        "7": "PULM",
        "8": "ABD",
        "9": "GU",
        "10": "BACK",
        "11": "MSK",
        "12": "SKIN",
        "13": "NEURO",
        "14": "PSYCH"
    }

    available_exams = {str(index + 1): exam for index, exam in enumerate(exams.values()) if str(index + 1) not in performed_exams}

    if not available_exams:
        return True

    print("\nChoose an exam to run (enter numbers separated by commas):")
    for index, exam in available_exams.items():
        print(f"{index}. {exam}")

    choice = input("\nEnter the numbers of the exams you want to perform (comma-separated): ")

    if choice == "0":
        typewriter_effect("\nYou have decided to end the interaction and proceed with the case.")
        return True

    selected_exams = choice.split(", ")

    for exam_number in selected_exams:
        exam_number = exam_number.strip()
        if exam_number in available_exams:
            if exam_number not in performed_exams:
                performed_exams.add(exam_number)
                
                response_index = int(exam_number) - 1
                response = responses[response_index]
                typewriter_effect(response)
            else:
                typewriter_effect(f"\nExam {exam_number} has already been performed.")
        else:
            typewriter_effect(f"\nExam number {exam_number} is not a valid choice.")

    return False

def interactive_exams():
    performed_exams = set()
    while True:
        end_interaction = perform_exams(performed_exams)
        if end_interaction:
            break

#interaction_labs
def perform_labs(performed_labs):
    labs = [
        {"Arterial Blood Gas": [("pH", variables["pH"], variables["normal_pH"], ""), 
                                ("pCO2", variables["pCO2"][0], variables["normal_pCO2"], variables["pCO2"][1]), 
                                ("pO2", variables["pO2"][0], variables["normal_pO2"], variables["pO2"][1])]},
        {"Chem 7": [("Sodium", variables["Sodium"][0], variables["normal_Sodium"], variables["Sodium"][1]), 
                    ("Potassium", variables["Potassium"][0], variables["normal_Potassium"], variables["Potassium"][1]), 
                    ("Chloride", variables["Chloride"][0], variables["normal_Chloride"], variables["Chloride"][1]), 
                    ("Bicarbonate", variables["Bicarbonate"][0], variables["normal_Bicarbonate"], variables["Bicarbonate"][1]), 
                    ("Glucose", variables["Glucose"][0], variables["normal_Glucose"], variables["Glucose"][1]), 
                    ("Creatinine", variables["Creatinine"][0], variables["normal_Creatinine"], variables["Creatinine"][1]), 
                    ("BUN", variables["BUN"][0], variables["normal_BUN"], variables["BUN"][1])]},
        {"Blood Type": [("Blood Type", variables["Blood_Type"], None, "")]},
        {"Ionized Calcium": [("Ionized Calcium", variables["Calcium_Ionized"][0], variables["normal_Calcium_Ionized"], variables["Calcium_Ionized"][1])]},
        {"Calcium": [("Calcium", variables["Calcium_Level"][0], variables["normal_Calcium_Level"], variables["Calcium_Level"][1])]},
        {"Coagulation Panel": [("INR", variables["INR"], variables["normal_INR"], ""), 
                               ("PT", variables["PT"][0], variables["normal_PT"], variables["PT"][1]), 
                               ("PTT", variables["PTT"][0], variables["normal_PTT"], variables["PTT"][1])]},
        {"CBC": [("WBC", variables["WBC"][0], variables["normal_WBC"], variables["WBC"][1]), 
                 ("Hgb", variables["Hgb"][0], variables["normal_Hgb"], variables["Hgb"][1]), 
                 ("Hct", variables["Hct"], variables["normal_Hct"], ""), 
                 ("Platelets", variables["Platelets"][0], variables["normal_Platelets"], variables["Platelets"][1])]},
        {"D-Dimer": [("D-Dimer", variables["DDimer"][0], variables["normal_DDimer"], variables["DDimer"][1])]},
        {"Lactate": [("Lactate", variables["Lactate"][0], variables["normal_Lactate"], variables["Lactate"][1])]},
        {"Lipase": [("Lipase", variables["Lipase"][0], variables["normal_Lipase"], variables["Lipase"][1])]},
        {"LFTs": [("ALP", variables["ALP"][0], variables["normal_ALP"], variables["ALP"][1]), 
                  ("ALT", variables["ALT"][0], variables["normal_ALT"], variables["ALT"][1]), 
                  ("AST", variables["AST"][0], variables["normal_AST"], variables["AST"][1]), 
                  ("Bilirubin I", variables["Bilirubin_I"][0], variables["normal_Bilirubin_I"], variables["Bilirubin_I"][1]), 
                  ("Bilirubin D", variables["Bilirubin_D"][0], variables["normal_Bilirubin_D"], variables["Bilirubin_D"][1])]},
        {"Magnesium": [("Magnesium", variables["Magnesium_Level"][0], variables["normal_Magnesium_Level"], variables["Magnesium_Level"][1])]},
        {"Phosphate": [("Phosphate", variables["Phosphate"][0], variables["normal_Phosphate"], variables["Phosphate"][1])]},
        {"pro-BNP": [("pro-BNP", variables["BNP"][0], variables["normal_BNP"], variables["BNP"][1])]},
        {"Troponin-T": [("Troponin-T", variables["Troponin_T"][0], None, variables["Troponin_T"][1])]},
        {"Urinalysis": []},
        {"Acetaminophen": [("Acetaminophen", variables["Acetaminophen"][0], variables["normal_Acetaminophen"], variables["Acetaminophen"][1])]},
        {"Amylase": [("Amylase", variables["Amylase"][0], variables["normal_Amylase"], variables["Amylase"][1])]},
        {"Blood Culture (x2)": []},
        {"CRP": [("CRP", variables["CRP"][0], variables["normal_CRP"], variables["CRP"][1])]},
        {"CK": [("CK", variables["CK"][0], variables["normal_CK"], variables["CK"][1])]},
        {"CSF Cell Count": []},
        {"CSF Glucose": []},
        {"CSF Gram Stain": []},
        {"CSF Protein": []},
        {"EtOH": [("EtOH Level", variables["EtOH_Level"][0], variables["normal_EtOH_Level"], variables["EtOH_Level"][1])]},
        {"LDH": [("LDH", variables["LDH"][0], variables["normal_LDH"], variables["LDH"][1])]},
        {"Osmolality": [("Osmolality", variables["Osmolality"][0], variables["normal_Osmolality"], variables["Osmolality"][1])]},
        {"Peripheral Smear": []},
        {"Salicylate": [("Salicylate", variables["Salicylate_Level"][0], variables["normal_Salicylate_Level"], variables["Salicylate_Level"][1])]},
        {"TSH": [("TSH", variables["TSH"][0], variables["normal_TSH"], variables["TSH"][1])]},
        {"Uric Acid": [("Uric Acid", variables["Uric_Acid"][0], variables["normal_Uric_Acid"], variables["Uric_Acid"][1])]},
        {"Urine Culture": []},
        {"Urine Tox Screen": []},
        {"COVID-19 Test": []},
        {"ESR": [("ESR", variables["ESR"][0], variables["normal_ESR"], variables["ESR"][1])]},
        {"CT Abdomen": []},
        {"CT Aorta": []},
        {"CT C-Spine": []},
        {"CT Thorax": []},
        {"CT Head": []},
        {"CT Pulmonary Embolus": []},
        {"CT/CTA Head & Neck": []},
        {"MRI Abdomen": []},
        {"MRI C-Spine": []},
        {"MRI T-Spine": []},
        {"MRI L-Spine": []},
        {"MRI/MRA Head & Neck": []},
        {"XR Thorax": []},
        {"XR Pelvis": []}
    ]

    available_labs = {str(index + 1): lab_name for index, lab_dict in enumerate(labs) for lab_name in lab_dict.keys() if lab_name not in performed_labs}

    if not available_labs:
        typewriter_effect("\nAll labs have been performed.")
        return True

    print("\nChoose labs to run (enter numbers separated by commas):")

    for key, lab_name in available_labs.items():
        print(f"{key}. {lab_name}")

    choice = input("\nEnter the numbers of the labs you want to perform (comma-separated): ")

    if choice == "0":
        typewriter_effect("\nYou have decided to end the interaction and proceed with the case.")
        return True

    selected_labs = choice.split(",")

    response = ""
    table_data = []

    for lab_number in selected_labs:
        lab_number = lab_number.strip()
        if lab_number in available_labs:
            lab_index = int(lab_number) - 1
            lab_info = labs[lab_index]
            lab_name = list(lab_info.keys())[0]

            if lab_name not in performed_labs:
                performed_labs.add(lab_name)
                for result in lab_info[lab_name]:
                    name = result[0]
                    value = result[1]
                    normal_range = result[2]
                    unit = result[3]
                    result_value = format_result(value, normal_range, unit)
                    table_data.append([name, result_value])
            else:
                response += f"\nLab {lab_name} has already been selected."
        else:
            response += f"\nLab number {lab_number} is not a valid choice."

    if table_data:
        response += "\nLab Results:\n"
        response += tabulate(table_data, headers=["Test", "Result"], tablefmt="grid")

    typewriter_effect(response)

    return False

def interactive_labs():
    performed_labs = set()
    while True:        
        end_interaction = perform_labs(performed_labs)
        if end_interaction:
            break

##########################################################
#interactive_conversation()
#interactive_exams()
#interactive_labs()
play_sound_with_text(intro_path, intro_text)
time.sleep(1)
play_sound_with_text(history_path, history_text)
time.sleep(1)
interactive_conversation()
time.sleep(1)
play_sound_with_text(differential_path, differential_text)
time.sleep(1)
play_sound_with_text(physical_path, physical_text)
time.sleep(1)
play_sound_with_text(hint_physical_path, hint_physical_text)
time.sleep(1)
interactive_exams()
play_sound_with_text(hint_monitoring_path, hint_monitoring_text)
time.sleep(1)
play_sound_with_text(hint_vasculature_path, hint_vasculature_text)
time.sleep(1)
play_sound_with_text(lab_path, lab_text)
interactive_labs()
time.sleep(1)
play_sound_with_text(hint_atb_path, hint_atb_text)
time.sleep(1)
play_sound_with_text(resolution_path, resolution_text)
time.sleep(1)
play_sound_with_text(hint_surgery_path, hint_surgery_text)
time.sleep(1)
play_sound_with_text(outro_path, outro_text)