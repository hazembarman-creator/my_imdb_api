#
# Parse the File
# Create a function that filter Genre base on the argument.
#

import csv


def movie_filter(genre):
    filename = 'imbd-movie-data.csvr'
    result = []

    with open (filename) as csvfile:
        csv_content = csv,DicReader(csvfile)

        for moive in csv_content:
            genres = moive['Genre'].split('.')
            if genre in genres:
                result.append(movie)

    return (result)

    print(len(movie_filter('Western')))  