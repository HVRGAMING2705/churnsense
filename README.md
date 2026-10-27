# ChurnSense — Customer Churn Predictor

Logistic regression (scikit-learn) trained on 800 synthetic telecom customers:
tenure, monthly charges, contract type, fiber internet, support calls,
paperless billing, senior-citizen status.

- 5-fold CV accuracy: 73.5%, AUC: 0.82 (majority-class baseline: 50.6%)
- `train.py` trains the model and exports `model.json`
- `index.html` is a single-page demo: the same coefficients run in JavaScript,
  so the browser demo reproduces the Python model exactly — no backend needed.

Live demo: https://churnsense.vercel.app

By Vikranth Reddy — B.Tech CSE (AI & ML), Woxsen University.
