import pandas as pd
import scipy.io
import glob
import os
import tqdm
import shutil
import torchvision
import PIL

ds_train=torchvision.datasets.STL10(root='./', split='train', download=True)
image_id=['']*ds_train.data.shape[0]
label=[999]*ds_train.data.shape[0]
lb_class=['']*ds_train.data.shape[0]
for idx in tqdm.tqdm(range(ds_train.data.shape[0]),total=ds_train.data.shape[0]):
    fname=str(idx).zfill(6)+'.png'
    npimg=ds_train.data[idx].transpose((1,2,0))
    img=PIL.Image.fromarray(npimg)
    img.save(f'train_images/{fname}')
    tgt=ds_train.labels[idx]

    image_id[idx]=fname
    label[idx]=tgt
    lb_class[idx]=ds_train.classes[tgt]
df=pd.DataFrame({'image_id':image_id,'label':label,'lb_class':lb_class})
df.to_csv('./train.csv',index=False)

ds_test=torchvision.datasets.STL10(root='./', split='test', download=True)
image_id=['']*ds_test.data.shape[0]
label=[999]*ds_test.data.shape[0]
lb_class=['']*ds_test.data.shape[0]
for idx in tqdm.tqdm(range(ds_test.data.shape[0]),total=ds_test.data.shape[0]):
    fname=str(idx).zfill(6)+'.png'
    npimg=ds_test.data[idx].transpose((1,2,0))
    img=PIL.Image.fromarray(npimg)
    img.save(f'test_images/{fname}')
    tgt=ds_test.labels[idx]

    image_id[idx]=fname
    label[idx]=tgt
    lb_class[idx]=ds_test.classes[tgt]
df=pd.DataFrame({'image_id':image_id,'label':label,'lb_class':lb_class})
df.to_csv('./test.csv',index=False)
