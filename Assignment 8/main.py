import pandas as pd  

superheroes =[ "Batman","Superman","Spider-man","Iron-Man",
              "Captain America","Wonder Woman"]
strenght_levels = (10, 119, 40, 70, 40, 120)

shSerie = pd.Series(superheroes)
slSerie = pd.Series(strenght_levels)

heroes = pd.Series(strenght_levels,superheroes)

#extract1 = heroes.head(2).add(heroes.tail(2), fill_value=0)
#extract2 = pd.concat([heroes.head(2),heroes.tail(2)])
extract3 = pd.concat([heroes[:2], heroes[-2:]])

unique = heroes.drop_duplicates().value_counts().sum()

maxStr = heroes.max()
minStr = heroes.min()
avgStr = heroes.mean()

herDouble = heroes*2

herDict = dict(heroes)