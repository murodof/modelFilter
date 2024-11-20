import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = '/home/azizbek/Desktop/PrepareArticle/modelFilter/data.xlsx'
data = pd.read_excel(file_path)

# Faqat son turidagi ustunlarni olib olamiz
numeric_columns = data.select_dtypes(include=["number"])
df = pd.DataFrame(numeric_columns)

# Matematik kutilma ya'ni o'rtacha qiymatni hisoblab olamiz
mean_values = df.mean()

#  R(i,j) matritsasini yaratib olamiz
R_matrix = {}
for i in df.columns:
    for j in df.columns:
        R_matrix[f"R({i},{j})"] = (df[i] / mean_values[i]) - (df[j] / mean_values[j])

R_matrix_df = pd.DataFrame(R_matrix)

# R(i,j) matritsasining har bir ustuni bo'yicha min max qiymatlarni topib olamiz
min_values = R_matrix_df.min()
max_values = R_matrix_df.max()

# Min va Max qiymatlar oralig'ini saqlash uchun dictionary yaratib olamiz
range_dict = {col: (min_values[col], max_values[col]) for col in R_matrix_df.columns}

# Datasetimiz ichidan ixtiyoriy bitta obektni tanlab olamiz test uchun albatta
test_object = df.sample(1).iloc[0]
random_object = np.random.uniform(low=df.min().min(), high=df.max().max(), size=len(df.columns))

test1_R_values = {}
for i in df.columns:
    for j in df.columns:
        test1_R_values[f"R({i},{j})"] = (test_object[i] / mean_values[i]) - (test_object[j] / mean_values[j])

random_R_values = {}
for i, col in enumerate(df.columns):
    for j, col_j in enumerate(df.columns):
        random_R_values[f"R({col},{col_j})"] = (random_object[i] / mean_values[col]) - (
                    mean_values[col_j] / mean_values[col_j])


# Bizda asosiy funksiya ya'ni Yangi test uchun kirib kelgan obektni R(i,j) matritsaning hamma mos  ustunlari
# (min,max) oraliqga tushsa True bo'lmasa tushmagan ustunini nomini qaytaradi

def check_ranges(test_R, range_dict):
    mismatched_columns = []
    for col, value in test_R.items():
        if col in range_dict:
            min_val, max_val = range_dict[col]
            if not (min_val <= value <= max_val):
                mismatched_columns.append(col)
    return True if not mismatched_columns else mismatched_columns


def visualize_results(result, range_dict):
    if result:
        # Tushmagan ustunlar ro'yxatini olish
        mismatched_columns = [col for col in result if col in range_dict]

        # Tushmagan ustunlar uchun chizma
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(mismatched_columns, [range_dict[col][0] for col in mismatched_columns], color='red', label='Min')
        ax.bar(mismatched_columns, [range_dict[col][1] for col in mismatched_columns], color='blue', alpha=0.5,
               label='Max')

        ax.set_xlabel('Ustunlar')
        ax.set_ylabel('Qiymatlar')
        ax.set_title('Tushmagan Ustunlar: Min-Max Oralig\'ida Tushmagan Qiymatlar')
        ax.legend()
        plt.xticks(rotation=45)
        plt.show()


# Test the random object
result1 = check_ranges(test1_R_values, range_dict)  # True
print(result1)
result2 = check_ranges(random_R_values, range_dict)
print(result2)


visualize_results(result2, range_dict)
