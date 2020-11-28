import pandas as pd

cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Endeavour','Audi A4', 'Volksvagen Polo GT'],
        'Price': [22000,25000,27000,35000,50000]
        }

dataframe = pd.DataFrame(cars, columns = ['Brand', 'Price'])
print(dataframe)

dataframe.to_csv('/home/whiskygrandee/Code/interop-project/02_TabularData/cars.csv', index = False, header = True)
'''
Thus the dataframe is saved as a .csv file by the name cars.csv.
'''