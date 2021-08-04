from sqlalchemy.orm import Session
from .. import model, schema
from fastapi import status, HTTPException


def get_all(db: Session):
    blogs = db.query(model.Blog).all()
    return blogs


def create(request: schema.Blog, db: Session):
    new_blog = model.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    db.query(model.Blog).filter(model.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return ('Blog with id: {id} is deleted permanently')


def update(id: int, request: schema.Blog, db: Session):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id: {id} not found")
    blog.update({'title': request.title, 'body': request.body}, synchronize_session=False)
    db.commit()
    return ('Updated')


def show(id: int, db: Session):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id: {id} is not available")
    return blog
