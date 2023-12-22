import numpy as np
import cv2

import webcamgpt

connector = webcamgpt.OpanAIConnector()

# Load an color image in grayscale
frame = cv2.imread('/home/ben/Pictures/xray_arm.png', 0)

# Show the image
cv2.imshow('image', frame)
cv2.waitKey(0)

connector = webcamgpt.OpanAIConnector()

prompt = input('Write your prompt:\n')
print('Your prompt was: ', prompt)
response = connector.simple_prompt(image=frame, prompt=prompt)
print('Response:')
print(response)

import pdb;pdb.set_trace()