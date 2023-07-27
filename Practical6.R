df <- read.csv(file.choose())
# declearing variables
x <- df[,'Hours']
y <- df[,'Scores']

cat("\n Missing values in Hours column", sum(is.na(x)))
cat("\n Missing values in Scores column", sum(is.na(y)))

meanTime <- mean(x, na.rm=TRUE)
meanScore <- mean(y, na.rm = TRUE)

x <- ifelse(is.na(x), ave(x, FUN = function(z) mean(z, na.rm=TRUE)), x)
y <- ifelse(is.na(y), ave(y, FUN = function(z) mean(z, na.rm=TRUE)), y)

df[,'Hours'] <- x
df[,'Scores'] <- y

norm_minmax <- function(x){
                           (x- min(x)) /(max(x)-min(x))
                          }

nrmlizeScore <- as.data.frame(lapply(y, norm_minmax))