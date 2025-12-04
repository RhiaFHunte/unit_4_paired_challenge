from lib.paired_challenge import *

"""
Given a new song
#Task: check that the list is empty to begin with
"""
def test_check_list_is_empty():
    spotifoo = Spotifoo()
    # assert spotifoo.list_songs == []
    
"""
Given a new song
#Task: song gets added to song storage
"""
def test_check_song_is_added_to_storage():
    spotifoo = Spotifoo()
    spotifoo.add_songs("song_1")
    result = spotifoo.list_songs() 
    assert result == ["song_1"]

"""
Given two songs
#Task: program returns the list of two songs
"""
def test_check_program_returns_list_of_songs():
    spotifoo = Spotifoo()
    spotifoo.add_songs("song_1")
    spotifoo.add_songs("song_2")
    assert spotifoo.list_songs() == ["song_1", "song_2"]

"""
Given an empty string
#Task: program returns an error message
"""
#def test_check_that_string_is_not_empty():
#    spotifoo = Spotifoo("")
#    assert result == "String cannot be empty!"