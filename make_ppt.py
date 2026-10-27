from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
def slide(title, bullets, sub=None):
    s = prs.slides.add_slide(BLANK)
    t = s.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(12), Inches(1))
    t.text_frame.word_wrap = True; t.text_frame.text = title
    t.text_frame.paragraphs[0].font.size = Pt(36); t.text_frame.paragraphs[0].font.bold = True
    y = 1.6
    if sub:
        b = s.shapes.add_textbox(Inches(0.6), Inches(y), Inches(12), Inches(0.7)); b.text_frame.word_wrap=True; b.text_frame.text=sub; b.text_frame.paragraphs[0].font.size=Pt(20); y += 0.9
    for line in bullets:
        b = s.shapes.add_textbox(Inches(0.8), Inches(y), Inches(11.8), Inches(0.8)); b.text_frame.word_wrap=True; b.text_frame.text="• "+line; b.text_frame.paragraphs[0].font.size=Pt(20); y += 0.85
    return s
slide("ChurnSense", ["Customer Churn Predictor"], "An AI/ML project by Vikranth Reddy — B.Tech CSE (AI & ML), Woxsen University")
slide("The Problem", ["Telecom companies lose customers without warning — winning a new customer costs far more than keeping one", "Support teams cannot tell which customers are about to leave", "Retention offers go to everyone instead of the customers who actually need them"])
slide("The Solution", ["ChurnSense predicts a customer's churn risk (0–100%) from 7 inputs", "Tenure, monthly charges, contract type, fiber internet, support calls, paperless billing, senior-citizen status", "Interactive demo: change any input, see the risk instantly — fully in the browser"])
slide("Tech Stack", ["Python + scikit-learn: logistic regression", "Synthetic dataset: 800 telecom customers (seed 42)", "HTML + CSS + vanilla JavaScript demo", "GitHub + Vercel hosting"])
slide("Architecture", ["Inputs: 7 customer features → standardization (train mean / std) → logistic regression → sigmoid → churn probability", "Model exported as model.json; the browser demo reproduces it exactly", "Strongest drivers: support calls, contract type and tenure"])
slide("Demo", ["Try the presets: at-risk new customer, loyal long-term customer, high-risk customer", "At-risk new customer (6 months, $95, 5 support calls) → 93.3% churn risk", "Loyal long-term customer (48 months, 2-year contract) → 1.6% churn risk"])
slide("Results", ["5-fold cross-validated accuracy = 73.5%", "AUC = 0.82 (majority-class baseline: 50.6% — about 1.45x better)", "Churn rate in training data: 50.6%", "Strongest drivers: support calls, short tenure and month-to-month contracts — matching real churn behaviour"])
slide("Future Scope", ["Train on real telecom data with usage and payment-history features", "Add retention recommendations: which offer fits each at-risk customer", "Explain each prediction: which feature raised or lowered the risk", "Track churn risk over time with monthly trend charts"])
slide("Thank You", ["ChurnSense — spot the customers about to leave, before they do."], "Vikranth Reddy · github.com/HVRGAMING2705/churnsense")
out = "/home/hatch/workspace/goals/daily-ai-ml-project-factory/files/AIML_ChurnSense_2026-10-27.pptx"
prs.save(out); print("saved", out, "slides:", len(prs.slides._sldIdLst))
