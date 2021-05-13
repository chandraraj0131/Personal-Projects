# Personal-Projects
No rules here, can be completely self-serving, or maybe involve others. Can also seemingly have no purpose or be completely unrelated to job or hobbies.



## Identif the Digits - MNIST 
7 models. Starting with a basic model and progressing to more deeper models.
Did not consider filtering out the models which failed to give best result as a depiction of the learning process, this being my first CNN project.
First 2 models are rather shallow and don't capture the intricacies of the image well Next is a deeper model with BatchNormalisation and Dropout. Using transferlearning, LeNet50 and ResNet50 (with imagenet weights) models are implemented taking on-the-fly augmented data, some training only selected layers at the end of the model.
Lastly, a deep CNN model taking in augmented data and working with decaying learning rate which gave the best result.
The epochs for few models are very low as they were not the best performing models. Hence their graphs do not really do justice to the actual performance due to less plotting points.
To skip to the best performing model jump to Cell 44.
