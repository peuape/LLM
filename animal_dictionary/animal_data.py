animal_dictionary = [
    {
        "common_name": "Glitterfang",
        "scientific_name": "Luminocanis aurorae",
        "habitat": ["Norway", "Sweden", "Finland"],
        "length": 1.8,
        "weight": 65,
        "colour": "Iridescent silver with streaks of glowing blue and purple",
    },
    {
        "common_name": "Lunarkeeper",
        "scientific_name": "Noctua celestialis",
        "habitat": ["Greenland", "Iceland", "Canada"],
        "length": 2.5,
        "weight": 75,
        "colour": "Dark midnight blue with glowing white spots resembling stars",
    },
    {
        "common_name": "Frostmane",
        "scientific_name": "Equus glacius",
        "habitat": ["Russia", "Mongolia", "Alaska"],
        "length": 2.2,
        "weight": 300,
        "colour": "Pale blue and white with shimmering frost-like patterns on its mane",
    },
    {
        "common_name": "Thundertusk",
        "scientific_name": "Mammuthus fulgur",
        "habitat": ["India", "Nepal", "Thailand"],
        "length": 4.5,
        "weight": 6000,
        "colour": "Stormy grey with golden streaks along its tusks and back",
    },
    {
        "common_name": "Flarehawk",
        "scientific_name": "Accipiter ignis",
        "habitat": ["Australia", "New Zealand", "Chile"],
        "length": 1.2,
        "weight": 15,
        "colour": "Fiery red with bright orange and yellow flame-like feathers",
    },
]

# Extract common names for reference
animals_in_dict = [animal["common_name"] for animal in animal_dictionary]
