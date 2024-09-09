#Solution 1
# keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education',
# 'company', 'salary']

# values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890',
# 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]

# info = {}

# for i in keys:
#     info[i] = values[keys.index(i)]

# print(info)

#Solution 2
keys = [
    'name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby',
    'education', 'company', 'salary'
]

values = [
    'Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890',
    'Reading', 'Masters in Computer Science', 'TechCorp', 90000
]

info = dict(zip(keys, values))

print(info)