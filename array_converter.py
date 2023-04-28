import pandas as pd
import numpy as np



class array:
    def get_data(path):
        data = pd.read_csv(path)
        return data

    path = 'dataset/kc_house_data.csv'
    data = get_data(path)
    
    data = data[data['price'] < 1127500.000]

    train_data = data[['price', 'bedrooms', 'bathrooms',
                    'floors', 'waterfront', 'view', 'condition', 'grade',
                    'sqft_living', 'sqft_lot', 'yr_built', 'zipcode']]
    
    @classmethod
    def get_array(self, bedrooms = train_data['bedrooms'].mean(),
                 bathrooms = train_data['bathrooms'].mean(),
                 floors = train_data['floors'].mean(),
                 waterfront = train_data['waterfront'].mean(),
                 view = train_data['view'].mean(),
                 condition = train_data['condition'].mean(),
                 grade = train_data['grade'].mean(),
                 sqft_living = train_data['sqft_living'].mean(),
                 sqft_lot = train_data['sqft_lot'].mean(),
                 yr_built = train_data['yr_built'].mean(),
                 zipcode = train_data['zipcode'].mean()
                 ):
        
        self.valores = (bedrooms, bathrooms, floors, waterfront,
                        view,condition, grade, sqft_living,
                        sqft_lot, yr_built, zipcode)
        self.array = np.array(self.valores)
        return self.array
