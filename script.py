limit = 11
lower = 1
interval = 10
sets = []

# Find ranges given limit and interval
for i in range(lower, limit, interval):
    intervals = [i, i + interval - 1]
    print(f"/api?Action=TopSites&Count={interval}&CountryCode=US&ResponseGroup=Country&Output=json&Start={intervals[0]}")

