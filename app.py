from horse_race import horse_racing
racing = horse_racing(12)
horse_id = racing.horse_with_id()
ages = racing.age_of_horses()
breeds = racing.breed_horse()
gender = racing.horses_gender()
df = racing.dataframe(horse_id, ages, breeds, gender)
print(df.head())


