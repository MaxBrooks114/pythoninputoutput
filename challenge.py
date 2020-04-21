


with open("challenge.txt", 'w') as challenge_file:
        for i in range(1,13):
            print("{:>2} times 2 is {}".format(i, i * 2),file=challenge_file)
