import json
def dic():
    print('Welcome to the dictionary!')
    print('If you want to quit, type EXIT')
    data = json.load(open("data.json"))
    flag = True
    while(flag):
        s = input('What do you want to search: ')
        if s=='EXIT':
            flag = False
        else:
            search = s.lower()
            if search in data:
                print(data[search])
            else:
                print('Sorry, word not found in dictionary')
                print('Check for spelling errors and try again.')
        
dic()
        
