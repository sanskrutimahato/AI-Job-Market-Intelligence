const mongoose = require("mongoose");

const atsReportSchema = new mongoose.Schema(
  {
    userId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },

    resumeId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Resume",
      required: true,
    },

    atsScore: {
      type: Number,
      default: 0,
    },

    jobMatchScore: {
      type: Number,
      default: 0,
    },

    skillGap: [String],

    readinessScore: {
      type: Number,
      default: 0,
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model("ATSReport", atsReportSchema);