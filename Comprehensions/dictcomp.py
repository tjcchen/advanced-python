#
# dictionary comprehensions
#

def main():
    # define a list of temperature values
    ctemps = [0, 12, 34, 100]

    # use a comprehension to build a dictionary
    tempDict = {t: (t*9/5) + 32 for t in ctemps}
    print(tempDict)  # {0: 32.0, 12: 53.6, 34: 93.2, 100: 212.0}
    tempDict2 = {t: (t*9/5) + 32 for t in ctemps if t < 100}
    print(tempDict2)  # {0: 32.0, 12: 53.6, 34: 93.2}
    print(tempDict2[12])  # 53.6

    # merge two dictionaries with a comprehension
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}

    # try not to use more than 2 comprehensions in a single expression
    newTeam = {k: v for team in (team1, team2) for k, v in team.items()}
    # ({'Jones': 24, 'Jameson': 18, 'Smith': 58, 'Burns': 7}, {'White': 12, 'Macke': 88, 'Perce': 4})
    print((team1, team2))
    # {'Jones': 24, 'Jameson': 18, 'Smith': 58, 'Burns': 7, 'White': 12, 'Macke': 88, 'Perce': 4}
    print(newTeam)


if __name__ == "__main__":
    main()
