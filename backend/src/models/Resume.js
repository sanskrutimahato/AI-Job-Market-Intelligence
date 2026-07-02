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

education: [mongoose.Schema.Types.Mixed],

experience: [mongoose.Schema.Types.Mixed],

projects: [mongoose.Schema.Types.Mixed],

certifications: [mongoose.Schema.Types.Mixed],
  },
  {
    timestamps: true,
  }
);

export default mongoose.model("Resume", resumeSchema);