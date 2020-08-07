import matplotlib.pyplot as plt
import pandas as pd

mood = pd.read_csv('spam_ham.csv')
mood_label = mood["label"].value_counts()
names = list(mood_label.index)
values = list(mood_label.values)
print(names)
print(values)
plt.bar(names, values)
plt.show()