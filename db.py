import json
class Database:
    def insert(self,name,email,password):
        with open('users.json','r') as json_file:
            users = json.load(json_file)

            if email in users:
                return 0
            else:
                users[email]=[name,password]

        with open('users.json', 'w') as outfile:
            json.dump(users, outfile,indent=4)
            return 1

    def search(self,email,password):
        with open('users.json','r') as json_file:
            users = json.load(json_file)
            if email in users:
                if users[email][1]==password:
                    return 1
                else:
                    return 0
            else:
                return 0