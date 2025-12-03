canciones_ana = ["Master of Puppets", "Painkiller", "Hallowed Be Thy Name", "Hallowed Be Thy Name", "Holy Wars", "Chop Suey!"]
canciones_luis = ["Painkiller", "Holy Wars", "Chop Suey!", "Walk", "The Trooper"]


# A)
canciones_ana_sin_repes = list(set(canciones_ana))
canciones_luis_sin_repes = list(set(canciones_luis))
print(f'Canciones que solo tiene Ana: {canciones_ana_sin_repes}')
print(f'Canciones que solo tiene Luis: {canciones_luis_sin_repes}')

# B)
ambos = list(set(canciones_ana) & set(canciones_luis))
print(f'Canciones que tienen ambos: {ambos}')

# C)
solo_ana = list(set(canciones_ana) - set(canciones_luis))
print(f'Canciones que solo tiene Ana: {solo_ana}')

# D)
tiene_repes_ana = len(canciones_ana) != len(set(canciones_ana))
tiene_repes_luis = len(canciones_luis) != len(set(canciones_luis))

print('Ana tiene canciones repetidas' if tiene_repes_ana else 'Ana NO tiene canciones repetidas')

print('Luis tiene canciones repetidas' if tiene_repes_luis else 'Luis NO tiene canciones repetidas')

# E)
playlist_conjunta = list(set(canciones_ana) | set(canciones_luis))
print(f'La playlist conjunta es: {playlist_conjunta}')

# F)
solo_luis = list(set(canciones_luis) - set(canciones_ana))
print(f'Canciones que solo tiene Luis: {solo_luis}')
