from pydantic import BaseModel
from typing import Optional, Union, List, Dict, Any


class ImageUrl(BaseModel):
    url: str


class ContentPartImage(BaseModel):
    type: str = "image_url"
    image_url: ImageUrl


class ContentPartText(BaseModel):
    type: str = "text"
    text: str


class ChatMessage(BaseModel):
    role: str
    content: Union[str, List[Union[ContentPartImage, ContentPartText]]]


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    temperature: Optional[float] = 1.0
    stream: Optional[bool] = False


class ChatChoice(BaseModel):
    index: int
    message: ChatMessage
    finish_reason: str


class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[ChatChoice]
    usage: Dict[str, int]


class OllamaMessage(BaseModel):
    role: str
    content: Union[str, List[dict]]
    images: Optional[List[str]] = None


class OllamaChatRequest(BaseModel):
    model: Optional[str] = None
    messages: List[OllamaMessage]
    stream: bool = False
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None


class OllamaChatResponse(BaseModel):
    model: str
    created_at: str
    message: OllamaMessage
    done: bool


class OllamaShowModelRequest(BaseModel):
    model: str


class OllamaModelDetails(BaseModel):
    parent_model: str
    format: str
    family: str
    families: List[str]
    parameter_size: str
    quantization_level: str


class OllamaModelShowResponse(BaseModel):
    license: str
    modelfile: str
    parameters: str
    template: str
    details: OllamaModelDetails
    model_info: Dict[str, Any]
    projector_info: Dict[str, Any]
    modified_at: str


class OllamaGenerateOptions(BaseModel):
    num_keep: Optional[int] = 5
    seed: Optional[int] = 42
    num_predict: Optional[int] = 100
    top_k: Optional[int] = 20
    top_p: Optional[float] = 0.9
    min_p: Optional[float] = 0.0
    typical_p: Optional[float] = 0.7
    repeat_last_n: Optional[int] = 33
    temperature: Optional[float] = 0.8
    repeat_penalty: Optional[float] = 1.2
    presence_penalty: Optional[float] = 1.5
    frequency_penalty: Optional[float] = 1.0
    mirostat: Optional[int] = 1
    mirostat_tau: Optional[float] = 0.8
    mirostat_eta: Optional[float] = 0.6
    penalize_newline: Optional[bool] = True
    stop: Optional[List[str]] = ["\\n", "user:"]
    numa: Optional[bool] = False
    num_ctx: Optional[int] = 1024
    num_batch: Optional[int] = 2
    num_gpu: Optional[int] = 1
    main_gpu: Optional[int] = 0
    low_vram: Optional[bool] = False
    vocab_only: Optional[bool] = False
    use_mmap: Optional[bool] = True
    use_mlock: Optional[bool] = False
    num_thread: Optional[int] = 8


class OllamaGenerateRequest(BaseModel):
    model: str
    prompt: str
    stream: Optional[bool] = False
    options: Optional[OllamaGenerateOptions] = OllamaGenerateOptions()
    images: Optional[List[str]]


class OllamaGenerateResponse(BaseModel):
    model: str
    created_at: str
    response: str
    done: bool
    context: List[int]
    total_duration: int
    load_duration: int
    prompt_eval_count: int
    prompt_eval_duration: int
    eval_count: int
    eval_duration: int
