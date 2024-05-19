import json
import re

class SaveFile:
    def __init__(self, steamId3):
        ls = set()
        l = set()
        self.commands = {}
        with open('a.txt', 'r') as f:
            for x in f.readlines():
                if x.startswith('#'):
                    continue
                x = x.strip()
                self.commands[x] = eval(f'self.{x}')
        file_path = r'C:\Program Files (x86)\Steam\userdata\\' + str(steamId3) + r'\1337520\remote\save.json'
        info = {}
        with open(file_path) as f:
            js = json.loads(f.read())
            for k, v in js['stats'].items():
                if(x := re.findall('^survivor_([a-zA-Z]+)_([a-zA-Z_]+)$', k)):
                    name, tag = x[0]
                    ls.add(f'{name}')
                    ls.add(f'{name}_{tag}')
                    l.add(tag)
                    if name not in info:
                        info[name] = {}
                    info[name][tag] = int(v);
        for x in sorted(list(l)):
            print('#', x, sep='')
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

    """
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
    """
    def test(self, name):
        wins = self.info[name]['wins']
        deaths = self.info[name]['deaths']
        games_played = self.info[name]['games_played']
        total_items = self.info[name]['total_items']
        total_kills = self.info[name]['total_kills']
        total_stages = self.info[name]['total_stages']
        wins = self.info[name]['wins']
        wins_hard = self.info[name]['wins_hard']
        win_ratio = (wins - wins_hard) / games_played
        win_ratio = round(win_ratio * 100, 2)
        win_hard_ratio = wins_hard / games_played
        win_hard_ratio = round(win_hard_ratio * 100, 2)
        loss_ratio = deaths / games_played
        loss_ratio = round(loss_ratio * 100, 2)
        abandonment_ratio = (games_played - wins - deaths) / games_played
        abandonment_ratio = round(abandonment_ratio * 100, 2)
        total_picks = 0
        for x in self.info.values():
            total_picks += x['games_played']
        pick_ratio = games_played / total_picks
        pick_ratio = round(pick_ratio * 100, 2)
        print('wins', wins)
        print('deaths', deaths)
        print('games_played', games_played)
        print('total_items', total_items)
        print('total_kills', total_kills)
        print('total_stages', total_stages)
        print('wins', wins)
        print('wins_hard', wins_hard)
        print('win_ratio', win_ratio)
        print('win_hard_ratio', win_hard_ratio)
        print('loss_ratio', loss_ratio)
        print('abandonment_ratio', abandonment_ratio)
        print('pick_ratio', pick_ratio)
    def enforcer(self):
        wins = self.info['enforcer']['wins']
        deaths = self.info['enforcer']['deaths']
        games_played = self.info['enforcer']['games_played']
        total_items = self.info['enforcer']['total_items']
        total_kills = self.info['enforcer']['total_kills']
        total_stages = self.info['enforcer']['total_stages']
        wins = self.info['enforcer']['wins']
        wins_hard = self.info['enforcer']['wins_hard']
        win_ratio = (wins - wins_hard) / games_played
        win_ratio = round(win_ratio * 100, 2)
        win_hard_ratio = wins_hard / games_played
        win_hard_ratio = round(win_hard_ratio * 100, 2)
        loss_ratio = deaths / games_played
        loss_ratio = round(loss_ratio * 100, 2)
        abandonment_ratio = (games_played - wins - deaths) / games_played
        abandonment_ratio = round(abandonment_ratio * 100, 2)
        total_picks = 0
        for x in self.info.values():
            total_picks += x['games_played']
        pick_ratio = games_played / total_picks
        pick_ratio = round(pick_ratio * 100, 2)
        print('wins', wins)
        print('deaths', deaths)
        print('games_played', games_played)
        print('total_items', total_items)
        print('total_kills', total_kills)
        print('total_stages', total_stages)
        print('wins', wins)
        print('wins_hard', wins_hard)
        print('win_ratio', win_ratio)
        print('win_hard_ratio', win_hard_ratio)
        print('loss_ratio', loss_ratio)
        print('abandonment_ratio', abandonment_ratio)
        print('pick_ratio', pick_ratio)
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
#commando
#h k -> huntress kills
#co -> commando, 
def best_fit(command, list_of_commands):
    if command in list_of_commands:
        return command, list_of_commands[command]
    valid_keys = list_of_commands.keys()
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
    print(test("abc_def_ghi"))
    while (line := input(">> ")):
        name, fn = best_fit(line, data.commands)
        if line == '?':
            for x in data.commands:
                print('  ', x)
        elif fn is None:
            print("What")
        else:
            print(name)
            fn()

if __name__ == '__main__':
    main()
    