"""
Created Date: 12/02/2023
Last Update: 03/11/2024
Description: Creating images using de API from OpenAI for images
Observation: Using a API key and a connection with OpenAI to create images using generative AI
"""
# YOU HAVE TO INSTALL IT FIRST: pip install openai
import openai

openai.api_key = 'YOUR API KEY FROM OPENAI HERE'
#
# Creation of a image from scratch 
#
reponse = openai.Image.create (
    prompt='a dog programming', # What you want to create
    n=1,                        # Number of images you want to generate
    size='1024x1024'            # Size of the image(s)
)

image_url_create = reponse['data'][0]['url']

print(f'URL of the generated image: {image_url_create}')
# 
# Manipulation of a existing image
# 
response = openai.Image.create_edit(
    image=open("image.png", "rb"),            # The image you want to manipulate
    mask=open("image_masked.png", "rb"),      # The new name of the image
    prompt="A red colour car in the garden",  # What you want to create in the original image
    n=1,                                      # Number of images you want to generate
    size="1024x1024"                          # Size of the image(s)
)

image_url_modified = response['data'][0]['url']

print(f'URL of the modified image: {image_url_modified}')