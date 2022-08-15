import random

name_list = ['Asigbey Ezekiel Kofi', 'Kpotor Seth Mawunya', 'Atali Edwin Edudzi', 'Atula Sylvia', 'Kpanazo Godwin',
             'Atsyatsya Samuel', 'Agroh Felix', 'Tsonyake Elikplim', 'Okyere Prosper', 'Akoto Ernest',
             'Obeng Clinton', 'Paa Kwesi Bartels', 'Akakpo Ernest K.M', 'Akotey Precious', 'Enoch Kwame',
             'Agbozo Theodore', 'Emmanuel Tokoli', 'Nabil Ablorh', 'Tettevia Sonidhi Sefakor', 'Nubor Kwame Eric',
             'Setugah Israel', 'Letsu Emmanuel Joe', 'Sitty Collins', 'Ekpe Fredrick', 'Edor Ignatius']
already_selected = ['Sitty Collins', 'Akotey Precious', 'Edor Ignatius', 'Ekpe Fredrick', 'Kpanazo Godwin']

person = random.choice(name_list)
if person in already_selected:
    name_list.remove(person)
    print('Hello! ' + person + ", you have already lead the class therefore you're not leading today.")
else:
    print('Hello! ' + person + ", you're leading the class today.")
    already_selected.append(person)

