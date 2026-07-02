import Resume from "../models/Resume.js";
import axios from "axios";
import FormData from "form-data";
import fs from "fs";
import { normalizeResume } from "../utils/normalizeResume.js";

// ================= UPLOAD RESUME =================

export const uploadResume = async (req, res) => {
  try {
    console.log("UPLOAD RESUME API HIT");

    if (!req.file) {
      return res.status(400).json({
        success: false,
        message: "No resume uploaded",
      });
    }

    // STEP 1: send file to FastAPI
    const formData = new FormData();
    formData.append("file", fs.createReadStream(req.file.path));

    const parserResponse = await axios.post(
      "http://127.0.0.1:8000/api/parseResume",
      formData,
      {
        headers: formData.getHeaders(),
        maxBodyLength: Infinity,
        maxContentLength: Infinity,
      }
    );

    const rawData = parserResponse.data?.data || {};
    const parsedData = normalizeResume(rawData);

    // ✅ FINAL FIX HERE (MOST IMPORTANT)
    const userId = req.user?.userId;

    if (!userId) {
      return res.status(401).json({
        success: false,
        message: "Invalid user token (userId missing)",
      });
    }

    const resume = await Resume.create({
      userId: req.user.userId,
      resumePath: req.file.path,
      skills: parsedData.skills || [],
      education: parsedData.education || [],
      experience: parsedData.experience || [],
      projects: parsedData.projects || [],
      certifications: parsedData.certifications || [],
    });

    return res.status(201).json({
      success: true,
      message: "Resume uploaded successfully",
      parsedData,
      resume,
    });

  } catch (error) {
    return res.status(500).json({
      success: false,
      message: "Server Error",
      error: error.message,
    });
  }
};

// ================= GET LATEST RESUME =================

export const getMyResume = async (req, res) => {
  try {
    // same fix here
    const userId = req.user?.userId;

    if (!userId) {
      return res.status(401).json({
        success: false,
        message: "Invalid user token",
      });
    }

    const resume = await Resume.findOne({ userId }).sort({
      createdAt: -1,
    });

    if (!resume) {
      return res.status(404).json({
        success: false,
        message: "Resume not found",
      });
    }

    return res.status(200).json({
      success: true,
      resume,
    });

  } catch (error) {
    return res.status(500).json({
      success: false,
      message: "Server Error",
      error: error.message,
    });
  }
};