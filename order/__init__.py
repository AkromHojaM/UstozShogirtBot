from aiogram import Router
from .admin import router as admin
from .callback_query import router as callback_query
from .header import router as header
from .start import router as start

router = Router()
router.include_router(admin)
router.include_router(callback_query)
router.include_router(header)
router.include_router(start)
