library(haven)
library(dplyr)
library(ggplot2)
library(scales)

# Load datasets
df <- read_spss('data/CASPIANI.sav')
df_iii <- read_spss('data/CASPIAN III.sav')
df_iv <- read_spss('data/caspian4_.sav')
df_v <- read_spss('data/last-caspian-v.sav')

# Function to rename columns based on dataset version
rename_features <- function(df, caspian_number) {
  df <- df %>% rename_with(tolower)
  
  if (caspian_number == 5) {
    df <- df %>% rename(weight = weight_1, height = height_2, university = universi, schoolType = ap_9)
  } else if (caspian_number == 4) {
    df <- df %>% select(-sex) %>% rename(sex = sex2, weight = weight_1, height = height_2, university = University, schoolType = ap_9)
  } else if (caspian_number == 3) {
    df <- df %>% rename(weight = weighte, height = heighte, university = province, region = area, schoolType = p9)
  } else if (caspian_number == 1) {
    df <- df %>% rename(university = univer, region = district, schoolType = schoolty)
  }
  return(df)
}

# Rename columns in each dataset
df <- rename_features(df, 1)
df_iv <- rename_features(df_iv, 4)
df_iii <- rename_features(df_iii, 3)
df_v <- rename_features(df_v, 5)

# Normalize values for sex and region
normalize_columns <- function(df) {
  df$sex <- ifelse(df$sex == "Female" | df$sex == "female", "Girl", ifelse(df$sex == "Male" | df$sex == "male", "Boy", df$sex))
  df$region <- ifelse(df$region == "Urban", "urban", ifelse(df$region == "Rural", "rural", df$region))
  df$schoolType <- case_when(
    df$schoolType %in% c("dolati", "Dolati") ~ "Public School",
    df$schoolType %in% c("gheyre entefaei", "gheyre entef", "gheyre entefai") ~ "Private School",
    TRUE ~ "Unknown"
  )
  return(df)
}

df <- normalize_columns(df)
df_iii <- normalize_columns(df_iii)
df_iv <- normalize_columns(df_iv)
df_v <- normalize_columns(df_v)

# Store datasets in a list
df_dict <- list(caspian_I = df, caspian_III = df_iii, caspian_IV = df_iv, caspian_V = df_v)

# Preprocess function
preprocess <- function(dataframes_dict) {
  processed_dfs <- list()
  
  for (name in names(dataframes_dict)) {
    df <- dataframes_dict[[name]]
    
    # Filter by age
    df <- df %>% filter(age >= 7 & age <= 18)
    
    # Convert height and weight to numeric
    df$height <- as.numeric(df$height)
    df$weight <- as.numeric(df$weight)
    
    # Calculate BMI
    df$bmi1 <- df$weight / ((df$height / 100) ^ 2)
    
    # Remove rows with NA values in height, weight, or sex
    records_with_nulls <- df %>% filter(is.na(weight) | is.na(height) | is.na(sex) | is.na(age))
    cat("Number of records with NA in", name, ":", nrow(records_with_nulls), "\n")
    
    df <- df %>% drop_na(height, weight, sex)
    
    processed_dfs[[name]] <- df
  }
  
  return(processed_dfs)
}

processed_dfs <- preprocess(df_dict)

# Growth chart function
growth_chart <- function(processed_dfs, feature, percentiles, sex, frec_rate) {
  for (name in names(processed_dfs)) {
    preprocess_df <- processed_dfs[[name]]
    
    # Calculate percentiles
    calculate_percentiles <- function(data, percentiles) {
      sapply(percentiles, function(p) quantile(data, probs = p / 100, na.rm = TRUE))
    }
    
    percentile_results <- preprocess_df %>%
      filter(sex == sex) %>%
      group_by(age) %>%
      summarise(across(all_of(feature), ~ calculate_percentiles(., percentiles))) %>%
      pivot_longer(cols = starts_with("height"), names_to = "percentile", values_to = "value")
    
    if (nrow(percentile_results) == 0) {
      cat("No percentile results for", name, "with feature", feature, "\n")
      next
    }
    
    # Plotting
    p <- ggplot(percentile_results, aes(x = age, y = value, color = percentile)) +
      geom_smooth(method = "loess", span = frec_rate, se = FALSE) +
      labs(x = "Age", y = feature, title = paste("Growth Chart for", sex, "in", name), color = "Percentile") +
      scale_color_viridis_d() +
      theme_minimal()
    
    # Save plot
    file_path <- paste0("charts/", name, "-smooth/", sex, "-", feature, "-age_smooth-", name, ".png")
    print(file_path)
    dir.create(dirname(file_path), recursive = TRUE, showWarnings = FALSE)
    ggsave(file_path, plot = p)
    cat("Chart saved for", sex, "in", name, "with feature", feature, "\n")
  }
}

# Usage example
growth_chart(processed_dfs, "height", c(5, 25, 50, 75, 95), "Boy", 0.3)

