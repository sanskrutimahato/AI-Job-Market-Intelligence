# AI-Powered Job Market Intelligence Platform

## Overview

The AI-Powered Job Market Intelligence Platform is a full-stack web application designed to help job seekers analyze resumes, evaluate ATS compatibility, identify skill gaps, and receive data-driven career insights.

The platform combines modern web technologies, artificial intelligence, and job market analytics to provide personalized recommendations and improve employability.

---

## Features

### Completed Features

#### Project Foundation

- Project setup and architecture
- React frontend structure
- Node.js + Express backend
- MongoDB Atlas integration
- Mongoose schema design
- ER Diagram documentation

#### Authentication System

- User Registration (Signup)
- User Login
- Password hashing using bcrypt
- JWT token generation
- JWT verification middleware
- Protected API routes

#### Resume Upload Module

- PDF resume upload support
- Multer-based file handling
- Secure resume upload API
- Resume storage in MongoDB
- User-resume association

#### Resume Parsing System

- FastAPI microservice integration
- PDF text extraction
- Resume section identification
- Basic information extraction
- Skills extraction
- Education extraction
- Experience extraction
- Project extraction
- Certification extraction
- Structured JSON output generation

#### ATS Analysis Engine

- Market skill profile generation
- Role-based skill analysis
- Tiered skill classification (Core / Important / Nice-to-Have)
- ATS compatibility scoring
- Market readiness scoring
- Missing skill identification
- Resume skill matching
- FastAPI ATS Score API

#### Backend Integration

- Upload → Parse → Normalize → Store workflow
- Resume normalization layer
- MongoDB structured storage
- Latest resume retrieval API
- Authentication-integrated resume management
- FastAPI and Node.js integration

---

## Features In Progress

- Job Match Engine
- Skill Gap Detection
- Resume Improvement Suggestions
- Career Readiness Assessment
---

## Planned Features

- AI Career Assistant
- Personalized Learning Roadmaps
- Job Market Trend Analytics
- Job Recommendation Engine
- Interactive Analytics Dashboard
- Resume Optimization Recommendations
- Real-Time Job Insights

---

## Technology Stack

### Frontend

- React
- Vite
- React Router DOM
- Axios
- CSS

### Backend

- Node.js
- Express.js
- MongoDB Atlas
- Mongoose
- JWT Authentication
- Multer
- Axios
- dotenv
- CORS

### AI Service

- Resume Parsing Pipeline
- ATS Score Engine
- Market Skill Profiling
- NLP-Based Extraction Modules

### Database

- MongoDB Atlas

---

## Project Structure

```text
AI-Job-Market-Intelligence
│
├── frontend
│   ├── public
│   ├── src
│   └── package.json
│
├── backend
│   ├── src
│   │   ├── config
│   │   ├── controllers
│   │   ├── middleware
│   │   ├── models
│   │   ├── routes
│   │   ├── utils
│   │   └── app.js
│   │
│   ├── uploads
│   ├── .env
│   └── package.json
│
├── ai-service
│   ├── app
│   │   ├── routes
│   │   ├── services
│   │   ├── utils
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── test files
│
├── docs
│   └── ER_Diagram.png
│
└── README.md
```

---

## Database Design

### Users Collection

Stores user account information:

- Name
- Email
- Password (Hashed)
- Created At
- Updated At

### Resumes Collection

Stores uploaded and processed resume information:

- User Reference
- Resume File Path
- Skills
- Education
- Experience
- Projects
- Certifications
- Created At
- Updated At

### ATS Reports Collection (Upcoming)

Will store:

- ATS Score
- Job Match Score
- Skill Gap Analysis
- Career Readiness Score
- Improvement Suggestions

---

## Authentication System

### Features

- User Registration
- User Login
- Password Hashing using bcrypt
- JWT Token Generation
- JWT Verification Middleware
- Protected API Routes

### Authentication Flow

```text
User Signup
      ↓
User Login
      ↓
JWT Token Issued
      ↓
Protected Route Access
```

---

## Resume Upload & Parsing System

### Features

- PDF Resume Upload
- JWT-Protected Endpoint
- Multer File Handling
- FastAPI Resume Parsing
- AI-Based Structured Extraction
- Resume Data Normalization
- MongoDB Storage
- User-Resume Association

### Processing Flow

```text
Upload Resume
      ↓
Multer Stores PDF
      ↓
FastAPI Parses Resume
      ↓
Extract Structured Data
      ↓
Normalize Resume Data
      ↓
Store in MongoDB
      ↓
Retrieve via API
```

---

## Resume Parsing Components

The AI Service currently extracts:

### Basic Information

- Name
- Email
- Phone Number
- LinkedIn
- GitHub
- Portfolio

### Skills

- Technical Skills
- Programming Languages
- Frameworks
- Tools
- Soft Skills

### Education

- Degree
- Institution
- Graduation Year

### Experience

- Job Role
- Company
- Duration
- Responsibilities

### Projects

- Project Title
- Tech Stack
- Description

### Certifications

- Certification Name
- Issuer
- Year

---

### ATS APIs

#### Generate ATS Score

```http
POST http://127.0.0.1:8000/api/atsScore
```
### Authentication APIs

#### Register User

```http
POST http://localhost:5000/api/auth/signup
```

#### Login User

```http
POST http://localhost:5000/api/auth/login
```

---

### Resume APIs

#### Upload Resume

```http
POST http://localhost:5000/api/resume/uploadResume
```

**Headers**

```text
Authorization: Bearer <JWT_TOKEN>
```

**Body**

```text
form-data

resume → PDF File
```

---

#### Get Latest Resume

```http
GET http://localhost:5000/api/resume/myResume
```

**Headers**

```text
Authorization: Bearer <JWT_TOKEN>
```

---

## Sample Parsed Resume Output

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "skills": [
    "Java",
    "Spring Boot",
    "React"
  ],
  "education": [
    {
      "degree": "B.Tech CSE",
      "institution": "ABC University"
    }
  ],
  "experience": [],
  "projects": [],
  "certifications": []
}
```

---

## Environment Variables

### Backend (.env)

```env
PORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/sanskrutimahato/AI-Job-Market-Intelligence.git
cd AI-Job-Market-Intelligence
```

---

### Backend Setup

```bash
cd backend
npm install
```

Start Backend Server:

```bash
npm run dev
```

---

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

### AI Service Setup

```bash
cd ai-service
pip install -r requirements.txt
```

Start FastAPI Server:

```bash
uvicorn app.main:app --reload
```

Default FastAPI URL:

```text
http://127.0.0.1:8000
```

---

## Security Features

- Password Hashing using bcrypt
- JWT Authentication
- Protected API Routes
- Token Verification Middleware
- PDF Upload Validation
- Secure User-Resume Association
- Backend Authentication Middleware

---

## Entity Relationship Diagram

![ER Diagram](docs/ER_Diagram.png)

### Relationships

- One User can have multiple Resumes (1:N)
- One Resume can generate one ATS Report (1:1)

---

## Current Project Status

| Phase | Description | Status |
|---------|------------|---------|
| Phase 1 | Requirements Analysis | ✅ Complete |
| Phase 2 | Project Setup | ✅ Complete |
| Phase 3 | Database Design | ✅ Complete |
| Phase 4 | Authentication System | ✅ Complete |
| Phase 5 | Resume Upload Module | ✅ Complete |
| Phase 6 | Resume Parsing Engine | ✅ Complete |
| Phase 7 | Backend + AI Service Integration | ✅ Complete |
| Phase 8 | ATS Analysis Engine | ✅ Complete |
| Phase 9 | AI Recommendation Features | ⏳ Pending |
| Phase 10 | Frontend Dashboard Integration | ⏳ Pending |
| Phase 11 | Testing & Deployment | ⏳ Pending |

---

## Contributors

### Person 1

Responsible for AI and analytics modules:

- Resume Parsing Enhancements
- ATS Analysis Engine
- Skill Gap Detection
- Recommendation Systems
- Career Intelligence Modules
- Job Market Analytics

### Person 2

Responsible for backend and integration:

- Database Design
- Authentication System
- Resume Upload Module
- FastAPI Integration
- Resume Storage System
- Resume Normalization Layer
- Backend API Development
- Frontend Integration Support
- Deployment Support

---

## Current Achievement

The platform currently supports the complete resume processing pipeline:

```text
User Login
      ↓
Upload Resume
      ↓
FastAPI Parsing
      ↓
Structured Data Extraction
      ↓
Normalization Layer
      ↓
MongoDB Storage
      ↓
Resume Retrieval API
```

Users can securely upload resumes, extract structured information using the AI service, store results in MongoDB, and retrieve their latest processed resume through authenticated APIs.

---

## Future Enhancements

- ATS Score Prediction
- Resume Improvement Suggestions
- Skill Gap Detection
- Job Match Analysis
- AI Career Assistant
- Personalized Learning Roadmaps
- Job Market Intelligence Dashboard
- Real-Time Job Recommendations

---

## License

This project is developed for academic and educational purposes.
