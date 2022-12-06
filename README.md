# Image-Captioning

## Description

Our problem is to convert an input image into a caption. We used the model developed by Mokady et al.
Please note that many of the code provided in this repo is their code and we just made some modifications to suit our project proposed solutions.

How to run:
Firstly, clone the repo, create a conda environment and activate it.
```
git clone https://github.com/OmarMoheyeldinMohamed/Image-Captioning
conda env create -f environment.yml
conda activate image_captioning
```
Download [training images](http://images.cocodataset.org/zips/train2014.zip) and [validation images](http://images.cocodataset.org/zips/val2014.zip) , unzip the folders and add them to the directory /data/coco.

Now we perform data augmentation on the training and validation datasets. First create two folders named val2014(1) and train2014(1) and make sure they are empty then run the following command
```
python change_input.py
```
After the code finishes running you can now remove the two folders train2014 and val2014 and rename the folders train2014(1) and val2014(1) to train2014 and val2014. Then start parsing the input images and run the following command replacing <model_type> with the type for the model you want to train we suggest RN50 which gave us the best results
```
python parse_coco.py --clip_model_type <model_type>
```
Now start training and modify the name for the data file according to the model type you chose
```
python train.py --only_prefix --data ./data/coco/oscar_split_RN50_train.pkl --out_dir ./coco_train/ --mapping_type transformer  --num_layers 8 --prefix_length 40 --prefix_length_clip 40 --is_rn
```
Now run the following commands to get the ground truth values and predictions and save them to files. Note the getting_model_predictions program will ask for the model weights path by default after training this will be ./coco_train/coco_latest_prefix.pt
```
python making_list.py
python getting_model_predictions.py 
```
Finally, run the follwing commant to use the saved files and evaluate the model.
```
python evaluation.py 
```

Finally, if you want to use the model to get predictions for single images run this [google colab](https://colab.research.google.com/drive/1lOXEAHm2ewPWZONICc2GGo4ozoiDizPm?usp=sharing) notebook. To run it you will need the final model weights to be uploaded on your drive in the folder "My Drive/CLIP". You can use any of our model weights by downloading this [folder](https://drive.google.com/drive/folders/1Cg6I2ncj8MoNEZi0Z79fduFVQrcYdiX5?usp=sharing).
