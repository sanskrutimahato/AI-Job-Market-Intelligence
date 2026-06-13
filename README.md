# AI Job Market Intelligence

A full-stack job market intelligence platform that combines a React frontend with a TypeScript/Node backend for resume uploads, analytics, authentication, and career insights.

## Summary

This project provides a modern web application for job seekers to upload resumes, view analytics, access career roadmap guidance, and interact via chat features. The frontend delivers a responsive user experience while the backend handles authentication, resume processing, and persistence.

## Tech Stack

- Frontend
  - React 19
  - Vite
  - React Router DOM
  - Axios
  - ESLint

- Backend
  - Node.js
  - TypeScript
  - Express 5
  - MongoDB via Mongoose
  - JWT authentication
  - Multer file upload
  - dotenv + CORS

## Structure

- `frontend/` — React single-page application
- `backend/` — TypeScript Express API

## Run Locally

1. Install dependencies in each folder:
   - `cd backend && npm install`
   - `cd frontend && npm install`
2. Start backend and frontend separately.

## Notes

- Add a `.env` file for backend database and JWT configuration.
- Ignore `node_modules`, build output, and environment files.
