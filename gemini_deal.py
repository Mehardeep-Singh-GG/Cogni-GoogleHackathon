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
#
import google.generativeai as genai
import ast
import os
# library = input("Which Library do ou want to understand")
genai.configure(api_key="AIzaSyArvzUuVG-TxNqeflFknBL1JlHfa5Y2Kww")

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(f'what are all the concepts of {library} documentation and library go in very detail with each and every concept just tell me the name of the concepts from beginner to advance level.MKae sure to cover each and every concept and topics')
x = response.text
# print(x)
#
# message = x + "MAke this into a python dictionary make sure there are only three keys Beginner Concepts, Intermediate Concepts,Advanced Concepts"
# messages = [ {"role": "system", "content": "You covert prompts into dictionaries"} ]
#
# api_key = "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"
# openai.my_api_key = api_key
# if message:
#     messages.append(
#         {"role": "user", "content": message},
#     )
#     chat = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo", messages=messages
#     )
#
# sample_string = chat.choices[0].message.content
# print(sample_string)
# pattern = r"```python(.*?)```"
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

data_dict= {
  "Beginner Concepts": [
    {
      "array": "Multidimensional data structures that store elements of the same data type."
    },
    {
      "indexing and slicing": "Techniques for accessing and manipulating specific elements or subsets of an array using indices and slices."
    },
    {
      "data types": "NumPy supports various data types for array elements, including numeric types (integers, floats), strings, and booleans."
    },
    {
      "broadcasting": "Performing operations on arrays of different shapes by automatically conforming dimensions for element-wise calculations."
    },
    {
      "universal functions (ufuncs)": "Operations that can be applied element-wise to entire arrays for efficient vectorized computations."
    }
  ],
  "Intermediate Concepts": [
    {
      "linear algebra operations": "Matrix operations like multiplication, inversion, solving linear systems, along with finding eigenvalues and eigenvectors."
    },
    {
      "random number generation": "Generating random numbers from various statistical distributions like uniform, normal, or binomial."
    },
    {
      "masking and filtering": "Selecting and manipulating elements based on conditions using boolean masks to create filtered sub-arrays."
    },
    {
      "aggregation functions": "Functions like `sum`, `mean`, `max`, and `min` that operate on entire arrays or specific axes to get summary statistics."
    },
    {
      "file input/output": "Reading and writing NumPy arrays to and from various file formats like text files (CSV) for data persistence."
    }
  ],
  "Advanced Concepts": [
    {
      "numpy arrays as function arguments": "Passing NumPy arrays as arguments to user-defined functions for efficient processing of numerical data."
    },
    {
      "vectorization": "Optimizing code by replacing loops with vectorized operations that leverage NumPy's capabilities for element-wise calculations."
    },
    {
      "custom ufuncs": "Creating user-defined functions that can be applied element-wise to arrays, extending NumPy's functionality."
    },
    {
      "n-dimensional arrays": "Working with arrays that have more than two dimensions, enabling complex data structures for scientific computing."
    },
    {
      "advanced indexing": "Indexing arrays using boolean masks or integer arrays for more sophisticated element selection and manipulation."
    }
  ],
  "Additional Info": {
    "library modules": "NumPy provides various submodules for specific functionalities:",
    "linear_algebra": "Module for matrix operations, linear equations, and eigenvalues (linalg)",
    "random_number_generation": "Module for generating random numbers (random)",
    "file_input_output": "Modules for reading/writing data (genfromtxt, savetxt)",
    "image_processing": "Module for image manipulation (image)",
    "fourier_transforms": "Module for fast Fourier transforms (fft)",
    "other_modules": "Additional modules include constants, polynomial operations (polynomial), meshgrid creation, version information, and access to module documentation and source files."
  }
}

listt = data_dict["Beginner Concepts"]
print(listt)
x = 1
library = "numpy"
current_dict = {}
for n in listt:
    data = n

    # Create a copy of the dictionary
    data_copy = data.copy()

    # Retrieve any key-value pair
    key, value = data_copy.popitem()
    print(key)

    response = model.generate_content(
        f' explain {n} concept of {library} in a humorous and funny way also provide code snipits which covers this in detail make it as long as you want an mak the person advance in {key} ')
    print(response.text)
    print(x)
    images = f"""
    In the Script, in ach sentence list which gif or image can be used (try to specicify in which part of the sentece)(try to cove each and every sentence where a gif or an image can be added):
    In the Use GIF , give the search query fr it try to amke this in a python dictionary
    In the Use Image , explain the image
    Focus on using GIFs wherever possible
    {response.text}

    ."""
    response = model.generate_content(
      f'{images}')
    print(response.text)
    # text_1 = response.text
    current_dict[key] = {"text": ""}

# num_py_concepts = ast.literal_eval(python_code)

# Print the dictionary
# print(num_py_concepts)



