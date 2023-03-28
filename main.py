import time
import random
global frage_ob_forfahren, auge_defender, auge_attacker


# Attack or Defend?
def spiel_als(character):
    global frage_ob_forfahren, auge_defender, auge_attacker
    if character == "defender" or character == "attacker":
        wahrscheinlichkeit(character)
        frage_ob_forfahren = input("Sicher das Sie fortfahren wollen (ja/nein)?\n>").lower()
        fuehre_entscheidung_durch(frage_ob_forfahren, character)


# Continue?
def fuehre_entscheidung_durch(fortfahren, character):
    global auge_defender, auge_attacker
    if fortfahren == "ja":
        auge_defender = random.randint(1, 6)
        auge_attacker = random.randint(1, 6)
        print("Der Würfel rollt...")
        time.sleep(1)
        print("...und rollt...")
        time.sleep(1)
        print("...rollt immernoch...")
        time.sleep(1)
        verloren_oder_gewonnen_text(character)
    elif fortfahren == "nein":
        char_wechsel()
    else:
        print("Ungültige Angabe!")


# Probability to win calc
def wahrscheinlichkeit(character):
    points_defender = 0
    points_attacker = 0
    for first_die in range(1, 7):
        for second_die in range(1, 7):
            if first_die >= second_die:
                points_defender += 1
            else:
                points_attacker += 1
    absoluter_wert = points_defender + points_attacker
    if character == "attacker":
        points_player = points_attacker
    else:
        points_player = points_defender
    wahrscheinlichkeit_1st_p_wins = points_player / absoluter_wert * 100
    print(f"Die Wahrscheinlichkeit das du gewinnst beträgt! {round(wahrscheinlichkeit_1st_p_wins, 2)}%")


# Change character?
def char_wechsel():
    while True:
        frage_character_wechsel = input("Wollen sie Character wechseln? (ja/nein)\n>").lower()
        if frage_character_wechsel == "ja":
            break
        elif frage_character_wechsel == "nein":
            quit()
        else:
            print("Ungültige Angabe!")


# Throw dice again?
def ob_nochmal_werfen():
    while True:
        frage_nochmal_werfen = input("Möchten Sie nochmal werfen?\n>").lower()
        if frage_nochmal_werfen == "ja":
            break
        elif frage_nochmal_werfen == "nein":
            quit()
        else:
            print("Ungültige Angabe!")


# Who won?
def verloren_oder_gewonnen_text(character):
    if character == "defender":
        if auge_defender >= auge_attacker:
            print(f"""
        Sie haben gewonnen!
        Ihre Verteidigung war eine JACKED {auge_defender}!!!.. der Angriff war eine schwache {auge_attacker}
        """)
            time.sleep(2)
            ob_nochmal_werfen()
        else:
            print(f"""
        Tja- Verloren! 
        Sie haben eine {auge_defender} gewürfelt.. der Angriff war eine {auge_attacker}
        """)
            time.sleep(2)
            ob_nochmal_werfen()
    else:
        if auge_attacker > auge_defender:
            print(f"""
        Sie haben gewonnen!
        Ihr Angriff war eine {auge_attacker}!!!! *VINE BOOM SOUND*- nichts gegen eine Verteidigung einer {auge_defender}
        """)
            time.sleep(2)
            ob_nochmal_werfen()
        else:
            print(f"""
        Tja- Verloren!
        Deren Verteidigung war eine ganze {auge_defender}.. dein Angriff eine {auge_attacker} 
        """)
            time.sleep(2)
            ob_nochmal_werfen()


# Start game?
def start_or_no():
    start_or_not = input("Start (j/n)?\n>").lower()
    if start_or_not == "j":
        while True:
            character = input("Chose your character (Defender/Attacker)\n>").lower()
            if character == "defender" or character == "attacker":
                spiel_als(character)
            else:
                print("Kein zulässiger Charakter")
    elif start_or_not == "n":
        quit()
    else:
        print("Ich versteh das nicht...")


# Create main
def risiko():
    start_or_no()


if __name__ == "__main__":
    print("Risiko Spiel!")
    risiko()

