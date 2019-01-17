import sys
import Augmentor as alteredAugmentor # pip install git+https://github.com/simonlousky/alteredAugmentor.git
# sys.path.append("/Users/orshemesh/Desktop/project repo/alteredAugmentor")  # To find local version of the library
# import Augmentor
# path = "/Users/orshemesh/Desktop/Project/augmented_leaves/"
# this dir must to contains input_dir (the name does not mather) + ground_truth dir

def augment_perform_pipe(src_path, ground_truth_path):

    # output dir will be in <path>/output
    p = alteredAugmentor.Pipeline(src_path, output_directory="../output_phase2/", save_format="PNG")

    p.ground_truth(ground_truth_path)

    # p.flip_left_right(probability=0.4)
    # p.flip_top_bottom(probability=0.2)
    # p.rotate(probability=1.0, max_left_rotation=25, max_right_rotation=25)
    # p.random_color(probability=1.0, min_factor=0.5, max_factor=1.7)
    # p.random_contrast(probability=1.0, min_factor=0.7, max_factor=1.7)
    # p.random_brightness(probability=1.0, min_factor=0.7, max_factor=1.5)
    # p.skew(probability=0.8, magnitude=0.3)
    # p.shear(probability=0.6, max_shear_left=7, max_shear_right=7)
    p.resize(probability=1.0, width=853, height=512)

    # p.gaussian_distortion(probability=1.0, grid_width = 700, grid_height=700, magnitude= 8, corner= "ul", method="in") very easy with big grid!!!!
    # p.random_distortion(probability=1.0, grid_height=400, grid_width=600, magnitude=7)

    p.set_save_format(save_format="PNG")

    p.process()
