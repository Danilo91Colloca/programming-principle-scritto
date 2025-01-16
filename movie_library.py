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
        index = None
        for index_item, key in enumerate(self.movies):
            """ 
            casefold() consent to ignore 
            case-sensitiveness 
            considering all in lowercase
            """
            if key["title"].casefold() == title.casefold():
                index = index_item
                break
        if index is not None:
            self.movies.pop(index)
            self.__update_json_file(self.movies)
    def update_movie():
        pass


""" define function that deserialize json """       
def jsonDeserializer(json_to_deserialize):
    with open(json_to_deserialize, "r") as all_movies:
        return json.load(all_movies)
    
movies_list = jsonDeserializer(file_json_path)

library = MovieLibrary(file_json_path, movies_list)
#library.add_movie("Gatto","danny", 1991, ["speriamo", "bene"])
#library.remove_movie("gAtto")