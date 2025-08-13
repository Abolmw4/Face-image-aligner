from pydantic import BaseModel
import base64
from typing import Union, List

class RequestBody(BaseModel):
    image: Union[bytes, List[bytes]]
    
    
    
    