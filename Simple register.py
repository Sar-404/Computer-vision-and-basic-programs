a={"name":"Alex Evans","age":23,"gender":"male"}
key=a.keys()
while True:
    command=input("Ask or Append\n")
    if command.lower() == "append":
        append_key = input("Enter the key\n")
        append_value = input("Enter the value\n")
        if append_key in key:
            print(f"Nice Try! {append_key.title()} is already registered")
        else:
            a[append_key.lower()] = append_value
    else:
        for i in key:
            if i in command.lower():
                print(f"Their {i} is {a.get(i)}")
