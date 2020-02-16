import random


a = [
    "Synchron",
    "Aktiv",
    "Konjunktur",
    "Organisatorisch",
    "Ambivalent",
    "Typisch deutsch",
    "Amtsintern",
    "Wissenschaftlich",
    "Bürgerfreundlich",
    "Modifiziert",
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
    "idiotie",
    "problematik",
    "effizienz",
    "praktiken",
    "programmierung",
    "tendenz",
    "konzepte",
    "prinzipien",
    "komponenten",
    "schwierigkeiten",
]


random.seed()
print(
    f"{a[random.randrange(len(a))]} {b[random.randrange(len(b))]}",
    f"{c[random.randrange(len(c))]}{d[random.randrange(len(d))]}")
