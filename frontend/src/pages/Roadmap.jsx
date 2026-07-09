import AppLayout from "../layouts/AppLayout";

const Roadmap = () => {
  return (
    <AppLayout>
      <div className="p-6">

        <h1 className="text-3xl font-bold mb-8">
          Career Roadmap
        </h1>

        {/* Overview Cards */}
        <div className="grid md:grid-cols-3 gap-6 mb-8">

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Current Role
            </p>

            <h2 className="text-2xl font-bold mt-2 text-blue-400">
              Frontend Developer
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Target Role
            </p>

            <h2 className="text-2xl font-bold mt-2 text-green-400">
              Full Stack Developer
            </h2>
          </div>

          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">
            <p className="text-gray-400">
              Completion
            </p>

            <h2 className="text-2xl font-bold mt-2 text-purple-400">
              45%
            </h2>
          </div>

        </div>

        {/* Career Tower */}
        <div className="flex flex-col items-center mt-12">

          {/* Achievement */}
          <div className="bg-gradient-to-r from-yellow-500 to-orange-500 p-6 rounded-2xl text-center w-full max-w-md shadow-lg opacity-60">
            <div className="text-5xl mb-2">🏆</div>

            <h2 className="text-2xl font-bold">
              Full Stack Developer
            </h2>

            <p className="text-sm mt-2">
              Reach Level 5 to unlock
            </p>
          </div>

          {/* XP Card */}
          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800 mb-8 w-full max-w-md mt-4">
            <div className="flex justify-between items-center">

              <div>
                <p className="text-gray-400">
                  Experience Points
                </p>

                <h2 className="text-3xl font-bold text-yellow-400">
                  450 XP
                </h2>
              </div>

              <div className="text-right">
                <p className="text-gray-400">
                  Next Level
                </p>

                <h3 className="text-blue-400 font-semibold">
                  Node.js
                </h3>
              </div>

            </div>
          </div>

          {/* Ladder */}
          <div className="flex flex-col items-center mt-4">

            {/* MongoDB */}
            <div className="h-12 border-l-4 border-gray-600"></div>

            <div className="bg-[#111827] opacity-70 border border-gray-700 rounded-full w-24 h-24 flex flex-col justify-center items-center">

              <span className="text-2xl">🔒</span>

              <span className="text-[10px] text-gray-500">
                LEVEL 5
              </span>

              <span className="text-xs">
                MongoDB
              </span>

            </div>

            {/* Node */}
            <div className="h-12 border-l-4 border-gray-600"></div>

            <div className="bg-[#111827] opacity-70 border border-gray-700 rounded-full w-24 h-24 flex flex-col justify-center items-center">

              <span className="text-2xl">🔒</span>

              <span className="text-[10px] text-gray-500">
                LEVEL 4
              </span>

              <span className="text-xs">
                Node.js
              </span>

            </div>

            {/* React Current */}
            <div className="h-12 border-l-4 border-blue-500"></div>

            <div className="relative bg-[#111827] border-2 border-blue-500 shadow-[0_0_30px_rgba(59,130,246,0.5)] rounded-full w-32 h-32 flex flex-col justify-center items-center animate-pulse">

              <span className="absolute -top-4 bg-blue-500 px-3 py-1 rounded-full text-xs font-semibold">
                YOU ARE HERE
              </span>

              <span className="text-3xl">
                🚀
              </span>

              <span className="text-[10px] text-blue-300">
                LEVEL 3
              </span>

              <span className="font-semibold">
                React.js
              </span>

            </div>

            {/* JavaScript */}
            <div className="h-12 border-l-4 border-green-500"></div>

            <div className="bg-[#111827] border border-green-500 shadow-[0_0_20px_rgba(34,197,94,0.3)] rounded-full w-24 h-24 flex flex-col justify-center items-center">

              <span className="text-2xl">
                ✅
              </span>

              <span className="text-[10px] text-green-300">
                LEVEL 2
              </span>

              <span className="text-xs">
                JavaScript
              </span>

            </div>

            {/* HTML/CSS */}
            <div className="h-12 border-l-4 border-green-500"></div>

            <div className="bg-[#111827] border border-green-500 shadow-[0_0_20px_rgba(34,197,94,0.3)] rounded-full w-24 h-24 flex flex-col justify-center items-center">

              <span className="text-2xl">
                ✅
              </span>

              <span className="text-[10px] text-green-300">
                LEVEL 1
              </span>

              <span className="text-xs">
                HTML/CSS
              </span>

            </div>

          </div>

        </div>

      </div>
    </AppLayout>
  );
};

export default Roadmap;