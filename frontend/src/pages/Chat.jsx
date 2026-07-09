import AppLayout from "../layouts/AppLayout";

const Chat = () => {
  return (
    <AppLayout>
      <div className="p-6">

        <h1 className="text-3xl font-bold mb-8">
          AI Career Mentor
        </h1>

        <div className="grid lg:grid-cols-4 gap-6">

          {/* Suggestions */}
          <div className="bg-[#111827] p-6 rounded-xl border border-gray-800">

            <h2 className="text-lg font-semibold mb-4">
              Suggested Questions
            </h2>

            <div className="space-y-3">

              <button className="w-full text-left bg-[#0f172a] p-3 rounded-lg hover:border-blue-500 border border-transparent transition">
                How can I improve my ATS score?
              </button>

              <button className="w-full text-left bg-[#0f172a] p-3 rounded-lg hover:border-blue-500 border border-transparent transition">
                Which skills should I learn next?
              </button>

              <button className="w-full text-left bg-[#0f172a] p-3 rounded-lg hover:border-blue-500 border border-transparent transition">
                Am I ready for Full Stack roles?
              </button>

              <button className="w-full text-left bg-[#0f172a] p-3 rounded-lg hover:border-blue-500 border border-transparent transition">
                Show trending technologies
              </button>

            </div>

          </div>

          {/* Chat Area */}
          <div className="lg:col-span-3 bg-[#111827] rounded-xl border border-gray-800 flex flex-col">

            {/* Messages */}
            <div className="flex-1 p-6 space-y-4 min-h-[500px]">

              <div className="flex justify-start">
                <div className="bg-[#0f172a] p-4 rounded-xl max-w-lg">
                  Hello 👋
                  <br />
                  I'm your AI Career Mentor.
                </div>
              </div>

              <div className="flex justify-end">
                <div className="bg-blue-600 p-4 rounded-xl max-w-lg">
                  What skills should I learn next?
                </div>
              </div>

              <div className="flex justify-start">
                <div className="bg-[#0f172a] p-4 rounded-xl max-w-lg">
                  Based on your roadmap, focus on:
                  <br />
                  • React Advanced Concepts
                  <br />
                  • Node.js
                  <br />
                  • MongoDB
                  <br />
                  • Docker
                </div>
              </div>

            </div>

            {/* Input */}
            <div className="border-t border-gray-800 p-4">

              <div className="flex gap-3">

                <input
                  type="text"
                  placeholder="Ask your AI mentor..."
                  className="flex-1 bg-[#0f172a] border border-gray-700 rounded-lg px-4 py-3 outline-none focus:border-blue-500"
                />

                <button className="bg-blue-600 px-6 rounded-lg hover:bg-blue-700">
                  Send
                </button>

              </div>

            </div>

          </div>

        </div>

      </div>
    </AppLayout>
  );
};

export default Chat;