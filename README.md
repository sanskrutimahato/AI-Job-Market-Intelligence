# AI-Powered Job Market Intelligence Platform

## Overview

The AI-Powered Job Market Intelligence Platform is a full-stack web application designed to help job seekers analyze their resumes, evaluate ATS compatibility, identify skill gaps, and receive data-driven career insights.

The platform combines modern web technologies, artificial intelligence, and job market analytics to provide personalized recommendations and improve employability.

---

## Features

### Current Features (Completed)

* Project setup and architecture
* React frontend structure
* Node.js + Express backend
* MongoDB Atlas database integration
* Mongoose configuration
* Database schema design
* ER Diagram documentation
* User Authentication System
* JWT-based Authorization
* Protected API Routes
* Password Hashing with bcrypt

### Planned Features

* Resume Upload and Management
* Resume Parsing
* ATS Score Analysis
* Job Match Scoring
* Skill Gap Detection
* Career Readiness Assessment
* Personalized Learning Roadmaps
* Job Market Trend Analytics
* AI Chat Assistant

---

## Technology Stack

### Frontend

* React
* Vite
* React Router DOM
* Axios
* CSS / UI Components

### Backend

* Node.js
* Express.js
* MongoDB Atlas
* Mongoose
* JWT Authentication 
* Multer (Planned)
* dotenv
* CORS

### Database

* MongoDB Atlas

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
│   │   ├── models
│   │   │   ├── User.js
│   │   │   ├── Resume.js
│   │   │   └── ATSReport.js
│   │   ├── routes
│   │   ├── controllers
│   │   ├── middleware
│   │   └── app.js
│   │
│   ├── .env
│   └── package.json
│
├── docs
│   └── ER_Diagram.png
│
└── README.md
```

---

## Database Design

The application uses MongoDB Atlas as the primary database and Mongoose as the ODM.

## Authentication System

The platform implements secure JWT-based authentication.

### Features

* User Registration (Signup)
* User Login
* Password Hashing using bcrypt
* JWT Token Generation
* JWT Verification Middleware
* Protected API Routes

### Authentication Flow

User Signup → User Login → JWT Token Issued → Protected Route Access


### Collections

#### Users

Stores user account information:

* Name
* Email
* Password
* Created At
* Updated At

#### Resumes

Stores parsed resume information:

* User Reference
* Skills
* Education
* Experience
* Projects
* Certifications
* Created At
* Updated At

#### ATSReports

Stores resume analysis results:

* User Reference
* Resume Reference
* ATS Score
* Job Match Score
* Skill Gap Analysis
* Readiness Score
* Created At
* Updated At

---

## Entity Relationship Diagram

![ER Diagram](docs/ER_Diagram.png)

### Relationships

* One User can have multiple Resumes (1:N)
* One Resume generates one ATS Report (1:1)

---

## Installation

### Clone Repository

```bash
git clone https://github.com/sanskrutimahato/AI-Job-Market-Intelligence.git
cd AI-Job-Market-Intelligence
```

### Backend Setup

```bash
cd backend
npm install
```

Create a `.env` file:

```env
PORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
```

Start backend:

```bash
npm run dev
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## Current Progress

| Phase                                    | Status        |
| ---------------------------------------- | ------------- |
| Phase 1 – Requirements Analysis          | ✅ Complete    |
| Phase 2 – Project Setup                  | ✅ Complete    |
| Phase 3 – Database Design                | ✅ Complete    |
| Phase 4 – Authentication                 | ✅ Complete    |
| Phase 5 – Resume Processing & AI Modules | ⏳ Pending     |
| Phase 6 – Frontend Integration           | ⏳ Pending     |
| Phase 7 – Testing & Deployment           | ⏳ Pending     |

---

## Contributors

### Person 1

* Resume Processing
* ATS Analysis
* AI Modules
* Job Market Analytics

### Person 2

* Database Design
* Backend Development
* Authentication System
* API Development
* Frontend Integration

---

## License

This project is developed for academic and educational purposes.
