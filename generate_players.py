import os

# Helper function to convert integers (1-28) to Roman numerals
def to_roman(number):
    roman_map = [
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ""
    for value, numeral in roman_map:
        while number >= value:
            result += numeral
            number -= value
    return result

# Configuration for the 4 gospels
GOSPELS = [
    {
        "prefix": "Matus",
        "chapters": 28,
        "secundum": "Mattheum",
        "mtmklkjn": "Mt",
        "podla": "Matúša"
    },
    {
        "prefix": "Marek",
        "chapters": 16,
        "secundum": "Marcum",
        "mtmklkjn": "Mk",
        "podla": "Marka"
    },
    {
        "prefix": "Lukas",
        "chapters": 24,
        "secundum": "Lucam",
        "mtmklkjn": "Lk",
        "podla": "Lukáša"
    },
    {
        "prefix": "Jan",
        "chapters": 21,
        "secundum": "Ioannem",
        "mtmklkjn": "Jn",
        "podla": "Jána"
    }
]

# HTML Template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="sk">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prehrávač - {roman}. {secundum}</title>

    <!-- 1. Link to your shared CSS file -->
    <link rel="stylesheet" href="../css/evangeliarum.css">

    <!-- 2. The ONLY page-specific style left behind -->
    <style>
        body {{ background-image: url("../assets/pictura/{bg_image}.jpg"); }}
    </style>
</head>

<body>

<div class="player-container">
    <img src="../assets/pictura/{roman}._{secundum}.jpg" alt="Ad Dei Gloriam">
    
    <h2>{arabic}. kapitola evanjelia podľa sv. {podla}</h2>

    <audio controls preload="auto">
        <source src="../assets/audio/{mtmklkjn}_{arabic}.m4a" type="audio/mp4">
        toto.
    </audio>
    
    <br>
    <a href="../Lectio-Divina.html" class="back-btn">◀ ▃▅▇ </a>
</div>

</body>
</html>
"""

def generate_all_players():
    output_dir = "Prehrávače"
    total_created = 0

    for gospel in GOSPELS:
        for ch in range(1, gospel["chapters"] + 1):
            roman = to_roman(ch)
            arabic = str(ch)
            mtmklkjn = gospel["mtmklkjn"]
            
            # {bg_image} = combination of {roman} and "._" and {mtmklkjn}
            bg_image = f"{roman}._{mtmklkjn}"
            
            # Populate HTML string
            html_content = HTML_TEMPLATE.format(
                roman=roman,
                secundum=gospel["secundum"],
                bg_image=bg_image,
                arabic=arabic,
                podla=gospel["podla"],
                mtmklkjn=mtmklkjn
            )
            
            # File naming convention: e.g., Matus-I.html
            filename = f"{gospel['prefix']}-{roman}.html"
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(html_content)
                
            total_created += 1

    print(f"Successfully generated all {total_created} player HTML files!")

if __name__ == "__main__":
    generate_all_players()
