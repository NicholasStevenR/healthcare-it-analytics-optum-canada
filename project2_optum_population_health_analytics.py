"""
Optum Canada Project 2: Population Health Risk Stratification Analytics
XmR (high-risk outreach completion rate) + p-chart (30-day readmission rate)
Author: Nicholas Steven | github.com/nicholasstevenr
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE   = "#1F4E79"
ORANGE = "#E36C09"
TEAL   = "#00B0A8"
RED    = "#C00000"
LGREY  = "#F2F2F2"

np.random.seed(77)

def outreach_xmr(n=24):
    base  = 72.4
    noise = np.random.normal(0, 0.9, n)
    x = base + noise
    x[3]  = 62.2   # COVID clinic access loss
    x[12] = 82.8   # OptumIQ predictive model v2.0 deployment
    x[20] = 61.8   # staffing agency contract gap
    mr     = np.abs(np.diff(x))
    mr_bar = mr.mean()
    x_bar  = x.mean()
    sigma  = mr_bar / 1.128
    ucl    = min(100.0, x_bar + 3 * sigma)
    lcl    = max(0.0,   x_bar - 3 * sigma)
    return x, x_bar, ucl, lcl

def readmission_pchart(n=24):
    p_bar = 0.084
    ni    = 400
    ucl   = p_bar + 3 * np.sqrt(p_bar * (1 - p_bar) / ni)
    lcl   = max(0.0, p_bar - 3 * np.sqrt(p_bar * (1 - p_bar) / ni))
    base  = np.random.normal(p_bar, 0.003, n)
    p     = np.clip(base, max(0, p_bar - 0.012), p_bar + 0.012)
    p[5]  = 0.128   # COVID rapid discharge acceleration
    p[13] = 0.044   # Enhanced Discharge Navigation Program
    p[21] = 0.134   # winter respiratory surge
    return p, p_bar, ucl, lcl

def plot_charts():
    months = [f"M{i+1}" for i in range(24)]
    x_vals, x_bar, ucl_x, lcl_x = outreach_xmr()
    p_vals, p_bar, ucl_p, lcl_p = readmission_pchart()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4))
    fig.patch.set_facecolor("white")

    # Left: High-Risk Outreach XmR
    ax1.set_facecolor(LGREY)
    ax1.plot(range(24), x_vals, color=BLUE, marker="o", markersize=4, linewidth=1.6, zorder=3)
    ax1.axhline(x_bar, color=TEAL, linestyle="--", linewidth=1.2, label=f"X-bar={x_bar:.1f}%")
    ax1.axhline(ucl_x, color=RED,  linestyle=":",  linewidth=1.2, label=f"UCL={ucl_x:.1f}%")
    ax1.axhline(lcl_x, color=RED,  linestyle=":",  linewidth=1.2, label=f"LCL={lcl_x:.1f}%")

    ooc = [i for i in range(24) if x_vals[i] > ucl_x or x_vals[i] < lcl_x]
    for i in ooc:
        ax1.plot(i, x_vals[i], "o", color=ORANGE, markersize=9, zorder=4)

    ann = {3: "COVID\nClinic Access Loss", 12: "OptumIQ\nModel v2.0", 20: "Staffing\nAgency Gap"}
    for i, lbl in ann.items():
        offset = 10 if x_vals[i] > x_bar else -28
        ax1.annotate(lbl, (i, x_vals[i]), textcoords="offset points",
                     xytext=(0, offset), fontsize=6.5, ha="center", color=ORANGE, fontweight="bold")

    # Risk tier mix
    cats   = ["High Risk\n28.4%", "Rising Risk\n42.4%", "Moderate\n18.4%", "Stable\n10.8%"]
    c_vals = [28.4, 42.4, 18.4, 10.8]
    c_col  = [BLUE, TEAL, ORANGE, RED]
    for j, (lbl, val, col) in enumerate(zip(cats, c_vals, c_col)):
        ax1.bar(14.8 + j * 2.1, val * 0.06, 1.6, bottom=lcl_x + 0.4,
                color=col, alpha=0.82, zorder=3)
        ax1.text(14.8 + j * 2.1, lcl_x + 0.4 + val * 0.06 + 0.2, lbl.split("\n")[1],
                 ha="center", fontsize=5.5, fontweight="bold")
        ax1.text(14.8 + j * 2.1, lcl_x - 1.2, lbl.split("\n")[0], ha="center", fontsize=5.5, color=col)

    ax1.set_xticks(range(24))
    ax1.set_xticklabels(months, fontsize=6.5, rotation=45)
    ax1.set_ylabel("High-Risk Members with Completed Outreach Contact (%)", fontsize=8)
    ax1.set_title("High-Risk Member Outreach Completion Rate XmR\n(X-bar=72.4% | OptumIQ +10.4pp | COVID -10.2pp | HQO QIP Benchmark)", fontsize=9, fontweight="bold", color=BLUE)
    ax1.legend(fontsize=7)
    ax1.grid(axis="y", alpha=0.4)
    ax1.tick_params(axis="y", labelsize=8)

    # Right: 30-Day Readmission p-chart
    ax2.set_facecolor(LGREY)
    ax2.plot(range(24), p_vals * 100, color=BLUE, marker="o", markersize=4, linewidth=1.6, zorder=3)
    ax2.axhline(p_bar * 100, color=TEAL, linestyle="--", linewidth=1.2, label=f"p-bar={p_bar*100:.1f}%")
    ax2.axhline(ucl_p * 100, color=RED,  linestyle=":",  linewidth=1.2, label=f"UCL={ucl_p*100:.1f}%")
    ax2.axhline(lcl_p * 100, color=RED,  linestyle=":",  linewidth=1.2, label=f"LCL={lcl_p*100:.1f}%")

    ooc_p = [i for i in range(24) if p_vals[i] > ucl_p or p_vals[i] < lcl_p]
    for i in ooc_p:
        ax2.plot(i, p_vals[i] * 100, "o", color=ORANGE, markersize=9, zorder=4)

    ann_p = {5: "COVID Rapid\nDischarge", 13: "Enhanced Discharge\nNavigation", 21: "Winter\nRespiratory Surge"}
    for i, lbl in ann_p.items():
        offset = 12 if p_vals[i] > p_bar else -28
        ax2.annotate(lbl, (i, p_vals[i] * 100), textcoords="offset points",
                     xytext=(0, offset), fontsize=6.5, ha="center", color=ORANGE, fontweight="bold")

    ax2.set_xticks(range(24))
    ax2.set_xticklabels(months, fontsize=6.5, rotation=45)
    ax2.set_ylabel("30-Day All-Cause Readmission Rate (%)", fontsize=8)
    ax2.set_title("30-Day Readmission Rate p-Chart\n(p-bar=8.4% | Discharge Navigation -4.0pp | Respiratory Surge +5.0pp | HQO Benchmark)", fontsize=9, fontweight="bold", color=BLUE)
    ax2.legend(fontsize=7, loc="upper right")
    ax2.grid(axis="y", alpha=0.4)
    ax2.tick_params(axis="y", labelsize=8)

    fig.text(0.5, 0.01, "Nicholas Steven - github.com/nicholasstevenr",
             ha="center", fontsize=7, color="#888888", style="italic")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    out = "/sessions/focused-epic-turing/mnt/job application/Applications/OptumCanada/chart_p2.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {out}")

if __name__ == "__main__":
    plot_charts()
