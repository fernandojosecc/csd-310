"""
Title: movies_update_and_delete.py
Author: Fernando Contreras
Date: May 2026
Description: This script connects to the movies database and demonstrates
how to insert, update, delete, and display records using Python and MySQL.
"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values

# load credentials from the .env file in module-5
secrets = dotenv_values("..//module-5//.env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

def show_films(cursor, title):
    """
    Function: show_films
    Description: Executes a SELECT query joining the film, genre, and studio
    tables, then displays the results with a given title label.
    Arguments: cursor (MySQL cursor object), title (string label for output)
    """

    # query that joins film, genre, and studio tables to get readable names
    cursor.execute("""
        SELECT film_name, film_director, genre_name, studio_name 
        FROM film 
        INNER JOIN genre ON film.genre_id = genre.genre_id 
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)

    # fetch all results from the query
    films = cursor.fetchall()

    # print the section title
    print("\n  -- {} --".format(title))

    # iterate over each film and display its details
    for film in films:
        print("Film Name: {}".format(film[0]))
        print("Director: {}".format(film[1]))
        print("Genre Name ID: {}".format(film[2]))
        print("Studio Name: {}\n".format(film[3]))


try:
    """ try/catch block for handling potential MySQL database errors """

    # connect to the movies database using config object
    db = mysql.connector.connect(**config)

    # create a cursor object to execute queries
    cursor = db.cursor()

    # -- display all films before any changes --
    show_films(cursor, "DISPLAYING FILMS")

    # -- insert a new film record --
    # using Star Wars as the new film with 20th Century Fox studio and SciFi genre
    cursor.execute("""
        INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
        VALUES('Star Wars', '1977', '121', 'George Lucas',
            (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'),
            (SELECT genre_id FROM genre WHERE genre_name = 'SciFi'))
    """)

    # commit the insert to the database
    db.commit()

    # display all films after insert
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # -- update Alien's genre from SciFi to Horror --
    cursor.execute("""
        UPDATE film 
        SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
        WHERE film_name = 'Alien'
    """)

    # commit the update to the database
    db.commit()

    # display all films after update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # -- delete the film Gladiator from the database --
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")

    # commit the delete to the database
    db.commit()

    # display all films after delete
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """
    db.close()