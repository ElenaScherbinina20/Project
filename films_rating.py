import requests

list_e = ["Titanic",
          "The Man in the Iron Mask",
          "Celebrity",
          "Beach",
          "Cafe Dons Plum",
          "Gangs of New York",
          "Catch Me If You Can",
          "Renegades",
          "blood diamond",
          "Body of lies"]

base_url = "http://www.omdbapi.com/?apikey=709c8af9&t="
less_5 = []
less_6 = []
less_7 = []
less_8 = []

for i in list_e:
    url = base_url + i
    result = requests.get(url)
    check = result.json()
    check_reting = check.get("Ratings")

    if check_reting is None:
        continue

    internet_Movie_Database = float(check_reting[0]["Value"][0:-3])
    rotten_Tomatoes = int(check_reting[1]["Value"][0:-1])
    metacritic = int(check_reting[2]["Value"][0:-4])
    s = (((metacritic + rotten_Tomatoes) / 10) + internet_Movie_Database)/3
    # m = {i: s}
    m = {i: round(s, 2)}

    if s < 6:
        less_5.append(m)
    elif 6 < s < 7:
        less_6.append(m)
    elif 7 < s < 8:
        less_7.append(m)
    else:
        less_8.append(m)

print(f"Рейтинг меньше шести: {less_5}\n"
      f"От шести до семи:: {less_6}\n"
      f"От семи до восьми: {less_7}\n"
      f"Больше восьми: {less_8}\n")
