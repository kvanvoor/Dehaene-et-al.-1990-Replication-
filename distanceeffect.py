#! /usr/bin/env python
# Time-stamp: <2021-03-24 08:15:54 christophe@pallier.org>
"""This is a simple decision experiment.

At each trial, a number between 0 and 9 is presented at the center of the
screen and the participant must press the key 'f' if the number is even, 'j' if
it is odd.

"""

import random
from random import sample
from expyriment import design, control, stimuli, misc

MAX_RESPONSE_DELAY = 2000
TARGETS= random.sample(list(range(100)), 100)
TARGETS_PRACTICE = random.sample(list(range(100)), 10)
LESSTHAN_RESPONSE = 'f'
GREATERTHAN_RESPONSE = 'j'
BUZZER = 'wrong-answer.ogg'
LESSTHAN_KEY = misc.constants.K_f
GREATERTHAN_KEY = misc.constants.K_j


exp = design.Experiment(name="Parity Decision", text_size=40)
control.initialize(exp)

cue = stimuli.FixCross(size=(50, 50), line_width=4)
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
for number in TARGETS_PRACTICE:
    p = design.Trial()
    p.set_factor('number', number)
    p.set_factor('is_greater', number > 55 )
    practice.append((number, stimuli.TextLine(str(number))))


print(practice) 
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

for p in practice:
    blankscreen.present()
    exp.clock.wait(2000)
    p[1].present()
    key, rt = exp.keyboard.wait(LESSTHAN_RESPONSE+ GREATERTHAN_RESPONSE, duration=MAX_RESPONSE_DELAY)
    is_correct_answer = (p.get_factor('is_greater') and key == GREATERTHAN_KEY) or \
                        (not p.get_factor('is_greater') and key ==  LESSTHAN_KEY)
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

