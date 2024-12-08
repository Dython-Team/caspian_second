knitr::opts_chunk$set(echo = TRUE)

library(haven)
library(dplyr)
library(gamlss)
library(ggplot2)
# library(tidyr)
library(ggplot2) # ggplot
library(gamlss) # lms()
library(tidyverse) # %>%

preprocess <- function(df_org) {
  df <- df_org

  # Filter age
  df <- df %>% filter(age >= 7 & age <= 18)
  df <- df %>% select(height, weight, age, sex, hip, waist)

  # Convert height and weight to numeric
  df$height <- as.numeric(df$height)
  df$weight <- as.numeric(df$weight)
  df$hip <- as.numeric(df$hip)
  df$waist <- as.numeric(df$waist)
  # Calculate BMI
  # df$bmi1 <- df$weight / ((df$height / 100) ^ 2)

  # Remove rows with NA in specified columns
  records_with_nulls <- df %>% filter(is.na(height) | is.na(weight) | is.na(sex) | is.na(waist) | is.na(hip))
  df <- df %>% drop_na(height, weight, sex,waist,hip)

  print(paste("Number of records with NaN value in weight or height:", nrow(records_with_nulls)))

  # Split the dataset by sex
  df_split <- split(df, df$sex)
  
  return(df_split)
}

df_i_next <- read_sav("/home/atefe_hjn97/Documents/VScode/caspian_second/data/caspian1 data.sav")
df_i_next <- preprocess(df_i_next)
df_boy <- df_i_next[[1]]
df_girl <- df_i_next[[2]]

print(
  ggplot(df_girl, aes(x=age, y=height)) +
    geom_point(shape = 1, color = "#0052bb", size = 1.5) +
    ggtitle("height caspian 1") +
    xlab("age") + ylab("height") +
    theme_bw()
)

# set.seed(080320)
# IND<-sample.int(dim(df_i_next)[1],10000, replace=FALSE)
# df_i_next<-df_i_next[IND,]
# ggplot(df_i_next, aes(x=age, y=height)) +
#   geom_point(shape = 1, color = "#0052bb", size = 1.5) +
#   ggtitle("Random sample of 10,000 observations") +
#   xlab("age") + ylab("height") +
#   theme_bw()

# Fit the LMS model
m0 <- lms(height, age, families = c("BCCGo", "BCPEo", "BCTo"), data = df_girl,
          k = 3, cent = c(3, 10, 25, 50, 75, 90, 97), calibration = FALSE, trans.x = TRUE)

centiles(m0, cent = c(3, 10, 25, 50, 75, 90, 97), cex = 0.5)