# 🧠 AI Moondream API – Vision AI Local Service

`ai-moondream` là một **dịch vụ AI Vision (nhìn ảnh + hiểu nội dung)** chạy **hoàn toàn local**, sử dụng **Moondream Vision-Language Model**, được đóng gói dưới dạng **FastAPI + Docker**.

Dự án cho phép:
- Nhận ảnh (base64)
- Phân tích nội dung ảnh
- Trả lời câu hỏi về ảnh (VQA)
- Mô tả ảnh, OCR, nhận diện món ăn / vật thể
- Tích hợp dễ dàng vào hệ thống chatbot, FoodBot, AI Assistant

👉 **Không phụ thuộc OpenAI – Không gửi dữ liệu ra ngoài**

---

## ✨ Tính năng chính

- 🖼️ Image Understanding (Vision + Language)
- 💬 Chat với ảnh (Vision Q&A)
- 🧠 Chạy local model Moondream (0.5B / 2B)
- 🚀 API REST (FastAPI)
- 🐳 Docker-ready
- ♻️ Cache model, không tải lại mỗi lần restart
- 🔄 Mock model cho dev/test

---

## 🏗️ Kiến trúc tổng quát

Client → FastAPI → Moondream Model (Local) → Response

---

## 📂 Cấu trúc thư mục

```
ai-moondream/
├── devcontainer/
├── libretranslate_models/
├── model_cache/
├── src/
│   ├── api.py
│   ├── config.py
│   ├── exceptions.py
│   ├── ollama_model_mocks.py
│   ├── routes.py
│   ├── schemas.py
│   ├── vision_service.py
├── docker-compose.yaml
├── Dockerfile
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## ⚙️ Cấu hình môi trường

```env
MODEL_NAME=moondream-0_5b-int8
MOONDREAM_MODE=local
MODEL_CACHE_DIR=/app/model_cache
```

---

## 🐳 Chạy bằng Docker

```bash
docker-compose up -d --build
```

API mặc định:
```
http://localhost:18000
```

Health check:
```
GET /health
```

---

## 🧠 Model hoạt động như thế nào?

- Model **đã được train sẵn**
- Không fine-tune, không học runtime
- Chỉ inference (suy luận)
- Cache model tại `model_cache/`

---

## 🔌 Tích hợp thực tế

- Chatbot bán hàng
- FoodBot AI
- Nhận diện menu, món ăn
- OCR hóa đơn
- Vision AI nội bộ doanh nghiệp

---

## 📌 Ghi chú quan trọng

- Khuyến nghị dùng **0.5B** cho VPS yếu
- Dùng **2B** khi có RAM/GPU tốt
- Nên kết hợp **RAG / Database** để AI trả lời đúng dữ liệu nghiệp vụ

---

## 👨‍🏫 Tác giả

**Code Web Không Khó**  
AI / Backend / System Design  
