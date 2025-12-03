# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Spotifoo:
    # User-facing properties:
    #   name: string, track name

    def __init__(self):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def add_songs(self, track_name):
        # Parameters:
        #   task: string representing a single music track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the song to the self object
        pass # No code here yet

    def list_songs(self)
        # Parameters: None
        # Returns: the complete list of songs
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a new song
#Task: check that the list is empty to begin with
"""
test_check_list_is_empty():
    spotifoo = Spotifoo([])
    asser spotifoo.list_songs == []
    
"""
Given a new song
#Task: song gets added to song storage
"""
test_check_song_is_added_to_storage():
    spotifoo = Spotifoo("song_1")
    assert spotifoo.add_songs == ["song_1"]

"""
Given a new song
#Task: program returns the complete list of songs
"""
test_check_program_returns_list_of_songs():
    spotifoo = Spotifoo(["song_1", "song_2"])
    assert spotifoo.list_songs == ["song_1", "song_2"]

"""
Given an empty string
#Task: program returns an error message
"""
test_check_that_string_is_not_empty():
    spotifoo = Spotifoo("")
    assert result == "String cannot be empty!"


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
