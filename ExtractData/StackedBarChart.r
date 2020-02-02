 # library
library(ggplot2)
 

setwd("../FormattedData")
meanDaySleepData <- read.csv(file='meanDaysData.csv')
head(meanDaySleepData)


# create a dataset
# specie <- c(rep("sorgho" , 3) , rep("poacee" , 3) , rep("banana" , 3) , rep("triticum" , 3) )
# condition <- rep(c("normal" , "stress" , "Nitrogen") , 4)
# value <- abs(rnorm(12 , 0 , 15))
# data <- data.frame(specie,condition,value)
 
# # Stacked
# ggplot(data, aes(fill=condition, y=value, x=specie)) + 
#     geom_bar(position="stack", stat="identity")