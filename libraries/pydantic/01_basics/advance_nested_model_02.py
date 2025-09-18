from typing import List, Optional, Union
from pydantic import BaseModel, Field


class TextContent(BaseModel):
    type : str = "text"
    content : str

class ImageContent(BaseModel):
    type : str = "image"
    url : str
    caption : Optional[str] = None


class Article(BaseModel):
        Title : str
        sections : List[Union[TextContent, ImageContent]]


#### NOT GOOD PRACTICES
# 
#         