elements = ['Abra', 'Apayao', 'Benguet', 'Ifugao', 'Kalinga', 'Mt  Province',
       'Ilocos Norte', 'Ilocos Sur', 'La Union', 'Pangasinan', 'Batanes',
       'Cagayan', 'Isabela', 'Nueva Viscaya', 'Quirino', 'Aurora',
       'Bataan', 'Bulacan', 'Nueva Ecija', 'Pampanga', 'Tarlac',
       'Zambales', 'Metro Manila', 'Batangas', 'Cavite', 'Laguna',
       'Quezon', 'Rizal', 'Marinduque', 'Occidental Mindoro',
       'Oriental Mindoro', 'Palawan', 'Romblon', 'Albay',
       'Camarines Norte', 'Camarines Sur', 'Catanduanes', 'Masbate',
       'Sorsogon', 'Aklan', 'Antique', 'Capiz', 'Guimaras', 'Iloilo',
       'Negros Occidental', 'Bohol', 'Cebu', 'Negros Oriental', 'Siquijor',
       'Biliran', 'Eastern Samar', 'Leyte', 'Northern Samar', 'Samar',
       'Southern Leyte', 'Zamboanga del Norte', 'Zamboanga del Sur',
       'Zamboanga Sibugay', 'Bukidnon', 'Camiguin', 'Lanao del Norte',
       'Misamis Occidental', 'Misamis Oriental', 'Compostela Valley',
       'Davao del Norte', 'Davao del Sur', 'Davao Oriental', 'Cotabato',
       'Saranggani', 'South Cotabato', 'Sultan Kudarat',
       'Agusan del Norte', 'Agusan del Sur', 'Dinagat Islands',
       'Surigao del Norte', 'Surigao del Sur', 'Basilan', 'Lanao del Sur',
       'Maguindanao', 'Sulu', 'Tawi-Tawi']

var = 0

for i in range(0,81):
    if (len(elements[i])>10):
        var = var+1

print var
