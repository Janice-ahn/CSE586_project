export DATA_DIR=""

accelerate launch --mixed_precision="fp16" --multi_gpu train_text_to_image.py \
  --pretrained_model_name_or_path='runwayml/stable-diffusion-v1-5' \
  --train_data_dir=$DATA_DIR \
  --use_ema \
  --center_crop --random_flip \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --gradient_checkpointing \
  --max_train_steps=15000 \
  --learning_rate=1e-05 \
  --max_grad_norm=1 \
  --enable_xformers_memory_efficient_attention \
  --lr_scheduler="constant" --lr_warmup_steps=0 \
  --output_dir="our-model"