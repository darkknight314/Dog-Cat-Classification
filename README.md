# Dog-Cat-Classification
Our experiments with creating a Deep Learning Classifier
# Model 1 : Resnet18 with Linear layer applied on top
Description : We applied a dense layer on the output layer of the pretrained Resnet18 mapping to 2 output neurons.  We used Cross Entropy Loss along with Adam optimizer with a learning rate of 1e-5. After training for 10 epochs, the model achieved an accuracy of ~97.9% on a test set having a baseline accuracy of 67%(determined by the Zero Rule)


