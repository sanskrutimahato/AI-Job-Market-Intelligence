import AppLayout from "../layouts/AppLayout";

const UploadResume = () => {
  return (
    <AppLayout>
      <div className="p-6">

        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold">
            Resume Analysis
          </h1>

          <p className="text-gray-400 mt-2">
            Upload your resume and get ATS insights, extracted skills, and improvement recommendations.
          </p>
        </div>

        {/* Top Section */}
        <div className="grid lg:grid-cols-3 gap-6">

          {/* Upload Area */}
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
                Upload PDF or DOCX files
              </p>

              <button className="mt-6 bg-blue-600 px-6 py-3 rounded-lg hover:bg-blue-700 transition">
                Choose File
              </button>

              <p className="text-gray-500 text-sm mt-4">
                Maximum file size: 5 MB
              </p>

            </div>

          </div>

          {/* ATS Score */}
          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              ATS Score
            </h2>

            <div className="flex flex-col items-center justify-center h-full">

              <div className="w-32 h-32 rounded-full border-8 border-blue-500 flex items-center justify-center">

                <span className="text-4xl font-bold text-blue-400">
                  85
                </span>

              </div>

              <p className="text-gray-400 mt-4">
                Resume Compatibility
              </p>

            </div>

          </div>

        </div>

        {/* Middle Cards */}
        <div className="grid md:grid-cols-3 gap-6 mt-6">

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Experience
            </p>

            <h2 className="text-3xl font-bold text-green-400 mt-2">
              2 Years
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Projects
            </p>

            <h2 className="text-3xl font-bold text-purple-400 mt-2">
              3
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Skills Found
            </p>

            <h2 className="text-3xl font-bold text-orange-400 mt-2">
              12
            </h2>
          </div>

        </div>

        {/* Bottom Section */}
        <div className="grid lg:grid-cols-2 gap-6 mt-6">

          {/* Skills */}
          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              Extracted Skills
            </h2>

            <div className="flex flex-wrap gap-3">

              <span className="px-4 py-2 bg-blue-500/20 text-blue-400 rounded-full">
                React
              </span>

              <span className="px-4 py-2 bg-green-500/20 text-green-400 rounded-full">
                Node.js
              </span>

              <span className="px-4 py-2 bg-purple-500/20 text-purple-400 rounded-full">
                MongoDB
              </span>

              <span className="px-4 py-2 bg-orange-500/20 text-orange-400 rounded-full">
                Express
              </span>

              <span className="px-4 py-2 bg-cyan-500/20 text-cyan-400 rounded-full">
                JavaScript
              </span>

              <span className="px-4 py-2 bg-pink-500/20 text-pink-400 rounded-full">
                Git
              </span>

            </div>

          </div>

          {/* Summary */}
          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              Resume Summary
            </h2>

            <p className="text-gray-400 leading-7">
              Candidate demonstrates strong MERN stack knowledge with project experience in React, Node.js, and MongoDB. Resume structure is ATS-friendly and contains relevant technical keywords. Adding cloud technologies and Docker could further improve market readiness.
            </p>

          </div>

        </div>

      </div>
    </AppLayout>
  );
};

export default UploadResume;