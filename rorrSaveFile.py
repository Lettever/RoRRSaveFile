import json
import re

class SaveFile:
    a = {'artificer': 'arti', 'hande': 'hand'}
    def __init__(self, steamId3):
        self.commands = {
            'acrid': self.survivor,
            'artificer': self.survivor,
            'bandit': self.survivor,
            'chef': self.survivor,
            'commando': self.survivor,
            'drifter': self.survivor,
            'enforcer': self.survivor,
            'engineer': self.survivor,
            'hande': self.survivor,
            'huntress': self.survivor,
            'loader': self.survivor,
            'mercenary': self.survivor,
            'miner': self.survivor,
            'pilot': self.survivor,
            'robomando': self.survivor,
            'sniper': self.survivor,
        }
        file_path = r'C:\Program Files (x86)\Steam\userdata\\' + str(steamId3) + r'\1337520\remote\save.json'
        info = {}
        with open(file_path) as f:
            js = json.loads(f.read())
            for k, v in js['stats'].items():
                if(x := re.findall('^survivor_([a-zA-Z]+)_([a-zA-Z_]+)$', k)):
                    name, tag = x[0]
                    if name not in info:
                        info[name] = {}
                    info[name][tag] = int(v);
        survivors = [
            'acrid', 'arti', 'bandit',
            'chef', 'commando', 'drifter',
            'enforcer', 'engineer', 'hand',
            'huntress', 'loader', 'mercenary',
            'miner', 'pilot', 'robomando',
            'sniper',
        ]
        valid_keys = [
            'wins_hard', 'wins', 'deaths',
            'games_played', 'total_items', 'total_kills',
            'total_stages',
        ]
        for x in survivors:
            if x not in info:
                info[x] = {}
            for k in valid_keys:
                if k not in info[x]:
                    info[x][k] = 0
        self.info = info

    def survivor(self, name):
        if name in self.a:
            name = self.a[name]
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
        print('   Wins: ', wins, sep='')
        print('   Deaths: ', deaths, sep='')
        print('   Games Played: ', games_played, sep='')
        print('   Total Items: ', total_items, sep='')
        print('   Total Kills: ', total_kills, sep='')
        print('   Total Stages: ', total_stages, sep='')
        print('   Wins: ', wins, sep='')
        print('   Monsoon Wins: ', wins_hard, sep='')
        print('   Win Ratio: ', win_ratio, '%', sep='')
        print('   Monsoon Win Ratio: ', win_hard_ratio, '%', sep='')
        print('   Loss Ratio: ', loss_ratio, '%', sep='')
        print('   Abandonment Ratio: ', abandonment_ratio, '%', sep='')
        print('   Pick Ratio: ', pick_ratio, '%', sep='')
        
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
        name, fn = best_fit(line.lower(), data.commands)
        if line == '?':
            for x in data.commands:
                print('  ', x)
        elif fn is None:
            print("What")
        else:
            fn(name)
        print()

if __name__ == '__main__':
    main()