# Hypothesis Testing

# Load the Dataset
install.packages("readxl")
library(readxl)


######## Cutlets.xlsx data ##########

Cutlets <- read_excel(file.choose())
View(Cutlets)
attach(Cutlets)

#############Normality test###############

#Ho= Data is normally distributed (no action take)
#Ha=Data is not normally distributed (action take)

shapiro.test(`Unit A`)
# p-value = 0.32 >0.05 so p high null fly => It follows normal distribution

shapiro.test(`Unit B`)
# p-value = 0.5225 >0.05 so p high null fly => It follows normal distribution


#############Variance test###############

var.test(`Unit A`,`Unit B`)
# p-value = 0.3136 > 0.05 so p high null fly => Equal variances accept null hypothesis.
#Ho= Variance of diameters of Unit A is equal to the variance of diameters of Unit B
#Ha= Variance of diameters of Unit A is not equal to the variance of diameters of Unit B


############2 sample t Test ###############

?t.test()
t.test(`Unit A`,`Unit B`, alternative = "two.sided",conf.level = 0.95)
# p-value = 0.4723 > 0.05 p high null fly accept null Hypothesis

# alternative = "two.sided" means we are checking for equal and unequal
#Ho= Averages of diameters of Unit A is equal to Averages of diameters of unit B
#Ha= Averages of diameters of Unit A is not equal to Averages of diameters of unit B


#Inference is that there is no significant difference in the diameters of Unit A and Unit B


