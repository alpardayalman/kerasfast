import streamlit as st
from PIL import Image
from tensorflow.keras import models
import os
import numpy as np

model = models.load_model("baseline.keras")

class Recognition:

    def __init__(self, class_names, model=model):
        self.model = model
        self.class_names = class_names

    def format_image(self):
         self.image = self.image.convert("RGB")
         self.image = self.image.resize((32, 32))

    def predict_image(self, image):
            self.format_image()
            data = np.asarray(self.image) # image normalization
            data = data / 255
        
            probs = self.model.predict(np.array([data])[:1])
            print(probs)
            best_prob = probs.max()
            best_pred = np.argmax(probs)
            st.markdown('<style> .big-text { font-size: 24px; color: #FFD700; text-shadow: 2px 2px 4px #000000;}</style><p class="big-text">'+ self.class_names[best_pred] +"</p>", unsafe_allow_html=True)

            st.progress(round(best_prob*100))
            st.write(f"{best_prob*100:0.2f}")

    def run(self):
        st.title("Detektif v0.1")
        st.write("Streamlit sayfasına hoş geldiniz")
        st.write('Ucak Otomobil Kuş Kedi Geyik Köpek Kurbağa At Gemi Kamyon resmi kullanınız :)')
        uploaded_file = st.file_uploader("Bir resim secin...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            self.image = Image.open(uploaded_file)
            st.image(self.image, caption="Uploaded Image", use_column_width=True)
        # Save the uploaded image locally
            self.predict_image(image=self.image)
    
    


def main():
    class_names = {
    0: 'Ucak',
    1: 'Otomobil',
    2: 'Kuş',
    3: 'Kedi',
    4: 'Geyik',
    5: 'Köpek',
    6: 'Kurbağa',
    7: 'At',
    8: 'Gemi',
    9: 'Kamyon',
    }

    Recognition(class_names=class_names, model=model).run()


if __name__ == "__main__":
    main()
