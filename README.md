AI-Powered Job Market Intelligence Platform
Overview

The AI-Powered Job Market Intelligence Platform is a full-stack web application designed to help job seekers analyze their resumes, evaluate ATS compatibility, identify skill gaps, and receive data-driven career insights.

The system combines modern web technologies with AI-powered resume parsing and job market intelligence to improve employability and career decision-making.

Features
Completed Features
Project setup and architecture
React frontend structure
Node.js + Express backend
MongoDB Atlas integration
Mongoose schema design
JWT-based authentication system
Secure login and signup
Password hashing using bcrypt
Protected API routes
Resume upload module (PDF support)
Multer file handling system
Resume storage in MongoDB
User–resume relationship mapping
FastAPI integration for resume parsing
AI-based resume parsing pipeline
Data normalization layer (backend preprocessing)
Complete upload → parse → store flow
In Progress Features
ATS score analysis engine
Resume enhancement suggestions
Skill gap detection system
Job matching algorithm
Career insights generation
Upcoming Features
AI career assistant chatbot
Job market trend analysis
Personalized learning roadmap generator
Frontend dashboard (analytics view)
Deployment (Render/Vercel)
Real-time job recommendations
Technology Stack
Frontend
React
Vite
React Router DOM
Axios
CSS / UI components
Backend
Node.js
Express.js
MongoDB Atlas
Mongoose
JWT Authentication
Multer
Axios
dotenv
CORS
AI / Processing Layer
FastAPI (Python service)
Resume parsing pipeline
NLP-based extraction modules
Data normalization utilities
Database
MongoDB Atlas
Project Structure
AI-Job-Market-Intelligence
│
├── frontend
│   ├── src
│   ├── public
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
│
├── docs
│   └── ER_Diagram.png
│
└── README.md
Database Design
Users Collection
name
email
password (hashed)
createdAt
updatedAt
Resumes Collection
userId (reference to User)
resumePath
skills
education
experience
projects
certifications
createdAt
updatedAt
ATSReports Collection (planned)
userId
resumeId
ATS score
job match score
skill gaps
readiness score
Authentication System
Features
User signup
User login
JWT token generation
Protected routes
Password encryption using bcrypt
Flow

Signup → Login → JWT Token → Protected APIs

Resume Upload System (Phase 5–7 Core)
Features
PDF upload support
Multer file handling
JWT protected endpoint
FastAPI resume parsing
AI-based structured extraction
Data normalization before database storage
MongoDB storage linked with user
Flow

Upload Resume
↓
Multer stores file
↓
FastAPI parses resume
↓
Normalization layer processes data
↓
MongoDB stores structured resume
↓
Linked to authenticated user

API Endpoints
Authentication APIs

Register
POST http://localhost:5000/api/auth/signup

Login
POST http://localhost:5000/api/auth/login

Resume APIs

Upload Resume
POST http://localhost:5000/api/resume/uploadResume

Headers:
Authorization: Bearer <JWT_TOKEN>

Body:
form-data
resume: PDF file

Get Latest Resume
GET http://localhost:5000/api/resume/myResume

Headers:
Authorization: Bearer <JWT_TOKEN>

Current Project Status
Phase	Status
Phase 1 – Requirements	Complete
Phase 2 – Setup	Complete
Phase 3 – Database Design	Complete
Phase 4 – Authentication System	Complete
Phase 5 – Resume Upload	Complete
Phase 6 – Resume Parsing	Complete
Phase 7 – Integration (Backend + AI)	Completed
Phase 8 – ATS Engine	Pending
Phase 9 – AI Features	Pending
Phase 10 – Frontend Dashboard	Pending
Phase 11 – Deployment	Pending
Contributors
Person 1
ATS score engine
Skill gap detection
AI recommendation system
Job market analytics
Resume intelligence layer
Person 2 (Fullstack Backend + Integration)
Authentication system
Database design
Resume upload system
FastAPI integration
Resume parsing pipeline
Data normalization
Backend APIs
Frontend integration support
Future Enhancements
AI resume reviewer
ATS score prediction model
Job matching system
Career roadmap generator
AI chat assistant
Real-time job suggestions
Smart skill recommendations
License

This project is developed for academic and learning purposes.

Final Note

The system supports a complete pipeline:

Upload → Parse → Normalize → Store → Retrieve resume data