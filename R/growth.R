library(gamlss)
library(gamlss.ggplots)
library(ggh4x)
library(dplyr)  # For data manipulation
library(haven)  # For reading .sav files

# Load the dataset
df <- read_spss('data/CASPIANI.sav')

# Convert SEX to a factor with labels "Male" and "Female"
df$SEX <- as_factor(df$SEX)

duplicate_ages <- df %>% 
  group_by(AGE) %>% 
  filter(n() > 1)

# Print out duplicates to examine
print(duplicate_ages)
# Check the first few rows to ensure the conversion worked
head(df$SEX)

# Select required columns, filter age range, and remove rows with NA
# Separate data for each sex
# Define the age list
age <- list(7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)

# Ensure filtered_male_df and filtered_female_df are correctly filtered
filtered_male_df <- df %>%
  select(AGE, SEX, HEIGHT) %>%  # Select only age, sex, and height columns
  filter(AGE >= 7 & AGE <= 18, SEX == "Male") %>%  # Filter for males
  na.omit()  # Remove rows with NA values

filtered_female_df <- df %>%
  select(AGE, SEX, HEIGHT) %>%  # Select only age, sex, and height columns
  filter(AGE >= 7 & AGE <= 18, SEX == "Female") %>%  # Filter for females
  na.omit()  # Remove rows with NA values

# Check if the filtered data has the correct columns
head(filtered_male_df)

# Loop to assign dataframes dynamically for each age
for(i in 1:12) {  # Loop through 1 to 12 (ages 7 to 18)
  # Dynamically create dataframes db1 to db12 with height data and corresponding age
  assign(paste0("db", i), data.frame(height = filtered_male_df$HEIGHT[filtered_male_df$AGE == age[[i]]], 
                                     age = rep(age[[i]], sum(filtered_male_df$AGE == age[[i]]))))
}
#bind dbs
Merge_DB<-rbind(db1,db2,db3,db4,db5,db6,db7,db8,db9,db10,db11,db12)
#delete missing values
Final_DB<-Merge_DB[complete.cases(Merge_DB),]
#sort by weight
Final_DB<-Final_DB[order(Final_DB$height), ]
summary(Final_DB)
table(Final_DB$age)

GPlot <- lms(y = height, 
             x = age, 
             data = Final_DB, 
             trans.x = FALSE, 
             control = gamlss.control(n.cyc = 200, c.crit = 0.01))



centiles_to_plot <- c(25, 75)  # Example: select 25th and 75th centiles
calibration(GPlot, xvar,legend = TRUE, fan = FALSE,points=FALSE,cent = centiles_to_plot)


# Modify the centiles function call
centiles(GPlot, legend = TRUE, 
         ylab = "Height(cm)", 
         xlab = "Age(month)", 
         main = "Growth_Curve (Girl)",
         cent = centiles_to_plot, 
         points = FALSE)# Extract fitted values for different centiles

# Create the plot as you did before
themeplot <- fitted_centiles_legend(GPlot, cent = centiles_to_plot,
                                    points = FALSE, show.legend = TRUE) +
  scale_x_continuous(expand = c(0,0), breaks = c(2*(0:12))) +
  scale_y_continuous(breaks = c(2*(0:100))) +
  theme(plot.title = element_text(hjust = 0.5),
        panel.background = element_rect(fill = "white", colour = "black"),
        panel.grid = element_blank()) +
  ggtitle("Growth_Curve (Girl)") +
  xlab('Age (months)') +
  ylab('Height (cm)')

# Save the plot to a file
ggsave("growth_curve_girl_multiple_centiles.png", plot = themeplot, width = 8, height = 6, dpi = 300)



# sss <- extractLMS(fit =GPlot,data = filtered_male_df ,sex = "M",grid = "classic", decimals = c(4, 4, 4),
#            flatAge = NULL )
