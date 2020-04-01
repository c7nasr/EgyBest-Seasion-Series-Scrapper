
link = "https://teco.egybest.site/season/star-trek-picard-season-1/?ref=home-tv"

name = link.split("season/")

name = name[1].replace("/","")
name = name.split("?")



print(name[0])