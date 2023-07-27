
# Read data frame from csv file or create using vectors
df <- read.csv(file.choose())
# declearing variables
x <- df[,'Hours']
y <- df[,'Scores']
#creating model
model <- lm(y~x)
#ploting graph using data points and model created line
plot(x,y, abline(lm(y~x)), main = "Student Score vs Study Time",
     xlab = "Study in Hrs", ylab = "Score out of 100")
# prediction if student will study for 9 hours
print(predict(model, data.frame(x = 9)))
# model summery
print(summary(model))
