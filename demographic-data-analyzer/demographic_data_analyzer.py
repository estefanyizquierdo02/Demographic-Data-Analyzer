import pandas as pd
# Para leer el documento
df = pd.read_csv("adult.data.csv")
**1)¿Cuántas personas de cada raza están representadas en este conjunto de datos?**
raza= df['race'].value_counts()
print(raza)
**2)¿Cuál es la edad promedio de los hombres?**
promedio_hombres = round(df[df['sex'] == 'Male']['age'].mean(), 1)
print("Edad promedio de los hombres:", promedio_hombres)
**3)¿Cuál es el porcentaje de personas que tienen una licenciatura?**
porcentaje_licenciatura = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)
print(f"Porcentaje de personas con licenciatura: {porcentaje_licenciatura}%")
**4)¿Qué porcentaje de personas con educación avanzada ( Bachelors, Masters, o Doctorate) ganan más de 50.000?**
educacion_avanzada = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
educacion_avanzada_rico = round((df[educacion_avanzada]['salary'] == '>50K').sum() / len(df[educacion_avanzada]) * 100, 1)
print(f"Porcentaje de personas con educación avanzada que ganan >50K: {educacion_avanzada_rico}%")
**5)¿Qué porcentaje de personas sin estudios superiores ganan más de 50.000 dólares?**
educacion_inferior = ~educacion_avanzada
educacion_inferior_rico = round((df[educacion_inferior]['salary'] == '>50K').sum() / len(df[educacion_inferior]) * 100, 1)
print(f"Porcentaje de personas sin educación avanzada que ganan >50K: {educacion_inferior_rico}%")
**6)¿Cuál es el número mínimo de horas que una persona trabaja por semana?**
minimo_horas = df['hours-per-week'].min()
print("Número mínimo de horas trabajadas:", minimo_horas)
**7)¿Qué porcentaje de las personas que trabajan el número mínimo de horas semanales tienen un salario superior a 50.000?**
trabajadores_minimos = df[
    df['hours-per-week'] == minimo_horas
]
porcentaje_ricos_minimos = round(((trabajadores_minimos['salary'] == '>50K').sum()/ len(trabajadores_minimos)) * 100,1)
print(f"Porcentaje de personas que trabajan "f"el mínimo de horas y ganan >50K: "f"{porcentaje_ricos_minimos}%")
**8)¿Qué país tiene el mayor porcentaje de personas que ganan más de 50.000 dólares y cuál es ese porcentaje?**
total_pais = df['native-country'].value_counts()
ricos_pais = df[df['salary'] == '>50K']['native-country'].value_counts()
porcentaje_pais = (ricos_pais / total_pais) * 100
pais_mayor_porcentaje = (porcentaje_pais.idxmax())
mayor_porcentaje = round(porcentaje_pais.max(), 1)
print(f"País con mayor porcentaje de personas "f"que ganan >50K: "f"{pais_mayor_porcentaje}")
print(f"Mayor porcentaje: "f"{mayor_porcentaje}%")
**9)Ocupación más popular en India con >50K**
india_ricos = df[(df['native-country'] == 'India') &(df['salary'] == '>50K')]
ocupacion_popular_india = india_ricos['occupation'].value_counts().idxmax()
print("Ocupación más popular en India para personas que ganan >50K:",ocupacion_popular_india)
