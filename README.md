﻿# blockchainpi

pip install fastapi pymongo uvicorn

# FastAPI Project

## Setup Instructions

### 1. สร้าง Virtual Environment ใหม่
ถ้าคุณยังไม่มีสภาพแวดล้อมเสมือน (virtual environment) สำหรับโปรเจกต์ของคุณ ให้สร้างใหม่:

```sh
python -m venv venv
```

### 2. เปิดใช้งาน Virtual Environment
หลังจากสร้างสภาพแวดล้อมเสมือนแล้ว ให้เปิดใช้งานมัน:
#### บน Windows:
```sh
.\venv\Scripts\activate
```

#### บน macOS และ Linux:
```sh
source venv/bin/activate
```

#### 3. ติดตั้ง Dependencies
ติดตั้งไลบรารีที่จำเป็นใน virtual environment ของคุณ:

```sh
pip install fastapi uvicorn pymongo
```

#### 4. ตรวจสอบโครงสร้างโปรเจกต์ของคุณ
ตรวจสอบว่าโครงสร้างโปรเจกต์ของคุณถูกต้องตามนี้:

```sh
your_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── users.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── connection.py
│   ├── schema/
│   │   ├── __init__.py
│   │   ├── schemas.py
│
├── venv/
├── requirements.txt
└── run.sh (optional)
```

#### 5. รัน Uvicorn
รันแอปพลิเคชันของคุณโดยใช้ uvicorn:
```sh
uvicorn app.main:app --reload
{ user_id: { $toObjectId: "$user_id" } }
```
