import pandas as pd
import email
import email.policy
import os
import re

data = pd.DataFrame(columns = ["content", "num_unique_words", "total_num_words", "label"])

rootdir = 'C:/Users/saswa/OneDrive/Documents(PC)/AI Club Summer Camp #/hamnspam'
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        list_path = subdir.split('/')
        label = list_path[-1]
        #print(file, label)

        full_path = subdir + "/" +  file
        #print(full_path)

        with open(full_path, "rb") as f:
            email_data = f.read()
            email_obj = email.message_from_bytes(email_data)
            from_who = email_obj['From']
            Subject = email_obj["Subject"]
            content = email_obj.get_payload()

            #print(type(content))

            #print(content)
            try:
                content = re.sub(r'\W+', ' ', content)
                words_list = content.split()
            except Exception as e:
                words_list = []
            total_num_words = len(words_list)
            num_unique_words = len(set(words_list))
            dict_sample = {"content": content, "num_unique_words": num_unique_words, "total_num_words": total_num_words, "label": list_path[-1]}
            data = data.append(dict_sample, ignore_index=True)

        #print(email_data)

data.to_csv("spam_ham.csv",index=False)