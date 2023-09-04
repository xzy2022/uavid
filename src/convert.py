# https://www.kaggle.com/datasets/awsaf49/uavid-semantic-segmentation-dataset

import glob
import os
import shutil
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dataset_tools.convert import unpack_if_archive
from dotenv import load_dotenv
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "UAVid Semantic Segmentation"
    dataset_path = "/mnt/d/datasetninja-raw/uavid"
    images_folder = "Images"
    masks_folder = "Labels"

    masks_ext = ".png"
    batch_size = 3

    def get_unique_colors(img):
        unique_colors = []
        img = img.astype(np.int32)
        h, w = img.shape[:2]
        colhash = img[:, :, 0] * 256 * 256 + img[:, :, 1] * 256 + img[:, :, 2]
        unq, unq_inv, unq_cnt = np.unique(colhash, return_inverse=True, return_counts=True)
        indxs = np.split(np.argsort(unq_inv), np.cumsum(unq_cnt[:-1]))
        col2indx = {unq[i]: indxs[i][0] for i in range(len(unq))}
        for col, indx in col2indx.items():
            if col != 0:
                unique_colors.append((col // (256**2), (col // 256) % 256, col % 256))

        return unique_colors

    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        tag_value = int(image_path.split("/")[-3][3:])
        tag = sly.Tag(tag_seq, value=tag_value)

        if ds_name != "test":
            mask_path = image_path.replace(images_folder, masks_folder)
            if file_exists(mask_path):
                mask_np = sly.imaging.image.read(mask_path)
                unique_colors = get_unique_colors(mask_np)
                for color in unique_colors:
                    mask = np.all(mask_np == color, axis=2)
                    ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
                    for i in range(1, ret):
                        obj_mask = curr_mask == i
                        bitmap = sly.Bitmap(data=obj_mask)
                        if bitmap.area > 150:
                            obj_class = color_to_obj_class[color]
                            label = sly.Label(bitmap, obj_class)
                            labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=[tag])

    color_to_obj_class = {
        (0, 0, 0): sly.ObjClass("background clutter", sly.Bitmap, color=(0, 0, 0)),
        (128, 0, 0): sly.ObjClass("building", sly.Bitmap, color=(128, 0, 0)),
        (128, 64, 128): sly.ObjClass("road", sly.Bitmap, color=(128, 64, 128)),
        (0, 128, 0): sly.ObjClass("tree", sly.Bitmap, color=(0, 128, 0)),
        (128, 128, 0): sly.ObjClass("low vegetation", sly.Bitmap, color=(128, 128, 0)),
        (64, 0, 128): sly.ObjClass("moving car", sly.Bitmap, color=(64, 0, 128)),
        (192, 0, 192): sly.ObjClass("static car", sly.Bitmap, color=(192, 0, 192)),
        (64, 64, 0): sly.ObjClass("human", sly.Bitmap, color=(64, 64, 0)),
    }

    tag_seq = sly.TagMeta("seq", sly.TagValueType.ANY_NUMBER)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)

    meta = sly.ProjectMeta(obj_classes=list(color_to_obj_class.values()), tag_metas=[tag_seq])
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in os.listdir(dataset_path):
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        data_folders = os.path.join(dataset_path, ds_name, ds_name)

        images_pathes = glob.glob(data_folders + "/*/{}/*.png".format(images_folder))

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_pathes))

        for images_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
            images_names_batch = []
            for im_path in images_pathes_batch:
                temp_prefix = im_path.split("/{}/{}/".format(ds_name, ds_name))[-1]
                im_prefix = temp_prefix.split("/")[0]
                im_name = im_prefix + "_" + get_file_name_with_ext(im_path)
                images_names_batch.append(im_name)

            img_infos = api.image.upload_paths(dataset.id, images_names_batch, images_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in images_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(images_names_batch))

    return project
