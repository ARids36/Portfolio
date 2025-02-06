project_info = [
    {"ID": "portfolio",
     "Title": "This Website!",
     "Info": "Created with Python and HTML, utilising Flask, Jinjer and Gunicorn. Based on an HTML5UP template.",
     "Icon": "icon fa-file-code"
     },

    {"ID": "text-to-morse",
     "Title": "Morse Code Converter",
     "Info": "A simple text-to-code GUI utilising Tkinter",
     "Icon": "icon fa-file-code"
     },

    {"ID": "noughts-and-crosses",
     "Title": "Noughts and Crosses",
     "Info": "A terminal based noughts and crosses game against an AI opponent",
     "Icon": "icon fa-file-code"
     },

]

project_main = {
    "text-to-morse": {
        "Heading": "Text-To-Morse",
        "Title": "A simple GUI to convert a text string into morse code",
        "Subtitle": "",
        "Body_1": "This converter was originally intended to run in the command line, "
                  "but I added a Tkinter GUI for a more complete feel. This made re-running "
                  "of the programme easier and a improved the user experience. Exception handling "
                  "was added to catch any errors made by the user.",
        "Body_2": "The option to convert a morse code signal back into a text string was then added "
                  "along with the ability to copy a morse code signal directly to the clipboard.",
        "Link": "https://github.com/ARids36/text-to-morse",
        "Stats": "Created using Python.\n"
                 "Utilises Tkinter, exception handling and lambda functions",
        "Image_1": "/static/images/text_to_morse_1.jpg",
        "Image_2": "/static/images/text_to_morse_2.jpg",
        "Image_3": "",
    },

    "portfolio": {
        "Heading": "This Website",
        "Title": "This portfolio was created using Python Flask, rendering a CSS styled HTML site",
        "Subtitle": "",
        "Body_1": "This site has been created using Python Flask, along with the Jinja templating "
                  "engine to render the project pages. The Gunicorn WSGI was used to deploy the site. The project "
                  "information is stored in a series of lists and dictionaries, used to populate the project.html "
                  "template to allow easier updates of the site once new projects are completed.",
        "Body_2": "An HTML5UP template was used as the starting point for the site, with the HTML and CSS edited "
                  "to create the current layout.",
        "Link": "",
        "Stats": "Created using Python, HTML and CSS.\n"
                 "Utilises the Flask, Jinja and Gunicorn frameworks, with HTML templating",
        "Image_1": "/static/images/portfolio_1.jpg",
        "Image_2": "/static/images/portfolio_2.jpg",
        "Image_3": "",
    },

    "noughts-and-crosses": {
            "Heading": "Noughts and Crosses",
            "Title": "A terminal based noughts and crosses game against an AI opponent",
            "Subtitle": "",
            "Body_1": "This game went through several iterations, trying to find the best way of tracking and "
                      "managing the board. This included using numpy arrays and object oriented programming, "
                      "before determining a simple list was sufficient. The game mechanics involve looping through "
                      "lists of possible plays and combinations, and list comprehension to determine available "
                      "moves and winning plays.",
            "Body_2": "The AI was improved in the second iteration. The first involved a system that simply checked "
                      "for winning combinations to either play or block, and made a random move in any other case. "
                      "In the upgraded version this was swapped for a system where the AI would rank all possible "
                      "squares based on the offensive and defensive advantages they gave, choosing the highest rank "
                      "square to play (randomly if squares were tied). This also streamlined the code into a "
                      "comprehensive nested loop",
            "Link": "https://github.com/ARids36/Noughts_and_crosses",
            "Stats": "Created using Python.\n"
                     "Includes an AI opponent, list comprehension and exception handling",
            "Image_1": "/static/images/noughts_and_crosses_2.png",
            "Image_2": "/static/images/noughts_and_crosses_1.png",
            "Image_3": "",
        },

}
