from fastapi import APIRouter
from data_model.request_body import RequestBody
from utils.util import load_json, deserialize, serialize
from facealigner.facealignment import align_face
from typing import List
import numpy as np

router = APIRouter()

@router.get('/')
async def get_info():
    conf = load_json()
    return conf

@router.post('/align')
async def alignment_process(Item: RequestBody):
    image_list: List[np.ndarray]
    if isinstance(Item.image, list):
        for item in Item:
            unaligned_img = deserialize(item.image)
            aligned_face = align_face(unaligned_img)
            image_list.append(serialize(aligned_face))
        return {"result": image_list}
    else:
        unaligned_img = deserialize(Item.image)
        aligned_face = align_face(unaligned_img)
        ser_iamge = serialize(aligned_face)
        return {"result": ser_iamge}

