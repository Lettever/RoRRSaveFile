import json
import re

class SaveFile:
    def __init__(self, steamId3):
        self.commands = eval(''.join(open('a.txt').readlines()))
        file_path = r'C:\Program Files (x86)\Steam\userdata\\' + str(steamId3) + r'\1337520\remote\save.json'
        info = {}
        with open(file_path) as f:
            js = json.loads(f.read())
            for k, v in js['stats'].items():
                if(x := re.findall('^survivor_([a-zA-Z]+)_([a-zA-Z_]+)$', k)):
                    print(k)
                    name, tag = x[0]
                    if name not in info:
                        info[name] = {}
                    info[name][tag] = int(v);
        valid_keys = [
            'wins_hard',
            'wins',
            'deaths',
            'games_played',
            'total_items',
            'total_kills',
            'total_stages',
        ]
        for i in info:
            for k in valid_keys:
                if k not in info[i]:
                    info[i][k] = 0
        self.info = info

    def print(self):
        valid_keys = [
            'wins_hard',
            'wins',
            'deaths',
            'games_played',
            'total_items',
            'total_kills',
            'total_stages',
        ]
        info = self.info
        for i in sorted(info):
            print(i.capitalize(), ': {', sep='')
            for key in valid_keys:
                x = info[i][key]
                key = ' '.join([word.capitalize() for word in key.split('_')])
                print('    ', key, ': ', x, sep='')
            print('}\n')

    def enforcer(self):
        print('enforcer function')
    def huntress(self):
        print('huntress function')
    def chef(self):
        print('chef function')
    def engineer(self):
        print('engineer function')
    def drifter(self):
        print('drifter function')
    def robomando(self):
        print('robomando function')
    def hand(self):
        print('hand function')
    def bandit(self):
        print('bandit function')
    def sniper(self):
        print('sniper function')
    def pilot(self):
        print('pilot function')
    def miner(self):
        print('miner function')
    def loader(self):
        print('loader function')
    def acrid(self):
        print('acrid function')
    def mercenary(self):
        print('mercenary function')
    def commando(self):
        print('commando function')
    def artificer(self):
        print('artificer function')


#huntress info
#huntress kills
#h k -> huntress kills
#co -> commando, 
def best_fit(command, list_of_commands):
    valid_keys = list_of_commands.keys()
    if command in valid_keys:
        return command, list_of_commands[command]
    c = ''
    for ch in command:
        c += ch
        valid_keys = [key for key in valid_keys if key.startswith(c)]
        if len(valid_keys) <= 1:
            break
    if len(valid_keys) != 1:
        return None, None
    res = valid_keys[0]
    if not res.startswith(command):
        return None, None
    return res, list_of_commands[res]

def test(string):
    s = string.split('_')
    res = {}
    cursor = res
    for i, x in enumerate(s):
        if i != len(s) - 1:
            cursor[x] = {}
            cursor = cursor[x]
        else:
            cursor[x] = string
    return res
    
def main():
    data = SaveFile(1047710596)
    data.print()
    print(test("abc_def_ghi"))
    while (line := input(">> ")):
        _, fn = best_fit(line, data.commands)
        if fn is None:
            print("What")
        else:
            fn()

if __name__ == '__main__':
    main()
    