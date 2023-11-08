import requests

baseurl = "https://hr.apografi.gov.gr/api/public/"

def main_request(baseurl, endpoint):
    r = requests.get(baseurl + endpoint)
    return r.json()


#function anazhthshs kwdikou forea
def find_org_code(uniName):
    #orismos api endpoint
    endpoint = 'organizations'
    #retrive data in json form
    data = main_request(baseurl, endpoint)
    code = ""
    #check if org exists
    for i in range(len(data['data'])):
        if data['data'][i]['preferredLabel'] == uniName:
           code = data['data'][i]['code']
    return code


def get_org_position_num(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    return len(data['data'])


#function pou emfanizei tis monades (organizational-units) entws tou panepistimiou me vasi ton monadiko kwdiko tou organismou
def get_organizational_units(orgcode):
    units = []
    endpoint = "organizational-units?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    for i in range(len(data['data'])):
        units.append(data['data'][i]['preferredLabel'])
    return units


def diakimansi_taktikou_prosopikou(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    posnum2019, posnum2020, posnum2021, posnum2022, posnum2023 = 0 ,0, 0, 0, 0

    for i in range(len(data['data'])):
        if 'jobDescriptionVersionDate' in data['data'][i]:
            date = data['data'][i]['jobDescriptionVersionDate']
            if str(date)[:4] == '2019' and data['data'][i]['type'] == 'Organic':
                posnum2019 = posnum2019+1
            elif str(date)[:4] == '2020' and data['data'][i]['type'] == 'Organic':
                posnum2020 = posnum2020 + 1
            elif str(date)[:4] == '2021' and data['data'][i]['type'] == 'Organic':
                posnum2021 = posnum2021 + 1
            elif str(date)[:4] == '2022' and data['data'][i]['type'] == 'Organic':
                posnum2022 = posnum2022 + 1
            elif str(date)[:4] == '2023' and data['data'][i]['type'] == 'Organic':
                posnum2023 = posnum2023 + 1

    return '2019: ' + str(posnum2019) + '\n' + '2020: ' + str(posnum2019 + posnum2020) + '\n' + '2021: ' + str(posnum2019 + posnum2020+ posnum2021) + '\n' + '2022: ' + str(posnum2019 + posnum2020+ posnum2021 + posnum2022) + '\n' + '2023: ' + str(posnum2019 + posnum2020+ posnum2021 + posnum2022 + posnum2023)


def diakimansi_proslipsewn_prosopikou(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    posnum2019, posnum2020, posnum2021, posnum2022, posnum2023 = 0 ,0, 0, 0, 0

    for i in range(len(data['data'])):
        if 'jobDescriptionVersionDate' in data['data'][i]:
            date = data['data'][i]['jobDescriptionVersionDate']
            if str(date)[:4] == '2019':
                posnum2019 = posnum2019+1
            elif str(date)[:4] == '2020':
                posnum2020 = posnum2020 + 1
            elif str(date)[:4] == '2021':
                posnum2021 = posnum2021 + 1
            elif str(date)[:4] == '2022':
                posnum2022 = posnum2022 + 1
            elif str(date)[:4] == '2023':
                posnum2023 = posnum2023 + 1

    return '2019: ' + str(posnum2019) + '\n' + '2020: ' + str(posnum2020) + '\n' + '2021: ' + str(posnum2021) + '\n' + '2022: ' + str(posnum2022) + '\n' + '2023: ' + str(posnum2023)



#1. Evresh kai ektypwsh kwdikou forea
print("Κωδικός ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ: " + find_org_code('ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ'))
print("Κωδικός ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ: " + find_org_code('ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ'))
print("Κωδικός ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: " + find_org_code('ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ'))

print('--------------------------------------------------------------------------------------')

#2. Diakimansi taktikou prosopikou
print('Διακύμανση τακτικού προσωπικού ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ: \n' + diakimansi_taktikou_prosopikou(find_org_code('ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ')))
print('Διακύμανση τακτικού προσωπικού ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ: \n' + diakimansi_taktikou_prosopikou(find_org_code('ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ')))
print('Διακύμανση τακτικού προσωπικού ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: \n' + diakimansi_taktikou_prosopikou(find_org_code('ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ')))

print('--------------------------------------------------------------------------------------')

#3. Diakimansi etisiwn proslipsewn
print('Διακύμανση ετήσιων προσλήψεων ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ: \n' + diakimansi_proslipsewn_prosopikou(find_org_code('ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ')))
print('Διακύμανση ετήσιων προσλήψεων ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ: \n' + diakimansi_proslipsewn_prosopikou(find_org_code('ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ')))
print('Διακύμανση ετήσιων προσλήψεων ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: \n' + diakimansi_proslipsewn_prosopikou(find_org_code('ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ')))




print('--------------------------------------------------------------------------------------')



#Emfanisi synolikou arithmou thesewn toy kathe panepistimiou
# print("Συνολικός αριθμός θέσεων ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ: " + str(get_org_position_num(find_org_code('ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ'))))
# print("Συνολικός αριθμός θέσεων ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ: " + str(get_org_position_num(find_org_code('ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ'))))
# print("Συνολικός αριθμός θέσεων ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: " + str(get_org_position_num(find_org_code('ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ'))))
#



#5. Ελεύθερο ερώτημα emfanisi monadwn entos twn panepistimiwn
print("UNITS ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ: " + str(get_organizational_units(find_org_code('ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ'))))
print("UNITS ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ: " + str(get_organizational_units(find_org_code('ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ'))))
print("UNITS ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: " + str(get_organizational_units(find_org_code('ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ'))))
