
from flask import Flask, render_template, request
 
import numpy as np
import os
 
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model



model =load_model("model/xceptionfinal_v4_1.h5")

 
 
def pred_cot_dieas(cott_plant):
  test_image = load_img(cott_plant, target_size = (224, 224))   
  test_image = img_to_array(test_image)/255 
  test_image = np.expand_dims(test_image, axis = 0) 
  result = model.predict(test_image)
  print('Raw result = ', result)
  pred = np.argmax(result , axis=1) 
 
  if pred == 0:
      return "Tomato_Bacterial_Spot", 'Tomato_Bacterial_Spot.html' 
  elif pred == 1:
      return 'Tomato_Early_Blight', 'Tomato_Early_Blight.html' 
  elif pred == 2:
      return 'Tomato_Late_Blight', 'Tomato_Late_Blight.html'
  elif pred == 3:
      return 'Tomato_Leaf_Mold', 'Tomato_Leaf_Mold.html'
  elif pred == 4:
      return 'Tomato_Septoria_Leaf', 'Tomato_Septoria_Leaf.html' 
  elif pred == 5:
      return 'Tomato_Spider_mites_Two-spotted_spider_mite', 'Tomato_Spider_mites_Two-spotted_spider_mite.html'
  elif pred == 6:
      return 'Tomato_Target_Spot', 'Tomato_Target_Spot.html'
  elif pred == 7:
      return 'Tomato_Tomato_Yellow_Leaf_Curl_Virust', 'Tomato_Tomato_Yellow_Leaf_Curl_Virus.html' 
  elif pred == 8:
      return 'Tomato_Tomato_mosaic_virus', 'Tomato_Tomato_mosaic_virus.html'
  elif pred == 9:
      return 'Tomato_healthy', 'Tomato_healthy.html'
     
  else:
    return "NO RESULT", 'index.html' 
 

     
 

app = Flask(__name__)
 

@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
     
  

@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] 
        filename = file.filename        
        print("Input shared = ", filename)
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)
        pred, output_page = pred_cot_dieas(cott_plant=file_path)      
        return render_template(output_page, pred_output = pred, user_image = file_path)
     

if __name__ == "__main__":
    app.run(threaded=False) 