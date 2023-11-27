from typing import List, Any

import pandas as pd
from votings_to_csvfile import arrange_votings

df_laws = pd.read_csv('pages/csv/6sep-15nov-2.csv', sep='|')
row_number = arrange_votings('pages/csv/uploads-media-default-0001-90-070923135531_06-09-2023 11-19 Голосование 6.pdf.csv')



def deputy_votes(fio):
    s = []
    row = row_number[row_number['Депутаты'] == fio].index[0]
    for link in df_laws['vote_link']:
        string = link.removeprefix('http://kenesh.kg//').replace('/', '-') + '.csv'
        votes = arrange_votings('pages/csv/' + string)
        s.append(votes.iloc[row, 1])
    fio_df = df_laws[['law', 'reading', 'initiators', 'committee']].copy()
    fio_df['vote'] = s
    return fio_df
