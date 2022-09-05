import requests
import re
base_url = "http://www.omdbapi.com/?t="
list_e = ["Titanic", "The+Man+in+the+Iron+Mask", "Celebrity", "Beach", "Cafe+Dons+Plum", "Gangs+of+New+York", "Catch+Me+If+You+Can",  "Renegades", "blood+diamond", "Body of lies"]
key = "&apikey=709c8af9"
nums = []
for i in list_e:
    url = base_url + i + key
    result = requests.get(url)
    check = result.json()
    check_title = check.get("Title")
    check_reting = check.get("Ratings")
    if check_reting == None or check_title == None:
        continue
    internet_Movie_Database = check_reting[0]["Value"]
    internet_Movie_Database_value = re.search(r"\d{1,2}\S\d{1,2}", internet_Movie_Database).group(0)
    rotten_Tomatoes = check_reting[1]["Value"]
    rotten_Tomatoes_value = re.search(r"\d{2,3}", rotten_Tomatoes).group(0)
    metacritic = check_reting[2]["Value"]
    metacritic_value = re.search(r"\d{2,3}", metacritic).group(0)
    metascore_value = check.get("Metascore")
    imdbRating_value = check.get("imdbRating")
    s = ((int(metacritic_value) + int(rotten_Tomatoes_value) )/10)
    b = float(internet_Movie_Database_value) + s
    v = float(b / 3)
    m = v, check_title
    nums.append(m)
    nums = sorted(nums, key=lambda x: x[0])

for n in nums:
    for c in n:
        age = isinstance(c, float)
        if age == True:
            # print(c)
            if c < 6:
                less_5 = c
                print("Рейтинг меньше 6ти: ", ' '.join(map(str, n)))
            if c > 6 and c < 7:
                less_6 = c
                print("Рейтинг от шести до семи: ", ' '.join(map(str, n)))
            if c > 7 and c < 8:
                less_7 = c
                print("Рейтинг от семи до восьми: ", ' '.join(map(str, n)))
            if c > 8:
                less_8 = c
                print("Рейтинг больше 8ти: ", ' '.join(map(str, n)))
