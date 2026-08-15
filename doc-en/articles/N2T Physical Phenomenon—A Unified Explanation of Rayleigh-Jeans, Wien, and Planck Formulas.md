---
author: Cunzhang
date: 2026-08-09
license: CC BY-SA 4.0
repository: https://github.com/dao-n2t-lab/node-network-theory
---

In standard physics, the Rayleigh-Jeans formula and the Wien formula are respectively the classical and early quantum theoretical descriptions of the blackbody radiation spectrum. The Rayleigh-Jeans formula diverges at high frequencies, the Wien formula deviates at low frequencies, and Planck unified the two through energy quantization. In the N2T framework, these three formulas are reinterpreted as three geometric descriptions of the frequency-matching relationship between traveling waves and standing waves in a node network across different frequency regimes.

This article presents the N2T framework's complete explanation of the blackbody radiation problem from four perspectives: the node-network definition of a blackbody, the geometric correspondence of the three formulas, the geometric origin of Planck quantization, and a unified comparison table.

## Table of Contents

I. Node-Network Definition of a Blackbody
II. The Rayleigh-Jeans Formula: The Cause of High-Frequency Divergence
III. The Wien Formula: The Cause of High-Frequency Exponential Decay
IV. The Planck Formula: The Discretization of Frequency
V. Unified Comparison of the Three Formulas
VI. Summary

## I. Node-Network Definition of a Blackbody

In standard physics, a blackbody is an idealized cavity that absorbs all incident radiation and re-emits thermal radiation. In the N2T framework, a blackbody is redefined as:

**A finite, bounded node cluster whose phase coupling between its shell-layer grid (boundary) and its internal node network (cavity) determines how it absorbs and emits traveling waves.**

The shape of the blackbody radiation spectrum is determined by the response characteristics of the node network at different frequencies:

- Low-frequency modes: The standing-wave mode distribution of the node network is denser, behaving close to the classical continuous model;
- High-frequency modes: The standing-wave modes of the node network are truncated by the minimum stable distance, deviating from the classical model.

## II. The Rayleigh-Jeans Formula: The Cause of High-Frequency Divergence

### 2.1 Standard Formulation

The Rayleigh-Jeans formula matches experiments at low frequencies but diverges at high frequencies (the ultraviolet region), leading to the "ultraviolet catastrophe":

$$\rho(\nu) = \frac{8\pi \nu^2}{c^3} kT$$

### 2.2 Explanation in the N2T Framework

In the node network, the "high-frequency divergence" of the Rayleigh-Jeans formula is naturally truncated:

- **Assumption failure**: The Rayleigh-Jeans formula assumes space is continuous, thus allowing infinitely many high-frequency modes. However, in a node network, space is discrete and the total number of nodes is finite;
- **Minimum wavelength cutoff**: Any node network has a minimum stable distance $l_{\min} \approx 2.82 \times 10^{-15}$ m. Traveling waves with frequencies above $f_{\max} = c / l_{\min}$ have wavelengths smaller than the minimum spacing and cannot propagate stably on the network;
- **Effective degree-of-freedom attenuation**: The "effective degrees of freedom" of high-frequency modes are not constant but rapidly decay to zero as they approach $f_{\max}$.

In the framework, the high-frequency divergence of the Rayleigh-Jeans formula is not a "mathematical problem" but rather a "failure of the continuity assumption at extreme scales." The discrete node network naturally provides a high-frequency cutoff.

## III. The Wien Formula: The Cause of High-Frequency Exponential Decay

### 3.1 Standard Formulation

The Wien formula matches experiments at high frequencies:

$$\rho(\nu) = \frac{8\pi h \nu^3}{c^3} e^{-h\nu / kT}$$

Its core feature is the exponential decay term $e^{-h\nu / kT}$, indicating that the contribution of high-frequency modes is strongly suppressed.

### 3.2 Explanation in the N2T Framework

In the node network, the exponential decay of the Wien formula originates from the frequency-matching probability between traveling waves and node clusters:

- Shorter wavelengths resonate more easily: High-frequency traveling waves have small wavelengths and are more sensitive to minute changes in node density, making them more easily absorbed or scattered by node clusters;
- Absorption probability grows exponentially with frequency: When a traveling wave passes through a node cluster, the probability of matching a node standing-wave mode grows exponentially with frequency;
- Transmission probability decays exponentially: High matching probability means low "transmission probability"—the transmittance of high-frequency traveling waves through the node network decays exponentially.

In the framework, the exponential term $e^{-h\nu/kT}$ in the Wien formula is not an "artificial assumption" but a geometric reflection of the declining transmission probability of high-frequency traveling waves in a discrete node network.

## IV. The Planck Formula: The Discretization of Frequency

### 4.1 Standard Formulation

The Planck formula unifies the Rayleigh-Jeans and Wien formulas:

$$\rho(\nu) = \frac{8\pi h \nu^3}{c^3} \cdot \frac{1}{e^{h\nu / kT} - 1}$$

Its core is energy quantization: $E = nh\nu$.

### 4.2 Explanation in the N2T Framework

In the node network, the quantization in the Planck formula originates from a geometric fact:

**On closed paths in a node network, only specific standing-wave modes (integer multiples of half-wavelengths) can exist stably.**

This implies:

- The frequencies of vibration modes supported by the internal node network of a blackbody cavity are discrete, not continuous;
- Each mode carries energy $E = n \cdot h\nu$, where $n$ is the mode order (i.e., the order of the standing-wave mode);
- As temperature rises, higher-order standing-wave modes are activated, manifesting as the statistical distribution in the Planck formula.

The "quantization" in the Planck formula is not a presupposed energy packet but rather the discrete frequency spectrum of standing-wave modes in a node network.

## V. Unified Comparison of the Three Formulas

### 5.1 Summary of the Unifying Mechanism

In the node network framework, the Rayleigh-Jeans, Wien, and Planck formulas are different manifestations of the same set of geometric constraints across different frequency regimes:

| Formula | Applicable Frequency Regime | Node Network Mechanism | Core Geometric Feature |
|:---:|:---|:---|:---|
| Rayleigh-Jeans | Low frequencies (far below $kT/h$) | Continuous standing-wave mode approximation holds | Low-frequency mode density of the node network is approximately continuous |
| Wien | High frequencies (far above $kT/h$) | High-frequency modes truncated by the node network | Traveling-wave transmission probability decays exponentially |
| Planck | Full spectrum | Complete statistical distribution of discrete standing-wave modes | Discretization of standing-wave modes on closed paths |

### 5.2 Correspondence with Standard Physics

| Standard Physics Concept | Node Network Framework Explanation |
|:---|:---|
| Rayleigh-Jeans formula | Classical theory, assumes equal weighting of continuous modes $\rightarrow$ Statistical average based on finite network degrees of freedom (high-frequency modes truncated) |
| Ultraviolet catastrophe | Symbol of classical physics failure $\rightarrow$ High-frequency traveling waves cannot exist in the node network (truncated by minimum spacing) |
| Wien formula | Early quantum theory, high-frequency exponential decay $\rightarrow$ Matching probability between high-frequency traveling waves and node standing-wave modes decays exponentially |
| Planck quantization | Energy is discontinuous, $E = nh\nu$ $\rightarrow$ Frequency spectrum of standing-wave modes is discrete (closed-path constraint) |
| Blackbody radiation | Cavity-radiation thermal equilibrium $\rightarrow$ Frequency matching and thermal exchange between node clusters (boundary) and internal traveling waves |

### 5.3 Comparison of Key Formulas

| Formula | Mathematical Expression | N2T Geometric Interpretation |
|:---:|:---|:---|
| Rayleigh-Jeans | $\rho(\nu) = \dfrac{8\pi \nu^2}{c^3} kT$ | Low-frequency continuous approximation; high-frequency truncated by $l_{\min}$ |
| Wien | $\rho(\nu) = \dfrac{8\pi h \nu^3}{c^3} e^{-h\nu/kT}$ | High-frequency traveling-wave transmission probability decays exponentially |
| Planck | $\rho(\nu) = \dfrac{8\pi h \nu^3}{c^3} \cdot \dfrac{1}{e^{h\nu/kT} - 1}$ | Complete statistics of discrete standing-wave modes across the full spectrum |

## VI. Summary

In the N2T framework, the Rayleigh-Jeans, Wien, and Planck formulas are unifiedly understood as:

**They are three geometric descriptions of the frequency-matching relationship between traveling waves and standing waves in a node network across different frequency regimes.**

- Rayleigh-Jeans corresponds to the low-frequency continuous approximation;
- Wien corresponds to high-frequency transmission attenuation;
- Planck corresponds to the full-spectrum discrete standing-wave statistical distribution.

The core conclusions of the three formulas:

- The high-frequency divergence of Rayleigh-Jeans is naturally truncated by the minimum spacing of the discrete node network;
- The high-frequency exponential decay of Wien corresponds to the geometric decline in matching probability between traveling waves and node standing-wave modes;
- The quantization in Planck originates from the discrete frequency spectrum of standing-wave modes on closed paths.

**The three formulas are not "three theories," but rather three statistical characteristics exhibited by the node network under the same set of geometric constraints across different frequency regimes.**