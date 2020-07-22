# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""
import requests
import math


def countdown(message, start, stop, completion_message):

    while start >= stop:
        print(message + " " + str(start))
        start = start - 1
    print(completion_message)


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    hypotenuse = ((height * height) + (base * base)) ** (1 / 2)
    return hypotenuse


def calculate_area(base, height):
    area = 1 / 2 * base * height
    return area


def calculate_perimeter(base, height):
    perimeter = ((height * height) + (base * base)) ** (1 / 2) + base + height
    return perimeter


def calculate_aspect(base, height):
    aspect = []
    if height > base:
        aspect = "tall"
    elif base > height:
        aspect = "wide"
    else:
        aspect = "equal"
    return aspect


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )
    if facts_dictionary["aspect"] == "tall":
        picture = tall.format(**facts_dictionary)
    elif facts_dictionary["aspect"] == "wide":
        picture = wide.format(**facts_dictionary)
    elif facts_dictionary["aspect"] == "equal":
        picture = equal.format(**facts_dictionary)
    facts = pattern.format(**facts_dictionary)
    return picture + "\n" + facts


def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    facts = get_triangle_facts(base, height)
    right = tell_me_about_this_right_triangle(facts)
    if return_diagram and return_dictionary:
        return {"diagram": right, "facts": facts}
    elif return_diagram:
        return right
    elif return_dictionary:
        return facts
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    pyramid = []
    Length = [3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4]
    pyramid.extend(list_of_words_with_lengths(Length))

    return pyramid


def get_a_word_of_length_n(length):
    import requests

    source = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={wordlength}"

    source_with_length = source.format(wordlength=length)
    Get_word = requests.get(source_with_length)

    if Get_word.status_code is 200:
        wordstring = str(Get_word.content)
        word_output = wordstring.split("'")
        output = word_output[1]
        return output


def list_of_words_with_lengths(list_of_lengths):
    import requests

    source = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={wordlength}"

    output = []

    for i in list_of_lengths:
        source_with_length = source.format(wordlength=i)
        Get_word = requests.get(source_with_length)

        if Get_word.status_code is 200:
            wordstring = str(Get_word.content)
            word_output = wordstring.split("'")
            output.append(word_output[1])
    return output


if __name__ == "__main__":
    # do_bunch_of_bad_things()
    countdown("We're about to start", 9, 1, "we finished, wheeeee!")
    triangle_master(3, 5)
    pyramid = wordy_pyramid()
    for word in pyramid:
        print(word)
