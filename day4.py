class Movie:
    def __init__(self,title,hero,heroine):
        self.title = title
        self.hero =hero 
        self.heroine = heroine 

    def info(self):
        print(f"Movie name:",self.title)
        print(f"Hero name:",self.hero)
        print(f"Heroine name:",self.heroine)

list_of_movies=[]
while True:
    title = input("Enter Movie Name:")
    hero = input("Enter Hero Name:")
    heroine = input("Enter Heroine Name:")
    m = Movie(title,hero,heroine)
    list_of_movies.append(m)
    print("movie added to the list successfully")
    option = input("Do you want to add more movies? (yes/no):")
    if option.lower() == "no":
        break
print("All Movies Information:")
print("#" * 40)
for movie in list_of_movies:
    movie.info()
    print()