import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-[#111827] border-b border-gray-800">
      <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">

        <h1 className="text-xl font-bold text-white">
          JobIntel AI
        </h1>

        <div className="flex gap-6 text-gray-300">

          <Link to="/" className="hover:text-blue-400">
            Home
          </Link>

          <Link to="/dashboard" className="hover:text-blue-400">
            Dashboard
          </Link>

          <Link to="/analytics" className="hover:text-blue-400">
            Analytics
          </Link>

          <Link to="/roadmap" className="hover:text-blue-400">
            Roadmap
          </Link>

          <Link to="/chat" className="hover:text-blue-400">
            AI Mentor
          </Link>

        </div>

        <Link
          to="/login"
          className="bg-blue-600 px-4 py-2 rounded-lg hover:bg-blue-700"
        >
          Login
        </Link>

      </div>
    </nav>
  );
};

export default Navbar;