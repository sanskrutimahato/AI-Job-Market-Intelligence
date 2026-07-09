import AppLayout from "../layouts/AppLayout";

const ATSReport = () => {
  return (
    <AppLayout>
      <div className="p-6">

        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold">
            ATS Analysis Report
          </h1>

          <p className="text-gray-400 mt-2">
            Detailed resume compatibility analysis.
          </p>
        </div>

        {/* ATS Score */}
        <div className="bg-[#111827] p-8 rounded-xl border border-gray-800 mb-6">

          <div className="flex flex-col items-center">

            <div className="w-40 h-40 rounded-full border-8 border-blue-500 flex items-center justify-center">

              <span className="text-5xl font-bold text-blue-400">
                85
              </span>

            </div>

            <h2 className="text-2xl font-bold mt-6">
              ATS Score
            </h2>

            <p className="text-green-400 mt-2">
              Excellent Compatibility
            </p>

          </div>

        </div>

        {/* Stats */}
        <div className="grid md:grid-cols-3 gap-6 mb-6">

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Keywords Matched
            </p>

            <h2 className="text-3xl font-bold text-green-400 mt-2">
              78%
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Missing Skills
            </p>

            <h2 className="text-3xl font-bold text-orange-400 mt-2">
              5
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Formatting
            </p>

            <h2 className="text-3xl font-bold text-purple-400 mt-2">
              92%
            </h2>
          </div>

        </div>

        {/* Skills */}
        <div className="grid lg:grid-cols-2 gap-6">

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              Matched Skills
            </h2>

            <div className="flex flex-wrap gap-3">

              <span className="px-4 py-2 bg-green-500/20 text-green-400 rounded-full">
                React
              </span>

              <span className="px-4 py-2 bg-green-500/20 text-green-400 rounded-full">
                Node.js
              </span>

              <span className="px-4 py-2 bg-green-500/20 text-green-400 rounded-full">
                MongoDB
              </span>

              <span className="px-4 py-2 bg-green-500/20 text-green-400 rounded-full">
                JavaScript
              </span>

            </div>

          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              Missing Skills
            </h2>

            <div className="flex flex-wrap gap-3">

              <span className="px-4 py-2 bg-orange-500/20 text-orange-400 rounded-full">
                Docker
              </span>

              <span className="px-4 py-2 bg-orange-500/20 text-orange-400 rounded-full">
                AWS
              </span>

              <span className="px-4 py-2 bg-orange-500/20 text-orange-400 rounded-full">
                Kubernetes
              </span>

            </div>

          </div>

        </div>

        {/* Suggestions */}
        <div className="bg-[#111827] p-6 rounded-xl border border-gray-800 mt-6">

          <h2 className="text-xl font-semibold mb-4">
            Recommendations
          </h2>

          <ul className="space-y-3 text-gray-400">

            <li>
              ✅ Add cloud technologies such as AWS.
            </li>

            <li>
              ✅ Include Docker and deployment experience.
            </li>

            <li>
              ✅ Increase keyword density for target roles.
            </li>

            <li>
              ✅ Add measurable project achievements.
            </li>

          </ul>

        </div>

      </div>
    </AppLayout>
  );
};

export default ATSReport;