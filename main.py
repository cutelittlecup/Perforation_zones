import pandas as pd


def check_values(row):
    if 1 in row.values:
        return 1
    else:
        return 0


well_head = 'скважина'
bottom_head = 'низ'
top_head = 'верх'
file_name = 'пример.xlsx'

df = pd.read_excel(file_name)

df[well_head] = df[well_head].astype(str)
df[well_head] = df[well_head].astype(str)
df[[bottom_head, top_head]] = df[[bottom_head, top_head]].astype(float)

unique_wells = df[well_head].unique()

md = [i for i in range(1, 4001)]

for well in unique_wells:
    df_well = df[df[well_head] == well].reset_index()

    columns = ['MD']
    for i in range(len(df_well)):
        columns = columns + ['перф' + str(i + 1)]
    df_md = pd.DataFrame(index=range(len(md)), columns=columns)
    df_md['MD'] = md

    for index, row in df_well.iterrows():
        bottom = row[bottom_head]
        top = row[top_head]
        if bottom > top:
            a = bottom
            bottom = top
            top = a

        df_md['перф' + str(index + 1)] = df_md['MD'].apply(lambda x: 1 if round(bottom) <= x == round(top) else 0)

    df_md_2 = pd.DataFrame(index=range(len(md)), columns=['MD', 'Итог'])

    df_md_2['Итог'] = df_md[columns[1:]].apply(check_values, axis=1)
    df_md_2['MD'] = md

    df_md_2.to_csv('скважина ' + well + '.txt', sep='\t', index=False)
