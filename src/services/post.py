from src.database import db_client
from databases.interfaces import Record
from fastapi import HTTPException, status
from src.models.post import posts
from src.schemas.post import PostIn, PostUpdateIn


class PostService:
    async def read_all(self, published: bool, limit: int, skip: int = 0) -> list[Record]:
        query = posts.select().where(posts.c.published == published).limit(limit).offset(skip)
        return await db_client.fetch_all(query)

    async def create(self, post: PostIn) -> int:
        command = posts.insert().values(
            title=post.title,
            content=post.content,
            published_at=post.published_at,
            published=post.published,
        )
        return await db_client.execute(command)

    async def read(self, id: int) -> Record:
        return await self.__get_by_id(id)

    async def update(self, id: int, post: PostUpdateIn) -> Record:
        total = await self.count(id)
        if not total:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post não encontrado")

        data = post.model_dump(exclude_unset=True)
        command = posts.update().where(posts.c.id == id).values(**data)
        await db_client.execute(command)

        return await self.__get_by_id(id)
    
    async def delete(self, id: int) -> None:
        command = posts.delete().where(posts.c.id == id)
        await db_client.execute(command)

    async def count(self, id: int) -> int:
        query = "select count(id) as total from posts where id = :id"
        result = await db_client.fetch_one(query, {"id": id})
        return result.total

    async def __get_by_id(self, id) -> Record:
        query = posts.select().where(posts.c.id == id)
        post = await db_client.fetch_one(query)
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post não encontrado")
        return post
