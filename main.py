from pyscript import display, document

nicknames = {
    "philippines": "The Pearl of the Orient Seas",
    "vietnam": "The Land of the Ascending Dragon",
    "thailand": "The Land of Smiles",
    "indonesia": "The Emerald of the Equator",
    "malaysia": "The Land of Diverse Cultures",
    "singapore": "The Lion City",
    "brunei": "The Abode of Peace",
    "cambodia": "The Kingdom of Wonder",
    "laos": "The Land of a Million Elephants",
    "myanmar": "The Golden Land",
    "timor-leste": "The Sunrise Country"
}

def country_nickname(e):
    country = document.getElementById("country").value.lower().strip()
    document.getElementById("result").innerHTML = ""

    if country in nicknames:
        display(nicknames[country], target="result")
    else:
        display("Country not found.", target="result")