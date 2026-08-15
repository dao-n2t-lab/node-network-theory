---
author: Cunzhang
date: 2026-08-15
license: CC BY-SA 4.0
repository: https://github.com/dao-n2t-lab/node-network-theory
---

In the N2T framework, the proton is modeled as a three-dimensional fan-blade topology: three quark triangular rings share a central node, symmetrically distributed around the central node at $120^\circ$ equal angles, with the planes of the three quark rings being non-coplanar in space.

Starting from this geometric structure, this article derives the distribution of frequency components among the 7 internal nodes of the proton and provides the numerical values and physical significance of each component type.

## Table of Contents

I. Geometric Parameters of the Proton Structure
II. Geometric Calculation of Frequency Components
III. Numerical Summary of Each Component
IV. Physical Significance
V. Summary

## I. Geometric Parameters of the Proton Structure

### 1.1 Node Distribution

The proton consists of 7 nodes:

- 1 central node $o$，located at the origin;
- 6 peripheral nodes, distributed in three non-coplanar directions around the central node.

Let the direction vectors of the three quark rings be:

$$\mathbf{u}_1 = (1,0,0),\quad \mathbf{u}_2 = \left(-\frac{1}{2},\frac{\sqrt{3}}{2},0\right),\quad \mathbf{u}_3 = \left(-\frac{1}{2},-\frac{\sqrt{3}}{2},0\right)$$

The planes of the three rings are perpendicular to these three direction vectors respectively. The peripheral nodes of each quark ring lie on their respective direction vectors, at a distance $L_0$ (natural length) from the central node.

### 1.2 Connection Relationships of the Fan-Blade Structure

Each peripheral node has 3 edges:

- 1 edge connecting to the central node (radial connection);
- 1 edge connecting to the other peripheral node within the same quark ring (intra-ring transverse connection);
- 1 edge connecting to a peripheral node of an adjacent quark ring (inter-ring transverse connection).

## II. Geometric Calculation of Frequency Components

### 2.1 Reference Frequency of the Central Node

As the shared node of the three quark rings, the central node's vibration frequency is the framework's initial frequency:

$$\omega_0 = 5.66 \times 10^{18} \text{ rad/s}$$

This is the reference value for all frequency components within the proton.

### 2.2 Frequency Component Distribution of Peripheral Nodes

Each peripheral node has 4 vibration components, with frequencies calculated through geometric projection.

**Component 1: Radial Component (Center-Periphery Connection)**

The central node's vibration propagates to peripheral nodes along radial edges. This component lies along the line connecting the center and the peripheral node, with a projection coefficient of 1 (no projection loss).

Frequency:

$$\omega_{\text{radial}} = \omega_0 = 5.66 \times 10^{18} \text{ rad/s}$$

**Component 2: Intra-Ring Transverse Component (Connection Between Two Peripheral Nodes in the Same Quark Ring)**

The two peripheral nodes within the same quark ring are connected by an edge. This edge forms an angle of $60^\circ$ with the radial direction, giving a projection coefficient of $\cos 60^\circ$.

Frequency:

$$\omega_{\text{intra-ring transverse}} = \omega_0 \cdot \cos 60^\circ = 2.83 \times 10^{18} \text{ rad/s}$$

**Components 3 and 4: Inter-Ring Transverse Components (Connections Between Peripheral Nodes of Adjacent Quark Rings)**

Each peripheral node connects to peripheral nodes of adjacent quark rings. The two components correspond to two different transverse coupling directions, with angles of $45^\circ$ and $135^\circ$ respectively (determined by the geometric symmetry of the three-dimensional fan-blade structure).

The projection coefficients are $\cos 45^\circ$ and $\cos 135^\circ$，i.e.，$\frac{\sqrt{2}}{2}$ and $-\frac{\sqrt{2}}{2}$.

Frequencies (taking absolute values):

$$\omega_{\text{inter-ring transverse A}} = \omega_0 \cdot \frac{\sqrt{2}}{2} = 4.00 \times 10^{18} \text{ rad/s}$$

$$\omega_{\text{inter-ring transverse B}} = \omega_0 \cdot \frac{\sqrt{2}}{2} = 4.00 \times 10^{18} \text{ rad/s}$$

Since the absolute values of the projection coefficients for $45^\circ$ and $135^\circ$ are equal, the two inter-ring transverse components have the same frequency, both $4.00 \times 10^{18}$ rad/s.

## III. Numerical Summary of Each Component

| Node Type | Component | Frequency (rad/s) | Source |
|:---:|:---|:---:|:---|
| Central node | Reference frequency | $5.66 \times 10^{18}$ | Framework initial frequency $\omega_0$ |
| Peripheral node | Radial | $5.66 \times 10^{18}$ | $\omega_0 \cdot \cos 0^\circ$ |
| Peripheral node | Intra-ring transverse | $2.83 \times 10^{18}$ | $\omega_0 \cdot \cos 60^\circ$ |
| Peripheral node | Inter-ring transverse A | $4.00 \times 10^{18}$ | $\omega_0 \cdot \cos 45^\circ$ |
| Peripheral node | Inter-ring transverse B | $4.00 \times 10^{18}$ | $\omega_0 \cdot \cos 135^\circ$ |

Due to symmetry equivalence, the 6 edges of the central node merge into a single vibration mode at frequency $\omega_0$. Peripheral nodes have 4 component types, with the two inter-ring transverse components sharing the same frequency.

## IV. Physical Significance

### 4.1 Physical Correspondence of Frequency Components

| Component | Frequency | Corresponding Physical Effect |
|:---|:---:|:---|
| Radial | $5.66 \times 10^{18}$ rad/s | Phase locking of quark rings, maintaining nucleon structure |
| Intra-ring transverse | $2.83 \times 10^{18}$ rad/s | Synchronous vibration of nodes within the same quark ring |
| Inter-ring transverse | $4.00 \times 10^{18}$ rad/s | Coupled vibration between quark rings |

### 4.2 Stress Corresponding to Frequency Differences

The frequency differences between different components correspond to stresses between quark rings:

| Frequency Difference | Value | Physical Meaning |
|:---|:---:|:---|
| $\omega_{\text{radial}} - \omega_{\text{intra-ring transverse}}$ | $2.83 \times 10^{18}$ rad/s | Intra-ring tension of quark ring |
| $\omega_{\text{radial}} - \omega_{\text{inter-ring transverse}}$ | $1.66 \times 10^{18}$ rad/s | Inter-ring tension between quark rings |

## V. Summary

In the three-dimensional fan-blade model of the N2T framework, the frequency component distribution of the proton has the following structure:

1. **1 central node**: reference frequency $\omega_0 = 5.66 \times 10^{18}$ rad/s

2. **6 peripheral nodes**: 4 types of frequency components

   - Radial: $\omega_0$
   - Intra-ring transverse: $\omega_0 / 2$
   - Inter-ring transverse A: $\omega_0 \cdot \sqrt{2}/2$
   - Inter-ring transverse B: $\omega_0 \cdot \sqrt{2}/2$

This frequency distribution is entirely determined by the geometric projection coefficients of the three-dimensional fan-blade structure, without introducing any additional free parameters. The differences between frequency components can explain the stress distribution within and between quark rings, corresponding to the confinement effects of the strong force at the nucleon scale.