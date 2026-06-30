import mongoose from "mongoose";

const resumeSchema = new mongoose.Schema(
  {
    userId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },
    resumePath: {
        type: String,
      },
    skills: [String],
    education: [String],
    experience: [String],
    projects: [String],
    certifications: [String],
  },
  {
    timestamps: true,
  }
);

export default mongoose.model("Resume", resumeSchema);