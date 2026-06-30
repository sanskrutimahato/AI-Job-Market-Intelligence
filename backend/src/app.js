import connectDB from "./config/db.js";
import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import authRoutes from "./routes/authRoutes.js";
import authMiddleware from "./middleware/authMiddleware.js";
import resumeRoutes from "./routes/resumeRoutes.js";

dotenv.config();
connectDB();
const app = express();

app.use(cors());
app.use(express.json());
app.use("/api/auth", authRoutes);
app.use("/api/resume", resumeRoutes);

app.get("/", (_req, res) => {
  res.send("Backend Running");
});

const PORT = process.env.PORT || 5000;

app.get(
  "/api/protected",
  authMiddleware,
  (req, res) => {
    res.json({
      message: "Protected route accessed",
      user: req.user,
    });
  }
);

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});