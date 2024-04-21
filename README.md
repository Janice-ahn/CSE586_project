1. Before starting the test:
    - We referenced [LoRA Hugging Face instruction](https://huggingface.co/docs/diffusers/main/en/training/lora).
    - Start with following command
      ```bash
        cd fine_tuning_diffuser
        pip install .
      ```
    - Navigate to the example folder with the training script and install the required dependencies for the script you’re using:
      ```bash
        cd examples/text_to_image
        pip install -r requirements.txt
      ```
    - Initialize an 🤗 Accelerate environment:
      ```bash
        accelerate config
      ```
    - To setup a default 🤗 Accelerate environment without choosing any configurations:
      ```bash
        accelerate config default
      ```

3. Processed Dataset:
    - Please refer to our shared [Google Drive Folder](https://drive.google.com/drive/u/1/folders/1yvBElWT5xer9HNJ1Ar-nam3LP3Px2FwE)
    - Download and unzip it in your codespace
    - Lora doesn't require huge amount of training datasets. Therefore, we sampled 30 images for each labels, including 15 of Male & 15 of Female.
    - Our Sampled dataset is located in `/fine_tuning_diffuser/examples/text_to_image/sampled30pics`

4. Shell Script and Fine-Tune the model
    - Please open the `run.sh` in `fine_tuning_diffuser/examples/text_to_image`. 
    - Specify your dataset directory in the 1st line `export` command.
    - run `run.sh` as follows:
      ```bash
        run.sh
      ```

5. Test
    - open the `run_test.py` in `fine_tuning_diffuser/examples/text_to_image`. 
    - Specify your model directory in line 17
      ```bash
        pipeline.load_lora_weights("/path/to/your/fine-tuned/model", weight_name="pytorch_lora_weights.safetensors")
      ```
    - Specify your prompt in line 23. Here is the example
      ```bash
        prompt = ["a photograph of a nurse"] * num_cols
      ```
    - Specify your output image file name and output folder name in line 32. Here is the example
      ```bash
        file_path = './image_result/' + 'nurse' + str(j) + '.png'
