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
        data = {
            "title": title,
            "director": director,
            "year": year,
            "genres": genres
        }
        self.movies.append(data)
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
        all_titles=[]
        for title in self.movies:
            all_titles.append(title["title"])
        
        return all_titles
    
    def count_movies(self):
        return len(self.movies)
    
    def get_movie_by_title(self, title):
        __index = None
        for index_item, key in enumerate(self.movies):
            if key["title"].casefold() == title.casefold():
                __index = index_item
                break
        print(self.movies[__index])

""" define function that deserialize json """       
def jsonDeserializer(json_to_deserialize):
    with open(json_to_deserialize, "r") as all_movies:
        return json.load(all_movies)
    
movies_list = jsonDeserializer(file_json_path)

library = MovieLibrary(file_json_path, movies_list)
#library.add_movie("test","danny", 1991, ["speriamo", "bene"])
#library.remove_movie("TEST")
#library.update_movie("gatto","Top",1500, ["forse", "top"])
#print(type(library.get_movie_titles()))

#print(library.count_movies())
#print(library.get_movie_by_title("the matrix"))