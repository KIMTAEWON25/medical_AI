# MRI Modality (t1ce, bb, others) Classification

This repository includes an MRI Modality Classification model that sorts MRI images into specific sequences: 

T1-weighted post-contrast (T1ce), Black Blood (BB), and other sequences. The model is designed to analyze scans across three different axial, sagittal, and coronal utilize the full spectrum of spatial information available in brain tissue imaging.


## **Model Architecture**

<p align="center">
    <img src="./model_Image.png" width="70%" height="70%">
</p>


The architecture is built on the DenseNet169 convolutional neural network framework, known for its dense connectivity pattern between layers which promotes feature reuse and reduces the number of parameters, making the network efficient and powerful for image classification tasks.

### **Data** 
The learning data consists of AMC(AsanMedicalCenter) 272, Snubh(Seoul National University Bundang Hospital) 543 patient data.

### **Input** 
MRI Images: The input to the model includes MRI scans in axial, sagittal, and coronal planes, providing a comprehensive view of the brain's anatom


### **Preprocessing** 
* Resize: All images are resized to 126x126 pixels to maintain uniformity across the dataset.
* Histogram Equalization (Equalize_hist): This step enhances the image contrast, allowing for better feature detection by the model.
* Normalization (Minimax): Pixel values are scaled to a standard range to improve model sensitivity and training efficiency.

### **Regularization**
* Dropout (0.5): A dropout rate of 50% during training helps in preventing overfitting and encourages the development of a more robust model.

## **How can we use ?**
- The example code below applies to almost all modules.
