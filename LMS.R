# Load required libraries
library(haven)
library(dplyr)
library(gamlss)
library(ggplot2)
library(tidyr)


# Preprocessing function
preprocess <- function(df_org) {
  df <- df_org
  
  # Filter age
  df <- df %>% filter(age >= 7 & age <= 18)
  
  # Convert height and weight to numeric
  df$height <- as.numeric(df$height)
  df$weight <- as.numeric(df$weight)
  
  # Calculate BMI
  df$bmi1 <- df$weight / ((df$height / 100) ^ 2)
  
  # Remove rows with NA in specified columns
  records_with_nulls <- df %>% filter(is.na(height) | is.na(weight) | is.na(sex))
  df <- df %>% drop_na(height, weight, sex)
  
  print(paste("Number of records with NaN value in weight or height:", nrow(records_with_nulls)))
  
  return(df)
}

# Read SPSS data
df_i_next <- read_sav("data/caspian1 data.sav")
df_i_next <- preprocess(df_i_next)
df_i_next_clean <- na.omit(df_i_next)
# Split data by sex
df_male <- df_i_next_clean %>% filter(sex == 1)
df_female <- df_i_next_clean %>% filter(sex == 2)
print('aaaa')

# Fit LMS model for males (simplify the formula)
GPlot_male <- lms(y = height, x = age, data = df_male, trans.x = FALSE)
# Fit LMS model for females (simplify the formula)
str(GPlot_male)


GPlot_female <- lms(y = height, x = age, data = df_female, trans.x = FALSE)

# Generate percentiles for males using the centiles() function
# GPlot_male <- gamlss(y = height, x = age, data = df_male, trans.x = FALSE)

# centiles_male <- centiles(GPlot_male, cent = c(3,5,10,15,25, 50, 75,90,95,97), points = FALSE)
# percentiles_male <- data.frame(age = centiles_male$age,
#                                P3 = centiles_male$y[centiles_male$cent == 3],
#                                P5 = centiles_male$y[centiles_male$cent == 5],
#                                P10 = centiles_male$y[centiles_male$cent == 10],
#                                P15 = centiles_male$y[centiles_male$cent == 15],
#                                P25 = centiles_male$y[centiles_male$cent == 25],
#                                P50 = centiles_male$y[centiles_male$cent == 50],
#                                P75 = centiles_male$y[centiles_male$cent == 75],
#                                P90 = centiles_male$y[centiles_male$cent == 90],
#                                P95 = centiles_male$y[centiles_male$cent == 95],
#                                P97 = centiles_male$y[centiles_male$cent == 97])
                                

# # Generate percentiles for females using the centiles() function
# print('cccc')
# centiles_female <- centiles(GPlot_female, cent =  c(3,5,10,15,25, 50, 75,90,95,97), points = FALSE)
# percentiles_female <- data.frame(age = centiles_female$age,
#                                  P3 = centiles_male$y[centiles_male$cent == 3],
#                                P5 = centiles_male$y[centiles_male$cent == 5],
#                                P10 = centiles_male$y[centiles_male$cent == 10],
#                                P15 = centiles_male$y[centiles_male$cent == 15],
#                                P25 = centiles_male$y[centiles_male$cent == 25],
#                                P50 = centiles_male$y[centiles_male$cent == 50],
#                                P75 = centiles_male$y[centiles_male$cent == 75],
#                                P90 = centiles_male$y[centiles_male$cent == 90],
#                                P95 = centiles_male$y[centiles_male$cent == 95],
#                                P97 = centiles_male$y[centiles_male$cent == 97])
# print('dddd')
# # Plot the growth curves
# ggplot() +
#   geom_line(data = percentiles_male, aes(x = age, y = P25, color = "25th Male"), linetype = "dotted") +
#   geom_line(data = percentiles_male, aes(x = age, y = P50, color = "50th Male"), linetype = "solid") +
#   geom_line(data = percentiles_male, aes(x = age, y = P75, color = "75th Male"), linetype = "dashed") +
#   geom_line(data = percentiles_female, aes(x = age, y = P25, color = "25th Female"), linetype = "dotted") +
#   geom_line(data = percentiles_female, aes(x = age, y = P50, color = "50th Female"), linetype = "solid") +
#   geom_line(data = percentiles_female, aes(x = age, y = P75, color = "75th Female"), linetype = "dashed") +
#   labs(title = "Height Growth Curves by Age and Sex",
#        x = "Age (years)", y = "Height (cm)") +
#   theme_minimal() +
#   scale_color_manual(values = c("25th Male" = "blue", "50th Male" = "darkblue", "75th Male" = "lightblue",
#                                 "25th Female" = "pink", "50th Female" = "red", "75th Female" = "orange")) +
#   theme(legend.title = element_blank())
# Generate percentiles for males
centiles_male <- centiles(GPlot_male, cent = c(3,5,10,15,25,50,75,90,95,97), points = FALSE)
print(str(centiles_male))

# Ensure centiles_male has the expected structure
percentiles_male <- data.frame(
  age = centiles_male$age,
  P3 = centiles_male$y[centiles_male$cent == 3],
  P5 = centiles_male$y[centiles_male$cent == 5],
  P10 = centiles_male$y[centiles_male$cent == 10],
  P15 = centiles_male$y[centiles_male$cent == 15],
  P25 = centiles_male$y[centiles_male$cent == 25],
  P50 = centiles_male$y[centiles_male$cent == 50],
  P75 = centiles_male$y[centiles_male$cent == 75],
  P90 = centiles_male$y[centiles_male$cent == 90],
  P95 = centiles_male$y[centiles_male$cent == 95],
  P97 = centiles_male$y[centiles_male$cent == 97]
)
# Generate percentiles for females
# centiles_female <- centiles(GPlot_female, cent = c(3,5,10,15,25,50,75,90,95,97), points = FALSE)
# percentiles_female <- data.frame(age = centiles_female$age,
#                                  P3 = centiles_female$y[centiles_female$cent == 3],
#                                  P5 = centiles_female$y[centiles_female$cent == 5],
#                                  P10 = centiles_female$y[centiles_female$cent == 10],
#                                  P15 = centiles_female$y[centiles_female$cent == 15],
#                                  P25 = centiles_female$y[centiles_female$cent == 25],
#                                  P50 = centiles_female$y[centiles_female$cent == 50],
#                                  P75 = centiles_female$y[centiles_female$cent == 75],
#                                  P90 = centiles_female$y[centiles_female$cent == 90],
#                                  P95 = centiles_female$y[centiles_female$cent == 95],
#                                  P97 = centiles_female$y[centiles_female$cent == 97])

# Check the first few rows of the percentiles_male data frame
# Ensure 'age' is part of the percentiles_male data frame
percentiles_male$age <- centiles_male$age

# Check column names to ensure proper structure
print('1111')
print(colnames(percentiles_male))
# colnames(percentiles_female)
print('1111')


                                               
print('bbbb')
# Plot growth curves for males
# Correct data frame and column references
male_plot <- ggplot() +
  geom_line(data = percentiles_male, aes(x = age, y = P25, color = "25th Male"), linetype = "dotted") +
  geom_line(data = percentiles_male, aes(x = age, y = P50, color = "50th Male"), linetype = "solid") +
  geom_line(data = percentiles_male, aes(x = age, y = P75, color = "75th Male"), linetype = "dashed") +
  geom_line(data = percentiles_male, aes(x = age, y = P3, color = "3rd Male"), linetype = "dotted") +
  geom_line(data = percentiles_male, aes(x = age, y = P5, color = "5th Male"), linetype = "solid") +
  geom_line(data = percentiles_male, aes(x = age, y = P10, color = "10th Male"), linetype = "dashed") +
  geom_line(data = percentiles_male, aes(x = age, y = P90, color = "90th Male"), linetype = "dotted") +
  geom_line(data = percentiles_male, aes(x = age, y = P95, color = "95th Male"), linetype = "solid") +
  geom_line(data = percentiles_male, aes(x = age, y = P97, color = "97th Male"), linetype = "dashed") +
  labs(title = "Height Growth Curves for Male",
       x = "Age (years)", y = "Height (cm)") +
  theme_minimal() +
  scale_color_manual(values = c("3rd Male" = "blue", "5th Male" = "darkblue", "10th Male" = "lightblue", 
                                "25th Male" = "green", "50th Male" = "darkgreen", "75th Male" = "orange",
                                "90th Male" = "red", "95th Male" = "darkred", "97th Male" = "purple")) +
  theme(legend.title = element_blank())

print('dddd')
# Save the male plot

print('eeee')

# Plot growth curves for females
# female_plot <- ggplot() +
#   geom_line(data = percentiles_female, aes(x = age, y = P3, color = "3rd Female"), linetype = "dotted") +
#   geom_line(data = percentiles_female, aes(x = age, y = P5, color = "5th Female"), linetype = "dotted") +
#   geom_line(data = percentiles_female, aes(x = age, y = P10, color = "10th Female"), linetype = "dotted") +
#   geom_line(data = percentiles_female, aes(x = age, y = P15, color = "15th Female"), linetype = "dotted") +
#   geom_line(data = percentiles_female, aes(x = age, y = P25, color = "25th Female"), linetype = "dotted") +
#   geom_line(data = percentiles_female, aes(x = age, y = P50, color = "50th Female"), linetype = "solid") +
#   geom_line(data = percentiles_female, aes(x = age, y = P75, color = "75th Female"), linetype = "dashed") +
#   geom_line(data = percentiles_female, aes(x = age, y = P90, color = "90th Female"), linetype = "dashed") +
#   geom_line(data = percentiles_female, aes(x = age, y = P95, color = "95th Female"), linetype = "dashed") +
#   geom_line(data = percentiles_female, aes(x = age, y = P97, color = "97th Female"), linetype = "dashed") +
#   labs(title = "Height Growth Curves for Females by Age",
#        x = "Age (years)", y = "Height (cm)") +
#   theme_minimal() +
#   scale_color_manual(values = c("3rd Female" = "pink", "5th Female" = "hotpink", "10th Female" = "lightpink", 
#                                 "15th Female" = "lightcoral", "25th Female" = "salmon", "50th Female" = "darkred",
#                                 "75th Female" = "orange", "90th Female" = "darkorange", "95th Female" = "orangered", 
#                                 "97th Female" = "darkviolet")) +
#   theme(legend.title = element_blank())

# Save the female plot
ggsave("male_growth_curve.png", plot = male_plot, width = 10, height = 6, dpi = 300)
# ggsave("female_growth_curve.png", plot = female_plot, width = 10, height = 6, dpi = 300)
