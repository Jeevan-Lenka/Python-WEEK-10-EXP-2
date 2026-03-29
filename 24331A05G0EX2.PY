import pandas as pd
df = pd.DataFrame({
	'Name': ['John', 'Alice', 'Bob', 'Diana'],
	'Age': [25, 30, 22, 35],
	'Salary': [50000, 60000, 45000, 70000]
})
print("Original:\n", df)
print("\nSort by Age:\n", df.sort_values('Age'))
print("\nSort by Salary (desc):\n", df.sort_values('Salary', ascending=False))
print("\nRow slice [1:3]:\n", df.iloc[1:3])
print("\nColumn slice 'Name':'Age':\n", df.loc[:, 'Name':'Age'])
print("\nSalary > 50000:\n", df[df['Salary'] > 50000])
 
