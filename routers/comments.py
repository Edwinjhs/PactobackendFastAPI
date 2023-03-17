# from fastapi import APIRouter, Depends
# from fastapi.responses import  JSONResponse
# from fastapi.encoders import jsonable_encoder
# from sqlalchemy.orm import session, Session

# from service.comment import CommentService as CommentService
# from schemas.comment import comment as CommentSchema

# # aca me traigo el token
# from service.token import user_token as TokenService

# comment_router = APIRouter()

# @comment_router.get("/api/post/comment",tags=['post'])
# def read_api(db: session = Depends(PostService.get_db)):
#     result = PostService(db).get_posts()
#     return JSONResponse(content=jsonable_encoder(result), status_code=200)

# @comment_router.post("/api/user/me/post/comment",tags=['post'],status_code=201,response_model=dict)
# def create_post(post:PostSchema,db: session = Depends(PostService.get_db),current_user: PostSchema = Depends(TokenService.get_current_active_user)):
#     result=PostService(db).create_post(post)
#     return JSONResponse(content={"message":'Se ha creado el post correctamente'})

# @comment_router.delete('/api/user/post/comment/{id}',tags=['post'])
# def delete_post(id:int, db: session = Depends(PostService.get_db),current_user: PostSchema = Depends(TokenService.get_current_active_user)):
#     success = PostService(db).delete_post(id)
#     if success:
#         return JSONResponse(status_code=202,content={"message":"Post deleted"})
#     else:
#         return JSONResponse(content="Post not found", status_code=404)

# @comment_router.get("/api/user/post/{status}",tags=['post'])
# def get_post_by_status(status, db: Session = Depends(PostService.get_db),current_user: PostSchema = Depends(TokenService.get_current_active_user)):
#     post = PostService(db).get_post_by_status(status)
#     return post

# @comment_router.put('/api/user/post/{id}',tags=['post'])
# def update_post(id:int,post:PostSchema, db: session = Depends(PostService.get_db),current_user: PostSchema = Depends(TokenService.get_current_active_user)):
#     result = PostService(db).update_post(id,post)
#     if not result:
#         return JSONResponse(content={"message":"No se ha encontrado ningun post","status_code":"404"})
#     PostService(db).update_post(id,post)
#     return JSONResponse(content={"message":'Se ha modificado el post con id: {id}'})
