import os

# --- CONFIGURATION FOR THE WEEK ---
# Change these two variables every Saturday before running the script
ROMAN_WEEK = "XVI"    # The current week in Roman numerals
ARABIC_WEEK = "16"    # The current week in Arabic numerals

# --- STATIC MAPPINGS ---
DAYS = [
    {"roman": "Sol", "arabic": "Ned", "bg": "11._Ned.jpg"}, # Sunday template exception handling
    {"roman": "Lun", "arabic": "Pon", "bg": "11._Ned.jpg"},
    {"roman": "Mar", "arabic": "Uto", "bg": "11._Ned.jpg"},
    {"roman": "Mer", "arabic": "Str", "bg": "11._Ned.jpg"},
    {"roman": "Iov", "arabic": "Štv", "bg": "11._Ned.jpg"},
    {"roman": "Ven", "arabic": "Pia", "bg": "11._Ned.jpg"}
]

# The base HTML template matching your exact design
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="sk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prehrávač - {roman_week}. {roman_day}</title>

     <!-- 1. Link to your shared CSS file -->
    <link rel="stylesheet" href="../css/scriptura.css">

    <!-- 2. The ONLY page-specific style left behind -->
    <style>
        body { background-image: url("../assets/pictura/{roman_week}._{roman_day}.jpg"); }
    </style>
</head>
<body>

<div class="player-container">
    <img src="../assets/pictura/{roman_week}._{roman_day}.jpg" alt="Dávid a žena pred jeho trónom">
    
    <h2>II. Kniha Samuelova 15-16</h2>
    <h2>Príslovia 12</h2>

    <audio id="audio-1" controls preload="auto">
        <source src="../assets/audio/{arabic_week}._{arabic_day}_1.m4a" type="audio/mp4">
        toto.
    </audio>

    <audio id="audio-2" controls preload="auto">
        <source src="../assets/audio/{arabic_week}._{arabic_day}_2.m4a" type="audio/mp4">
        toto.
    </audio>

    <audio id="audio-3" controls preload="auto">
        <source src="../assets/audio/{arabic_week}._{arabic_day}_3.m4a" type="audio/mp4">
        toto.
    </audio>
  
    <br>
    <a href="../Lectio-Divina.html" class="back-btn">◀ ▃▅▇ </a>
</div>
    
</body>
</html>"""

def generate_weekly_files():
    output_dir="Prehrávače"
    
    for day in DAYS:
        # Dynamically inject the week numbers and specific day components
        file_content = HTML_TEMPLATE.format(
            roman_week=ROMAN_WEEK,
            roman_day=day["roman"],
            arabic_week=ARABIC_WEEK,
            arabic_day=day["arabic"],
            bg_image=day["bg"]
        )
        
        # Build the exact output filename (e.g., "XVI._Sol.html")
        filename = f"{ARABIC_WEEK}._{day['arabic']}.html"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(file_content)
            
        print(f"Created successfully: {filename}")

if __name__ == "__main__":
    generate_weekly_files()
