from typing import List, Optional
from pydantic import BaseModel, Field


class Comment(BaseModel):
    id : int
    content : str
    replies : Optional[List["Comment"]] = None

## Required after self-referencing
Comment.model_rebuild()


comment = Comment(
    id=1,
    content="This is a comment",
    replies=[
        Comment(
            id=2,
            content="This is a reply",
            replies=[
                Comment(
                    id=3,
                    content="This is a nested reply"
                )
            ]
        ),
        Comment(
            id=4,
            content="This is another reply"
        )
    ]
)
print(comment)