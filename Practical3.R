#install.packages("modeest")
df <- read.csv(file.choose())
# declearing variables
x <- df[,'Hours']
y <- df[,'Scores']

cat("\n Mean of Score: ",mean(y))
cat("\n Median of Score: ", median(y))
library('modeest')
mode <- mfv(df$Scores)
cat("\n Mode of Score: ", mode)