import express from "express";

import upload from "../config/multer.js";
import { uploadResume } from "../controllers/resumeController.js";
import authMiddleware from "../middleware/authMiddleware.js";

const router = express.Router();

router.post(
  "/uploadResume",
  authMiddleware,
  upload.single("resume"),
  uploadResume
);

export default router;