# import openai
# from pygments import highlight
# from pygments.formatters import ImageFormatter
# from pygments.lexers import get_lexer_by_name
#
# code_snippet = "def my_function():\n    print('Hello, world!')"
# lexer = get_lexer_by_name("python")  # Specify language for highlighting
# formatter = ImageFormatter(font_name="Consolas", font_size=12, line_numbers=True)  # Customize
#
# img = highlight(code_snippet, lexer, formatter)
# with open("code_image.png", "wb") as f:
#     f.write(img)
library = "numpy"
import google.generativeai as genai
import ast
import os
# library = input("Which Library do ou want to understand")
genai.configure(api_key="AIzaSyArvzUuVG-TxNqeflFknBL1JlHfa5Y2Kww")

model = genai.GenerativeModel('gemini-1.5-pro-latest')
# response = model.generate_content(f'what are all the concepts of {library} documentation and library go in very detail with each and every concept just tell me the name of the concepts from beginner to advance level.MKae sure to cover each and every concept and topics')
# x = response.text
# print(x)

# message = x + "MAke this into a python dictionary make sure there are only three keys Beginner Concepts, Intermediate Concepts,Advanced Concepts and no variable assinged to the dictionary the keys should have the list as a response something like this
# "Beginner Concepts": [
#     "Creating arrays",
#     "Array indexing and slicing",
#     "Data types",
#     "Array shapes",
#     "Linear algebra operations (dot product, matrix multiplication)",
#     "Basic statistical operations (mean, median, standard deviation)",
#     "Array broadcasting",
#     "Fancy indexing",
#     "Universal functions (ufuncs)"
#   ],"
#
# responsee = model.generate_content(message)
# print(responsee.text)

# responsee = """```python
#  {
#     "Beginner Concepts": {
#         "NumPy Array Basics": [
#             "ndarray object, attributes, and creation routines",
#             "Array indexing and slicing",
#             "Array data types",
#             "Array broadcasting",
#             "Universal functions (ufuncs)"
#         ],
#         "Array Operations": [
#             "Arithmetic operations",
#             "Bitwise operations",
#             "Comparisons",
#             "Aggregate functions"
#         ],
#         "Linear Algebra": [
#             "Matrix operations",
#             "Solving linear equations and eigenvalue problems"
#         ]
#     },
#     "Intermediate Concepts": {
#         "Array Manipulation": [
#             "Reshaping and resizing arrays",
#             "Joining and splitting arrays",
#             "Array iteration"
#         ],
#         "Advanced Indexing and Selection": [
#             "Boolean indexing",
#             "Fancy indexing",
#             "Masking"
#         ],
#         "Random Number Generation": [
#             "Creating random numbers from various distributions",
#             "Setting random seeds"
#         ],
#         "Input/Output": [
#             "Loading and saving arrays",
#             "NumPy's binary format"
#         ]
#     },
#     "Advanced Concepts": {
#         "Broadcasting": [
#             "Broadcasting rules and limitations",
#             "Advanced usage"
#         ],
#         "Memory Management and Performance": [
#             "Memory-efficient techniques",
#             "Memory layout and data alignment",
#             "NumPy's C API"
#         ],
#         "Linear Algebra (Advanced)": [
#             "Decompositions and applications",
#             "Solving systems of linear equations",
#             "Eigenvalue problems"
#         ],
#         "Fourier Transforms and Signal Processing": [
#             "Performing Fourier transforms",
#             "Windowing and filtering"
#         ],
#         "Integration with Other Libraries": [
#             "SciPy, Pandas, Matplotlib integration",
#             "Machine learning and scientific computing"
#         ]
#     }
# }
# ``` """
# sample_string = responsee
# pattern = r"```python(.*?)```"
# print("we are here")
# import re
# # Using re.findall to find all matches of the pattern in the string
# matches = re.findall(pattern, sample_string, re.DOTALL)
#
# # Extracted code snippet
# if matches:
#     extracted_code = matches[0].strip()
#
#
#
#     data_dict = extracted_code
#     print(extracted_code)
#
# data_dict = ast.literal_eval(extracted_code)
data_dict = {
  "Beginner Concepts": [

    "Array indexing and slicing",
    "Data types",
    "Array shapes",
    "Linear algebra operations (dot product, matrix multiplication)",
    "Basic statistical operations (mean, median, standard deviation)",
    "Array broadcasting",
    "Fancy indexing",
    "Universal functions (ufuncs)"
  ],
  "Intermediate Concepts": [
    "Multidimensional arrays",
    "Array manipulation (reshaping, flattening, stacking)",
    "Linear algebra functions (linalg module)",
    "Random number generation",
    "File I/O with arrays",
    "Masked arrays",
    "Memory mapping",
    "Customizing NumPy printing"
  ],
  "Advanced Concepts": [
    "Broadcasting in detail",
    "Vectorization",
    "Performance optimization",
    "Interfacing with C/C++ libraries",
    "Fourier transforms",
    "Sparse matrices",
    "NumPy and threading",
    "Metaprogramming with NumPy"
  ]
}
print(data_dict["Beginner Concepts"])


listt = data_dict["Beginner Concepts"]
print(listt)
x = 1
library = "numpy"
current_dict = {}
# data_dict= {
#   "Beginner Concepts": [
#     {
#       "array": "Multidimensional data structures that store elements of the same data type."
#     },
#     {
#       "indexing and slicing": "Techniques for accessing and manipulating specific elements or subsets of an array using indices and slices."
#     },
#     {
#       "data types": "NumPy supports various data types for array elements, including numeric types (integers, floats), strings, and booleans."
#     },
#     {
#       "broadcasting": "Performing operations on arrays of different shapes by automatically conforming dimensions for element-wise calculations."
#     },
#     {
#       "universal functions (ufuncs)": "Operations that can be applied element-wise to entire arrays for efficient vectorized computations."
#     }
#   ]}
# listt = data_dict["Beginner Concepts"]
# if x == 1:
#     for n in listt:
#         current_topic = n
#
#         # Create a copy of the dictionary
#
#         response_under = """**Imagine arrays as the ultimate partygoers at the data science dance party.**
#
#             They're a group of like-minded individuals (all the same data type) who know how to have a good time. They can move in perfect synchronization, twisting and turning as one.
#
#             **Code Snippet: The Array Shuffle**
#
#             ```python
#             import numpy as np
#
#             # Create an array of partygoers (all of type 'int')
#             partygoers = np.array([1, 2, 3, 4, 5, 6])
#
#             # Shuffle the partygoers
#             np.random.shuffle(partygoers)
#
#             # Watch them dance!
#             print(partygoers)
#             ```
#
#             **Now, arrays can also be multidimensional, like that one friend who's always the life of the party in more than one way.**
#
#             Imagine a dance floor with multiple levels. Each level represents a different dimension. The first dimension is like the ground floor, the second dimension is the balcony, and so on.
#
#             **Code Snippet: The Multidimensional Dance Party**
#
#             ```python
#             # Create a 2D array (think of it as a dance floor with two levels)
#             dance_floor = np.array([[1, 2, 3], [4, 5, 6]])
#
#             # Get your groove on with the first dimension (the ground floor)
#             print(dance_floor[0])  # [1 2 3]
#
#             # Now, let's head to the balcony (the second dimension)
#             print(dance_floor[1])  # [4 5 6]
#             ```
#
#             **But arrays aren't just all about the party. They're also super efficient and powerful.**
#
#             Imagine you're trying to calculate the total number of guests at the party. An ordinary person would start counting one by one. But an array wizard? They'd just use a single command, "sum."
#
#             **Code Snippet: Party Population Calculator**
#
#             ```python
#             # Calculate the total number of partygoers
#             total_partygoers = np.sum(partygoers)
#
#             # Voila!
#             print(total_partygoers)
#             ```
#
#             **And arrays can even dance with other arrays, creating new and exciting formations.**
#
#             Imagine two arrays on the dance floor, one representing the X-coordinates and the other representing the Y-coordinates. When they come together, they create a beautiful symphony of movement.
#
#             **Code Snippet: Array Dance Party Extravaganza**
#
#             ```python
#             # Create an array of X-coordinates
#             x_coords = np.array([1, 2, 3])
#
#             # Create an array of Y-coordinates
#             y_coords = np.array([4, 5, 6])
#
#             # Let them dance!
#             combined_coords = np.concatenate((x_coords, y_coords))
#
#             # Show off their moves
#             print(combined_coords)
#             ```
#
#             **So, there you have it, arrays in all their hilarious and powerful glory.**
#
#             They're the ultimate partygoers, the dance floor masters, and the efficiency gurus of the data science world.
#
#             **Now go forth, embrace the array, and conquer the dance party of data science!**"""
#         # script = model.generate_content(
#         #     f' explain {current_topic} concept of {library} in a humorous and funny way also provide code snipits which covers this in detail make it as long as you want an mak the person advance in {current_topic} make it something like this {response_under}')
#         # response = script.text
#         # print(response)
#         responsed = """## Array Indexing and Slicing: The NumPy Dance Party Extravaganza
#
# **Picture this:** Arrays, those vibrant data structures, are the life of the NumPy dance party! They groove and shimmy in perfect unison, each element knowing its place on the dance floor. But how do they navigate this organized chaos? It's all thanks to the magic of indexing and slicing!
#
# **Indexing: The Dance Floor Coordinates**
#
# Imagine each element in the array has a unique ID card, like a VIP pass to the party. This ID is its **index**, a numerical label that pinpoints its exact location on the dance floor.
#
# *   **One-dimensional arrays:** Think of them as a conga line of partygoers. Each person has a number, starting from 0 for the leader. To find the third dancer, you'd simply call out "index 2!" (Remember, Python starts counting from 0, not 1. Don't be that person who messes up the count and breaks the flow!)
# *   **Multi-dimensional arrays:** Now we're talking about a dance floor with multiple levels, like a disco ball with a built-in balcony! Each element needs two coordinates: one for the level (the row) and one for their position within that level (the column). So, to find the dancer on the second level, third position, you'd say, "index (1, 2)!" (Again, starting from 0, because arrays are cool like that).
#
# **Code Snippet: Finding the Groove**
#
# ```python
# import numpy as np
#
# # A conga line of party animals
# party_line = np.array([10, 20, 30, 40, 50])
#
# # The third dancer shows their moves
# print(party_line[2])  # Outputs: 30
#
# # A multi-level dance floor
# disco_floor = np.array([[1, 2, 3], [4, 5, 6]])
#
# # The dancer on the second level, third position, strikes a pose
# print(disco_floor[1, 2])  # Outputs: 6
# ```
#
# **Slicing: Group Dance Moves**
#
# Sometimes, you want a whole crew to bust a move together. That's where slicing comes in! It's like calling out a section of the dance floor and having them perform a synchronized routine.
#
# *   **Basic slicing:** Imagine you want dancers 2 through 4 to do the limbo. You'd yell, "Indexes 2 to 4, get low!" In Python, it looks like this: `party_line[2:5]` (The last number is like a bouncer – it tells you where to stop, but doesn't join the party).
# *   **Fancy footwork:** Slicing can get even fancier! You can use steps to skip dancers (like every second person for a polka), or negative numbers to start from the back of the line (perfect for a moonwalk).
#
# **Code Snippet: Choreographing the Party**
#
# ```python
# # Limbo time!
# limbo_crew = party_line[2:5]  # [30, 40, 50]
#
# # Polka dot party!
# polka_dots = party_line[::2]  # [10, 30, 50]
#
# # Moonwalking backwards!
# moonwalkers = party_line[-2:]  # [40, 50]
# ```
#
# **Bonus Moves: Advanced Slicing and Fancy Indexing**
#
# For the true dance floor masters, there are even more advanced moves:
#
# *   **Slicing multi-dimensional arrays:** It's like calling out specific sections on each level of the dance floor. You can even grab diagonal lines of dancers with fancy tricks!
# *   **Boolean masks:** Imagine spotlighting dancers based on their outfit colors. Boolean masks let you select elements based on conditions, like "all the dancers wearing red."
#
# **With these moves in your repertoire, you'll be the king or queen of the NumPy dance floor, orchestrating data with grace and style! Now go forth and make those arrays boogie!** """
#         promt_1 = responsed + """ seperate this by sentences and give the response in a dictionary something like this(make sure to not use any variables):
#               1: sentence_1,
#               2: sentence_2,
#               3: sentence_3
#               do this for all the sentences present in the latter
#               make sure not to change the language or grammar of the sentences
#           }
#           """
#         print(promt_1)
#         sentence_maker = model.generate_content(promt_1
#             )
#         m = sentence_maker.text
#         pattern = r"```python(.*?)```"
#         print("we are here")
#         import re
#         # Using re.findall to find all matches of the pattern in the string
#         matches = re.findall(pattern,m , re.DOTALL)
#         extracted_code = ""
#         # Extracted code snippet
#         if matches:
#             extracted_code = matches[0].strip()
#
#
#
#             sentence_dict = extracted_code
#             print(extracted_code)
#
#         sentence_dict = ast.literal_eval(extracted_code)
#         print(sentence_dict)
# sentence_dict = {
# 1: "Arrays, those vibrant data structures, are the life of the NumPy dance party!",
# 2: "They groove and shimmy in perfect unison, each element knowing its place on the dance floor.",
# 3: "But how do they navigate this organized chaos?",
# 4: "It's all thanks to the magic of indexing and slicing!",
# 5: "Imagine each element in the array has a unique ID card, like a VIP pass to the party.",
# 6: "This ID is its index, a numerical label that pinpoints its exact location on the dance floor.",
# 7: "Think of them as a conga line of partygoers.",
# 8: "Each person has a number, starting from 0 for the leader.",
# 9: "To find the third dancer, you'd simply call out 'index 2!'",
# 10: "(Remember, Python starts counting from 0, not 1.",
# 11: "Don't be that person who messes up the count and breaks the flow!)",
# 12: "Now we're talking about a dance floor with multiple levels, like a disco ball with a built-in balcony!",
# 13: "Each element needs two coordinates: one for the level (the row) and one for their position within that level (the column).",
# 14: "So, to find the dancer on the second level, third position, you'd say, 'index (1, 2)!'",
# 15: "(Again, starting from 0, because arrays are cool like that).",
# 16: "Sometimes, you want a whole crew to bust a move together.",
# 17: "That's where slicing comes in!",
# 18: "It's like calling out a section of the dance floor and having them perform a synchronized routine.",
# 19: "Imagine you want dancers 2 through 4 to do the limbo.",
# 20: "You'd yell, 'Indexes 2 to 4, get low!'",
# 21: "In Python, it looks like this: `party_line[2:5]`",
# 22: "(The last number is like a bouncer – it tells you where to stop, but doesn't join the party).",
# 23: "Slicing can get even fancier!",
# 24: "You can use steps to skip dancers (like every second person for a polka), or negative numbers to start from the back of the line (perfect for a moonwalk).",
# 25: "For the true dance floor masters, there are even more advanced moves:",
# 26: "It's like calling out specific sections on each level of the dance floor.",
# 27: "You can even grab diagonal lines of dancers with fancy tricks!",
# 28: "Imagine spotlighting dancers based on their outfit colors.",
# 29: "Boolean masks let you select elements based on conditions, like 'all the dancers wearing red.'",
# 30: "With these moves in your repertoire, you'll be the king or queen of the NumPy dance floor, orchestrating data with grace and style!",
# 31: "Now go forth and make those arrays boogie!"
# }
# images = f"""
# In the Script, in ach sentence list which gif or image can be used (try to specicify in which part of the sentece)(try to cove each and every sentence where a gif or an image can be added):
# In the Use GIF , give the search query fr it try
# In the Use Image , explain the image
# Focus on using GIFs wherever possible
# {sentence_dict}
#
# ."""
#
#
#
#
# dict_ = model.generate_content(
#   f'{images} make  a python dictionary out of this witht these keys: "UseGIF" and "UseImage" in the value of these keys add another dict ith these keys:"explanation" and "query" make sure not to change the name of the kes from what i provided, you can make the search query, such that a gif can be found make sure to give response for each and every sentenc if it doent feel to use image or gif for a sentence in  sentnce number: "no"  make sure not to change the text')
# print(dict_.text)
# pattern = r"```python(.*?)```"
# print("we are here")
# import re
# # Using re.findall to find all matches of the pattern in the string
# matches = re.findall(pattern, dict_.text, re.DOTALL)
# extracted_code = dict_.text
# # Extracted code snippet
# if matches:
#     extracted_code = matches[0].strip()
#
#
#
#     resources = extracted_code
#     print(extracted_code)
#
# resources = ast.literal_eval(extracted_code)
# print(resources)


resources = {1: {'usegif': {'explanation': 'A GIF showing a vibrant dance party with people moving in unison.', 'query': 'vibrant dance party GIF'}}, 2: {'UseGIF': {'explanation': 'A GIF of a synchronized dance routine, like a chorus line or a group doing the electric slide.', 'query': 'synchronized dance routine GIF'}}, 3: {'UseGIF': {'explanation': 'A GIF of people looking confused or lost in a crowd.', 'query': 'confused in a crowd GIF'}}, 4: {'UseGIF': {'explanation': 'A magician pulling a rabbit out of a hat.', 'query': 'magic trick GIF'}}, 5: {'UseImage': {'explanation': 'An image of a VIP pass or a backstage pass with a unique ID number.'}}, 6: {'UseGIF': {'explanation': 'A person searching for someone in a crowd.', 'query': 'searching in a crowd GIF'}}, 7: {'UseGIF': {'explanation': 'A conga line of people dancing.', 'query': 'conga line GIF'}}, 8: {'UseImage': {'explanation': 'A numbered list, starting from 0.'}}, 9: {'UseGIF': {'explanation': 'Someone calling out a specific number in a line.', 'query': 'calling out a number GIF'}}, 10: {'UseImage': {'explanation': 'A number line starting from 0.'}}, 11: {'UseGIF': {'explanation': 'Someone messing up a dance move and causing a chain reaction.', 'query': 'messing up dance move GIF'}}, 12: {'UseImage': {'explanation': 'A disco ball with multiple levels or a building with a balcony.'}}, 13: {'UseImage': {'explanation': 'A grid with rows and columns labeled.'}}, 14: {'UseGIF': {'explanation': 'Someone pointing to a specific location on a grid.', 'query': 'pointing to location on grid GIF'}}, 15: {'UseImage': {'explanation': 'A number line starting from 0.'}}, 16: {'UseGIF': {'explanation': 'A group of people dancing together in a coordinated way.', 'query': 'group dance routine GIF'}}, 17: {'UseGIF': {'explanation': 'A spotlight shining on a specific section of a stage or dance floor.', 'query': 'spotlight on stage GIF'}}, 18: {'UseGIF': {'explanation': 'A synchronized swimming routine or a marching band performance.', 'query': 'synchronized swimming GIF'}}, 19: {'UseGIF': {'explanation': 'People doing the limbo dance.', 'query': 'limbo dance GIF'}}, 20: {'UseGIF': {'explanation': 'A person yelling into a megaphone.', 'query': 'yelling into megaphone GIF'}}, 21: {'UseImage': {'explanation': 'Code snippet showing the slicing syntax in Python.'}}, 22: {'UseGIF': {'explanation': 'A bouncer standing at the entrance of a club.', 'query': 'bouncer at club entrance GIF'}}, 23: {'UseGIF': {'explanation': 'A dancer doing fancy footwork or acrobatics.', 'query': 'fancy dance moves GIF'}}, 24: {'UseGIF': {'explanation': 'People doing the polka or the moonwalk.', 'query': 'polka or moonwalk GIF'}}, 25: {'UseGIF': {'explanation': 'A professional dancer performing a complex routine.', 'query': 'professional dancer GIF'}}, 26: {'UseImage': {'explanation': 'A grid with highlighted sections on different levels.'}}, 27: {'UseGIF': {'explanation': 'A spotlight moving diagonally across a stage.', 'query': 'diagonal spotlight GIF'}}, 28: {'UseImage': {'explanation': 'Dancers wearing different colored outfits.'}}, 29: {'UseGIF': {'explanation': 'A searchlight scanning a crowd and stopping on specific people.', 'query': 'searchlight scanning crowd GIF'}}, 30: {'UseGIF': {'explanation': 'A conductor leading an orchestra.', 'query': 'conductor leading orchestra GIF'}}, 31: {'UseGIF': {'explanation': 'A disco ball spinning and lights flashing.', 'query': 'disco ball and lights GIF'}}}
print(resources)
print()
print()
account_dictionary = {}
for keys, value in resources.items():
    check_var = value
    for use, query in value.items():
        if use.lower() == "usegif":
            search_query = query["query"]
            print(search_query)
            account_dictionary[keys] = "gif"

        elif use.lower() == "useimage":
            image_promt = query["explanation"]
            print(image_promt)
            account_dictionary[keys] = "image"

        else:
            print("no image or gif")
            account_dictionary[keys] = "no"

print(account_dictionary)


# Print the dictionary
# print(num_py_concepts)



