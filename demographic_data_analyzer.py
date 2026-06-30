import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leer los datos desde el archivo
    df = pd.read_csv('adult.data.csv')

    # 1. ¿Cuántas personas de cada raza están representadas?
    race_count = df['race'].value_counts()

    # 2. ¿Cuál es la edad promedio de los hombres?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. ¿Qué porcentaje de personas tienen una licenciatura?
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # 4. Porcentaje con educación avanzada que ganan >50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)

    # 5. Porcentaje sin educación avanzada que ganan >50K
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)

    # 6. Mínimo de horas que trabaja una persona por semana
    min_work_hours = df['hours-per-week'].min()

    # 7. Porcentaje de los que trabajan el mínimo de horas que ganan >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0]) * 100, 1)

    # 8. ¿Qué país tiene el mayor porcentaje de personas que ganan >50K?
    country_stats = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)

    # 9. Ocupación más popular para quienes ganan >50K en la India
    top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].mode()[0]

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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
