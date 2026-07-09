import AppLayout from "../layouts/AppLayout";

const Analytics = () => {
  return (
    <AppLayout>
      <div className="p-6">

        <h1 className="text-3xl font-bold mb-8">
          Market Analytics
        </h1>

        {/* Stats */}
        <div className="grid md:grid-cols-4 gap-6 mb-8">

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">ATS Score</p>
            <h2 className="text-4xl font-bold text-blue-400 mt-2">
              85
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">Skill Match</p>
            <h2 className="text-4xl font-bold text-green-400 mt-2">
              78%
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">Missing Skills</p>
            <h2 className="text-4xl font-bold text-orange-400 mt-2">
              5
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">Market Readiness</p>
            <h2 className="text-4xl font-bold text-purple-400 mt-2">
              82
            </h2>
          </div>

        </div>

        {/* Charts */}
        <div className="grid md:grid-cols-2 gap-6">

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <h2 className="text-xl font-semibold mb-4">
              Skill Demand Trend
            </h2>

            <div className="h-64 bg-[#0f172a] rounded-lg flex items-center justify-center text-gray-500">
              Chart Placeholder
            </div>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <h2 className="text-xl font-semibold mb-4">
              Salary Insights
            </h2>

            <div className="h-64 bg-[#0f172a] rounded-lg flex items-center justify-center text-gray-500">
              Chart Placeholder
            </div>
          </div>

        </div>

        {/* Market Insights */}
        <div className="grid md:grid-cols-2 gap-6 mt-6">

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              Top Skills In Demand
            </h2>

            <div className="space-y-4">

              <div>
                <div className="flex justify-between">
                  <span>Python</span>
                  <span>92%</span>
                </div>

                <div className="h-2 bg-gray-700 rounded-full mt-2">
                  <div className="h-2 w-[92%] bg-purple-500 rounded-full"></div>
                </div>
              </div>

              <div>
                <div className="flex justify-between">
                  <span>SQL</span>
                  <span>88%</span>
                </div>

                <div className="h-2 bg-gray-700 rounded-full mt-2">
                  <div className="h-2 w-[88%] bg-blue-500 rounded-full"></div>
                </div>
              </div>

              <div>
                <div className="flex justify-between">
                  <span>Machine Learning</span>
                  <span>80%</span>
                </div>

                <div className="h-2 bg-gray-700 rounded-full mt-2">
                  <div className="h-2 w-[80%] bg-green-500 rounded-full"></div>
                </div>
              </div>

            </div>

          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              Top Hiring Locations
            </h2>

            <div className="space-y-3 text-gray-300">

              <p>📍 Bangalore</p>
              <p>📍 Hyderabad</p>
              <p>📍 Pune</p>
              <p>📍 Mumbai</p>
              <p>📍 Gurgaon</p>

            </div>

          </div>

        </div>

        {/* Industry Insights */}
      <div className="mt-6 bg-[#111827] p-6 rounded-xl border border-gray-800">

        <h2 className="text-xl font-semibold mb-4">
          Market Insights
        </h2>

        <div className="grid md:grid-cols-3 gap-6">

          <div>
            <h3 className="font-semibold text-blue-400 mb-2">
              Fastest Growing Skill
            </h3>

            <p className="text-gray-400">
              Generative AI demand has increased by 120% this year.
            </p>
          </div>

          <div>
            <h3 className="font-semibold text-green-400 mb-2">
              Highest Paying Role
            </h3>

            <p className="text-gray-400">
              Machine Learning Engineer remains one of the highest paying tech roles.
            </p>
          </div>

          <div>
            <h3 className="font-semibold text-purple-400 mb-2">
              Hiring Trend
            </h3>

            <p className="text-gray-400">
              Companies are prioritizing AI, Cloud, and Data Engineering skills.
            </p>
          </div>

        </div>

      </div>

      </div>
    </AppLayout>
  );
};

export default Analytics;