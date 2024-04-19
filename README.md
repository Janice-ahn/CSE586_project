1. Before starting the test:
    - I followed this [LoRA Hugging Face instruction](https://huggingface.co/docs/diffusers/main/en/training/lora).
    - I recommend you to follow the link except cloning their GitHub repo; start with:
      ```bash
      cd diffusers
      pip install .
      ```
    - if something doesn't work about the code, please consider removing diffusers directory and start with cloning their repo.  


2. Dataset Format:
    1) What they used for their own example (Pokemon) was from [hugging face hub](https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions).
   - I have requested accessibility to their file to see the structure.
    2) Alternatively, we can refer to the file [`create_dataset.md`](link to the file) for using our dataset locally.