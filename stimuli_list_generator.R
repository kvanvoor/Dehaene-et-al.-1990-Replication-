#generating list of all the stimuli

list <- c(rep(41:54,4), rep(56:69,4),rep(11:40,2), rep(70:100,2))
list1 <- sample(list)

df1 <- as.data.frame(list1)

write.csv(df1, "df1.csv")
