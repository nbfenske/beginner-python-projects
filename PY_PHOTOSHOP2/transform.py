"""
Python Image Manipulation Empty Template by Kylie Ying (modified from MIT 6.865)
YouTube Kylie Ying: https://www.youtube.com/ycubed
Twitch KylieYing: https://www.twitch.tv/kylieying
Twitter @kylieyying: https://twitter.com/kylieyying
Instagram @kylieyying: https://www.instagram.com/kylieyying/
Website: https://www.kylieying.com
Github: https://www.github.com/kying18
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ
"""

from image import Image
import numpy as np

def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    x_pixels, y_pixels, num_channels = image.array.shape
    # make new mutable image
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_im.array[x,y,c] = image.array[x, y, c] * factor

    new_im.array = image.array * factor

    return new_im

def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    x_pixels, y_pixels, num_channels = image.array.shape
    # make new mutable image
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_im.array[x,y,c] = (image.array[x,y,c] - mid) * factor + mid
    
    new_im.array = (image.array - mid) * factor + mid

    return new_im

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels, num_channels = image.array.shape
    # make new mutable image
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    neighbor_range = kernel_size // 2 # neighbors to each side

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                # iterate through each neighbor and sum
                total = 0
                for x_i in range(max(0,x-neighbor_range), min(x_pixels - 1, x+neighbor_range) + 1):
                    for y_i in range(max(0,y-neighbor_range), min(y_pixels - 1, y+neighbor_range) + 1):
                        total += image.array[x_i, y_i, c]
                new_im.array[x,y,c] = total / (kernel_size ** 2)

    return new_im

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    x_pixels, y_pixels, num_channels = image.array.shape
    # make new mutable image
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    kernel_size = kernel.shape[0]
    neighbor_range = kernel_size // 2 # neighbors to each side

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0,x-neighbor_range), min(x_pixels - 1, x+neighbor_range) + 1):
                    for y_i in range(max(0,y-neighbor_range), min(y_pixels - 1, y+neighbor_range) + 1):
                        x_k = x_i + neighbor_range - x
                        y_k = y_i + neighbor_range - y
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val
                new_im.array[x,y,c] = total

    return new_im

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    x_pixels, y_pixels, num_channels = image1.array.shape
    # make new mutable image
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x,y,c] = (image1.array[x,y,c]**2 + image2.array[x,y,c]**2)**.5
    return new_im

if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    # brighten_im = brighten(lake, 1.7)
    # brighten_im.write_image('bright_test.png')

    # darkened_im = brighten(lake, .3)
    # darkened_im.write_image('dark_test.png')

    # incr_contrast = adjust_contrast(lake, 2, 0.5)
    # incr_contrast.write_image('contrast_test.png')
    # decr_contrast = adjust_contrast(lake, .5, .5)
    # decr_contrast.write_image('contrast_test2.png')

    # blur_im = blur(city, 3)
    # blur_im.write_image('blur_test.png')
    # blur_im2 = blur(city, 15)
    # blur_im2.write_image('blur_test2.png')

    # sobel edge detection kernel
    # sobel_x_kernel = np.array([
    #     [1,2,1],
    #     [0,0,0],
    #     [-1,-2,-1]
    # ])

    # sobel_y_kernel = np.array([
    #     [1,0,-1],
    #     [2,0,-2],
    #     [1,0,-1]
    # ])

    # sobel_x = apply_kernel(city, sobel_x_kernel)
    # sobel_x.write_image('kernel_x_test.png')
    # sobel_y = apply_kernel(city, sobel_y_kernel)
    # sobel_y.write_image('kernel_y_test.png')

    # combine
    # sobel_xy = combine_images(sobel_x, sobel_y)
    # sobel_xy.write_image('combine_test.png')
