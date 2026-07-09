import Sidebar from "../components/Sidebar";

const AppLayout = ({ children }) => {
  return (
    <div className="min-h-screen bg-[#0b1220] text-white">

      {/* Mobile Navbar */}
      <div className="md:hidden bg-[#111827] border-b border-gray-800 p-4">

        <h2 className="text-xl font-bold">
          JobIntel AI
        </h2>

      </div>

      <div className="flex">

        <Sidebar />

        <main className="flex-1 p-4 md:p-6 overflow-y-auto">
          {children}
        </main>

      </div>

    </div>
  );
};

export default AppLayout;