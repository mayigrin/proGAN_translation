## Overview


This code provides the necessary tools for converting a tensorflow-trained proGAN into a pytorch-based model with the same structure, so that the user can then run Gandissect on their model.

## Instructions

In order to perform the conversion, the user should first create a new directory with their name of choice inside of `netdissect`, and place the `.pkl` file of their model in that directory.

The user should then run
```
python netdissect/translate.py --id <name of directory>
```
The conversion code will then output a `.pth` file inside of the directory you made. If you'd like to then dissect this converted version of your model, the next step is to copy or move that `.pth` file into `models/karras`, and then follow the instructions listed in [the original ganddisect repo](https://github.com/CSAILVision/gandissect).

## Credits

Much of the code in this project was borrowed from the following sources. 

All files except the ones listed below are from [https://github.com/CSAILVision/gandissect](https://github.com/CSAILVision/gandissect).

The following files are from [https:(https://github.com/llSourcell/Progressive_GANs](https://github.com/llSourcell/Progressive_GANs):
- netdissect/dataset.py
- netdissect/legacy.py
- netdissect/misc.py
- netdissect/networks.py
- netdissect/tfutil.py

The following file is from [https://github.com/NVlabs/stylegan/blob/master/config.py](https://github.com/NVlabs/stylegan/blob/master/config.py):
- netdissect/config.py

The following file is originally from [https://gandissect.csail.mit.edu](https://gandissect.csail.mit.edu), after which I made some modifications.
- netdissect/translate.py

## Citations

David Bau, Jun-Yan Zhu, Hendrik Strobelt, Bolei Zhou, Joshua B. Tenenbaum, William T. Freeman, Antonio Torralba. _GAN Dissection: Visualizing and Understanding Generative Adversarial Networks_, Proceedings of the International Conference on Learning Representations (ICLR), 2019.
