data = {
	"j@g.com": {"age": "20", "calories exercise": "1560", "calories intake": "2300", "gender": "female", "height": "189", "macros": {"carbs": "35", "fats": "12", "protein": "64"}, "name": "jack", "weight": "78"},
	"kx@g.com": {"age": "19", "calories exercise": "1200", "calories intake": "2000", "gender": "female", "height": "170", "macros": {"carbs": "12", "fats": "39", "protein": "50"}, "name": "kaitlyn", "weight": "67"}, 
	"nic@g.com": {"age": "22", "calories exercise": "800", "calories intake": "1500", "gender": "female", "height": "176", "macros": {"carbs": "15", "fats": "30", "protein": "40"}, "name": "nicole", "weight": "73"}
}

print data.values()[0].values()[0].values() + data.values()[0].values()[1:]