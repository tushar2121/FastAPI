from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schema, database, model
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(prefix="/blog", tags=["BLOGS"])
get_db = database.get_db


@router.get('/', response_model=List[schema.ShowBlog])
def all_blogs(db: Session = Depends(get_db),current_user: schema.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schema.Blog, db: Session = Depends(get_db),current_user: schema.User = Depends(get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db),current_user: schema.User = Depends(get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schema.Blog, db: Session = Depends(get_db),current_user: schema.User = Depends(get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schema.ShowBlog)
def show(id: int, db: Session = Depends(get_db),current_user: schema.User = Depends(get_current_user)):
    return blog.show(id, db)
