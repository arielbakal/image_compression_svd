import numpy as np
import imageio.v2 as imageio

def svd_truncation(matrix, rank):
    U, s, Vt = np.linalg.svd(matrix)

    U_truncated = U[:,:rank]
    Vt_truncated = Vt[:rank]
    s_truncated = s[:rank]

    return np.shape(matrix), U_truncated, Vt_truncated, s_truncated

def matrix_padding(shape, U_truncated, Vt_truncated, s_truncated):
    n, m = shape

    U_padded = np.pad(U_truncated, ((0, n - U_truncated.shape[0]), (0, n - U_truncated.shape[1])), mode='constant')

    Vt_padded = np.pad(Vt_truncated, ((0, m - Vt_truncated.shape[0]), (0, m - Vt_truncated.shape[1])), mode='constant')

    Z_padded = np.zeros((n, m))
    Z_padded[:s_truncated.shape[0], :s_truncated.shape[0]] = np.diag(s_truncated)

    matrix_padded = U_padded @ Z_padded @ Vt_padded
    return matrix_padded

def compress_image(path, rank):

    image = imageio.imread(path) # read image as a matrix

    # Compression for mxn images
    if len(image.shape) == 2:
      shape, U_truncated, Vt_truncated, s_truncated = svd_truncation(image, rank)
      compressed_image = matrix_padding(shape, U_truncated, Vt_truncated, s_truncated).clip(0, 255).astype(np.uint8)
      imageio.imwrite('compressed_image.jpg', compressed_image)

    # Compression for mxnx3 images
    elif len(image.shape) == 3:
      image_channels = []

      # Compressing the 3 channels
      for k in range(3):
        shape, U_truncated, Vt_truncated, s_truncated = svd_truncation(image[:,:,k], rank)
        compressed_channel = matrix_padding(shape, U_truncated, Vt_truncated, s_truncated).clip(0, 255).astype(np.uint8)
        image_channels.append(compressed_channel)

      # Then stacking them
      compressed_image = np.dstack(image_channels)
      imageio.imwrite('compressed_image.jpg', compressed_image)

    else:
      print('only mxn or mxnx3 images')