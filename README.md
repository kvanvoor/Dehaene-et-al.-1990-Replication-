PCBS Project, May 2021
=====================
Dehaene et al.,1990 : Experiment 1
-----------------------------------
* Git Hub page:https://github.com/kvanvoor/PCBS_Project

The aim of our project was to produce a replication of Experiment 1 from Dehaene et al.,1990 as close as possible to the original paradigm. See [here](https://github.com/kvanvoor/PCBS_Project/blob/main/Dehaene%20et%20al.%20-%201990%20-%20Is%20numerical%20comparison%20digital%20Analogical%20and%20sy.pdf) for reference.

The experiment consists of a practice session and experimental session in which the participant is presented a number between 11 and 100, except the standard 55, and asked to determine whether it is greater than or less than 55. They are asked to respond by pressing the 'f' or 'j' keys for 'less than' and 'greater than' respectively.

The stimuli were two pseudo-randomized lists which we created using R and manually implementing the paramters that were outline ins Dehaene et al. (1990), namely:
  * there were not three consecutive numbers greater than 55 or less than 55 presented
  * there were never two of the same numbers presented consecutively
Every number was presented 2 times, except those between 41 and 69, which were presented 4 times. 


The experiment presents a random number between 1 and 99, and asks the subject to decide wether the presented number is smaller or larger than 55. We then plot the reactions times as a function of the number.

Do you replicate the distance effect reported by Dehaene, S., Dupoux, E., & Mehler, J. (1990) in “Is numerical comparison digital? Analogical and symbolic effects in two-digit number comparison.” Journal of Experimental Psychology: Human Perception and Performance, 16, 626–641.?



References
----------
Dehaene, S., Dupoux, E., & Mehler, J. (1990). Is numerical comparison digital? Analogical and symbolic effects in two-digit number comparison. Journal of experimental Psychology: Human Perception and performance, 16(3), 626.

