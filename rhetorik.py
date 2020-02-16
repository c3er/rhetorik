import random


a = [
    "synchron",
    "aktiv",
    "Konjunktur",
    "organisatorisch",
    "ambivalent",
    "typisch deutsch",
    "amtsintern",
    "wissenschaftlich",
    "bürgerfreundlich",
    "modifiziert",
]
b = [
    "punktuelle",
    "orientierte",
    "qualifizierte",
    "progressive",
    "bedingte",
    "maximierte",
    "konzentrierte",
    "integrierte",
    "flexible",
    "strukturierte",
]
c = [
    "Steuerrechts",
    "Reform",
    "Gewerkschafts",
    "Veranlagungs",
    "Aufgabenverteilungs",
    "Personal",
    "Behörden",
    "Vorgesetzten",
    "Kollegialitäts",
    "Arbeitsplatz",
]
d = [
    "Idiotie",
    "Problematik",
    "Effizienz",
    "Praktiken",
    "Programmierung",
    "Tendenz",
    "Konzepte",
    "Prinzipien",
    "Komponenten",
    "Schwierigkeiten",
]


random.seed()
for i in range(5):
    print(
        f"{a[random.randrange(len(a))]} {b[random.randrange(len(b))]}",
        f"{c[random.randrange(len(c))]}{d[random.randrange(len(d))]}")
