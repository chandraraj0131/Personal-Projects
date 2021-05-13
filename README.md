# Personal-Projects
No rules here, can be completely self-serving, or maybe involve others. Can also seemingly have no purpose or be completely unrelated to job or hobbies.

## Horse Colic 
The dataset has 23 features and has a good mix of categorical and continuous features. It has a large number of features and instances with missing values, therefore understanding methods to replace these missing values and using it in modeling is made more practical in this treatment. Huge fraction of missing data (30%) is in fact a notable feature of this dataset. The data consists of attributes that are continuous, as well as categorical in type. Also, the presence of self-predictors makes working with this dataset instructive from a practical standpoint.


## Identif the Digits - MNIST 
7 models. Starting with a basic model and progressing to more deeper models.
Did not consider filtering out the models which failed to give best result as a depiction of the learning process, this being my first CNN project.
First 2 models are rather shallow and don't capture the intricacies of the image well Next is a deeper model with BatchNormalisation and Dropout. Using transferlearning, LeNet50 and ResNet50 (with imagenet weights) models are implemented taking on-the-fly augmented data, some training only selected layers at the end of the model.
Lastly, a deep CNN model taking in augmented data and working with decaying learning rate which gave the best result.
The epochs for few models are very low as they were not the best performing models. Hence their graphs do not really do justice to the actual performance due to less plotting points.
To skip to the best performing model jump to Cell 44.


## Iris Species 
OneVsAll Logistic Regeression model implemented solely by Numpy and Pandas.
Aim for this project was to implement vectorized Cost Function and Gradient descent and make a OneVsAll Logistic Regeression model (3 categories) without the use of any libraries but Numpy and Pandas. I have used the Scipy library to use its fmincg funtion which returns the values of theta by optimizing the Cost funtion.
