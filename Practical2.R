data1 <- read.csv("E:/CHEEKO BOYEE/Programs/2Python/Data sets/Latest Covid-19 India Status.csv")
print(data1)

library("xlsx")
data2 <- read.xlsx("E:/CHEEKO BOYEE/Programs/2Python/Data sets/SampleData.xlsx", sheetIndex = 2)
print(data2)

library(readr)
myData <- read_lines("E:/CHEEKO BOYEE/Programs/2Python/Data sets/Datafile.txt")
print(myData)

write.csv(data1, file = "E:/CHEEKO BOYEE/Programs/2Python/Data sets/datafile.csv")

write.xlsx(data1,"datafile1.xlsx")

write.table(data1, "data.txt")
