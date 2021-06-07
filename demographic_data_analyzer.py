import pandas as pd

def get_percentage(df, country_key):
  total_mask = df["native-country"] == country_key
  sal_mask = df["salary"] == ">50K"

  total = df[total_mask].shape[0]
  sal = df[sal_mask & total_mask].shape[0]

  percent = round((sal / total) * 100.0, 1)
  return [country_key, percent]

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv") 

    people = df.shape[0]

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    # show all the types of data for info
    #print(df.columns)

    race_count = df["race"].value_counts()

    # What is the average age of men?

    men_mask = df["sex"] == "Male" 
    average_age_men = round(df[men_mask]["age"].mean(), 1)
    #print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?

    bat_mask = df["education"] == "Bachelors"
    percentage_bachelors = round(df[bat_mask].shape[0] / people * 100.0, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    ed_mask = df["education"].isin(["Bachelors", "Masters", "Doctorate"])

    educated = df[ed_mask]
    uneducated = df[~ed_mask]
    
    sal_mask = df["salary"] == ">50K"

    educated_high_earners = df[(ed_mask & sal_mask)]    
    uneducated_high_earners = df[(~ed_mask & sal_mask)]

    # with and without `Bachelors`, percentr `Doctorate`
    higher_education = df[ed_mask]
    lower_education = df[~ed_mask]

    # percentage with salary >50K
    higher_education_rich = round((educated_high_earners.shape[0] / educated.shape[0]) * 100.0, 1)
    lower_education_rich = round((uneducated_high_earners.shape[0] / uneducated.shape[0]) * 100.0, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"] == 1]

    rich_min_worker_mask = (df["hours-per-week"] == 1) & (df["salary"] == ">50K")
    rich_percentage = round(df[rich_min_worker_mask].shape[0] / df[df["hours-per-week"] == 1].shape[0] * 100.0)

    countries = df["native-country"].value_counts()
    country_keys = countries.index.to_list()

    country_percentages = []
    for country_key in country_keys:
      per_country = get_percentage(df, country_key)
      country_percentages.append(per_country)

    sorted_countries = sorted(country_percentages, key=lambda country: country[1], reverse=True)
    
    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = sorted_countries[0][0]
    highest_earning_country_percentage = sorted_countries[0][1]

    # Identify the most popular occupation for those who earn >50K in India.
    india_mask = df["native-country"] == "India"
    india_high_earners = df[sal_mask & india_mask]

    top_IN_occupation = (india_high_earners["occupation"].mode()).to_list()[0]

    # DO NOT MODIFY BELOW THIS LINE
    
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
