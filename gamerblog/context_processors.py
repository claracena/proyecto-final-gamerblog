from random import randrange

def background(request):
    number = randrange(1, 10)
    return {'bg': f'bg-{number:02d}.jpg'}