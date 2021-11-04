import requests, json, xlwt

# url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)

data = response.json()

# Save in json file
filename = 'githubusers.json'
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

# Write data to excel file
w = xlwt.Workbook()
ws = w.add_sheet('github_users')
row = 0

# Write to first row
ws.write(row, 0, 'login')
ws.write(row, 1, 'repos_url')
row += 1

# Write data to subsequent rows (NOT WORKING)
for user in data:
    ws.write(row, 0, 'login')
    ws.write(row, 1, 'reps_url')
    row += 1

w.save('github_users.xls')

