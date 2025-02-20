import pandas as pd

#load data set
df=pd.read_csv("customer_purchases.csv")
print(df)

# Blank line
print()

#revenue by segment
revenue_by_segment= df.groupby('Segment')['Revenue'].sum()
print(revenue_by_segment)
print()

#Budget Allocation based on revenue
marketing_budget={
                  'Segment A': 5000 if revenue_by_segment['Segment A'] >1000 else 3000,
                  'Segment B': 3000 if revenue_by_segment['Segment B'] >500 else 2000,
                  'Segment C': 2000 if revenue_by_segment['Segment C'] >400 else 1000
                 }

# print the Marketing Budget Allocation
print("Marketing Budget Allocation:")
for segment,budget in marketing_budget.items():
    print(f"Allocate {budget} to marketing for {segment}")

# Plotting Revenue by Segment (Bar Chart)

# importing Libraries
import matplotlib.pyplot as plt

# Plotting Revenue by Segment (Bar Chart)
plt.figure(figsize=(8,6))
revenue_by_segment.plot(kind='bar', color='skyblue')
plt.title('Revenue by Segment')
plt.xlabel('Segment')
plt.ylabel('Total Revnue')
plt.savefig('Revenue_by_segment.png')
plt.show()

# Plotting Revenue by Segment(Pie Chart)
plt.figure(figsize=(8,6))
revenue_by_segment.plot(kind='pie',autopct='%1.1f%%',startangle=90,colors=['yellow','red','skyblue'])
plt.title('Revenue by Segment')
plt.ylabel('')
plt.savefig('Revenue_pie_segment.png')
plt.show()

# Plotting Marketing Allocation(Bar chart)
segments=list(marketing_budget.keys())
budgets=list(marketing_budget.values())
plt.figure(figsize=(8,6))
plt.bar(segments,budgets,color='lightgreen')
plt.title('Marketing Budget Allocation')
plt.xlabel('Segments')
plt.ylabel('Budget Allocation')
plt.savefig('Marketing Budget Allocation.png')
plt.show()