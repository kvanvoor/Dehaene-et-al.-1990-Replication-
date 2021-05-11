PCBS Project, May 2021
=====================
Dehaene et al.,1990 : Experiment 1
-----------------------------------
* Git Hub page:https://github.com/kvanvoor/PCBS_Project

The aim of our project was to produce a replication of Experiment 1 from Dehaene et al.,1990 as close as possible to the original paradigm. See [here](https://github.com/kvanvoor/PCBS_Project/blob/main/Dehaene%20et%20al.%20-%201990%20-%20Is%20numerical%20comparison%20digital%20Analogical%20and%20sy.pdf) for reference.

The experiment consists of a practice session and experimental session in which the participant is presented a number between 11 and 100, except the standard 55, and asked to determine whether it is greater than or less than 55. They are instructed to respond by pressing the 'f' or 'j' keys for 'less than' and 'greater than' respectively.

The stimuli were two pseudo-randomized lists which we created using R and manually implementing the paramters that were outlined in Dehaene et al. (1990), namely:
  * there were not three consecutive numbers greater than 55 or less than 55 presented.
  * there were never two of the same numbers presented consecutively,

As in Dehaene et al. (1990), we were concerned with measuring the response times of the participant during each trial. 

**Table of Contents**

- [Preparation of the stimuli](#preparation-of-the-stimuli)
- [Creating the list of trials](#creating-the-list-of-trials)
- [Running the experiment](#running-the-experiment)

# Preparation of the stimuli
To generate a list of numbers we use a simple [R code](https://github.com/kvanvoor/PCBS_Project/blob/main/stimuli_list_generator.R) and exported the data frame into a csv file. Again, because we wanted to create an experiment as close as possible to the orginal, we followed the same constraints at Deheane et al. All numbers between 11 and 99 (except 55) were entered. Numbers between 41 and 69 were included 4 times, whereas as those outside of this range were included only twice.

Next, we randomly shuffled the list in excel. We then manually ensured that the list adhered to the parameters described above, used by Dehaene et al.

We then created a second list that reversed the order of the first, as Dehaene et al. did.

# Running-the-experiment
We included a practice session with ten stimuli that includes a feedback via a buzzer. The practice session is followed by the experimental session with the list determined by the parity of subject number.

References
----------
Dehaene, S., Dupoux, E., & Mehler, J. (1990). Is numerical comparison digital? Analogical and symbolic effects in two-digit number comparison. Journal of experimental Psychology: Human Perception and performance, 16(3), 626.

