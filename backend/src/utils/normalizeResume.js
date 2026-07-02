// src/utils/normalizeResume.js

export const normalizeResume = (data = {}) => {
  return {
    name: data.name || "",
    email: data.email || "",
    phone: data.phone || "",
    linkedin: data.linkedin || "",
    github: data.github || "",
    portfolio: data.portfolio || "",

    // ================= SKILLS =================
    skills: Array.isArray(data.skills)
      ? [...new Set(data.skills.map(s => String(s).trim()))]
      : [],

    // ================= EDUCATION =================
    education: Array.isArray(data.education)
      ? data.education.map((edu) => {
          if (typeof edu === "string") {
            return {
              institution: "",
              degree: edu,
              year: "",
            };
          }

          return {
            institution: edu.institution || "",
            degree: edu.degree || "",
            year: edu.year || "",
          };
        })
      : [],

    // ================= EXPERIENCE =================
    experience: Array.isArray(data.experience)
      ? data.experience.map((exp) => {
          if (typeof exp === "string") {
            return {
              role: exp,
              company: "",
              location: "",
              duration: "",
              description: [],
            };
          }

          return {
            role: exp.role || "",
            company: exp.company || "",
            location: exp.location || "",
            duration: exp.duration || "",
            description: Array.isArray(exp.description)
              ? exp.description.map(d => String(d).trim())
              : [],
          };
        })
      : [],

    // ================= PROJECTS =================
    projects: Array.isArray(data.projects)
      ? data.projects.map((p) => {
          if (typeof p === "string") {
            return {
              title: p,
              tech_stack: "",
              duration: "",
              links: [],
              description: [],
            };
          }

          return {
            title: p.title || "",
            tech_stack: p.tech_stack || "",
            duration: p.duration || "",
            links: Array.isArray(p.links) ? p.links : [],
            description: Array.isArray(p.description) ? p.description : [],
          };
        })
      : [],

    // ================= CERTIFICATIONS =================
    certifications: Array.isArray(data.certifications)
      ? data.certifications.map((c) => {
          if (typeof c === "string") {
            return {
              name: c,
              issuer: "",
              year: "",
            };
          }

          return {
            name: c.name || "",
            issuer: c.issuer || "",
            year: c.year || "",
          };
        })
      : [],

    raw_text: data.raw_text || "",
  };
};