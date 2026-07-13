import AppLayout from "../layouts/AppLayout";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const navigate = useNavigate();

  return (
    <AppLayout>
      <div className="p-4 md:p-6">

        {/* Header */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">

          <div className="md:col-span-2 bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl p-6">

            <h1 className="text-2xl md:text-3xl font-bold">
              Welcome Back 👋
            </h1>

            <p className="text-blue-100 mt-2">
              Track your career growth, ATS score, and market readiness.
            </p>

          </div>

          <div className="bg-[#111827] rounded-2xl p-6 border border-gray-800">

            <h3 className="text-lg font-semibold">
              Profile
            </h3>

            <div className="flex items-center gap-4 mt-4">

              <div className="w-12 h-12 rounded-full bg-purple-600 flex items-center justify-center font-bold">
                JD
              </div>

              <div>
                <p className="font-semibold">
                  John Doe
                </p>

                <p className="text-sm text-gray-400">
                  Computer Engineering
                </p>
              </div>

            </div>

            <div className="mt-4 text-green-400 text-sm">
              ● Active
            </div>

          </div>

        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-6 mb-6">

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">ATS Score</p>
            <h2 className="text-4xl font-bold text-blue-400 mt-2">
  {localStorage.getItem("atsScore") || 0}
</h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">Job Match</p>
            <h2 className="text-4xl font-bold text-green-400 mt-2">
  {localStorage.getItem("jobMatchScore") || 0}%
</h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">Market Readiness</p>
            <h2 className="text-4xl font-bold text-purple-400 mt-2">
              82
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">Active Roadmaps</p>
            <h2 className="text-4xl font-bold text-orange-400 mt-2">
              6
            </h2>
          </div>

        </div>

        {/* Quick Actions */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">

          <div
            onClick={() => navigate("/resume")}
            className="bg-[#111827] p-6 rounded-xl border border-gray-800 hover:border-blue-500 transition cursor-pointer"
          >
            <h3 className="font-semibold text-lg mb-2">
              Resume Analysis
            </h3>

            <p className="text-gray-400 text-sm">
              Analyze uploaded resume and extract skills.
            </p>
          </div>

          <div
            onClick={() => navigate("/roadmap")}
            className="bg-[#111827] p-6 rounded-xl border border-gray-800 hover:border-green-500 transition cursor-pointer"
          >
            <h3 className="font-semibold text-lg mb-2">
              Generate Roadmap
            </h3>

            <p className="text-gray-400 text-sm">
              Create a personalized learning roadmap.
            </p>
          </div>

          <div
            onClick={() => navigate("/chat")}
            className="bg-[#111827] p-6 rounded-xl border border-gray-800 hover:border-purple-500 transition cursor-pointer"
          >
            <h3 className="font-semibold text-lg mb-2">
              AI Mentor
            </h3>

            <p className="text-gray-400 text-sm">
              Ask career and skill-related questions.
            </p>
          </div>

        </div>

        {/* Progress + Skills */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

          {/* Progress */}
          <div className="md:col-span-2">

            <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

              <h2 className="text-xl font-semibold mb-4">
                Progress Overview
              </h2>

              <div className="h-64 flex items-center justify-center text-gray-500 bg-[#0f172a] rounded-lg">
                Career Growth Graph
              </div>

            </div>

          </div>

          {/* Skills */}
          <div>

            <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

              <h2 className="text-xl font-semibold mb-4">
                Top Skills In Demand
              </h2>

              <div className="space-y-5">

                <div>
                  <div className="flex justify-between text-sm md:text-base">
                    <span>Python</span>
                    <span>92%</span>
                  </div>

                  <div className="h-2 bg-gray-700 rounded-full mt-2">
                    <div className="h-2 w-[92%] bg-purple-500 rounded-full"></div>
                  </div>
                </div>

                <div>
                  <div className="flex justify-between text-sm md:text-base">
                    <span>SQL</span>
                    <span>88%</span>
                  </div>

                  <div className="h-2 bg-gray-700 rounded-full mt-2">
                    <div className="h-2 w-[88%] bg-pink-500 rounded-full"></div>
                  </div>
                </div>

                <div>
                  <div className="flex justify-between text-sm md:text-base">
                    <span>Machine Learning</span>
                    <span>80%</span>
                  </div>

                  <div className="h-2 bg-gray-700 rounded-full mt-2">
                    <div className="h-2 w-[80%] bg-blue-500 rounded-full"></div>
                  </div>
                </div>

                <div>
                  <div className="flex justify-between text-sm md:text-base">
                    <span>Power BI</span>
                    <span>70%</span>
                  </div>

                  <div className="h-2 bg-gray-700 rounded-full mt-2">
                    <div className="h-2 w-[70%] bg-green-500 rounded-full"></div>
                  </div>
                </div>

              </div>

            </div>

          </div>

        </div>

      </div>
    </AppLayout>
  );
};

export default Dashboard;