import re

terremotos = {

    1: {
        "mag":5.9,
        "place": "254 km NW of Tianpeng, China",
        "time": 1654795717481,
        "alert": "yellow"
        },
    2: {
        "mag":5.6,
        "place":"248 km NW of Tianpeng, China",
        "time":1654790606429,
        "alert":"yellow"
    },
    3: {
        "mag": 6.5,
        "place": "111 km SSW of Tarauaca, Brazil",
        "time": 1654649747303,
        "alert": "green"
    },
    4: {
        "mag": 6.3,
        "place": "Rat Islands, Aleutian Islands, Alaska",
        "time": 1654385892708,
        "alert": "green"
    },
    5: {
        "mag": 6.4,
        "place": "west of Macquarie Island",
        "time": 1654348668209,
        "alert": "green"
    },
    6: {
        "mag": 6.3,
        "place": "128 km NW of Neiafu, Tonga",
        "time": 1654348045914,
        "alert": "green"
    },
    7:{
        "mag":4.14,
        "place":"7km NW of Bay Point, CA",
        "time":1654171642230,
        "alert":"green"
    },
    8:{
        "mag":5.9,
        "place":"45 km W of Linqiong, China",
        "time":1654074008122,
        "alert":"yellow",
    },
    9:{
        "mag":6.2,
        "place":"38 km NE of Lospalos, Timor Leste",
        "time":1653618965637,
        "alert":"green"
    },
    10:{
        "mag":6.4,
        "place":"southeast of the Loyalty Islands",
        "time":1653579477710,
        "alert":"green"
    },
    11:{
        "mag":7.2,
        "place":"Southern Peru",
        "time":1653566540271,
        "alert":"green"
    },
    12:{
        "mag":4.67,
        "place":"3 km NW of Holualoa, Hawaii",
        "time":1653212985350,
        "alert":"green"
    },
    13:{
        "mag":6.3,
        "place":"south of the Fiji Islands",
        "time":1653203187797,
        "alert":"green"
    },
    14:{
        "mag":6.1,
        "place":"1 km ENE of Bungahan, Philippines",
        "time":1653169848143,
        "alert":"green"
    },
    15:{
        "mag":6.9,
        "place":"Macquarie Island region",
        "time":1652955211721,
        "alert":"green"
    },
    16:{
        "mag":5.5,
        "place":"11 km W of San Bartolo, Peru",
        "time":1652392548525,
        "alert":"yellow"
    },
    17:{
        "mag":6.8,
        "place":"85 km NNW of San Antonio de los Cobres, Argentina",
        "time":1652223992600,
        "alert":"green"
    },
    18:{
        "mag":6.3,
        "place":"177 km SW of Lorengau, Papua New Guinea",
        "time":1652135586817,
        "alert":"green"
    },
    19:{
        "mag":6.3,
        "place":"70 km SW of Yonakuni, Japan",
        "time":1652077383133,
        "alert": "green"
    },
    20:{
        "mag":3.25,
        "place":"5 km ESE of Elgin, South Carolina",
        "time":1652074367550,
        "alert":"None"
    }
}

import re

country = input("Pais: ")

for x in range(1, 20):
    place_container = terremotos[x]["place"]

if re.search(country, place_container):
    print(f"Los temblores reportados en {country} fueron: ")


