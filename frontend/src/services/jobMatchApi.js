const API_URL = "http://127.0.0.1:8000/api/jobMatch";

export const getJobMatch = async (
  resumeFile,
  jobDescription
) => {
  const formData = new FormData();

  formData.append("resume", resumeFile);
  formData.append("job_description", jobDescription);

  const response = await fetch(API_URL, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Job Match API Failed");
  }

  return await response.json();
};