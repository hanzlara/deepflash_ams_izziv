import SimpleITK as sitk
import glob

DATA_IN = "./imagesTr/*.nii"

data_len = len(list(glob.glob(DATA_IN)))
print(f"loading {data_len} files")

for i, filename in enumerate(glob.glob(DATA_IN)):
  img = sitk.ReadImage(filename)
  newname = "./imagesOutTr"+"".join(filename.split(".")[:-1])+".mhd"
  print(newname)
  sitk.WriteImage(img, newname)
  print(i, "/", data_len)


