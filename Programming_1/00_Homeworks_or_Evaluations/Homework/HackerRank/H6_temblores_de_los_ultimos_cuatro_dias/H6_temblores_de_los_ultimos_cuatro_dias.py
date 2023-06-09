temblores = {
   1 : ["2023-05-31 09:01:45.537000","off the east coast of the Kamchatka Peninsula, Russia"],
   2 : ["2023-05-31 06:20:13.509000","125 km WSW of Myitkyina, Myanmar"],
   3 : ["2023-05-31 05:55:18.193000","250 km N of Puerto Ayora, Ecuador"],
   4 : ["2023-05-30 23:04:49.967000","53 km ENE of Balkanabat, Turkmenistan"],
   5 : ["2023-05-30 21:21:23.155000","Auckland Islands, New Zealand region"],
   6 : ["2023-05-30 19:58:41.233000","Kepulauan Mentawai region, Indonesia"],
   7 : ["2023-05-30 11:51:36.770000","68 km SW of La Tirana, Chile"],
   8 : ["2023-05-30 10:22:34.391000","Luzon, Philippines"],
   9 : ["2023-05-30 03:49:17.485000","54 km NNW of Itoigawa, Japan"],
   10 : ["2023-05-29 23:01:33.443000","206 km SE of Hihifo, Tonga"],
   11 : ["2023-05-29 20:04:31.886000","13 km SE of Abra de Ilog, Philippines"],
   12 : ["2023-05-29 19:52:06.116000","Volcano Islands, Japan region"],
   13 : ["2023-05-29 12:08:16.844000","31 km W of Ipil, Philippines"],
   14 : ["2023-05-29 10:59:59.380000","Pulau Pulau Tanimbar, Indonesia"],
   15 : ["2023-05-29 10:02:29.594000","99 km WNW of Candelaria, Argentina"],
   16 : ["2023-05-29 08:52:51.758000","Kepulauan Barat Daya, Indonesia"],
   17 : ["2023-05-29 05:05:00.457000","21 km WNW of Port-Olry, Vanuatu"],
   18 : ["2023-05-28 23:57:33.108000","48 km NNE of Pucallpa, Peru"],
   19 : ["2023-05-28 21:33:32.124000","13 km NW of Dhekiajuli, India"],
   20 : ["2023-05-28 21:18:17.548000","239 km NE of Bamboo Flat, India"],
   21 : ["2023-05-28 14:08:22.211000","9 km NNE of Lluta, Peru"],
   22 : ["2023-05-28 13:51:22.804000","113 km NNE of Lhuentse, Bhutan"],
   23 : ["2023-05-28 13:03:11.519000","Sakhalin, Russia"],
   24 : ["2023-05-28 11:13:57.872000","106 km W of Lata, Solomon Islands"],
   25 : ["2023-05-28 10:45:56.635000","3 km N of Aratoca, Colombia"],
   26 : ["2023-05-28 07:52:39.263000","42 km W of Kimbe, Papua New Guinea"],
   27 : ["2023-05-28 00:49:56.404000","35 km SE of Jurm, Afghanistan"]
}

pais = input()

temblores_pais = []
for key, value in temblores.items():
    if pais.lower() in value[1].lower():
        fecha = value[0][:16]  # Obtiene los primeros 16 caracteres de la fecha (sin los segundos)
        ubicacion = value[1].split(",")[0]  # Obtiene la ubicación antes de la coma
        temblores_pais.append([fecha, ubicacion])

if temblores_pais:
    print(f"Los temblores reportados en {pais.capitalize()} fueron:")
    print("Fecha, Ubicacion")
    for temblor in temblores_pais:
        print(f"{temblor[0]}, {temblor[1]}")
else:
    print(f"No se encontraron temblores reportados en {pais.capitalize()}.")

