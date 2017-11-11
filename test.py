import re

url = 'https://www.c5game.com/dota/14926397-S.html'
m = re.search('(\d{2,15})',url).group(1)
print(m)
