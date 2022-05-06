import os
import pandas as pd

product_id = input("Please enter id of the product: ")

#print(*[file[:file.rfind('.')] for file in os.listdir("./opinions/")], sep='\n')

opinions = pd.read_json(f"opinions/opinions_{product_id}.json")

print(opinions)