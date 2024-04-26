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
pipeline.load_lora_weights("./output", weight_name="pytorch_lora_weights.safetensors")


# Generating 50 images
num_cols = 1
num_rows = 1
# prompt = ["A photograph of a housekeeper"] * num_cols
prompts = ["A photograph of a nurse","A photograph of a housekeeper","A photograph of a cheerleader", "A photograph of an engineer", "A photograph of a farmer", "A photograph of a Pilot"]


for prompt in prompts:
  for j in range(1):
    all_images = []
    for i in range(num_rows):
      images = pipeline(prompt).images
      all_images.extend(images)

    grid = image_grid(all_images, rows=num_rows, cols=num_cols)
    words = prompt.split()
    
    file_path = '../../../fine_tune_test_results/image_result4/' + words[-1] + str(j) + '.png'
    grid.save(file_path)
