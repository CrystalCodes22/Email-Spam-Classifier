import pandas as pd
import matplotlib.pyplot as plt

# Read the appointments dataset
appt_data = pd.read_csv('spam_ham.csv')

# Plot the no-show compile
label_col = appt_data['label']
no_show_col = appt_data['label'].value_counts()

names = list(no_show_col.index)
values = list(no_show_col.values)
"""
plt.bar(names, values)
plt.show()
"""
# Resample the data
df_subset_1 = appt_data[appt_data['label']=="hamnspam\ham"]
print('number of sample with label ham', len(df_subset_1))
df_subset_2 = appt_data[appt_data['label']=="hamnspam\spam"]
print('number of sample with label spam',len(df_subset_2))
df_subset_1 = df_subset_1.sample(n=len(df_subset_2), replace=True)

new_df = pd.concat([df_subset_1, df_subset_2])

# Plot the re-sampled data.
no_show_col = new_df['label'].value_counts()

names = list(no_show_col.index)
values = list(no_show_col.values)
plt.bar(names, values)
plt.show() 

new_df.to_csv("spam_ham_resampled.csv",index=False)