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


#function pou emfanizei tis monades (organizational-units) entws tou panepistimiou me vasi ton monadiko kwdiko tou organismou
def get_organizational_units(orgcode):
    units = []
    endpoint = "organizational-units?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    for i in range(len(data['data'])):
        units.append(data['data'][i]['preferredLabel'])
    return units

#Function pou emfanizei poses Organic kai Temporary theseis ergasias yparxoun gia to etos 2023se ena panepistimio
def get_position_type_num(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    oragnic, temporary= 0, 0

    for i in range(len(data['data'])):
        if 'jobDescriptionVersionDate' in data['data'][i]:
            date = data['data'][i]['jobDescriptionVersionDate']
            if str(date)[:4] == '2023' and data['data'][i]['type'] == 'Organic':
                oragnic +=1
            elif str(date)[:4] == '2023' and data['data'][i]['type'] == 'Temporary':
                temporary += 1

    return "Organic: " + str(oragnic) + "\n" + "Temporary: " + str(temporary)

#Fuction pou epistrefei to plithos twn ergasiakwn sxesewn poy yparxoyn se ena panepistimio giato etos 2023
def get_employmentType_num(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    empType1, empType3,empType10 = 0, 0, 0
    for i in range(len(data['data'])):
        if 'jobDescriptionVersionDate' in data['data'][i] and 'employmentType' in data['data'][i]:
            date = data['data'][i]['jobDescriptionVersionDate']
            if str(date)[:4] == '2023':
                match data['data'][i]['employmentType']:
                    case 1:
                        empType1 += 1
                    case 3:
                        empType3 += 1
                    case 10:
                        empType10 += 1
    return "ΜOΝΙΜΟΙ ΥΠAΛΛΗΛΟΙ ΤΟΥ ΔΗΜΟΣIΟΥ /ΔΙΚΑΣΤΙΚΟI ΛΕΙΤΟΥΡΓΟI /ΔΗΜOΣΙΟΙ ΛΕΙΤΟΥΡΓΟI (employmentType 1): " + str(empType1) + "\n" + "ΙΔΙΩΤΙΚΟΥ ΔΙΚΑΙΟΥ ΑΟΡΙΣΤΟΥ ΧΡΟΝΟΥ(employmentType 3): " + str(empType3) + "\n" + "ΕΜΜΙΣΘΗ ΕΝΤΟΛΗ(employmentType 10): " + str(empType10)

#function pou emfanizei tis theseis tou panepistimioy to 2023 me vasi thn kathgoria ekpaideusis
def get_educationType_num(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    eduType1, eduType2, eduType3, eduType4, eduType5, eduType6, eduType7 = 0, 0, 0, 0, 0, 0, 0
    for i in range(len(data['data'])):
        if 'jobDescriptionVersionDate' in data['data'][i] and 'employmentType' in data['data'][i]:
            date = data['data'][i]['jobDescriptionVersionDate']
            if str(date)[:4] == '2023':
                match data['data'][i]['educationType']:
                    case 1:
                        eduType1 += 1
                    case 2:
                        eduType2 += 1
                    case 3:
                        eduType3 += 1
                    case 4:
                        eduType4 += 1
                    case 5:
                        eduType5 += 1
                    case 6:
                        eduType6 += 1
                    case 7:
                        eduType7 += 1
    return "ΑΝΕΥ ΚΑΤΗΓΟΡΙΑΣ ΕΚΠ/ΣΗΣ: " + str(eduType1) + "\n" + "ΠΕ: " + str(eduType2) + "\n" + "ΤΕ: " + str(eduType3) + "\n" + "ΔΕ: " + str(eduType4) + "\n" + "ΥΕ: " + str(eduType5) + "\n" + "ΕΙΔΙΚΩΝ ΘΕΣΕΩΝ: " + str(eduType6) + "\n" + "ΕΕΠ: " + str(eduType7)



def get_professionCategory_num(orgcode):
    endpoint = "positions?organizationCode=" + str(orgcode)
    data = main_request(baseurl, endpoint)
    departments_count = {}

    for i in range(len(data['data'])):
        if 'professionCategory' in data['data'][i] and 'jobDescriptionVersionDate' in data['data'][i]:
            date = data['data'][i]['jobDescriptionVersionDate']
            if str(date)[:4] == '2023':
                version = str(data['data'][i]['professionCategory'])
                if version not in departments_count:
                    departments_count[version] = 1
                else:
                    departments_count[version] += 1

    return str(departments_count)

#1. Να εντοπίσετε τον κωδικό φορέα των Ιδρυμάτων που θα εστιάσετε.
print("Κωδικός ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ: " + find_org_code('ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ'))
print("Κωδικός ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ: " + find_org_code('ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ'))
print("Κωδικός ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: " + find_org_code('ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ'))

print('--------------------------------------------------------------------------------------')

#3. Για ένα μόνο ΑΕΙ, να μελετήσετε και να καταγράψετε τις θέσεις του για το έτος 2023 σύμφωνα με συγκεκριμένα κριτήρια (τύπος θέσης, εργασιακή σχέση, κατηγορία εκπαίδευσης, κλάδος, κτλ.)
print("Θέσεις του Πανεπιστημίου Πατρών για το έτος 2023 σύμφωνα με συγκεκριμένα κριτήρια (τύπος θέσης, εργασιακή σχέση, κατηγορία εκπαίδευσης, κλάδος) \n")
print("Τύποι θέσης: \n" + get_position_type_num(find_org_code("ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ")) + "\n")
print("Eργασιακή σχέση: \n" + get_employmentType_num(find_org_code("ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ")) + "\n")
print("Κατηγορία εκπαίδευσης: \n" + get_educationType_num(find_org_code("ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ")) + "\n")
print("Κλάδοι: \n" + get_professionCategory_num(find_org_code("ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ")) + "\n")


print('--------------------------------------------------------------------------------------')

#4. Ελεύθερο ερώτημα emfanisi monadwn entos twn panepistimiwn
print("Ελεύθερο ερώτημα εμφάνιση μονάδων εντός των πανεπιστημίων \n")
print("UNITS ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ: " + str(get_organizational_units(find_org_code('ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ'))))
print("UNITS ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ: " + str(get_organizational_units(find_org_code('ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ'))))
print("UNITS ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: " + str(get_organizational_units(find_org_code('ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ'))))
