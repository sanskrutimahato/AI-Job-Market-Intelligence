import { useState } from "react";
import AppLayout from "../layouts/AppLayout";
import { getJobMatch } from "../services/jobMatchApi";

const UploadResume = () => {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobMatchScore, setJobMatchScore] = useState(0);
  const [matchedSkills, setMatchedSkills] = useState([]);
  const [missingSkills, setMissingSkills] = useState([]);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
const [analysisDone, setAnalysisDone] = useState(false);
  
const handleAnalyzeResume = async () => {
    console.log("HANDLE ANALYZE CLICKED");

    if (!resumeFile) {
      alert("Please upload a resume");
      return;
    }

    if (!jobDescription.trim()) {
      alert("Please enter a job description");
      return;
    }

    try {
      setLoading(true);

      const response = await getJobMatch(
        resumeFile,
        jobDescription
      );

      console.log("API RESPONSE:", response);

      const result = response.data || response;

      setJobMatchScore(result.job_match || 0);

localStorage.setItem(
  "jobMatchScore",
  result.job_match || 0
);
      setMatchedSkills(result.matched_keywords || []);
      setMissingSkills(result.missing_keywords || []);
      localStorage.setItem(
  "atsScore",
  Math.round((result.job_match || 0) + 50)
);
      setAnalysisDone(true);

    } catch (error) {
      console.error("JOB MATCH ERROR:", error);
      alert("Job Match Analysis Failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <AppLayout>
      <div className="p-6">

        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold">
            Resume Analysis
          </h1>

          <p className="text-gray-400 mt-2">
            Upload your resume and get ATS insights,
            extracted skills, and improvement recommendations.
          </p>
        </div>

        {/* Top Section */}
        <div className="grid lg:grid-cols-3 gap-6">

          {/* Upload Card */}
          <div className="lg:col-span-2 bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              Upload Resume
            </h2>

            <div className="border-2 border-dashed border-gray-700 rounded-xl p-12 text-center hover:border-blue-500 transition">

              <div className="text-6xl mb-4">
                📄
              </div>

              <h3 className="text-xl font-semibold">
                Drag & Drop Resume
              </h3>

              <p className="text-gray-400 mt-2">
                Upload PDF files
              </p>

              <label className="mt-6 inline-block bg-blue-600 px-6 py-3 rounded-lg hover:bg-blue-700 transition cursor-pointer">

                Choose File

                <input
                  type="file"
                  accept=".pdf"
                  className="hidden"
                  onChange={(e) => setResumeFile(e.target.files[0])}
                />

              </label>

              {resumeFile && (
                <p className="mt-4 text-green-400">
                  Selected: {resumeFile.name}
                </p>
              )}

              <p className="text-gray-500 text-sm mt-4">
                Maximum file size: 5 MB
              </p>

              {/* Job Description */}
              <div className="mt-6">

                <label className="block mb-2 text-gray-300">
                  Job Description
                </label>

                <textarea
                  rows="6"
                  value={jobDescription}
                  onChange={(e) =>
                    setJobDescription(e.target.value)
                  }
                  placeholder="Paste job description here..."
                  className="w-full bg-[#0f172a] border border-gray-700 rounded-lg p-4 text-white focus:outline-none focus:border-blue-500"
                />

                <button
                  onClick={handleAnalyzeResume}
                  disabled={loading}
                  className="mt-4 w-full bg-green-600 hover:bg-green-700 rounded-lg py-3 font-semibold transition disabled:opacity-50"
                >
                  {loading
                    ? "Analyzing..."
                    : "Analyze Resume"}
                </button>

              </div>

            </div>

          </div>

          {/* Job Match Score */}
          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              Job Match Score
            </h2>

            <div className="flex flex-col items-center justify-center h-full">

              <div className="w-32 h-32 rounded-full border-8 border-blue-500 flex items-center justify-center">

                <span className="text-4xl font-bold text-blue-400">
                  {Number(jobMatchScore).toFixed(2)}%
                </span>

              </div>

              <p className="text-gray-400 mt-4">
                Resume Compatibility
              </p>

            </div>

          </div>

        </div>

        {/* Results */}
        <div className="grid lg:grid-cols-2 gap-6 mt-6">

          {/* Skills */}
          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              Skills Analysis
            </h2>

            <h3 className="text-green-400 font-semibold mb-3">
              Matched Skills
            </h3>

            <div className="flex flex-wrap gap-3 mb-6">

              {matchedSkills.length > 0 ? (
                matchedSkills.map((skill, index) => (
                  <span
                    key={index}
                    className="px-4 py-2 bg-green-500/20 text-green-400 rounded-full"
                  >
                    {skill}
                  </span>
                ))
              ) : (
                <p className="text-gray-500">
                  No matched skills yet
                </p>
              )}

            </div>

            <h3 className="text-red-400 font-semibold mb-3">
              Missing Skills
            </h3>

            <div className="flex flex-wrap gap-3">

              {missingSkills.length > 0 ? (
                missingSkills.map((skill, index) => (
                  <span
                    key={index}
                    className="px-4 py-2 bg-red-500/20 text-red-400 rounded-full"
                  >
                    {skill}
                  </span>
                ))
              ) : (
                <p className="text-gray-500">
                  No missing skills
                </p>
              )}

            </div>

          </div>

          {/* Summary */}
          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              Resume Summary
            </h2>

            <p className="text-gray-400 leading-7">
              {analysisDone
                ? `Your resume matches ${jobMatchScore.toFixed(
                    2
                  )}% of the job requirements. You currently match ${matchedSkills.length} key skills and are missing ${missingSkills.length} important skills. Focus on learning ${missingSkills.join(
                    ", "
                  )} to improve your chances for this role.`
                : "Upload a resume and job description to generate a real-time job match score and skill gap analysis."}
            </p>

          </div>

        </div>

      </div>
    </AppLayout>
  );
};

export default UploadResume;