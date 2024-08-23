import os
import time
import threading
from playsound import playsound
from tabulate import tabulate

#
RED = "\033[31m"
RESET = "\033[0m"
pH = 7.37
normal_pH = (7.37,7.44)
pCO2 = (38, "mmol/L")
normal_pCO2 = (35,45)
pO2 = (80, "mmol/L")
normal_pO2 = (80,100)
Glucose = (3.9, "mmol/L")
normal_Glucose = (3.6,6.1)
Creatinine = (71, "µmol/L")
normal_Creatinine = (71,115)
BUN = (7.1, "mmol/L")
normal_BUN = (2.9,7.5)
Bicarbonate = (28, "mmol/L")
normal_Bicarbonate = (24,28)
Chloride = (103, "mmol/L")
normal_Chloride = (101,105)
Potassium = (4.4, "mmol/L")
normal_Potassium = (3.6,4.9)
Sodium = (142, "mmol/L")
normal_Sodium = (138,143)
Blood_Type = "O+"
Calcium_Ionized = (1.1, "mmol/L")
normal_Calcium_Ionized = (1.1,1.35)
Calcium_Level = (2.54, "mmol/L")
normal_Calcium_Level = (2.13,2.55)
INR = 1.2
normal_INR = (0.8,1.3)
PTT = (33.6, "seconds")
normal_PTT = (25,35)
PT = (11.7, "seconds")
normal_PT = (11,13)
Platelets = (170, "x10^9/L")
normal_Platelets = (150,400)
Hgb = (146.2, "g/L")
normal_Hgb = (130,170)
Hct = 0.39
normal_Hct = (0.4,0.52)
WBC = (18.9, "x10^9/L")
normal_WBC = (3.2,9.8)
DDimer = (289, "ng/mL")
normal_DDimer = (0,500)
Lactate = (0.9, "mmol/L")
normal_Lactate = (0.4,2.3)
Lipase = (0.96, "µKat/L")
normal_Lipase = (0.42,1.61)
ALP = (88, "U/L")
normal_ALP = (36,92)
ALT = (6, "U/L")
normal_ALT = (0,35)
AST = (0.11, "µKat/L")
normal_AST = (0,0.59)
Bilirubin_I = (19.29, "µmol/L")
normal_Bilirubin_I = (5.13,20.52)
Bilirubin_D = (7.29, "µmol/L")
normal_Bilirubin_D = (5.13,17.1)
Magnesium_Level = (0.65, "mmol/L")
normal_Magnesium_Level = (0.62,0.82)
Phosphate = (1.23, "mmol/L")
normal_Phosphate = (0.81,1.45)
BNP = (73, "pg/mL")
normal_BNP = (0,100)
Troponin_T = ("<",0.01) 
#Urinalysis = ("Yellow", "Clear")
Acetaminophen = (0, "µmol/L")
normal_Acetaminophen = (0,200)
Amylase = (1.03, "µKat/L")
normal_Amylase = (0,2.21)
#Blood_Culture = ()
CRP = (42, "mg/L")
normal_CRP = (0,10)
CK = (2.76, "µKat/L")
normal_CK = (0.51,2.89)
EtOH_Level = (0, "mmol/L")
normal_EtOH_Level = (0,4.3)
LDH = (61, "U/L")
normal_LDH = (60,160)
Osmolality = (283, "mmol/kg H2O")
normal_Osmolality = (275,295)
#Peripheral smear = ()
Salicylate_Level = (0, "mmol/L")
normal_Salicylate_Level = (0,2.17)
TSH = (2.6, "mlU/L")
normal_TSH = (0.5,5)
Uric_Acid = (0.47, "mmol/L")
normal_Uric_Acid = (0.15,0.48)
#Urine_Culture = ()
#Urine_TOX_Screen = ()
#COVID-19_Test = ()
ESR = (36, "mm/h")
normal_ESR = (0,20)

def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def play_audio(file_path):
    playsound(file_path)

def play_sound_with_text(file_path, text):
    audio_thread = threading.Thread(target=play_audio, args=(file_path,))
    audio_thread.start()
    typewriter_effect(text)
    audio_thread.join()

def ask_question(asked_questions):
    questions = {
        "1": "Can you describe the pain?",
        "2": "Have you experienced anything like this before?",
        "3": "Do you have any other symptoms, such as fever or nausea?",
        "4": "Have you taken any medication?",
        "5": "Have you noticed any changes in appetite, bowel habits, or urinary symptoms?",
        "0": "End interaction."
    }

    available_questions = {key: value for key, value in questions.items() if key not in asked_questions}

    print("\nChoose a question to ask the patient:")
    for key, value in available_questions.items():
        print(f"{key}. {value}")

    choice = input("\nEnter the number of the question you want to ask: ")

    if choice == "0":
        typewriter_effect("\nYou have decided to end the interaction and proceed with the examination.")
        return True

    if choice in available_questions:
        asked_questions.add(choice)

        if choice == "1":
            response = "\nThe pain is dull and localized to my middle right side of the abdomen."
        elif choice == "2":
            response = "\nNo, this is the first time I've felt something like this."
        elif choice == "3":
            response = "\nYes, I also feel nauseous. No fever though."
        elif choice == "4":
            response = "\nI took some over-the-counter painkillers, but they didn't help."
        elif choice == "5":
            response = "\nI'm not really hungry, but it might be because of the pain. No diarrhea or vomiting."

        typewriter_effect(response)
    else:
        typewriter_effect("\nPlease choose a valid question.")
        return ask_question(asked_questions)

    return False

def check_if_ready_to_proceed(asked_questions):
    critical_questions = {"1", "3", "5"}

    if critical_questions.issubset(asked_questions):
        time.sleep(1)
        print("\nHere's the summary:")
        return True
    else:
        return False

def excellent():
    play_sound_with_text(excellent_path, excellent_text)

def interactive_conversation():
    asked_questions = set()
    while True:
        if check_if_ready_to_proceed(asked_questions):
            break
        
        end_interaction = ask_question(asked_questions)
        if end_interaction:
            break


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
        "14": "PSYCH",
        "0": "End interaction."
    }

    available_exams = {key: value for key, value in exams.items() if key not in performed_exams}

    print("\nChoose an exam to run:")
    for key, value in available_exams.items():
        print(f"{key}. {value}")

    choice = input("\nEnter the number of the exam you want to perform: ")

    if choice == "0":
        typewriter_effect("\nYou have decided to end the interaction and proceed with the case.")
        return True

    if choice in available_exams:
        performed_exams.add(choice)

        if choice == "1":
            response = "\nAirway is patent without obstruction or stridor."
        elif choice == "2":
            response = "\nBilateral, symmetric breath sounds with normal chest rise."
        elif choice == "3":
            response = "\n2+ peripheral pulses, normal capillary refill."
        elif choice == "4":
            response = "\nNormocephalic, atraumatic, PERRL, EOMI, oropharynx is clear, no scleral icterus. Mucous membranes dry."
        elif choice == "5":
            response = "\nNo masses, trachea midline, supple with full range of motion without C-spine tenderness."
        elif choice == "6":
            response = "\nTachycardic, regular rhythm, no murmurs, rubs or gallops."
        elif choice == "7":
            response = "\nClear to auscultation bilaterally, no retractions, no wheezes, rhonchi or rales."
        elif choice == "8":
            response = "\nSoft, RLQ tenderness with mild guarding, no rebound. Right-sided pain with palpation of the LLQ with bowel sounds.\nSuspicion of appendicitis."
        elif choice == "9":
            response = "\nNo CVAT bilaterally. Normal penis and testicles; no tenderness or masses."
        elif choice == "10":
            response = "\nNo CVA tenderness, no tenderness to the thoracic or lumbar spine."
        elif choice == "11":
            response = "\nNo clubbing, cyanosis or edema. Normal range of motion without bony point tenderness."
        elif choice == "12":
            response = "\nWarm and dry, no rashes."
        elif choice == "13":
            response = "\nAwake and alert, speech clear. CN 2-12 intact, normal bulk, tone and strength in all extremities. No drift or dysmetria."
        elif choice == "14":
            response = "\nNormal mood and affect with intact attention and calculation."

        typewriter_effect(response)
    else:
        typewriter_effect("\nPlease choose a valid exam.")
        return perform_exams(performed_exams)

    return False

def interactive_exams():
    performed_exams = set()
    while True:
        if check_if_ready_to_proceed(performed_exams):
            break
        
        end_interaction = perform_exams(performed_exams)
        if end_interaction:
            break

def format_result(value, normal_range=None, unit=""):
    if value is None:
        return ""

    if normal_range is None:
        return f"{value} {unit}"

    if normal_range and isinstance(normal_range, tuple) and len(normal_range) == 2:
        if normal_range[0] <= value <= normal_range[1]:
            return f"{value} {unit}"
        else:
            return f"{RED}{value} {unit}{RESET}"
    else:
        return f"{value} {unit}"


def new_labs():
    lab_results = {
        {"index", "name", "results"} : {1, "Alex", [("pH", pH, normal_pH, ""), ("pCO2", pCO2[0], normal_pCO2, pCO2[1]), ("pO2", pO2[0], normal_pO2, pO2[1])]},
    }

def perform_labs(performed_labs):
    lab_results = {
        "1": {"name": "Arterial Blood Gas", "results": [("pH", pH, normal_pH, ""), ("pCO2", pCO2[0], normal_pCO2, pCO2[1]), ("pO2", pO2[0], normal_pO2, pO2[1])]},
        "2": {"name": "Chem 7", "results": [("Sodium", Sodium[0], normal_Sodium, Sodium[1]), ("Potassium", Potassium[0], normal_Potassium, Potassium[1]), ("Chloride", Chloride[0], normal_Chloride, Chloride[1]), ("Bicarbonate", Bicarbonate[0], normal_Bicarbonate, Bicarbonate[1]), ("Glucose", Glucose[0], normal_Glucose, Glucose[1]), ("Creatinine", Creatinine[0], normal_Creatinine, Creatinine[1]), ("BUN", BUN[0], normal_BUN, BUN[1])]},
        "3": {"name": "Blood Type", "results": [("", Blood_Type, None, "")]},
        "4": {"name": "Ionized Calcium", "results": [("", Calcium_Ionized[0], normal_Calcium_Ionized, Calcium_Ionized[1])]},
        "5": {"name": "Calcium", "results": [("", Calcium_Level[0], normal_Calcium_Level, Calcium_Level[1])]},
        "6": {"name": "Coagulation Panel", "results": [("INR", INR, normal_INR, ""), ("PT", PT[0], normal_PT, PT[1]), ("PTT", PTT[0], normal_PTT, PTT[1])]},
        "7": {"name": "CBC", "results": [("WBC", WBC[0], normal_WBC, WBC[1]), ("Hgb", Hgb[0], normal_Hgb, Hgb[1]), ("Hct", Hct, normal_Hct, ""), ("Platelets", Platelets[0], normal_Platelets, Platelets[1])]},
        "8": {"name": "D-Dimer", "results": [("", DDimer[0], normal_DDimer, DDimer[1])]},
        "9": {"name": "Lactate", "results": [("", Lactate[0], normal_Lactate, Lactate[1])]},
        "10": {"name": "Lipase", "results": [("", Lipase[0], normal_Lipase, Lipase[1])]},
        "11": {"name": "LFTs", "results": [("ALP", ALP[0], normal_ALP, ALP[1]), ("ALT", ALT[0], normal_ALT, ALT[1]), ("AST", AST[0], normal_AST, AST[1]), ("Bilirubin I", Bilirubin_I[0], normal_Bilirubin_I, Bilirubin_I[1]), ("Bilirubin D", Bilirubin_D[0], normal_Bilirubin_D, Bilirubin_D[1])]},
        "12": {"name": "Magnesium", "results": [("", Magnesium_Level[0], normal_Magnesium_Level, Magnesium_Level[1])]},
        "13": {"name": "Phosphate", "results": [("", Phosphate[0], normal_Phosphate, Phosphate[1])]},
        "14": {"name": "pro-BNP", "results": [("", BNP[0], normal_BNP, BNP[1])]},
        "15": {"name": "Troponin-T", "results": [("", Troponin_T[0], None, Troponin_T[1])]},
        "16": {"name": "Urinalysis", "results": []},
        "17": {"name": "Acetaminophen", "results": [("", Acetaminophen[0], normal_Acetaminophen, Acetaminophen[1])]},
        "18": {"name": "Amylase", "results": [("", Amylase[0], normal_Amylase, Amylase[1])]},
        "19": {"name": "Blood Culture (x2)", "results": []},
        "20": {"name": "CRP", "results": [("", CRP[0], normal_CRP, CRP[1])]},
        "21": {"name": "CK", "results": [("", CK[0], normal_CK, CK[1])]},
        "22": {"name": "CSF Cell Count", "results": []},
        "23": {"name": "CSF Glucose", "results": []},
        "24": {"name": "CSF Gram Stain", "results": []},
        "25": {"name": "CSF Protein", "results": []},
        "26": {"name": "EtOH", "results": [("", EtOH_Level[0], normal_EtOH_Level, EtOH_Level[1])]},
        "27": {"name": "LDH", "results": [("", LDH[0], normal_LDH, LDH[1])]},
        "28": {"name": "Osmolality", "results": [("", Osmolality[0], normal_Osmolality, Osmolality[1])]},
        "29": {"name": "Peripheral Smear", "results": []},
        "30": {"name": "Salicylate", "results": [("", Salicylate_Level[0], normal_Salicylate_Level, Salicylate_Level[1])]},
        "31": {"name": "TSH", "results": [("", TSH[0], normal_TSH, TSH[1])]},
        "32": {"name": "Uric Acid", "results": [("", Uric_Acid[0], normal_Uric_Acid, Uric_Acid[1])]},
        "33": {"name": "Urine Culture", "results": []},
        "34": {"name": "Urine Tox Screen", "results": []},
        "35": {"name": "COVID-19 Test", "results": []},
        "36": {"name": "ESR", "results": [("", ESR[0], normal_ESR, ESR[1])]},
        "37": {"name": "CT Abdomen", "results": []},
        "38": {"name": "CT Aorta", "results": []},
        "39": {"name": "CT C-Spine", "results": []},
        "40": {"name": "CT Thorax", "results": []},
        "41": {"name": "CT Head", "results": []},
        "42": {"name": "CT Pulmonary Embolus", "results": []},
        "43": {"name": "CT/CTA Head & Neck", "results": []},
        "44": {"name": "MRI Abdomen", "results": []},
        "45": {"name": "MRI C-Spine", "results": []},
        "46": {"name": "MRI T-Spine", "results": []},
        "47": {"name": "MRI L-Spine", "results": []},
        "48": {"name": "MRI/MRA Head & Neck", "results": []},
        "49": {"name": "XR Thorax", "results": []},
        "50": {"name": "XR Pelvis", "results": []},
    }

    available_labs = {key: value for key, value in lab_results.items() if key not in performed_labs}

    print("\nChoose labs to run (enter numbers separated by commas):")
    index = 0
    for i in range((int((available_labs.__len__() - 5) / 5) + 1)):
        item = list(available_labs.items())[index]
        item1 = list(available_labs.items())[index+1]
        item2 = list(available_labs.items())[index+2]
        item3 = list(available_labs.items())[index+3]
        item4 = list(available_labs.items())[index+4]
        print(f"{item[0]}. {list(item[1].items())[0][1]}     {item1[0]}. {list(item1[1].items())[0][1]}     {item2[0]}. {list(item2[1].items())[0][1]}     {item3[0]}. {list(item3[1].items())[0][1]}          {item4[0]}. {list(item4[1].items())[0][1]}")
        index+=5

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
            performed_labs.add(lab_number)
            lab_info = lab_results[lab_number]
            for result in lab_info["results"]:
                name = result[0] if len(result) > 0 else ""
                value = result[1] if len(result) > 1 else None
                normal_range = result[2] if len(result) > 2 else None
                unit = result[3] if len(result) > 3 else ""

                if not name:
                    name = lab_info['name']

                result_value = format_result(value, normal_range, unit)
                table_data.append([name, result_value])
        else:
            response += f"\nLab number {lab_number} is not a valid choice or has already been selected."

    if table_data:
        response += "\nLab Results:\n"
        response += tabulate(table_data, headers=["Test", "Result"], tablefmt="grid")

    typewriter_effect(response)
    
    return False


def interactive_labs():
    performed_labs = set()
    while True:
        if check_if_ready_to_proceed(performed_labs):
            break
        
        end_interaction = perform_labs(performed_labs)
        if end_interaction:
            break

#
excellent_path = "D:/Python/Appendicitis/excellent.mp3"
excellent_text = (
    "\nExcellent!"
)

intro_path = "intro.mp3"
intro_text = (
    "\nDC is a 29 year old man presenting to the emergency room with abdominal pain and nausea, no fever."
    "\nHe says the pain had started yesterday out of nowhere and has been getting worse ever since to"
    "\nthe point where it is unbearable."
)

history_path = "history.mp3"
history_text = (
    "\nWhen taking the patient's history, focus on the progression of symptoms, associated factors like" 
    "\nfever or nausea, and any specific triggers or alleviating factors. During the discussion of "
    "\nbody systems, inquire about any recent changes in appetite, bowel habits, urinary symptoms" 
    "\nand any other relevant systemic complaints."
)

differential_path = "differential.mp3"
differential_text = (
    "\nThe patient presents with abdominal pain, poor appetite, nausea and chills."
    "\nThe absence of fever, vomiting, diarrhoea, dysuria and recent travel history" 
    "\nhelps narrow down the possible differentials. The differential diagnosis" 
    "\nmay include: ileus, cholecystitis, diverticulitis and appendicitis."
    "\nEach of these conditions presents with distinct features that need" 
    "\nto be considered based on the patient's symptoms and examination findings."
)

physical_path = "physical.mp3"
physical_text = (
    "\nDuring the physical examination, focus on eliciting right lower quadrant tenderness,"
    "\nspecifically at McBurney's point, located between the anterior superior iliac spine" 
    "\nand the umbilicus. Additionally, assess for signs such as Rovsing's sign, psoas sign," 
    "\nand obturator sign, which can indicate peritoneal irritation and help in the diagnosis."
)

hint_physical_path = "hint_physical.mp3"
hint_physical_text = (
    "\nRemember to thoroughly asses the abdomen for any signs of discomfort or sensitivity," 
    "\nas this can provide valuable information about the patient's condition."
)

hint_monitoring_path = "hint_monitoring.mp3"
hint_monitoring_text = (
    "\nMake sure to connect the patient to the necessary equipment to continuously monitor vital signs," 
    "\nas this will provide valuable information for ongoing assessments and management."
)

hint_vasculature_path = "hint_vasculature.mp3"
hint_vasculature_text = (
    "\nRemember to establish vascular access for the patient to ensure the timely administration" 
    "\nof necessary treatments."
)

lab_path = "lab.mp3"
lab_text = (
    "\nTo investigate the patient presenting with suspected appendicitis, it is crucial to perform" 
    "\nbasic laboratory tests including a chemistry profile and a complete blood count to assess" 
    "\nfor any abnormalities. Additionally, obtaining a CT of the abdomen with contrast is essential" 
    "\nto confirm the diagnosis and guide further management decisions."

)

hint_atb_path = "hint_atb.mp3"
hint_atb_text = (
    "\nRemember to consider prophylactic antibiotics, especially those covering gram-negative bacteria."
)

resolution_path = "resolution.mp3"
resolution_text = (
    "\nBased on the patient's presentation of right lower quadrant tenderness, anorexia, and elevated white blood cell count," 
    "\nthis seems like a classical case of appendicitis and a surgical intervention may be necessary, specifically appendectomy." 
    "\nPrep the patient for the operating room as soon as possible, this is crucial to prevent complications such as perforation and peritonitis."
)

hint_surgery_path = "hint_surgery.mp3"
hint_surgery_text = (
    "\nRemember, in cases where surgical intervention may be necessary, it is crucial to" 
    "\ninvolve the appropriate specialty early on for optimal patient care and managment."
)

outro_path = "outro.mp3"
outro_text = (
    "\nThanks to timely medical intervention, he received the treatment he needed." 
    "\nDC has since made a full recovery."
)

#
interactive_labs()
play_sound_with_text(intro_path, intro_text)
time.sleep(1)
play_sound_with_text(history_path,history_text)
time.sleep(1)
interactive_conversation()
time.sleep(1)
play_sound_with_text(differential_path,differential_text)
time.sleep(1)
play_sound_with_text(physical_path,physical_text)
time.sleep(1)
play_sound_with_text(hint_physical_path,hint_physical_text)
time.sleep(1)
interactive_exams()
play_sound_with_text(hint_monitoring_path,hint_monitoring_text)
time.sleep(1)
play_sound_with_text(hint_vasculature_path,hint_vasculature_text)
time.sleep(1)
play_sound_with_text(lab_path,lab_text)
interactive_labs()
time.sleep(1)
play_sound_with_text(hint_atb_path,hint_atb_text)
time.sleep(1)
play_sound_with_text(resolution_path,resolution_text)
time.sleep(1)
play_sound_with_text(hint_surgery_path,hint_surgery_text)
time.sleep(1)
play_sound_with_text(outro_path,outro_text)