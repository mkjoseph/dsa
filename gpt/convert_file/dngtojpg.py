# need to:  pip install rawpy imageio

# Import necessary libraries
# Note: Assuming rawpy and imageio are available in the environment. If not, they need to be installed using pip.
import rawpy
import imageio


def convert_dng_to_jpg(dng_file_path, jpg_file_path, jpg_quality=95):
  """
    Converts a DNG file to a JPG file.

    Parameters:
    - dng_file_path (str): The file path of the DNG file to be converted.
    - jpg_file_path (str): The file path where the JPG file will be saved.
    - jpg_quality (int): The quality of the JPG file on a scale from 0 to 100.

    This function reads the DNG file using rawpy, processes it to an RGB image,
    and then saves it as a JPG file using imageio with the specified quality.
    """

  # Read the DNG file using rawpy
  with rawpy.imread(dng_file_path) as raw:
    # Process the image (convert to RGB)
    rgb = raw.postprocess()

  # Save the processed image as a JPG file
  imageio.imwrite(jpg_file_path, rgb, quality=jpg_quality)


# Example usage (commented out to prevent execution):
# convert_dng_to_jpg('path/to/input.dng', 'path/to/output.jpg')
