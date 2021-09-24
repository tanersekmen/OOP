import random
import pandas as pd

class horse_racing:
    def __init__(self, num_horse):
        """
            Params:
                num_horse: this parameter shows us to how many horse will race.

            Example use:
                horse = horse_racing(10)

        """

        self.num_horse = num_horse


    def horse_with_id(self):
        """
            this block returns horses id to see which one will win the race.
            like 1.index, 6.index or more. 
            It will adjust according to number of horses
        """
        ## Buraya bak !!!s
        horse_id = [i for i in range(self.num_horse)]
        df = pd.DataFrame(horse_id, columns=['horse_id'])
        return df

    def age_of_horses(self):
        """
            age: shows what is the age of horses by yearly
                from 2 to 8 
                because horses can not race before they grow enough.
        """

        ages = (2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5 ,8, 8.5)
        random_ages = random.sample(ages, self.num_horse)
        df_age = pd.DataFrame(random_ages, columns=['age'])
        return df_age


    def breed_horse(self):
        """
            breed: Breed of horse affects more than runway, location or other. Note: English horse generally wins.
                {0: 'English', 1: 'Arabic'}
        """

        all_breeds = [breed for breed in range(0,2)] 
        if self.num_horse % 2 == 1:
            breed_values = (all_breeds * int(self.num_horse / 2))
            df_breed = pd.DataFrame(breed_values, columns=['breed'])
            return df_breed
        else:
            breed_values = (all_breeds * int(self.num_horse / 2))
            df_breed = pd.DataFrame(breed_values, columns=['breed'])
            return df_breed
            

    def horses_gender(self):
        """
            gender:  female or male for gender of horse. 
                {0 : 'male', 1: 'female' }
        """
        genders = [gender for gender in range(0,2)] 
        if self.num_horse % 2 == 1:
            gender_values = (genders * int(self.num_horse / 2))
            df_gender = pd.DataFrame(gender_values, columns=['gender'])
            return df_gender
        else:
            gender_values = (genders * int(self.num_horse / 2))
            df_gender = pd.DataFrame(gender_values, columns=['gender'])
            return df_gender


    def dataframe(self, horse_id, ages, breed, gender):
        df = pd.concat([horse_id, ages], axis = 1)
        data = pd.concat([df, breed], axis = 1)
        dataframe = pd.concat([data, gender], axis = 1)
        return dataframe



if __name__ == '__main__':
    racing = horse_racing(4)
    horse_id = racing.horse_with_id()
    ages = racing.age_of_horses()
    breeds = racing.breed_horse()
    gender = racing.horses_gender()
    racing.dataframe(horse_id, ages, breeds, gender)


