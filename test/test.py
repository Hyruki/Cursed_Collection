from PIL import Image, ImageDraw

# Dimensions de l'image
width, height = 16, 16

# Créer une nouvelle image
image = Image.new("RGB", (width, height), (50, 50, 50))  # Fond gris foncé
draw = ImageDraw.Draw(image)

# Définir des couleurs pour la texture cobblestone
colors = [
    (60, 60, 60),  # Gris foncé
    (80, 80, 80),  # Gris moyen
    (100, 100, 100)  # Gris clair
]

# Dessiner les "blocs" de pierre
shapes = [
    [(1, 1), (6, 6)],  # Bloc en haut à gauche
    [(8, 2), (13, 7)],  # Bloc en haut à droite
    [(2, 9), (7, 14)],  # Bloc en bas à gauche
    [(9, 10), (14, 15)]  # Bloc en bas à droite
]

for i, shape in enumerate(shapes):
    draw.rectangle(shape, fill=colors[i % len(colors)])

# Sauvegarder l'image
path = "cobblestone_16x16.png"
image.save(path)
path
