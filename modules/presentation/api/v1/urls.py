from ninja import Router
from modules.presentation.api.v1.task.handlers import router as note_router

router = Router(tags=['v1'])

router.add_router(prefix='task', router=note_router)
