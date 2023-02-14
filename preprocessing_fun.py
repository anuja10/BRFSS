import os

def state_filter(df, path):
    statedf = df[df['Locationabbr']=='IN']
    statedf.to_csv(os.path.join(path, 'BRFSS_IN.csv'))
    return statedf