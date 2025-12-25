class VisionServiceException(Exception):
    """Base exception for Vision Service"""

    pass


class ModelDownloadError(VisionServiceException):
    """Exception raised for errors during model download"""

    pass


class ModelLoadError(VisionServiceException):
    """Exception raised for errors during model loading"""

    pass


class ImageAnalysisError(VisionServiceException):
    """Exception raised for errors during image analysis"""

    pass
