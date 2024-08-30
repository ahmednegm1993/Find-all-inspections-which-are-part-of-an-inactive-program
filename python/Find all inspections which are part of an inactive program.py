import pandas as pd

df=pd.read_excel(r'E:\\Data_analysis_projects\\Find all inspections which are part of an inactive program\\dataset\\Find all inspections which are part of an inactive program.xlsx')
df_inactive=df[df['program_status']=='INACTIVE']
print(df_inactive)