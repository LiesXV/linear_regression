import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame
    """
    try:
        if not isinstance(path, str):
            raise ValueError("Path must be a string")
        if not path.endswith(".csv"):
            raise ValueError("Path must be a CSV file")
        dataset = pd.read_csv(path, header=None, names=['km', 'price'], skiprows=1)
    except Exception as e:
        print(e)
        return None
    return dataset

def __main__():
	"""Main function to execute the script."""
	filepath = "data.csv"
	df = load(filepath)
	if df is None:
		print("Failed to load data.")
		return

	km = df.iloc[:, 0]
	price = df.iloc[:, 1]

	km_max = max(km)
	km_normalized = [x / km_max for x in km]

	m = len(df)
	learningRate = 0.1
	theta0 = 0
	theta1 = 0
	
	nb_iterations = 1000

	for iteration in range(nb_iterations):
		sum_erreurs = 0.0
		sum_erreurs_ponderees = 0.0

		for i in range(m):
			prediction = theta0 + theta1 * km_normalized[i]
			# print(prediction)
			erreur = prediction - price[i]
			sum_erreurs += erreur
			sum_erreurs_ponderees += erreur * km_normalized[i]

		theta0 = theta0 - (learningRate * 1/m * sum_erreurs)
		theta1 = theta1 - (learningRate * 1/m * sum_erreurs_ponderees)
	
	theta1 = theta1 / km_max

	with open("thetas.txt", "w") as f:
		f.write(str(theta0))
		f.write('\n')
		f.write(str(theta1))
		f.write('\n')

if __name__ == "__main__":
	__main__()