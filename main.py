from fastapi import FastAPI
from config.database import init_db
from routes.auth_route import auth_router
from contextlib import asynccontextmanager
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Startup event (before app starts)
        await init_db()
        yield
    except Exception as e:
        logger.error(f"Error during app lifespan: {e}")
        raise
    finally:
        logger.info("Application shutdown complete.")

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
