from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://politicaltrader.libsyn.com/rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30002),
            'path': "https://bcovlive-a.akamaihd.net/r8ceb94e3229b4c0bb2dd461dacb3ab07/us-east-1/us-east-1/6057994532001/profile_2/c5s2x2oq_7ff6bd10c4804cf19626a72c71dd9994_media_162885.ts",
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/b/4/d/9/b4d95ef6e81d4e2a/TT1289_POD02.png",
            'is_playable': True},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/b/6/1/d/b61d9db20f4dea7c/TT1297_Political_Trade_logo.png"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/b/6/1/d/b61d9db20f4dea7c/TT1297_Political_Trade_logo.png"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
