# A-8: リストを要素に持つリスト

# Name: Bob, Age: 79
# Name: Tom, Age: 59
# Name: Ken, Age: 61

users_info = [["Bob", 79],
              ["Tom", 59],
              ["Ken", 61]]

for name, age in users_info:
    print(f"name: {name}, Age: {age}")
