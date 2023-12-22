import os
import cv2

import webcamgpt

connector = webcamgpt.OpanAIConnector()

# export OPENAI_API_KEY=""

# import the opencv library 
import cv2 
  
vid = cv2.VideoCapture(0)
  
while(True): 
    ret, frame = vid.read() 
  
    cv2.imshow('frame', frame) 
      
    k = cv2.waitKey(1)
    if k == ord('q'): 
        break

    if k == ord('s'):
        prompt = input('Write your prompt:\n')
        print('Your prompt was: ', prompt)
        response = connector.simple_prompt(image=frame, prompt=prompt)
        print('Response:')
        print(response)
        # TODO how to keep prompting in same context?
        # TODO save image and show elsewhere or? 
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
