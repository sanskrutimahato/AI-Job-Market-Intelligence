import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <div className="hidden md:flex w-64 min-h-screen bg-[#111827] text-white p-6 border-r border-gray-800 flex-col">

      <h2 className="text-2xl font-bold mb-8">
        JobIntel AI
      </h2>

      <nav className="flex flex-col gap-4">

        <Link
          to="/dashboard"
          className="text-gray-300 hover:text-blue-400 transition"
        >
          Dashboard
        </Link>

        <Link
          to="/resume"
          className="text-gray-300 hover:text-blue-400 transition"
        >
          Resume Analysis
        </Link>

        <Link
          to="/analytics"
          className="text-gray-300 hover:text-blue-400 transition"
        >
          Analytics
        </Link>

        <Link
          to="/job-match"
          className="text-gray-300 hover:text-blue-400 transition"
        >
          Job Match
        </Link>

        <Link
          to="/roadmap"
          className="text-gray-300 hover:text-blue-400 transition"
        >
          Roadmap
        </Link>

        <Link
          to="/chat"
          className="text-gray-300 hover:text-blue-400 transition"
        >
          AI Mentor
        </Link>

      </nav>

    </div>
  );
};

export default Sidebar;