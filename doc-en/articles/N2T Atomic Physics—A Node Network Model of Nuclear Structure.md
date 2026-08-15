---
author: Cunzhang
date: 2026-08-09
license: CC BY-SA 4.0
repository: https://github.com/dao-n2t-lab/node-network-theory
---

In standard nuclear physics, the atomic nucleus is composed of protons and neutrons bound together by the strong interaction (nuclear force), and its structure is described by the shell model, collective model, or liquid drop model. In the N2T framework, the atomic nucleus is reinterpreted as: a stress-balanced node cluster formed by nucleons (protons and neutrons) connected through shared nodes and strong-force edges.

This article presents the N2T framework's geometric explanation of nuclear structure from five perspectives: the node structure of nucleons, inter-nucleon connections, the stress balance of the nucleus, the geometric origin of shell structure and magic numbers, and the correspondence with standard nuclear physics.

## Table of Contents

I. The Node Structure of Nucleons
II. Inter-Nucleon Connections: The Formation of Strong-Force Edges
III. The Stress Balance of the Nucleus
IV. Shell Structure and Magic Numbers
V. The Stability Boundary of the Nucleus
VI. Correspondence with Standard Nuclear Physics
VII. Summary

## I. The Node Structure of Nucleons

In the N2T framework, each nucleon (proton or neutron) is a node cluster consisting of three quark rings sharing a central node.

### 1.1 The Node Structure of the Proton

- **Three quark rings**: two up quark rings (u), one down quark ring (d);
- **Total nodes**: 7 basic nodes (1 central node + 6 peripheral nodes);
- **Topology**: three quark rings share the central node, with peripheral nodes symmetrically distributed at $120^\circ$ angles;
- **Net charge**: +1 (the phase contribution of two up quarks exceeds that of one down quark).

### 1.2 The Node Structure of the Neutron

- **Three quark rings**: one up quark ring (u), two down quark rings (d);
- **Total nodes**: 7 basic nodes (1 central node + 6 peripheral nodes);
- **Topology**: three quark rings share the central node, with peripheral nodes symmetrically distributed at $120^\circ$ angles;
- **Net charge**: 0 (the phase contributions of up and down quarks cancel each other).

### 1.3 Phase Locking Within Quark Rings

Each quark ring consists of three nodes with fixed phase differences of $0^\circ$, $120^\circ$, and $240^\circ$. This phase locking is the geometric origin of quark "color charge" and the foundation of stability within the nucleon.

## II. Inter-Nucleon Connections: The Formation of Strong-Force Edges

### 2.1 How Do Two Nucleons Establish a Connection?

When two nucleons approach each other, they establish shared edges between their peripheral nodes through phase matching:

- If the phase difference between the peripheral nodes of the two nucleons is close to opposite phase ($180^\circ$), the stress on the edge increases, forming a strong-force connection;
- The connection strength is determined by the number of shared edges and the degree of phase matching.

**The geometric essence of the strong force**: the compressive stress edge established when the peripheral nodes of nucleons are in opposite phase.

### 2.2 Structural Types of Inter-Nucleon Connections

| Connection Type | Shared Nodes | Structural Example |
|:---|:---|:---|
| Single-edge connection | 1 shared edge | Initial connection of the deuteron (2 nucleons) |
| Dual-nucleon shared nodes | Multiple nodes shared | Tetrahedral structure of the helium nucleus (4 nucleons) |
| Multi-nucleon nesting | Layered sharing | Fractal stacking of heavy nuclei (e.g., iron, uranium) |

## III. The Stress Balance of the Nucleus

### 3.1 Internal-to-External Stress Ratio R

The stability of the nucleus is determined by the internal-to-external stress ratio:

$$R = \frac{\sigma_{\text{internal}}}{\sigma_{\text{external}}}$$

- Internal stress $\sigma_{\text{internal}}$: the average stress on strong-force edges between nucleons;
- External stress $\sigma_{\text{external}}$: the stress between the nuclear surface and the external node network.

A stable nucleus satisfies:

$$R \in \left[1 - \frac{\alpha}{2},\; 1 + \frac{\alpha}{2}\right]$$

where $\alpha \approx 1/137$ is the fine-structure constant.

### 3.2 Stress-Minimized Nuclear Configurations

The stable configuration of the nucleus is the result of stress minimization:

- The edges between nucleons are as close as possible to the natural length $d_0$;
- The phase differences between nucleons are as small as possible;
- The entire nucleus is in a state of internal-external stress balance.

The shape, size, and stability of the nucleus are all determined by the stress-minimization conditions of the node network.

## IV. Shell Structure and Magic Numbers

### 4.1 The Geometric Origin of Magic Numbers

The magic numbers of the nucleus (2, 8, 20, 28, 50, 82, 126) in the N2T framework correspond to perfectly symmetric closed node shells.

When the number of nucleons reaches a magic number, the shared edges between nucleons form a complete symmetric polyhedral structure:

| Magic Number | Corresponding Geometry | Node Shell Type |
|:---:|:---|:---|
| 2 | Vertices of a tetrahedron (helium nucleus) | 1s shell closed |
| 8 | Vertices of a cube (oxygen nucleus) | 2s shell closed |
| 20 | Vertices of a regular dodecahedron (calcium nucleus) | 3s shell closed |
| 28 | Vertices of a truncated tetrahedron (nickel nucleus) | 4s shell closed |
| 50 | Vertices of a truncated octahedron (tin nucleus) | 5s shell closed |
| 82 | Vertices of a truncated icosahedron (lead nucleus) | 6s shell closed |
| 126 | A more complex polyhedron | 7s shell closed |

### 4.2 Why Are Magic-Number Nuclides the Most Stable?

When the number of nucleons reaches a magic number:

- The strong-force edges between nucleons form a perfectly symmetric closed topology, and the internal stress reaches a global minimum;
- The internal-to-external stress ratio $R$ is exactly equal to 1;
- The nucleus is in the "ideal state" of stress minimization—with neither internal stress accumulation nor external stress intrusion.

**Magic numbers are an inevitable result of the node network forming closed symmetric structures, not empirical parameters.**

## V. The Stability Boundary of the Nucleus

In the N2T framework, the stability of the nucleus is jointly determined by the following factors:

| Factor | Explanation |
|:---|:---|
| Internal-to-external stress ratio $R$ | Must be within the interval $[1 - \alpha/2,\; 1 + \alpha/2]$ |
| Phase locking between nucleons | The phase differences between nucleons must remain stable |
| Nuclear surface node network | Surface nodes must form closed phase loops |
| Total number of nucleons | Stability is highest when reaching magic numbers |

When the nucleus exceeds a certain size (such as uranium-238), the phase locking between nucleons begins to destabilize—internal stress exceeds the threshold, and the nucleus undergoes radioactive decay to release excess stress.

## VI. Correspondence with Standard Nuclear Physics

| Standard Nuclear Physics Concept | N2T Framework Correspondence |
|:---|:---|
| Proton | Node cluster of three quark rings (uud) sharing a central node |
| Neutron | Node cluster of three quark rings (udd) sharing a central node |
| Strong force | Compressive stress edge generated by opposite-phase peripheral nodes of nucleons |
| Nuclear radius $R \approx 1.2 A^{1/3}$ | Macroscopic statistical average of geometric stress $S_g$ |
| Magic numbers (2, 8, 20, 28, 50, 82, 126) | Perfectly symmetric closed node shells |
| Radioactive decay | Inter-nucleon stress exceeds threshold; node unlocking |
| Nuclear shell structure | Periodic standing waves of node density in the radial direction |

## VII. Summary

In the N2T framework, the atomic nucleus is reinterpreted as:

**A node cluster formed by nucleons connected through shared nodes and opposite-phase edges. The stability of the nucleus is determined by the internal-to-external stress ratio $R$, magic numbers correspond to perfectly symmetric closed node shells, and radioactive decay is the unlocking process after stress exceeds the threshold.**

The nucleus is not "a pile of protons and neutrons stuck together by the strong force," but a node network in stress balance—its shape, size, and stability are all driven by phase locking between nodes and stress minimization.