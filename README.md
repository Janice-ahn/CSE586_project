1. Before starting the test:
    - I followed this [LoRA Hugging Face instruction](https://huggingface.co/docs/diffusers/main/en/training/lora).
    - I recommend you to follow the link including cloning their GitHub repo; starts with:
      ```bash
        git clone https://github.com/huggingface/diffusers
        cd diffusers
        pip install .
      ```


2. Dataset Format:
    1) What they used for their own example (Pokemon) was from [hugging face hub](https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions).
   - I have requested accessibility to their file to see the structure.
    2) Alternatively, we can refer to the file [`create_dataset.md`](link to the file) for using our dataset locally. That file is in 'diffusers/docs/source/en/training/'
  

3. Processed Dataset:
    - Please refer to our shared [Google Drive Folder](https://drive.google.com/drive/u/1/folders/1yvBElWT5xer9HNJ1Ar-nam3LP3Px2FwE)
    - Download and unzip it in your codespace
  

4. Shell Script
    - Please paste the `run.sh` to `diffusers/examples/text_to_image`. Specify your dataset directory in the 1st line `export` command.
