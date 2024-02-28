import pygame
from os import walk
from os.path import join


def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = join(path, image)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list


def import_folder_dict(path):
    surface_dict = {}
    for _, __, img_files in walk(path):
        for image in img_files:
            tile_name = image.split('.')[0]
            file_path = join(path, image)
            image_surf = pygame.image.load(file_path).convert_alpha()
            surface_dict[tile_name] = image_surf

    return surface_dict
