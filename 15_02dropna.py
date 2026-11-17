# 실습 4
import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'
df = pd.read_csv(F_PROC)

#versions = {'원본': df, '행제거':df.dropna(), 'thresh20': df.dropna(thresh=20)}
#comparison_rows =[]

#for name, frame in versions.items():
#    comparison_rows.append({
#        '방식': name, '행수': len(frame),
#        '손실률_%': (1 - len(frame) / len(df)) * 100,
#        '불량수': int(frame['불량여부'].sum()),
#        '불량비율_%': frame['불량여부'].mean() * 100
#    })

#comparison = pd.DataFrame(comparison_rows)
#print(comparison.round(1).to_string(index=False))

# 실습 5

#col = '최대사출압'
#mask = df[col].isna()
#print('원래 결측:', mask.sum())          

#mean_val = df[col].mean()               
#median_val = df[col].median()           
#df_mean = df.copy()
#df_mean[col] = df_mean[col].fillna(mean_val)

#df_median = df.copy()
#df_median[col] = df_median[col].fillna(median_val)

#print('평균대체 후 NaN:', df_mean[col].isna().sum())     
#print('중앙값대체 후 NaN:', df_median[col].isna().sum()) 

#idx = df.index[mask][:3]
#print(pd.DataFrame({
#    '평균대체': df_mean.loc[idx, col],
#    '중앙값대체': df_median.loc[idx, col]
#}))

#print('관측값 유지:',
#      df_mean.loc[~mask, col].equals(df.loc[~mask, col]) and
#      df_median.loc[~mask, col].equals(df.loc[~mask, col]))

# ffill, bfill

series_demo = pd.Series([None, 73.0, None, None, 75.0])

# ffill - 앞에서 마지막으로 확인한 값으로 채움
print(series_demo.ffill().tolist())           #[nan, 73.0 , 73.0, 73.0, 75.0]
# - limit: 연속 결측 구간에서 최대 몇칸을 채울지
# bfill - 뒤에서 처음 확인되는 값으로 채움
print(series_demo.bfill().tolist())           #[73.0, 73.0, 75.0, 75.0, 75.0]

# 실습 6
NA_RULES = {'배럴온도': [999], '사출입력': [0], '스크루속도':[999]}
log = pd.read_csv(F_LOG, na_values=NA_RULES, parse_dates=['측정시각'])
log['측정시각'] = pd.to_datetime(log['측정시각'], errors='raise')
unknown = log.loc[log['사출기'].isna()].copy()
known = log.loc[log['사출기'].notna()].copy()

known = known.sort_values(['사출기', '측정시각'])
print(len(known), len(unknown))
print(int(log.isna().sum().sum()))

# 앞의 값
candidate = (known.groupby("사출기")["배럴온도"].ffill(limit=1))

observed_at = known['측정시각'].where(known['배럴온도'].notna())
last_time = observed_at.groupby(known['사출기']).ffill()
gap = known['측정시각'] - last_time
print(known['측정시각'], last_time)
can_fill = (known['배럴온도'].isna() & candidate.notna()
            & gap.le(pd.Timedelta('2min')))

# gap.le(pd.Timedelta('2min'))
# - ,le : 이하인지 비교
# - pd.Timedelta('2min') : 2분

# 허용 위치에 온도 넣기
known.loc[can_fill, "배럴온도"] = candidate.loc[can_fill]
print(int(can_fill.sum()))