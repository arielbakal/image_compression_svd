# Image Compression Algorithm using SVD

This is a simple algorithm which works in terms of rank reduction. It does a singular value descomposition (SVD) of the image's matrix, and then reduce our rank while reducing its singular values.

Wrapping all together we get a new image with less singular values (less information) and that's it!

Feel free to suggest or ask anything!

## Usage

``` 
python main.py <image_location> <compression percentage>
```

This **compression percentage** must be expressed in terms of percentage, not decimals.

Then the compressed image appears inside the repository's folder named 'compressed_image'.

__NOTE__ : This algorithm only works with mxn and mxnx3 images and saves the compressed image with jpg.

## Jupyter Notebook

There is a notebook where i explain how the algorithm works and how to implement it.
