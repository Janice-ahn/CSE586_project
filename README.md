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