import React from "react";

const ResumeCard = () => {
  const resumeData = {
    name: "John Doe",
    skills: ["React", "Node.js", "MongoDB"],
    projects: 3,
    education: "B.Tech Computer Engineering",
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h2 className="text-xl font-semibold mb-4">
        Resume Details
      </h2>

      <p>
        <strong>Name:</strong> {resumeData.name}
      </p>

      <p>
        <strong>Education:</strong> {resumeData.education}
      </p>

      <p>
        <strong>Projects:</strong> {resumeData.projects}
      </p>

      <div className="mt-3">
        <strong>Skills:</strong>

        <div className="flex flex-wrap gap-2 mt-2">
          {resumeData.skills.map((skill, index) => (
            <span
              key={index}
              className="bg-blue-100 text-blue-700 px-3 py-1 rounded"
            >
              {skill}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ResumeCard;