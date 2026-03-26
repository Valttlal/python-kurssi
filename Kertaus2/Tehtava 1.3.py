sanat = ["puu", "koivu", "mänty", "tietokone", "hiiri", "hiirimatto"]

laskuri = 0

for sana in sanat:
    if len(sana) > 5:
        laskuri += 1

print("Yli 5 kirjainta sisältäviä sanoja:", laskuri)