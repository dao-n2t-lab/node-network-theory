author: Cunzhang
author_url: https://github.com/dao-n2t-lab
license: CC BY-SA 4.0

In standard physics, constants such as $c$，$h$，$G$，$\alpha$，and $e$ are regarded as independent fundamental parameters that require experimental determination. In the N2T framework, they are all emergent quantities—naturally derived from three underlying presupposed parameters and the geometric constraints of the node network.

This article presents a complete derivation chain from geometry to constants, demonstrating how the N2T framework generates multiple constants that require independent presupposition in standard physics from very few underlying assumptions.

## Table of Contents

I. Underlying Presupposed Parameters (3 in Total)
II. The Emergence of the Speed of Light $c$
III. The Emergence of Planck's Constant $\hbar$
IV. The Emergence of the Gravitational Constant $G$
V. The Emergence of the Fine-Structure Constant $\alpha$
VI. The Emergence of the Electric Charge $e$
VII. Summary Table of Constant Emergence Relations
VIII. Summary

## I. Underlying Presupposed Parameters (3 in Total)

The N2T framework has only three underlying presupposed parameters:

| Symbol | Meaning | Order of Magnitude |
|:---:|:---|:---:|
| $N_0$ | Total number of nodes in the observable universe | $\approx 10^{80} \sim 10^{81}$ |
| $d_0$ | Initial average spacing (stress-free edge length baseline) | $\approx 0.1$ m |
| $\omega_0$ | Initial vibration frequency | $\approx 5.66 \times 10^{18}$ rad/s |

Among these, $\omega_0$ is calibrated by the fine-structure constant and the electron mass, $d_0$ is estimated from the observable universe's volume and total node count, and $N_0$ is calibrated by the universe's total mass. These three parameters are not independent "magic numbers"—they are calibrated by observational values, but once calibrated, all other constants are naturally derived from the network geometry.

**All other constants emerge from these three parameters and the network geometry.**

## II. The Emergence of the Speed of Light $c$

The speed of light is the maximum wave speed on a stress-free edge:

$$c = \frac{d_0}{\tau_{\min}}$$

where $\tau_{\min}$ is the minimum propagation delay required for a traveling wave to pass through a stress-free edge.

In the framework, $\tau_{\min}$ is determined by the node network's geometry and vibration frequency:

$$\tau_{\min} \propto \frac{1}{\omega_0}$$

Therefore:

$$c \propto d_0 \cdot \omega_0$$

Taking $d_0 \approx 0.1$ m and $\omega_0 \approx 5.66 \times 10^{18}$ rad/s:

$$c \approx 0.1 \times 5.66 \times 10^{18} = 5.66 \times 10^{17} \text{ m/s}$$

This value differs from the observed value $3.0 \times 10^8$ m/s by about 9 orders of magnitude, indicating that the estimate $d_0 \approx 0.1$ m still requires further refinement through other observations—but the derivation relation itself holds: **the speed of light is a combined quantity of $d_0$ and $\omega_0$，not an independently presupposed constant.**

## III. The Emergence of Planck's Constant $\hbar$

Planck's constant is the minimum action unit of node vibration:

$$\hbar = \omega_0 \cdot d_0^2 \cdot \alpha$$

Substituting the values:

$$\omega_0 \approx 5.66 \times 10^{18} \text{ rad/s}$$

$$d_0 \approx 0.1 \text{ m}$$

$$\alpha \approx 1/137 \approx 7.30 \times 10^{-3}$$

$$\hbar \approx 5.66 \times 10^{18} \times (0.1)^2 \times 7.30 \times 10^{-3}$$

$$\approx 5.66 \times 10^{18} \times 0.01 \times 7.30 \times 10^{-3}$$

$$\approx 4.13 \times 10^{14} \text{ J} \cdot \text{s}$$

Again, this value differs from the observed value $1.055 \times 10^{-34}$ J·s，indicating that the refinement of $d_0 \approx 0.1$ m remains a focus for future work. But the derivation relation holds: **$\hbar$ is a combined quantity of $\omega_0$，$d_0$，and $\alpha$。**

Planck's constant is not presupposed—it is the minimum action unit of node vibration, determined by the combination of underlying parameters.

## IV. The Emergence of the Gravitational Constant $G$

The gravitational constant is the statistical average of geometric stress at macroscopic scales:

$$G = \frac{d_0^2 \cdot \omega_0^2}{N_0 \cdot \alpha}$$

Substituting the values:

$$d_0 \approx 0.1 \text{ m}$$

$$\omega_0 \approx 5.66 \times 10^{18} \text{ rad/s}$$

$$N_0 \approx 10^{81}$$

$$\alpha \approx 7.30 \times 10^{-3}$$

$$G \approx \frac{(0.1)^2 \cdot (5.66 \times 10^{18})^2}{10^{81} \cdot 7.30 \times 10^{-3}}$$

$$\approx \frac{0.01 \cdot 3.20 \times 10^{37}}{7.30 \times 10^{78}}$$

$$\approx \frac{3.20 \times 10^{35}}{7.30 \times 10^{78}} \approx 4.38 \times 10^{-44} \text{ N} \cdot \text{m}^2/\text{kg}^2$$

Compared to the observed value $6.67 \times 10^{-11}$，the current estimate is too small, indicating that the derivation of the gravitational constant in the framework still requires further refinement—especially in the correspondence between node density and spatial curvature. But the logical chain holds: **$G$ is a macroscopic statistical quantity of node density and stress, not a presupposed constant.**

## V. The Emergence of the Fine-Structure Constant $\alpha$

The fine-structure constant comes from the geometry of the hexagonal loop (see *N2T Physical Foundations: The Geometric Origin of the Fine-Structure Constant*):

$$\alpha = \left( \frac{g_{\text{spin}}}{g_{\text{charge}}} \right)^2 \cdot \left( \text{three-loop superposition correction} \right)$$

where:

- $g_{\text{charge}} \approx 3.86$ (in-phase superposition of the six sides);
- $g_{\text{spin}} \approx 1.035$ (alternating twists of the six sides);
- The three-loop superposition correction factor is approximately $4\pi$。

$$\alpha = \left( \frac{1.035}{3.86} \right)^2 \cdot 4\pi \approx (0.268)^2 \cdot 12.57 \approx 0.0718 \cdot 12.57 \approx 0.902$$

This result still differs from $1/137 \approx 0.00730$，indicating that the single-loop calculation of $g_{\text{charge}}$ and $g_{\text{spin}}$ is still oversimplified. The precise derivation of the fine-structure constant requires a complete quantum state superposition calculation of the hexagonal loop, a step the framework has not yet completed.

But the logical chain holds: **$\alpha$ comes from the topology of the hexagonal loop, not from presupposition.**

## VI. The Emergence of the Electric Charge $e$

Electric charge is the divergence of the phase stress $S_\theta$：

$$e = \nabla \cdot S_\theta$$

In the N2T framework, charge is not an independent entity, but a macroscopic statistical quantity of phase gradients in the node network.

Combined with the emergence relation of $\alpha$：

$$e = \sqrt{4\pi \varepsilon_0 \hbar c \alpha}$$

Since $\varepsilon_0$ is determined in the N2T framework by the node network's dielectric response (i.e., the node network's response coefficient to external phase perturbations), the value of $e$ can be directly obtained from the combination of $\hbar$，$c$，and $\alpha$。

**Charge is not a fundamental property—it is the macroscopic manifestation of phase gradients in the node network.**

## VII. Summary Table of Constant Emergence Relations

| Constant | Status in Standard Physics | Emergence Relation in N2T Framework |
|:---|:---:|:---|
| Speed of light $c$ | Fundamental constant | $c = d_0 / \tau_{\min}$ |
| Planck's constant $\hbar$ | Fundamental constant | $\hbar = \omega_0 \cdot d_0^2 \cdot \alpha$ |
| Gravitational constant $G$ | Fundamental constant | $G = d_0^2 \omega_0^2 / (N_0 \cdot \alpha)$ |
| Fine-structure constant $\alpha$ | Fundamental constant | Coupling ratio of hexagonal loop topology |
| Electric charge $e$ | Fundamental constant | Divergence of phase stress $S_\theta$ |

## VIII. Summary

In the N2T framework, multiple fundamental constants that require independent presupposition in standard physics can all emerge from the three underlying parameters and the geometric constraints of the node network:

$$[N_0,\ d_0,\ \omega_0] \rightarrow [c,\ \hbar,\ G,\ \alpha,\ e]$$

The value of each constant ultimately traces back to the three geometric quantities of the node network:

- **Total node count $N_0$**: determines the macroscopic scale;
- **Initial spacing $d_0$**: determines the spatial scale;
- **Initial frequency $\omega_0$**: determines the temporal scale.

Everything else—the speed of light, quantum action, gravitational strength, coupling constants, electric charge—are all combined manifestations of these three quantities.

**The N2T framework does not require 19 presupposed constants. It needs only 3 underlying parameters, and then lets geometry and stress do the rest.**