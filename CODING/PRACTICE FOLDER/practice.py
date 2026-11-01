import pandas as pd

cols = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
df = pd.read_csv("car_evaluation.csv", header=None, names=cols)

print(df.shape)                      # should be (1728, 7)
print(df["class"].value_counts())    # unacc 1210, acc 384, good 69, vgood 65