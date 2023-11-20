
#Pass Statement
for i in range(5):
    if i == 2:
        pass  # Placeholder, no action needed for i == 2
    else:
        print(i)


#Continue Statement
for i in range(5):
    if i == 2:
        continue  # Skip the rest of the loop for i == 2
    else:
        print(i)

#In summary, pass is used when a syntactical requirement needs a statement
# but no action is necessary, while continue is used to skip the remaining code in a loop
# for the current iteration and move to the next iteration