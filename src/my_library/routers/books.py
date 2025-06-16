from fastapi import APIRouter

# https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter

router = APIRouter(prefix="/books")

@router.get("/", tags=["books"])
async def get_all_books():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{book_id}", tags=["books"])
async def get_single_book(book_id: str):
    return {"username": book_id}


@router.put(
    "/",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_book(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}