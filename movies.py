import time
from random import choice, randint

from test import Movies

now = time.strftime("%d/%m/%Y")

class Filmy:
    def __init__ (self, title, year, type):
        self.title = title
        self.year = year
        self.type = type
        self.view = 0

    def __str__ (self):
        return (f"\nTytuł: {self.title}\n - data produkcji: {self.year}\n - gatunek: {self.type}")

    print(f'\nHistoria ostatnio wyświetlonych filmów znajdujących się w bibliotece:\n')

    def play(self):
        self.view += 1
        print(f'{self.title} - liczba wyświetleń: {self.view}')

class Seriale(Filmy):
    def __init__ (self, season, episode, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.season = season
         self.episode = episode

    def __str__(self):
        return (
            f'\nTytuł: {self.title}\n - data produkcji: {self.year}\n - gatunek: {self.type}\n * Sezon/odcinek: S{self.season:02}E{self.episode:02}')


movie1 = Filmy(title="Skazani na Shawshank", year=1994, type="Dramat")
movie2 = Filmy(title="Nietykalni", year=2011, type="Biograficzny / Dramat / Komedia")
movie3 = Filmy(title="Zielona mila", year=1999, type="Dramat")
movie4 = Filmy(title="Ojciec chrzestny", year=1972, type="Dramat / Gangsterski")
movie5 = Filmy(title="Forrest Gump", year=1994, type="Dramat / Komedia")
serie1 = Seriale(title="Dom z papieru", year=2017, type="Thriller, Akcja", season=5, episode=1)
serie2 = Seriale(title="Czarnobyl", year=2019, type="Dramat", season=1, episode=1)
serie3 = Seriale(title="Breaking Bad", year=2008, type="Dramat, Kryminał", season=5, episode=1)

filmy_seriale = [movie1, movie2, movie3, movie4, movie5, serie1, serie2, serie3]
by_title = sorted(filmy_seriale, key=lambda picture: picture.title)
by_date = sorted(filmy_seriale, key=lambda picture: picture.year)

def get_movies():
    pictures = []
    for picture in by_title:
          if not isinstance (picture, Seriale):
            pictures.append(picture)
            print(f"- {picture.title}")
    return pictures

def get_series():
    pictures = []
    for picture in by_title:
        if isinstance(picture, Seriale):
            pictures.append(picture)
            print(f"- {picture.title}")
    return pictures


def search():
    text = input("Wpisz tytuł filmu aby wyświetlić szczegółowe informacje: ")
    for picture in filmy_seriale:
        if picture.title.lower() == text.lower():
            print(picture)

movie1.play()
movie1.play()
movie1.play()
serie3.play()
serie1.play()
movie4.play()
movie3.play()
movie2.play()
movie2.play()
movie5.play()
serie2.play()
serie1.play()
serie3.play()
movie4.play()
movie2.play()
movie5.play()

def top_title(type):
    top = []
    if type == "Filmy":
      for picture in filmy_seriale:
        if picture.view > 0:
            if not isinstance(picture, Seriale):
              top.append(picture.view)
              print(f'{picture} liczba odtworzeń - {picture.view}')
    elif type == "Serie":
      for picture in filmy_seriale:
        if picture.view > 0:
            if isinstance(picture, Seriale):
              top.append(picture.view)
              print(f'{picture} liczba odtworzeń - {picture.view}')
    return top

def top_3(top):
    top = []
    for picture in filmy_seriale:
        if picture.view in top[:3]:
            print(f"{picture} with {picture.view} views")
    return top

def generate_views(times=10):
    for i in range(times):
        index = random()
        add_views(index)
        plays = filmy_seriale[index].view
        title = filmy_seriale[index].title
        print(f"View generated for {title} {plays}")

def random():
    elements = len(filmy_seriale)
    return randint(0, elements - 1)

def add_views(index):
    views = randint(1, 100)
    return filmy_seriale[index].play(views)

def run():
    print(f"\n------------------------ BAZA FILMOW I SERIALI {now} ------------------------\n")
    print("Wybierz proszę co chcesz zrobić?\n\n 1 - Wyświetl listę wszystkich filmów\n 2 - Wyświetl listę wszystkich filmów wielosezonowych\n 3 - Lista najpopularniejszych filmów\n 4 - Lista najpopularniejszych filmów sezonowych\n 5 - Wyszukaj informacje o filie z bazy\n\n 'exit' zakończenie działania programu\n")
    choice = input("Twój wybór: ")
    
    while True: 
        if choice == "1":
            print("")
            get_movies()
            return

        elif choice == "2":
            print("")
            get_series()
            return
            
        elif choice == "3":
            top_title("Filmy")
            return
        
        elif choice == "4":
            top_title("Serie")
            return

        elif choice == "5":
            search()
            return

        elif choice == "exit":
            print("                       ")
            print("Wpadnij jeszcze kiedyś!")
            print("                       ")
            exit()

        else:
            error = f"Error!"
            print(error)
            exit()

run()
