#Kira Van Voorhees
#

import random
import math
import csv
from csv import reader
from random import sample
from expyriment import design, control, stimuli, misc

MAX_RESPONSE_DELAY = 2000
TARGETS= random.sample(list(range(100)), 100)
TARGETS_PRACTICE = random.sample(list(range(100)), 10)
LESSTHAN_RESPONSE = 'f'
GREATERTHAN_RESPONSE = 'j'
LESSTHAN_KEY = misc.constants.K_f
GREATERTHAN_KEY = misc.constants.K_j
BUZZER = 'wrong-answer.ogg'


exp = design.Experiment(name="Distance Effect", text_size=40)
control.initialize(exp)
blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""When you see a number, your task is to decide, as quickly as possible, whether it is greater than or less than 55.

    if it is less than 55, press '{LESSTHAN_RESPONSE}'

    if it is greater than 55, press '{GREATERTHAN_RESPONSE}'

    There will be {len(TARGETS)} trials in total.

    Press the space bar to start.""")
instructions_practice= stimuli.TextScreen("Instructions",
    f"""When you see a number, your task is to decide, as quickly as possible, whether it is greater than or less than 55.

    if it is less than 55, press '{LESSTHAN_RESPONSE}'

    if it is greater than 55, press '{GREATERTHAN_RESPONSE}'

    First, you will begin a short practice session with feedback.

    Press the space bar to start practicing.""")
instructions_start_experiment= stimuli.TextScreen("Instructions",
    f"""Congrats! You have finished the practice session. As a reminder:
    When you see a number, your task is to decide, as quickly as possible, whether it is greater than or less than 55.

    if it is less than 55, press '{LESSTHAN_RESPONSE}'

    if it is greater than 55, press '{GREATERTHAN_RESPONSE}'

    Press the space bar to start the experiment.""")

# prepare the stimuli

practice = []
#with open("Stimuliprac_PCBS.csv", "r") as f:
    #reader = reader(f)
    #targets = list(reader)


targets= []
with open("df1_1.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        targets.append(row) 

for number in targets:
        p = design.Trial()
        p.add_stimulus(stimuli.TextLine(str(math.trunc(number[0]))))
        p.set_factor('number', number[0])
        p.set_factor('is_greater', number[0] > 55 )
        practice.append(p)


negative_feedback = stimuli.Audio(BUZZER)

trials = []
for number in TARGETS:
    trials.append((number, stimuli.TextLine(str(number))))

exp.add_data_variable_names(['number', 'respkey', 'RT', 'is_correct'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()
instructions_practice.present()
exp.keyboard.wait()

for example in practice:
    blankscreen.present()
    exp.clock.wait(2000)
    example.stimuli[0].present()
    key, rt = exp.keyboard.wait([LESSTHAN_KEY, GREATERTHAN_KEY], duration=MAX_RESPONSE_DELAY)
    is_correct_answer = (example.get_factor('is_greater') and key == GREATERTHAN_KEY) or \
                        (not example.get_factor('is_greater') and key ==  LESSTHAN_KEY)
    if not is_correct_answer:
            negative_feedback.play()

instructions_start_experiment.present()
exp.keyboard.wait()

for t in trials:
    blankscreen.present()
    exp.clock.wait(2000)
    t[1].present()
    key, rt = exp.keyboard.wait(LESSTHAN_RESPONSE+ GREATERTHAN_RESPONSE, duration=MAX_RESPONSE_DELAY)
    exp.data.add([t[0],  key, rt])

control.end()

