import os


class Settings:
    MODEL_NAME: str = os.getenv(
        "MODEL_NAME", "moondream-0_5b-int8"
    )  # also moondream-2b-int8 available
    DEFAULT_PROMPT: str = "Analyze the objects in these images from the security camera. Focus on the actions, behavior, and potential intent of the objects, rather than just describing its appearance."
    BASE_MODEL_DIR: str = os.getenv("MODEL_CACHE_DIR", "../model_cache")
    MAX_IMAGE_SIZE: int = 2048  # Longest edge
    MOONDREAM_2B_URL: str = os.getenv("MOONDREAM_2B_URL", "")
    MOONDREAM_500M_URL: str = os.getenv("MOONDREAM_500M_URL", "")
    MOONDREAM_MODE: str = os.getenv("MOONDREAM_MODE", "local")  # 'local' or 'api'
    MOONDREAM_API_KEY: str = os.getenv(
        "MOONDREAM_API_KEY",
        "",
    )


settings = Settings()
