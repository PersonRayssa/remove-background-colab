!pip install rembg pillow

#upload da imagem com Google Colab
from google.colab import files
uploaded = files.upload()

from rembg import remove
from PIL import Image

input_img = next(iter(uploaded.keys()))
output_img = "fundo removido.png"
input = Image.open(input_img)
output = remove(input)
output.save(output_img)

#download da imagem sem fundo
from google.colab import files
files.download(output_img)