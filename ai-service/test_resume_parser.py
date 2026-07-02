from pprint import pprint

from app.services.resume_parser import parse_resume


resume = parse_resume("uploads/resume.pdf")

print("\n========== COMPLETE RESUME ==========\n")

pprint(resume)