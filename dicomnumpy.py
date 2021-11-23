'''
!pip install dicom2nifti
!pip install SimpleITK
'''

import numpy as np
import nibabel as nib
import os 
import sys
import glob
import dicom2nifti
import SimpleITK as sitk

data_path = '/location'
files_list = os.listdir(data_path)

files_list

for case in range(len(files_list)):
  img_bb = os.path.join(data_path,files_list[case],'T1BB')
  img_ce = os.path.join(data_path,files_list[case],'T1CE')
  #directory
  directory_bb_np = os.path.join(data_path,files_list[case],'T1BB_npy')
  directory_ce_np = os.path.join(data_path,files_list[case],'T1CE_npy')
  if not os.path.exists(directory_bb_np):
      os.makedirs(directory_bb_np)
  if not os.path.exists(directory_ce_np):
      os.makedirs(directory_ce_np)
  img_bb_list = os.listdir(img_bb)
  img_ce_list = os.listdir(img_ce)
  img_bb_list = [file for file in img_bb_list if file.endswith(".dcm")]
  img_ce_list = [file for file in img_ce_list if file.endswith(".dcm")]
  if not os.path.isfile(directory_ce_np+'/a0150.npy'):
    for dicom in range(len(img_bb_list)):
        print(dicom,img_bb_list[dicom])
        bb_dicom = os.path.join(img_bb,img_bb_list[dicom])
        ce_dicom = os.path.join(img_ce,img_ce_list[dicom])
        print(bb_dicom,dicom,img_bb_list[dicom])
        bb = sitk.ReadImage(bb_dicom)
        ce = sitk.ReadImage(ce_dicom)
        bb_np = np.save(os.path.join(directory_bb_np,img_bb_list[dicom].replace('.dcm','')),sitk.GetArrayFromImage(bb))
        ce_np = np.save(os.path.join(directory_ce_np,img_ce_list[dicom].replace('.dcm','')),sitk.GetArrayFromImage(ce))
