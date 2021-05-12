##Data analyses with no pre-processing in Python
#Using function from Expyriment to import into R
library(tidyverse)

read.expyriment.data = function(folder, filename_pattern) 
{
  pattern = paste("^", filename_pattern, ".*\\.xpd", sep="") 
  
  data = data.frame()
  for (fl_name in list.files(path=folder, pattern )) {
    path = file.path(folder, fl_name)
    message("reading ", path)
    d = read.csv(path, comment.char="#", na.strings=c("NA", "None"))
    fl = file(path, "r")
    while(TRUE){
      line = readLines(fl, n=1)
      if (!length(line) || !length(grep("#", line)) )
        break
      else {
        if (length(grep("^#s ", line))>0) {
          tmp = unlist(strsplit(sub("#s ","", line), ":"))
          if (length(tmp)<2) {
            tmp = unlist(strsplit(sub("#s ","", line), "="))
          }
          if (grep("^ ", tmp[2]))
            tmp[2] = substring(tmp[2], 2)
          if (tmp[1] != "id") {
            d = cbind(d, new = tmp[2])
            names(d)[ncol(d)] = tmp[1]
          }
        }
      }
    }
    close(fl)
    if (nrow(data)<1) 
      data = d
    else 
      data = rbind(data, d)
  }
  data
}

#uploading data to R
mydata <- read.expyriment.data("/Users/kiravanvoorhees/Desktop/PCBS/PCBS_Project/data", "distanceeffect")

#begin data cleaning
data1 <- mydata %>%
  filter(is_correct =="True") %>%
  select(number, RT)

#boxplot creation
ggplot(data1,aes(number, y = RT)) +
  geom_boxplot(aes(group = number))+
  geom_vline(xintercept= 55, color="red")
  
