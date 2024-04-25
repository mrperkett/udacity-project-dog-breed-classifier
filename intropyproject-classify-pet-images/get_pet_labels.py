#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
import os.path

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = dict()
    file_names = listdir(image_dir)
    file_names.sort()
    for file_name in file_names:
        # skip any files starting with "."
        if file_name.startswith("."):
            continue

        # strip the extension from file_name and split on "_"
        base_name, _ = os.path.splitext(file_name)
        split_name = base_name.split("_")
        
        # check for format violations
        if len(split_name) < 2:
            raise AssertionError(f"file_name ({file_name}) has a different format than expected.  It does not split into 2+ values.")
        if not split_name[-1].isdigit():
            raise AssertionError(f"file_name ({file_name}) has a different format than expected. The last split element isn't composed of only digits")

        # create the pet label from the split name (only the last item should be ignored)
        #   - strip white space
        #   - set to lowercase
        #   - delimit multiple words with a space
        pet_label = " ".join([val.strip().lower() for val in split_name[:-1]])

        # add to dictionary
        if file_name in results_dic:
            raise AssertionError(f"Logic error: file_name ({file_name}) is repeated")
        results_dic[file_name] = [pet_label]

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
