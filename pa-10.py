#task 1
danceability = header.index('danceability')
summ = 0
for row in rows:
    summ += float(row[danceability])
summ_avg = summ / len(rows)
print(summ_avg)

#task 2
liveness = header.index('liveness')
energy = header.index('energy')
sum_liveness = 0
counter = 0
for row in rows:
    if float(row[energy]) > 0.5:
        sum_liveness += float(row[liveness])
        counter += 1
avg_liveliness = sum_liveness / counter
print(avg_liveliness)

#task 3
name_counter_dict = {}
artist_name = header.index('artist_name')
for row in rows:
    name_counter_dict[row[artist_name]] = 0
for row in rows:
    if row[artist_name] in name_counter_dict:
        name_counter_dict[row[artist_name]] += 1

print(name_counter_dict)
sorteddd = sorted(name_counter_dict.items(), key = lambda x: x[1], reverse=True)
print(sorteddd[0])

#task 5
name_counter_dict = {}
year_ind = header.index('album_release_date')
years = {}
for row in rows:
    year = row[year_ind]
    years[year[0:4]] = 0

for row in rows:
    year_2 = row[year_ind][0:4]
    if year_2[0:4] in years:
        years[year_2] += 1
top = sorted(years.items(), key = lambda x: x[1], reverse=True)
print(top[0])
