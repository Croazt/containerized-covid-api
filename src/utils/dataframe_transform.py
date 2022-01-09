def transform_df(is_type : str, df, since, upto) :
    res = df
    if is_type == 'year' :
        res = res.groupby(['year'])['positive','recovered','deaths'].sum().reset_index()
    
    if is_type == 'month' :
        res = res.groupby(['year','month'])['positive','recovered','deaths'].sum().reset_index()
        res['month'] = res['month'].astype(str).apply(lambda x: x.zfill(2))
        res['month'] = res[['year','month']].astype(str).agg('-'.join,axis=1)
        res = res.drop(columns=['year'])

    if is_type == 'date' :
        res['month'] = res['month'].astype(str).apply(lambda x: x.zfill(2))
        res['date'] = res['date'].astype(str).apply(lambda x: x.zfill(2))
        res['date'] = res[['year','month','date']].astype(str).agg('-'.join,axis=1)
        res = res.drop(columns=['year','month', 'key'])

    res = res[(res[is_type] >= (since)) & (res[is_type] <= (upto))]

    res['active'] = res['positive'] - res['recovered'] - res['deaths']
    return res
