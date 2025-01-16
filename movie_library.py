import json

"""production file json"""
#file_json_path = "/Applications/MAMP/htdocs/programming-principle-scritto/movies.json"
"""test file json"""
file_json_path = "/Applications/MAMP/htdocs/programming-principle-scritto/test.json"

    
"""Define Movie library class"""
class MovieLibrary:
    """
        A class rappresenting a library of movies with imports of all movies 
        and a collection of a movie that has title,director,year,genre

        Attributes: 
            json_file:  
            movies: collection of film
    """
    def __init__(self, json_file, movies):
        self.json_file = json_file
        self.movies = movies   


    def get_movies(self):
        return self.movies
    
    def __update_json_file(self, new_movie):
        with open(self.json_file, "w", encoding="utf-8") as inside_movies:
            return json.dump(new_movie, inside_movies, indent=4)

    def add_movie(self, title:str, director:str, year:int, genres:list):
        __data = {
            "title": title,
            "director": director,
            "year": year,
            "genres": genres
        }
        self.movies.append(__data)
        self.__update_json_file(self.movies)
    
    def remove_movie(self, title):
        __index = None
        for index_item, key in enumerate(self.movies):
            """ 
            casefold() consent to ignore 
            case-sensitiveness 
            considering all in lowercase
            """
            if key["title"].casefold() == title.casefold():
                __index = index_item
                break
        if __index is not None:
            self.movies.pop(__index)
            self.__update_json_file(self.movies)

    def update_movie(self,title: str, director: str=None,year: int=None,genres: list=None):
        __index = None
        for index_item, key in enumerate(self.movies):
            if key["title"].casefold() == title.casefold():
                __index = index_item
                break
        if __index is not None:
            match (director, year, genres):
                case (None, None, None):
                    pass
                case (director, None, None):
                    self.movies[__index].update({
                        "director": director
                    })
                case (None, None, genres):
                    self.movies[__index].update({
                        "genres": genres
                    })            
                case (None, year, None):
                    self.movies[__index].update({
                        "year": year
                    })            
                case (director, None, genres):
                    self.movies[__index].update({
                        "director": director,
                        "genres": genres
                    })
                case (director, year, None):
                    self.movies[__index].update({
                        "director": director,
                        "year": year
                    })            
                case (None, year, genres):
                    self.movies[__index].update({
                        "year": year,
                        "genres": genres
                    })            
                case (director,year,genres):
                    self.movies[__index].update({
                        "director":director,
                        "year": year,
                        "genres": genres
                    })    
            self.__update_json_file(self.movies)
                
    def get_movie_titles(self):
        __all_titles=[]
        for title in self.movies:
            __all_titles.append(title["title"])
        
        return __all_titles
    
    def count_movies(self):
        return len(self.movies)
    
    def get_movie_by_title(self, title):
        __index = None
        for index_item, key in enumerate(self.movies):
            if key["title"].casefold() == title.casefold():
                __index = index_item
                break
        return self.movies[__index]

    def get_movie_by_title_substring(self, substring:str):
        __movies_by_substring=[]
        for index_item, key in enumerate(self.movies):
            if key["title"].find(substring) > -1:
                __movies_by_substring.append(self.movies[index_item])
        return __movies_by_substring

    def get_movies_by_year(self,year: int):
        __index = None
        __all_movies_by_year = []
        for index_item, key in enumerate(self.movies):
            if key["year"] == year:
                __index = index_item
                __all_movies_by_year.append(self.movies[__index])
        return __all_movies_by_year

    def count_movies_by_director(self,director: str):
        count_movies_by_director = 0
        for i, key in enumerate(self.movies):
            if key["director"].casefold() == director.casefold():
                count_movies_by_director += 1
        return count_movies_by_director
        
    def get_movies_by_genre(self, genre: str):
        movies_by_genre = []
        for index_movie, key in enumerate(self.movies):
            for i in key["genres"]:
                if i.casefold() == genre.casefold():
                    movies_by_genre.append(self.movies[index_movie])
        return movies_by_genre

    


""" define function that deserialize json """       
def jsonDeserializer(json_to_deserialize):
    with open(json_to_deserialize, "r") as all_movies:
        return json.load(all_movies)
    
movies_list = jsonDeserializer(file_json_path)

library = MovieLibrary(file_json_path, movies_list)
#print(library.get_movies())

#library.add_movie("gatto","danny", 1991, ["speriamo", "bene"])
#library.remove_movie("TEST")
#library.update_movie("gatto","Top",1500, ["forse", "top"])

#print(type(library.get_movie_titles()))
#print(library.get_movie_titles())

#print(library.count_movies())
#print(library.get_movie_by_title("the matrix"))

#print(library.get_movie_by_title_substring("Lord"))

#print(library.get_movies_by_year(1994))

#print(library.count_movies_by_director("Christopher NOLAN"))

# print(library.get_movies_by_genre("DRama"))
# print(len(library.get_movies_by_genre("DRama")))