import AppLayout from "../layouts/AppLayout";

const JobMatch = () => {
  return (
    <AppLayout>
      <div className="p-6">

        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold">
            Job Match Analysis
          </h1>

          <p className="text-gray-400 mt-2">
            AI-powered matching between your resume and current market opportunities.
          </p>
        </div>

        {/* Summary Cards */}
        <div className="grid md:grid-cols-4 gap-6 mb-8">

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Match Score
            </p>

            <h2 className="text-4xl font-bold text-green-400 mt-2">
              78%
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Jobs Found
            </p>

            <h2 className="text-4xl font-bold text-blue-400 mt-2">
              124
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Missing Skills
            </p>

            <h2 className="text-4xl font-bold text-orange-400 mt-2">
              5
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Readiness
            </p>

            <h2 className="text-4xl font-bold text-purple-400 mt-2">
              82%
            </h2>
          </div>

        </div>

        {/* Best Matches */}
        <div className="bg-[#111827] p-6 rounded-xl border border-gray-800 mb-6">

          <h2 className="text-xl font-semibold mb-4">
            Best Matching Roles
          </h2>

          <div className="space-y-4">

            <div className="bg-[#0f172a] p-4 rounded-lg flex justify-between items-center">
              <div>
                <h3 className="font-semibold">
                  Frontend Developer
                </h3>
                <p className="text-gray-400 text-sm">
                  React • JavaScript • Tailwind
                </p>
              </div>

              <span className="text-green-400 font-bold">
                92%
              </span>
            </div>

            <div className="bg-[#0f172a] p-4 rounded-lg flex justify-between items-center">
              <div>
                <h3 className="font-semibold">
                  MERN Stack Developer
                </h3>
                <p className="text-gray-400 text-sm">
                  React • Node • MongoDB
                </p>
              </div>

              <span className="text-blue-400 font-bold">
                85%
              </span>
            </div>

            <div className="bg-[#0f172a] p-4 rounded-lg flex justify-between items-center">
              <div>
                <h3 className="font-semibold">
                  Full Stack Developer
                </h3>
                <p className="text-gray-400 text-sm">
                  React • Node • MongoDB • Docker
                </p>
              </div>

              <span className="text-orange-400 font-bold">
                72%
              </span>
            </div>

          </div>

        </div>

        {/* Skill Gap */}
        <div className="grid lg:grid-cols-2 gap-6">

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              Skills You Have
            </h2>

            <div className="flex flex-wrap gap-3">

              <span className="px-4 py-2 bg-green-500/20 text-green-400 rounded-full">
                React
              </span>

              <span className="px-4 py-2 bg-green-500/20 text-green-400 rounded-full">
                JavaScript
              </span>

              <span className="px-4 py-2 bg-green-500/20 text-green-400 rounded-full">
                Node.js
              </span>

              <span className="px-4 py-2 bg-green-500/20 text-green-400 rounded-full">
                MongoDB
              </span>

            </div>

          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-xl font-semibold mb-4">
              Skills To Learn
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

              <span className="px-4 py-2 bg-orange-500/20 text-orange-400 rounded-full">
                CI/CD
              </span>

            </div>

          </div>

        </div>

        {/* Recommendation */}
        <div className="bg-[#111827] p-6 rounded-xl border border-gray-800 mt-6">

          <h2 className="text-xl font-semibold mb-4">
            AI Recommendation
          </h2>

          <p className="text-gray-400 leading-7">
            Based on your current skill set, you are highly aligned with
            Frontend and MERN Stack roles. Learning Docker, AWS, and CI/CD
            practices can significantly increase your chances of securing
            Full Stack Developer positions.
          </p>

        </div>

      </div>
    </AppLayout>
  );
};

export default JobMatch;