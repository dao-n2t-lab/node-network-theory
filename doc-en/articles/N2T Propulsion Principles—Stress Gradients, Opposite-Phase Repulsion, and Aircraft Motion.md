author: Cunzhang
author_url: https://github.com/dao-n2t-lab
license: CC BY-SA 4.0

In the N2T framework, the essence of aircraft forward motion is not the generation of reaction force by expelling propellant, but the regulation of the stress distribution of the node network around itself, causing itself to move from a high-stress region toward a low-stress region. The core operation of propulsion is to create a net stress gradient and allow the aircraft node network to move along the direction of that gradient.

This article presents the N2T framework's complete explanation of the phenomenon of "propulsion" from four perspectives: the stress gradient mechanism, the phase conditions for repulsion/attraction, frequency regulation strategies, and corresponding practices in real-world engineering.

## Table of Contents

I. The Essence of Propulsion: Stress-Gradient-Driven Motion
II. Phase Conditions for Repulsion and Attraction
III. Frequency Regulation Strategy: Maintaining the Opposite-Phase State
IV. Real-World Engineering Correspondences
V. Comparison with Existing Propulsion Methods
VI. Summary

## I. The Essence of Propulsion: Stress-Gradient-Driven Motion

In the N2T framework, the stress distribution around a node cluster (aircraft) determines its direction of motion. If the stress in front of the aircraft is lower than that behind it, the node cluster will naturally move from the high-stress region toward the low-stress region:

$$\vec{F}_{\text{tr}} = -\nabla S$$

That is: **the net thrust on the aircraft points in the direction of the fastest decrease in total stress.**

To achieve forward motion, the aircraft needs to simultaneously satisfy two conditions:

1. **Reduce stress in front**: bring the phases of the node network in front toward synchronization, edges toward natural length, and stress down;
2. **Increase stress behind**: perturb the phases of the node network behind, compressing or stretching edges, and stress up.

When these two conditions are simultaneously met, a low-stress region forms in front and a high-stress region forms behind, and the node cluster is "pushed" toward the low-stress direction—that is, forward motion.

## II. Phase Conditions for Repulsion and Attraction

The increase in stress behind must manifest as repulsion (pushing rear nodes away), not attraction (pulling rear nodes back). These are determined by the phase difference between the aircraft surface nodes and the rear node network:

| Phase Difference | Interaction Effect | Force Type |
|:---|:---|:---|
| In-phase ($0^\circ$) | Rear nodes converge toward the aircraft | Attraction |
| $90^\circ$ | Weak interaction, no stable force | Neutral |
| Opposite-phase ($180^\circ$) | Rear nodes are pushed away from the aircraft | Maximum repulsion |

Therefore, the basic condition for generating forward thrust is: **the aircraft surface nodes maintain opposite phase (phase difference $180^\circ$) with the rear node network.**

## III. Frequency Regulation Strategy: Maintaining the Opposite-Phase State

Opposite phase alone is not sufficient to generate sustained propulsion—because the phases of the node network drift over time, and the relative motion between the aircraft and rear nodes also changes the phase difference. To maintain a stable opposite-phase state, a specific frequency ratio condition must be satisfied:

$$f_{\text{aircraft}} = \frac{2n+1}{2} \cdot f_{\text{rear node network}}$$

That is: **the vibration frequency of the aircraft surface nodes should be a half-integer multiple ($0.5, 1.5, 2.5, \dots$) of the natural frequency of the rear node network.**

This frequency ratio ensures that even if the phase difference drifts, the system will be "pulled back" to the opposite-phase state after each vibration cycle, thereby maintaining a stable repulsive force.

## IV. Real-World Engineering Correspondences

The concept of "using opposite phase to generate repulsion or thrust" is an underlying mechanism in the N2T framework; in real-world engineering, it has already been implemented through the languages of fluid mechanics and mechanical structures.

### 1. Dual Synthetic Jet Technology

The dual synthetic jet is an active flow control technology. When two adjacent jets operate in **opposite phase**, they can produce a "boost/self-sustaining" effect, deflecting the mainstream by up to $22^\circ$，thereby generating significant lateral force or additional thrust. Experiments show that by adjusting the peak velocity and **excitation frequency** of the jets, the deflection angle and thrust direction can be controlled.

| Operation | Engineering Implementation | N2T Mechanism Correspondence |
|:---|:---|:---|
| Creating opposite-phase jets | Controlling the ejection/suction cycles of two jet outlets to be opposite | Rear node network maintains opposite phase with aircraft surface nodes |
| Adjusting excitation frequency | Changing the jet ejection frequency to optimize mainstream deflection | Adjusting the frequency ratio between aircraft surface nodes and rear node network |

### 2. Opposite-Phase Flapping-Wing Aircraft

In flapping-wing aircraft design, opposite-phase flapping is a mature control strategy. In patented designs, the wings on both sides achieve opposite-phase flapping through mechanical linkages (one wing up, one wing down), balancing torque while generating stable lift and thrust.

In the N2T framework, the force generated by opposite-phase flapping comes from phase coupling between the wings and the air node network—that is, actively regulating the phase of the rear node network through mechanical vibration to continuously maintain the opposite-phase state.

### 3. Spin Missile Phase Control

In single-channel control of spin missiles, the phase difference between the linearization signal and the control signal directly affects the magnitude and direction of the periodic average force. That is: **the phase difference directly determines the direction and magnitude of the "average thrust."**

This is highly consistent at the phenomenological level with your proposed mechanism of "opposite phase $\rightarrow$ repulsion, in-phase $\rightarrow$ attraction."

## V. Comparison with Existing Propulsion Methods

| Propulsion Method | Standard Physics Explanation | N2T Framework Explanation |
|:---|:---|:---|
| Rocket propulsion | Conservation of momentum (expelling propellant generates reaction force) | Stress in the rear node network increases, forming a forward stress gradient |
| Propeller propulsion | Propeller blades push air/water to generate reaction force | Blades couple in opposite phase with the fluid node network, generating a net stress gradient |
| Jet propulsion | Compressed air expelled generates reaction force | Phase perturbation at the nozzle creates a high-stress region in the node network |
| Dual synthetic jet | Jet interaction generates deflection force and thrust | Opposite-phase jets regulate the stress distribution of the rear node network |
| Flapping-wing flight | Wing flapping generates lift and thrust | Opposite-phase flapping maintains opposite-phase coupling between wings and the air node network |

## VI. Summary

In the N2T framework, the essence of propulsion is stress-gradient driving—the aircraft regulates the stress distribution of the node networks in front and behind, causing itself to move from a high-stress region toward a low-stress region.

To generate net forward thrust, two conditions must be met:

1. Stress in front decreases and stress behind increases, forming a forward-pointing stress gradient;
2. The stress behind must manifest as repulsion, meaning the aircraft surface nodes maintain opposite phase with the rear node network.

To maintain a stable opposite-phase state, the vibration frequency of the aircraft surface nodes should maintain a **half-integer multiple relationship** with the natural frequency of the rear node network, allowing the system to automatically reset after phase drift.

Real-world technologies such as dual synthetic jets, opposite-phase flapping-wing aircraft, and spin missile phase control demonstrate that the logic of "opposite phase $\rightarrow$ stress gradient $\rightarrow$ thrust" has already been applied in engineering—only currently understood as localized tools in fluid mechanics or mechanical control, rather than as macroscopic manifestations of node network phase regulation. The N2T framework provides a unified language that reduces these practices to the same underlying mechanism.