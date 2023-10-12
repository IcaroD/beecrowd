meses = {(1, "January"), (2, "February"), (3, "March"), (4, "April"), (5, "May"), (6, "June"), (7, "July"), (8, "August"), (9, "September"), (10, "October"), (11, "November"), (12, "December")}

num = int(input())

for item in meses:
    if num == item[0]:
        print(item[1])