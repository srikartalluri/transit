import pandas as pd

routes = pd.read_csv('data/routes.txt')
stop_times = pd.read_csv('data/stop_times.txt')
stops = pd.read_csv('data/stops.txt')
fare_rules = pd.read_csv('data/fare_rules.txt')
fare_attributes = pd.read_csv('data/fare_attributes.txt')
trips = pd.read_csv('data/trips.txt')


print(fare_rules)
print(fare_attributes)


# def getAllFaresFromOrigin(df, origin):
#     return df.loc[df['origin_id']  == origin]




fareComb = fare_attributes.join(fare_rules, how='inner', lsuffix='l')#.drop('fare_idl', axis=1)

print(fareComb)

