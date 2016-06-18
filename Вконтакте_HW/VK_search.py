# -*- coding: utf-8 -*-
import requests, codecs, os

users_search = 'https://api.vk.com/method/users.search'
parameters = {
    'access_token':'14ff99154e15b92963e63900e2e874af6365ac0788f7ca03b79097a009b263ca6433b0b4793f4da2bae01',
    'count':100,
    'city': 283, 
    'country': 1,
    'fields':'bdate, sex, occupation'
}

OUTPUT_DIR = 'C:\\Users\\Pasha\\Desktop\\VK_posts\\' #прописать папку, куда складывать посты

def get_users(users_search, parameters):
    '''
    Достаём персональную информацию (дату рождения, пол, род занятий) 
    100 пользователей из города Надым
    '''
    users = requests.get(users_search, params=parameters)
    data = users.json()
    return data

def save_users_info(users_data):
    '''
    Записаваем метаданные пользователей в .csv файл
    '''
    fOut = codecs.open('metadata.csv', 'w', 'utf-8')
    fOut.write('first_name; last_name; sex; bdate; uid; occupation\n')
    keys = ['first_name', 'last_name', 'sex', 'bdate', 'uid', 'occupation']
    for i in info['response'][1:100]:
        mass = ''
        for key in keys:
            if key in i.keys():
                if key != 'occupation':
                    mass += str(i[key]) + ';'
                else:
                    mass += str(i[key]['name']) + '\n'
            else:
                if key == 'occupation':
                    mass += 'NONE\n'
                else:
                    mass += 'NONE; '
        fOut.write(mass)
    fOut.close()

def save_wall_info(users_data, OUTPUT_DIR):
    '''
    Создаём документ .txt и записываем в него посты со стены пользователя
    '''
    for i in range(1, len(users_data['response'])):
        personID = users_data['response'][i]['uid']
        path = 'https://api.vk.com/method/wall.get'
        wall_parameters = {
            'owner_id': personID,
            'count':10,
            'filter':'owner'
        }
        save_posts = requests.get(path, params=wall_parameters)
        posts = save_posts.json()
        fOut = codecs.open(OUTPUT_DIR + str(personID) + '.txt', 'w', 'utf-8')
        try:
            for post in posts['response'][1:]:
                cleared = post['text'].replace('<br>', '\n')
                if cleared != '':
                    fOut.write('НОВЫЙ ПОСТ:\n')
                    fOut.write(cleared + '\n')
                    fOut.write('\n')
                else:
                    os.remove(OUTPUT_DIR + personID + '.txt')
        except:
            continue

info = get_users(users_search, parameters)
save_users_info(info)
save_wall_info(info, OUTPUT_DIR)
