import pandas as pd
from sqlalchemy import create_engine

df= pd.DataFrame([[9999, 1250, 3000], [4000, 5000, 6000], [7, 8, 9]],
                 columns=['a', 'b', 'c'])

usr = 'leonardo'
pas = 'Postgres2018!'
hst = 'postgres-hst'
prt = '5432'
db = 'db_test'
drivers = ['postgresql+psycopg2', 'mysql+mysqldb']
engine = create_engine(f'{drivers[0]}://{usr}:{pas}@{hst}:{prt}/{db}')
print(engine)
print(df)
df.to_sql('sample', con=engine, if_exists='replace', index=False)

