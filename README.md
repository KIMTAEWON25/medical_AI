# MRI Modality (t1ce, bb, others) Classification

This repository includes an MRI Modality Classification model that sorts MRI images into specific sequences: 

T1-weighted post-contrast (T1ce), Black Blood (BB), and other sequences. The model is designed to analyze scans across three different axial, sagittal, and coronal utilize the full spectrum of spatial information available in brain tissue imaging.


## **Model Architecture**

<p align="center">
    <img src="./model_Image.png" width="70%" height="70%">
</p>


The architecture is built on the DenseNet169 convolutional neural network framework, known for its dense connectivity pattern between layers which promotes feature reuse and reduces the number of parameters, making the network efficient and powerful for image classification tasks.
