import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Dashboard from "./pages/Dashboard";
import Analytics from "./pages/Analytics";
import Roadmap from "./pages/Roadmap";
import Chat from "./pages/Chat";
import UploadResume from "./pages/UploadResume";
import ATSReport from "./pages/ATSReport";
import JobMatch from "./pages/JobMatch";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/roadmap" element={<Roadmap />} />
        <Route path="/chat" element={<Chat />} />
        <Route path="/resume" element={<UploadResume />} />
        <Route path="/ats-report" element={<ATSReport />} />
        <Route path="/job-match" element={<JobMatch />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;