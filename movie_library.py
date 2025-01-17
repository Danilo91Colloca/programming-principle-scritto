import json
import collections
import os

"""Define Movie library class."""


class MovieLibrary:

    """
        A class rappresenting a movie's library with
        a json_file where get the file which contains
        the movies and movies which contains a list
        of dictionaries that contains title, director,
        year and genres.

        Attributes:
            json_file (str): The file' s absolute path.
            movies (list): collection of movies (dict).

    """

    def __init__(self, json_file: str, movies: list):
        """
            Inizialize a new MovieLibrary object with
            file's absolute path and movie's list.

            Args:
                json_file (str): The file' s absolute path.
                movies (list): collection of movies (dict).

        """

        self.json_file = json_file
        self.movies = movies

        class FileNotFoundError(Exception):
            """
                Custom Exception rises
                if file does not exist.

            """

            def __init__(self):
                """
                    Inizialize the error message with
                    the wring file name.

                """
                self.errorMsg = f"File not found: {json_file}"
                """
                    Return the object message to the parent class

                """
                super().__init__(self.errorMsg)

        def check_file_exist(file_json: str):
            """
                Check if the file exsist.

                Args:
                    file_json (str): The file to check.

                Raises:
                    FileNotFoundError: if the file name or path
                    is not found.
            """
            if not os.path.exists(file_json):
                raise FileNotFoundError

        try:
            check_file_exist(self.json_file)
        except FileNotFoundError as e:
            print(e)

    def get_movies(self) -> list:
        """
            Get the list that contain all movies.

            return:
                movies (list): The entire deserialized
                json_file content.

        """
        return self.movies

    def __update_json_file(self, new_movie):
        """
            Update the entire file that contain movie's data after
            any modification like, add new movie, remove a movie or update
            a movie.

            Return
                json.dump(arg1, arg2, param) :
                arg1 = data to be serialized.
                arg2 = object where arg1 is written.
                param (indent = 4) = space of indentazion per level.

        """

        with open(self.json_file, "w", encoding="utf-8") as inside_movies:
            return json.dump(new_movie, inside_movies, indent=4)

    def add_movie(self, title: str, director: str, year: int, genres: list):
        """
            Add new movie into the file which contain movies

            Args:
                title (str): the new movie's title.
                director (str): the new movie's director.
                year (int): the new movie's publication year.
                genres (list): the new movie' s genres list.

        """

        __data = {
            "title": title,
            "director": director,
            "year": year,
            "genres": genres
        }
        self.movies.append(__data)
        """
            Invoke the private methods that update the movie's file.

            GOOD THINGS TO DO
            Including a check of the arguments and
            their error messages is a desirable thing to do
            before sending data.

        """
        self.__update_json_file(self.movies)

    class MovieNotFoundError(Exception):
        """
            Custom Exception raises if a request movie
            is not found into the file that contain all movies.

        """
        def __init__(self):
            self.errorMsg = "Movie was not found"
            super().__init__(self.errorMsg)

    def remove_movie(self, title):
        """
            Remove movie from the file that contain all movies,
            ensuring title exist.

            Args:
                title (str): The title to be removed.

            Risees:
                MovieNotFoundError: if title is not found.
        """
        try:
            __index = None
            for index_item, key in enumerate(self.movies):
                """
                    casefold() is used to allow py
                    to ignore case-sensitiveness
                    considering all in lowercase

                """
                if key["title"].casefold() == title.casefold():
                    __index = index_item
                    break
            if __index is not None:
                self.movies.pop(__index)
                self.__update_json_file(self.movies)
            else:
                raise self.MovieNotFoundError
        except self.MovieNotFoundError as e:
            print(e)

    def update_movie(
            self,
            title: str,
            director: str = None,
            year: int = None,
            genres: list = None
            ) -> None:
        """
            Update the movie into the file that contain
            all movies.

            Args:
                title (str): the title of the movie to be updated

                Optional args:
                    director (str): the director.

            Raises:
                MovieNotFoundError: if movie to update is
                not found into the file that contain all movies.

        """

        try:
            __index = None
            for index_item, key in enumerate(self.movies):
                if key["title"].casefold() == title.casefold():
                    __index = index_item
                    break

            if __index is not None:
                """
                    The use of match/case is less verbose than if/elif

                """
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
                    case (director, year, genres):
                        self.movies[__index].update({
                            "director": director,
                            "year": year,
                            "genres": genres
                        })
                self.__update_json_file(self.movies)
            else:
                raise self.MovieNotFoundError
        except self.MovieNotFoundError as e:
            print(e)

    def get_movie_titles(self) -> list:
        """
            Get all titles of the movies

                Return:
                    List with all movie titles
        """

        __all_titles = []
        for title in self.movies:
            __all_titles.append(title["title"])

        return __all_titles

    def count_movies(self) -> int:
        return len(self.movies)

    def get_movie_by_title(self, title: str):
        __index = None
        for index_item, key in enumerate(self.movies):
            if key["title"].casefold() == title.casefold():
                __index = index_item
                break
        return self.movies[__index]

    def get_movie_by_title_substring(self, substring: str):
        __movies_by_substring = []
        for index_item, key in enumerate(self.movies):
            if key["title"].find(substring) > -1:
                __movies_by_substring.append(self.movies[index_item])
        return __movies_by_substring

    def get_movies_by_year(self, year: int):
        __index = None
        __all_movies_by_year = []
        for index_item, key in enumerate(self.movies):
            if key["year"] == year:
                __index = index_item
                __all_movies_by_year.append(self.movies[__index])
        return __all_movies_by_year

    def count_movies_by_director(self, director: str):
        __count_movies_by_director = 0
        for i, key in enumerate(self.movies):
            if key["director"].casefold() == director.casefold():
                __count_movies_by_director += 1
        return __count_movies_by_director

    def get_movies_by_genre(self, genre: str):
        __movies_by_genre = []
        for index_movie, key in enumerate(self.movies):
            for i in key["genres"]:
                if i.casefold() == genre.casefold():
                    __movies_by_genre.append(self.movies[index_movie])
        return __movies_by_genre

    def get_oldest_movie_title(self):
        __reorderd_movies_list = sorted(
            self.movies,
            key=lambda x: x['year']
        )
        return __reorderd_movies_list[0]

    def get_average_release_year(self):
        __all_years_to_sum = []
        for index_item, key in enumerate(self.movies):
            __all_years_to_sum.append(float(key["year"]))
        return sum(__all_years_to_sum)/len(__all_years_to_sum)

    def get_longest_title(self):
        __longest_title = sorted(
            self.movies,
            key=lambda k: len(k["title"]),
            reverse=True
        )
        return __longest_title[0]["title"]

    def get_titles_betweens_years(self, start_year: int, end_year: int):
        __title_list_list = []
        for i, key in enumerate(self.movies):
            if key["year"] >= start_year and key["year"] <= end_year:
                __title_list_list.append(key["title"])
        return __title_list_list

    def get_most_common_year(self):
        __all_years = []
        for i, key in enumerate(self.movies):
            __all_years.append(key["year"])
        __count_most_common = collections.Counter(__all_years)
        return __count_most_common.most_common()[0][0]


"""
production file json

file_json_path = f"{os.path.abspath("programming-principle-scritto/movies.json")}"
"""

"""test file json"""
file_json_to_deserialize = os.path.abspath(
    "programming-principle-scritto/test.json"
)
""" define function that deserialize json """


def jsonDeserializer(json_to_deserialize):
    with open(json_to_deserialize, "r") as all_movies:
        return json.load(all_movies)


movies_deserialized_list = jsonDeserializer(file_json_to_deserialize)


library = MovieLibrary(
    os.path.abspath("programming-principle-scritto/test.json"),
    movies_deserialized_list
)

# print(library.get_movies())

# library.add_movie("ciao","danny", 1500, ["speriamo", "bene"])

# library.remove_movie("ciao")

# library.update_movie("gatto","Top",1900, ["forse", "top"])

# print(type(library.get_movie_titles()))

# print(library.get_movie_titles())

# print(library.count_movies())

# print(library.get_movie_by_title("the matrix"))

# print(library.get_movie_by_title_substring("Lord"))

# print(library.get_movies_by_year(1994))

# print(library.count_movies_by_director("Christopher NOLAN"))

# print(library.get_movies_by_genre("DRama"))

# print(len(library.get_movies_by_genre("DRama")))

# print(library.get_oldest_movie_title())

# print(library.get_average_release_year())

# print(type(library.get_average_release_year()))

# print(library.get_longest_title())

# print(library.get_titles_betweens_years(1990,1995))

# print(library.get_most_common_year())
