import json, numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.metrics import accuracy_score, roc_auc_score

rng = np.random.default_rng(42)
n = 800
tenure = rng.uniform(0, 72, n)
monthly = rng.uniform(20, 120, n)
contract = rng.integers(0, 3, n).astype(float)   # 0 month-to-month, 1 one-year, 2 two-year
fiber = rng.integers(0, 2, n).astype(float)
calls = rng.integers(0, 11, n).astype(float)
paperless = rng.integers(0, 2, n).astype(float)
senior = rng.integers(0, 2, n).astype(float)
# Generative churn logit: short tenure, high bills, month-to-month, fiber
# (pricier, more complaints) and many support calls raise churn risk.
logit = (-1.2 - 0.030*tenure + 0.018*monthly - 0.9*contract + 0.5*fiber
         + 0.28*calls + 0.3*paperless + 0.2*senior)
p = 1/(1+np.exp(-logit))
y = (rng.random(n) < p).astype(int)
X = np.column_stack([tenure, monthly, contract, fiber, calls, paperless, senior])
names = ["tenure_months","monthly_charges","contract","is_fiber","support_calls","paperless_billing","is_senior"]
mu, sd = X.mean(0), X.std(0)
Xs = (X - mu)/sd
model = LogisticRegression(max_iter=1000, C=1.0).fit(Xs, y)
kf = StratifiedKFold(5, shuffle=True, random_state=42)
pred_cv = cross_val_predict(LogisticRegression(max_iter=1000, C=1.0), Xs, y, cv=kf)
proba_cv = cross_val_predict(LogisticRegression(max_iter=1000, C=1.0), Xs, y, cv=kf, method="predict_proba")[:,1]
acc = float(accuracy_score(y, pred_cv)); auc = float(roc_auc_score(y, proba_cv))
base = float(max(y.mean(), 1-y.mean()))
print(f"CV accuracy={acc:.3f} AUC={auc:.3f} churn_rate={y.mean():.3f} baseline={base:.3f}")
print("coef", model.coef_, "intercept", model.intercept_)
mj = {"features": names, "means": mu.tolist(), "stds": sd.tolist(),
      "coef": model.coef_[0].tolist(), "intercept": float(model.intercept_[0]),
      "metrics": {"cv_accuracy": acc, "cv_auc": auc, "churn_rate": float(y.mean()), "baseline_accuracy": base, "n": n}}
with open("model.json","w") as f: json.dump(mj, f, indent=1)
def predict(v):
    z = (np.array(v)-mu)/sd
    return float(1/(1+np.exp(-(model.intercept_[0] + z @ model.coef_[0]))))
samples = [[6,95,0,1,5,1,0],[48,45,2,0,0,0,0],[2,110,0,1,8,1,1],[36,60,1,0,1,0,0],[60,80,2,1,2,1,0]]
for s in samples: print(s, round(predict(s),4))
