# napari-ultrasound-reader

This napari plugin allows napari to read 3D images from dicom, h5 or hdf5 files.

This plugin was developed by Leopold Franz, ETH D-BSSE Iber Lab

----------------------------------
## Usage
Once you have installed `napari-ultrasound-reader` to your python environment, you can start napari 
by typing the following in the terminal:

```bash
napari
```

You can then import 3D images in the standard DICOM format (".dcm") or Hierarchical Dataset Format 5 (HDF5) 
files (".h5"/".hdf5") by drag and dropping them into the napari viewer. Note that the raw image arrays stored 
in the HDF5 files need to be stored in the top hierarchical layer or in "left"/"right" datasets.

## Installation

You can install `napari-ultrasound-reader` to your python environment by running
```bash
pip install .
```

## License

Distributed under the terms of the [BSD-3] license,
"follicle-tracker" is free and open source software