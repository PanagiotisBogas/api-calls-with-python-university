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




#1. Evresh kai ektypwsh kwdikou forea
print("Κωδικός ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ: " + find_org_code('ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ'))
print("Κωδικός ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ: " + find_org_code('ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ'))
print("Κωδικός ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: " + find_org_code('ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ'))


print('--------------------------------------------------------------------------------------')

#Emfanisi synolikou arithmou thesewn toy kathe panepistimiou
print("Συνολικός αριθμός θέσεων ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ: " + str(get_org_position_num(find_org_code('ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΘΕΣ/ΝΙΚΗΣ'))))
print("Συνολικός αριθμός θέσεων ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ: " + str(get_org_position_num(find_org_code('ΕΘΝΙΚΟ ΚΑΙ ΚΑΠΟΔΙΣΤΡΙΑΚΟ ΠΑΝΕΠΙΣΤΗΜΙΟ ΑΘΗΝΩΝ'))))
print("Συνολικός αριθμός θέσεων ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ: " + str(get_org_position_num(find_org_code('ΠΑΝΕΠΙΣΤΗΜΙΟ ΠΑΤΡΩΝ'))))




