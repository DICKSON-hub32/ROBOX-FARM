import csv

# Data for the CSV file with ranges for soil moisture, latitude, and soil pH
data = [
    ["crop_name", "Nitrogen (g/kg)", "Phosphorous (g/kg)", "Potassium (g/kg)", "Soil Moisture (%)", "Number of times of irrigation in a day", "Number of days of irrigation in a week", "Latitude", "Soil pH"],
    ["Maize", "1.8-2.2", "1.3-1.7", "2.8-3.2", "60-70", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Rice", "2.3-2.7", "1.6-2.0", "2.6-3.0", "70-80", 2, 6, "1.2900-1.2950", "5.0-6.5"],
    ["Wheat", "1.6-1.9", "1.1-1.3", "2.3-2.7", "50-60", 1, 3, "1.2900-1.2950", "6.0-7.5"],
    ["Sorghum", "1.4-1.6", "0.9-1.1", "1.9-2.1", "40-50", 1, 2, "1.2900-1.2950", "5.5-7.0"],
    ["Millet", "1.1-1.3", "0.7-0.9", "1.7-1.9", "30-40", 1, 2, "1.2900-1.2950", "5.0-6.5"],
    ["Beans", "1.9-2.1", "1.3-1.5", "2.4-2.6", "60-70", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Peas", "1.7-1.9", "1.2-1.4", "1.9-2.1", "55-65", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Sweet Potatoes", "1.4-1.6", "1.0-1.2", "2.0-2.4", "70-80", 1, 2, "1.2900-1.2950", "5.5-7.0"],
    ["Irish Potatoes", "1.5-1.7", "1.3-1.5", "2.2-2.6", "75-85", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Cassava", "1.2-1.4", "0.9-1.1", "1.8-2.2", "65-75", 1, 2, "1.2900-1.2950", "5.5-7.0"],
    ["Taro", "1.8-2.2", "1.4-1.6", "2.3-2.7", "80-90", 2, 6, "1.2900-1.2950", "5.5-7.0"],
    ["Groundnuts (Peanuts)", "1.8-2.2", "1.2-1.4", "2.3-2.7", "60-70", 1, 2, "1.2900-1.2950", "5.5-7.0"],
    ["Soybeans", "2.0-2.4", "1.4-1.6", "2.6-3.0", "55-65", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Sunflower", "1.4-1.6", "1.1-1.3", "1.9-2.1", "50-60", 1, 2, "1.2900-1.2950", "5.5-7.0"],
    ["Cabbage", "1.7-1.9", "1.4-1.6", "2.1-2.3", "60-70", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Carrots", "1.5-1.7", "1.3-1.5", "2.0-2.4", "65-75", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Tomatoes", "1.9-2.2", "1.4-1.6", "2.3-2.7", "70-80", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Onions", "1.6-1.8", "1.2-1.4", "2.1-2.5", "65-75", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Kales (Sukuma Wiki)", "1.8-2.0", "1.3-1.5", "2.2-2.6", "60-70", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Okra", "1.7-1.9", "1.3-1.5", "2.1-2.5", "70-80", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Pumpkin", "1.4-1.6", "1.2-1.4", "2.0-2.4", "65-75", 1, 2, "1.2900-1.2950", "5.5-7.0"],
    ["Chili Peppers", "1.8-2.0", "1.3-1.5", "2.3-2.7", "80-90", 2, 4, "1.2900-1.2950", "5.5-7.0"],
    ["Eggplant", "1.6-1.8", "1.2-1.4", "2.1-2.5", "60-70", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Coriander", "1.4-1.6", "1.1-1.3", "2.0-2.2", "55-65", 1, 2, "1.2900-1.2950", "5.5-7.0"],
    ["Lettuce", "1.7-1.9", "1.3-1.5", "2.1-2.5", "60-70", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Spinach", "1.9-2.2", "1.4-1.6", "2.3-2.7", "65-75", 1, 3, "1.2900-1.2950", "5.5-7.0"],
    ["Beetroot", "1.5-1.7", "1.2-1.4", "2.0-2.4", "70-80", 1, 2, "1.2900-1.2950", "5.5-7.0"]
]

# Writing to a CSV file
with open('crops_data_with_ranges_and_ph.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
