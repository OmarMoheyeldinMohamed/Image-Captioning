import clip
import os
from torch import nn
import numpy as np
import torch
import torch.nn.functional as nnf
import sys
from typing import Tuple, List, Union, Optional
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AdamW, get_linear_schedule_with_warmup
from tqdm import tqdm, trange
import skimage.io as io
import PIL.Image
from enum import Enum
import copy
import json

cwd = os.getcwd()

with open('./data/coco/annotations/train_caption.json', 'r') as f:
        data = json.load(f)
val_dir = "/val2014/"
print("%0d captions loaded from json " % len(data))
all_captions = []
count = 0
files = set()

evaluation_dataset = {}
for i in tqdm(range(len(data))):
  d = data[i]
  img_id = d["image_id"]
  
  for j in range(5):
    if (j == 0):
      filename = f"COCO_val2014_{int(img_id):012d}.jpg"
    elif j == 1:
      filename = f"COCO_val2014_{int(img_id):012d}_bright.jpg"
    elif j == 2:
      filename = f"COCO_val2014_{int(img_id):012d}_dark.jpg"
    elif j == 3:
      filename = f"COCO_val2014_{int(img_id):012d}_rotated1.jpg"
    else:
      filename = f"COCO_val2014_{int(img_id):012d}_rotated2.jpg"
    
    
    
    check = os.path.isfile("./data/coco/val2014/"+filename)
    if not check:
      skip = True
      continue
    row = d['caption']
    if filename not in evaluation_dataset:
      evaluation_dataset[filename] = [row]
    else:
      evaluation_dataset[filename].append(row)
    
  if skip:
    skip = False
    continue




# write evaluation_dataset to file
with open('evaluation_dataset.json', 'w') as f:
    json.dump(evaluation_dataset, f)


  



#read evaluation_dataset from file
# with open('evaluation_dataset.json', 'r') as f:
#         evaluation_dataset = json.load(f)

