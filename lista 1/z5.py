import math

print(5.5/2)
print(5.5//2)
print(round((5.5/2)))
print(math.floor((5.5/2)))

# 1) Dzielenie bez reszty '//' daje liczbę zmiennoprzecinkową, która jest wynikiem
#    dzielenia nie biorąc pod uwagę reszty z dzielenia
# 2) Operacja 'round' zaokrągla liczbę zmiennoprzecinkową, aby stała się liczbą
#    całkowitą w taki sposób, że cyfrę po kropce mniejszą od 5 zaokrągla w dół,
#    a większą bądź równą 5 zaokrągla w górę
# 3) Operacja 'floor' zaokrąga liczbę zmiennoprzecinkową w dół, czyli zostaje tylko
#	 to co przed kropką
