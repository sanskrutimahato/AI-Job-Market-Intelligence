import Resume from "../models/Resume.js";

export const uploadResume = async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({
        success: false,
        message: "No resume uploaded",
      });
    }

    const resume = await Resume.create({
      userId: req.user.userId,
      resumePath: req.file.path,
    });

    res.status(201).json({
      success: true,
      message: "Resume uploaded successfully",
      file: {
        filename: req.file.filename,
        path: req.file.path,
      },
      resume,
    });
  } catch (error) {
    console.error(error);

    res.status(500).json({
      success: false,
      message: "Server Error",
    });
  }
};