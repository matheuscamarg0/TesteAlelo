import pandas as pd

print('Insira o código da informação desejada: ')
print("""
1. Total de atletas participantes.
2. Total de participantes homens.
3. Total de participantes mulheres.
4. Total de participantes por esporte. 
5. Total de medalhas por país. 
6. País com mais medalhas de ouro.
7. País com mais medalhas de prata.
8. País com mais medalhas de bronze.
9. País com menos medalhas de ouro.
10. País com menos medalhas de prata.
11. País com menos medalhas de bronze.
12. Lista com esportes participantes.
13. Lista de esportes com mais homens do que mulheres.
14. Lista de esportes com mais mulheres do que homens.
""")

option = input('Escolha a opção: ')


athlete = pd.read_excel('./-5033154410368452840final/Athletes.xlsx')
gender = pd.read_excel('./-5033154410368452840final/EntriesGender.xlsx')
medals = pd.read_excel('./-5033154410368452840final/Medals.xlsx')

index = athlete.index
males = gender.Male
females = gender.Female
discipline = gender.Discipline
allCountrys = medals.Team_NOC
gold = medals.Gold
silver = medals.Silver
bronze = medals.Bronze

totalDiscipline = len(discipline)
country = len(allCountrys)


def countAthletes():
    row_number = len(index)
    print("Está é a quantidade total de atletas: ", row_number)


def countGenders(sex):
    totalMales = 0
    totalFemales = 0

    for x in males:
        totalMales += x

    for y in females:
        totalFemales += y

    if sex == 'masc':
        print('Este é o total de homens participantes: ' + str(totalMales))
    else:
        print('Este é o total de mulheres participantes: ' + str(totalFemales))


def countParticipantsForSport():
    totalParticipants = 0

    for i in range(totalDiscipline):
        totalParticipants = females[i] + males[i]
        print(discipline[i] + " " + str(totalParticipants))


def countSportsParticipants():
    print('Esta é a lista de esportes participantes: ', discipline)


def countMFForSport(sex):
    listMaleSport = []
    listFemaleSport = []
    listEquals = []

    for i in range(totalDiscipline):
        if females[i] > males[i]:
            listFemaleSport.append(discipline[i])
        elif females[i] == males[i]:
            listEquals.append(discipline[i])
        else:
            listMaleSport.append(discipline[i])
    if sex == 'masc':
        print('Esta é a lista dos esportes com mais homens: ', listMaleSport)
    else:
        print('Esta é a lista dos esportes com mais mulheres: ', listFemaleSport)


def countTotalMedals():
    country = len(allCountrys)
    totalMedals = 0
    for c in range(country):
        totalMedals = gold[c] + silver[c] + bronze[c]
        print(allCountrys[c] + " " + str(totalMedals))


def countMaxMedalsForCountry(medal):
    listGoldMedalsMax = []
    listSilverMedalsMax = []
    listBronzeMedalsMax = []
    # -----------------------------
    countryGoldMedalsMax = ''
    countrySilverMedalsMax = ''
    countryBronzeMedalsMax = ''
    # -----------------------------------------
    for c in range(country):
        listGoldMedalsMax.append(gold[c])
        if gold[c] == max(listGoldMedalsMax):
            countryGoldMedalsMax = allCountrys[c]

        listSilverMedalsMax.append(silver[c])
        if silver[c] == max(listSilverMedalsMax):
            countrySilverMedalsMax = allCountrys[c]

        listBronzeMedalsMax.append(bronze[c])
        if bronze[c] == max(listBronzeMedalsMax):
            countryBronzeMedalsMax = allCountrys[c]
    # -----------------------------------------
    if medal == 'gold':
        print("Gold Medals Max: " + countryGoldMedalsMax)
    elif medal == 'silver':
        print("Silver Medals Max: " + countrySilverMedalsMax)
    else:
        print("Bronze Medals Max: " + countryBronzeMedalsMax)


def countMinMedalsForCountry(medal):
    listGoldMedalsMin = []
    listSilverMedalsMin = []
    listBronzeMedalsMin = []
    # -----------------------------
    countryGoldMedalsMin = ''
    countrySilverMedalsMin = ''
    countryBronzeMedalsMin = ''
    # -----------------------------
    for c in range(country):
        listGoldMedalsMin.append(gold[c])
        if gold[c] == min(listGoldMedalsMin):
            countryGoldMedalsMin = allCountrys[c]

        listSilverMedalsMin.append(silver[c])
        if gold[c] == min(listSilverMedalsMin):
            countrySilverMedalsMin = allCountrys[c]

        listBronzeMedalsMin.append(bronze[c])
        if gold[c] == min(listBronzeMedalsMin):
            countryBronzeMedalsMin = allCountrys[c]
    # -----------------------------------------
    if medal == 'gold':
        print("Gold Medals Min: " + countryGoldMedalsMin)
    elif medal == 'silver':
        print("Silver Medals Min: " + countrySilverMedalsMin)
    else:
        print("Bronze Medals Min: " + countryBronzeMedalsMin)


def invalid_option():
    print('Está opção é inválida, verifique o número da opção e tente novamente.')


def switch(param):
    if param == '1':
        countAthletes()
    elif param == '2':
        countGenders('masc')
    elif param == '3':
        countGenders('fem')
    elif param == '4':
        countParticipantsForSport()
    elif param == '5':
        countTotalMedals()
    elif param == '6':
        countMaxMedalsForCountry('gold')
    elif param == '7':
        countMaxMedalsForCountry('silver')
    elif param == '8':
        countMaxMedalsForCountry('bronze')
    elif param == '9':
        countMinMedalsForCountry('gold')
    elif param == '10':
        countMinMedalsForCountry('silver')
    elif param == '11':
        countMinMedalsForCountry('bronze')
    elif param == '12':
        countSportsParticipants()
    elif param == '13':
        countMFForSport('masc')
    elif param == '14':
        countMFForSport('fem')
    else:
        invalid_option()


switch(option)
