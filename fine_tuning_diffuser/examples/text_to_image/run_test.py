from PIL import Image
from diffusers import AutoPipelineForText2Image
import torch

def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size

    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

pipeline = AutoPipelineForText2Image.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16).to("cuda")
pipeline.load_lora_weights("./out_5", weight_name="pytorch_lora_weights.safetensors")


# Generating 50 images
num_cols = 1
num_rows = 1
prompt = ["A photograph of a farmer"] * num_cols

for j in range(10):
  all_images = []
  for i in range(num_rows):
    images = pipeline(prompt).images
    all_images.extend(images)

  grid = image_grid(all_images, rows=num_rows, cols=num_cols)
  file_path = './image_result2/' + 'farmer' + str(j) + '.png'
  grid.save(file_path)