import Navbar from "../components/Navbar";

const Home = () => {
  return (
    <>
      <Navbar />

      <div className="min-h-screen bg-[#0b1220] text-white">
  <div className="max-w-6xl mx-auto px-6 py-12">

        {/* Hero Section */}
        <div className="text-center py-20">
          <h1 className="text-5xl font-bold leading-tight">
            AI-Powered Job Market Intelligence Platform
          </h1>

          <p className="mt-6 text-xl text-gray-300 max-w-3xl mx-auto">
            Analyze your resume, improve ATS score,
            identify skill gaps, discover market trends,
            and generate personalized career roadmaps.
          </p>

          <div className="mt-8 flex justify-center gap-4">
            <button className="bg-blue-600 text-white px-6 py-3 rounded">
              Get Started
            </button>

            <button className="border border-gray-600 px-6 py-3 rounded-lg">
              Learn More
            </button>
          </div>
        </div>

        {/* Features Section */}
        <div className="mt-20">
          <h2 className="text-3xl font-bold text-center mb-10">
            Platform Features
          </h2>

          <div className="grid md:grid-cols-3 gap-6">

            <div className="bg-[#111827] border border-gray-800 rounded-xl p-6 hover:border-blue-500 transition">
              <h3 className="text-xl font-semibold mb-3">
                Resume Analysis
              </h3>

              <p className="text-gray-400">
                Extract skills, education, projects,
                certifications, and experience from resumes.
              </p>
            </div>

            <div className="bg-[#111827] border border-gray-800 rounded-xl p-6 hover:border-blue-500 transition">
              <h3 className="text-xl font-semibold mb-3">
                ATS Scoring
              </h3>

              <p className="text-gray-400">
                Evaluate resume compatibility with ATS systems
                and improve visibility.
              </p>
            </div>

            <div className="bg-[#111827] border border-gray-800 rounded-xl p-6 hover:border-blue-500 transition">
              <h3 className="text-xl font-semibold mb-3">
                Career Roadmaps
              </h3>

              <p className="text-gray-400">
                Generate personalized learning paths and
                career growth recommendations.
              </p>
            </div>

          </div>
        </div>

        {/* Stats Section */}
        <div className="mt-24">

          <h2 className="text-4xl font-bold text-center mb-12">
            Platform Impact
          </h2>

          <div className="grid md:grid-cols-4 gap-6">

            <div className="bg-[#111827] p-6 rounded-xl border border-gray-800 text-center">
              <h3 className="text-4xl font-bold text-blue-400">
                82
              </h3>
              <p className="text-gray-400 mt-2">
                Average ATS Score
              </p>
            </div>

            <div className="bg-[#111827] p-6 rounded-xl border border-gray-800 text-center">
              <h3 className="text-4xl font-bold text-green-400">
                78%
              </h3>
              <p className="text-gray-400 mt-2">
                Job Match Accuracy
              </p>
            </div>

            <div className="bg-[#111827] p-6 rounded-xl border border-gray-800 text-center">
              <h3 className="text-4xl font-bold text-purple-400">
                50K+
              </h3>
              <p className="text-gray-400 mt-2">
                Resumes Analyzed
              </p>
            </div>

            <div className="bg-[#111827] p-6 rounded-xl border border-gray-800 text-center">
              <h3 className="text-4xl font-bold text-orange-400">
                1200+
              </h3>
              <p className="text-gray-400 mt-2">
                Career Roadmaps Generated
              </p>
            </div>

          </div>

        </div>

        { /*How it Works */}
                <div className="mt-20">
        <h2 className="text-4xl font-bold text-center mb-12">
            How It Works
        </h2>

        <div className="grid md:grid-cols-3 gap-6">

            <div className="bg-[#111827] border border-gray-800 rounded-xl p-6 text-center hover:border-blue-500 transition">
            <div className="text-5xl font-bold text-blue-400 mb-4">1</div>
            <h3 className="text-xl font-semibold mb-2">
                Upload Resume
            </h3>
            <p className="text-gray-400">
                Upload your resume in PDF format.
            </p>
            </div>

            <div className="bg-[#111827] border border-gray-800 rounded-xl p-6 text-center hover:border-blue-500 transition">
            <div className="text-5xl font-bold text-green-400 mb-4">2</div>
            <h3 className="text-xl font-semibold mb-2">
                Analyze Skills
            </h3>
            <p className="text-gray-400">
                Our system extracts skills and evaluates ATS compatibility.
            </p>
            </div>

            <div className="bg-[#111827] border border-gray-800 rounded-xl p-6 text-center hover:border-blue-500 transition">
            <div className="text-5xl font-bold text-purple-400 mb-4">3</div>
            <h3 className="text-xl font-semibold mb-2">
                Get Insights
            </h3>
            <p className="text-gray-400">
                Receive job trends, recommendations, and career roadmaps.
            </p>
            </div>

        </div>
        </div>
        {/* CTA Section */}
        <div className="mt-24">

          <div className="bg-gradient-to-r from-purple-600 to-blue-600 rounded-3xl p-10 text-center">

            <h2 className="text-4xl font-bold mb-4">
              Start Building Your Career Today
            </h2>

            <p className="text-lg text-purple-100 max-w-2xl mx-auto">
              Analyze your resume, discover skill gaps, improve ATS performance,
              and get personalized career recommendations powered by AI.
            </p>

            <button className="mt-8 bg-white text-black font-semibold px-8 py-3 rounded-xl hover:scale-105 transition">
              Get Started Free
            </button>

          </div>

        </div>
        {/* Footer */}
        <footer className="mt-20 border-t pt-8 pb-8 text-center text-gray-600">
        <p>
            © 2026 AI-Powered Job Market Intelligence Platform
        </p>

        <p className="mt-2">
            Resume Analysis • ATS Optimization • Career Roadmaps
        </p>
        </footer>
            </div>
            </div>
    </>
  );
};

export default Home;