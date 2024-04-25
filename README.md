# Introduction
This is my submission for the *Use a Pre-trained Image Classifier to Identify Dog Breeds* project as part of the Udacity nanodegree [AI Programming with Python](https://learn.udacity.com/nanodegrees/nd089).  The point of this project was to complete the missing implementation and to demonstrate familiarity with PyTorch.

I have left the provided file structure unchanged for ease of review.  It seems that there may be an updated version of this project available (MIT License):

https://github.com/udacity/AIPND-revision

# Setup
Instructions for setting up and running locally using `pyenv`.

```
pyenv install 3.11.7
pyenv virtualenv 3.11.7 udacity-dog-classifier
pyenv local udacity-dog-classifier
python3 -m pip install --upgrade pip

git clone git@github.com:mrperkett/udacity-project-dog-breed-classifier.git
cd udacity-project-dog-breed-classifier/
python3 -m pip install -r requirements.txt
```

# Running
```
cd intropyproject-classify-pet-images

# running on 40 provided images
python3 ./check_images.py --dir pet_images --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt
python3 ./check_images.py --dir pet_images --arch resnet --dogfile dognames.txt > resnet_pet-images.txt
python3 ./check_images.py --dir pet_images --arch vgg --dogfile dognames.txt > vgg_pet-images.txt

# running on uploaded images
python3 ./check_images.py --dir uploaded_images --arch alexnet --dogfile dognames.txt > alexnet_uploaded-images.txt
python3 ./check_images.py --dir uploaded_images --arch resnet --dogfile dognames.txt > resnet_uploaded-images.txt
python3 ./check_images.py --dir uploaded_images --arch vgg --dogfile dognames.txt > vgg_uploaded-images.txt
```

# Results
## Classifying provided pet images
Running `check_images.py` on the 40 provided pet images using each of the three model architectures (AlexNet, RESNET, VGG16), yields the results in the table below.


| |AlexNet	|RESNET	|VGG16|
|-|---------|-------|-----|
|Num images	|40	|40	|40|
|Num dog images	|30	|30	|30|
|Num not dog images	|10	|10	|10|
|Num correctly labeled dog / not dog	|40	|39	|40|
|Num correctly labeled not dog	|10 (100%)	|9 (90%)	|10 (100%)|
|Num correctly labeled dog	|30 (100%)	|30 (100%)	|30 (100%)|
|Num correctly labeled dogs with the correct breed	|24 (80%)	|27 (90%)	|28 (93.3%)|
|Num exactly matching labels	|30 (75.0%)	|33 (82.5%)	|35 (87.5%)|

## Classifying uploaded images
The exercise also asked that you upload four images: a dog, the same dog horizontally flipped, a non-dog animal, and an object.  I have included the results in [uploaded_images_classification_summary.pdf](intropyproject-classify-pet-images/uploaded_images_classification_summary.pdf).