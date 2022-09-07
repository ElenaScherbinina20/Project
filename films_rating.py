import requests
import re

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
nums = []

for i in list_e:
    url = base_url + i
    result = requests.get(url)
    check = result.json()
    check_title = check.get("Title")
    check_reting = check.get("Ratings")

    if check_reting is None:
        continue

    internet_Movie_Database = check_reting[0]["Value"]
    internet_Movie_Database_value = re.search(r"\d{1,2}\S\d{1,2}", internet_Movie_Database).group(0)
    rotten_Tomatoes = check_reting[1]["Value"]
    rotten_Tomatoes_value = re.search(r"\d{2,3}", rotten_Tomatoes).group(0)

    metacritic = check_reting[2]["Value"]
    metacritic_value = re.search(r"\d{2,3}", metacritic).group(0)
    metascore_value = check.get("Metascore")
    imdbRating_value = check.get("imdbRating")

    s = float((((int(metacritic_value) + int(rotten_Tomatoes_value)) / 10)) + float(internet_Movie_Database_value))/3
    m = s, check_title

    nums.append(m)
    nums = sorted(nums, key=lambda x: x[0])

less_5 = []
less_6 = []
less_7 = []
less_8 = []

for n in nums:
    for c in n:
        a = isinstance(c, float)

        if a == True:
            # print(c)
            if c < 6:
                less_5.append(n)
            if c > 6 and c < 7:
                less_6.append(n)
            if c > 7 and c < 8:
                less_7.append(n)
            if c > 8:
                less_8.append(n)

print("Рейтинг меньше 6ти: ", ' '.join(map(str, less_5)))
print("Рейтинг от шести до семи: ", ' '.join(map(str, less_6)))
print("Рейтинг от семи до восьми: ", ' '.join(map(str, less_7)))
print("Рейтинг больше 8ти: ", ' '.join(map(str, less_8)))
