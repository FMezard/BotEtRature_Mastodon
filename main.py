import mastodon
from mastodon import Mastodon
import csv
from datetime import date
from random import randint
FIRST_DAY = date(2022, 0o4, 0o1)


def mastodon_authentification():
    m = Mastodon(access_token="qydcVh2v555UFJspF2IQmPngqwVzVasCPW5v-jd7t7k ", api_base_url="https://botsin.space")
    return m


def pick_a_website():
    with open('littenum.csv', "r", newline='\n', encoding="UTF-8") as csvfile:
        dictreader = csv.DictReader(csvfile, delimiter='\t', quotechar='"')
        data_litte = list(dictreader)
    try:
        print((date.today() - FIRST_DAY).days)
        workpiece = data_litte[(date.today() - FIRST_DAY).days]
    except IndexError:
        print("Tout a déjà été twitté")
    return workpiece

def create_toot_content(workpiece):
    tweet_content_list = [f"""{workpiece['URL']} est l'oeuvre de littérature web du jour ! Vous aussi partagez vos coups de coeur du web et participez à cultiver ce bot : https://framaforms.org/partage-de-litterature-web-1670335823""",
    f"""Connaissiez-vous {workpiece['URL']} ? Maintenant oui ! Si elle vous fait penser à un compte twitter, un site, une fanfic ... faites le savoir à ce bot : https://framaforms.org/partage-de-litterature-web-1670335823""",
    f"""Allez jeter un coup d'oeil à {workpiece['URL']}, alors qu'en pensez-vous ? Partagez vos coups de coeurs littéraire avec ce bot sur https://framaforms.org/partage-de-litterature-web-1670335823""",
    f"""Cliquez ici pour une petite pause littéraire : {workpiece['URL']}. Nous avons besoin de vous pour partager toujours plus de littérature sur ce réseau : https://framaforms.org/partage-de-litterature-web-1670335823""",
    f"""Vous reprendez-bien un petit peu de littérature en ligne ? {workpiece['URL']} ? Et vous, que lisez-vous en ligne ? Faites le moi savoir : https://framaforms.org/partage-de-litterature-web-1670335823"""]

    tweet_content = tweet_content_list[randint(0, 4)]
    return tweet_content

def create_toot_response(workpiece):
    if workpiece["commentaire"]:
        return f'{workpiece["commentaire"]}'
    else:
        return None

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    m = mastodon_authentification()
    website = pick_a_website()
    toot_website = create_toot_content(website)
    id_toot_website = m.toot(toot_website)
    toot_comment = create_toot_response(website)
    if toot_comment :
        m.status_post(status=toot_comment, in_reply_to_id=id_toot_website)
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
