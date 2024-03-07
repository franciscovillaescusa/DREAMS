.. _codes:

Simulation codes
================

The simulations of the DREAMS project have been run using three different codes. Below, we provide details about these codes and the physics they model.

IllustrisTNG
~~~~~~~~~~~~

The simulations in the IllustrisTNG suite have been run with the `Arepo code <https://arxiv.org/abs/1909.04667>`__ using the same subgrid physics as the IllustrisTNG simulation. Arepo uses TreePM to solve for gravity and a moving Voronoi mesh to solve for ideal magnetohydrodynamics (MHD). The IllustrisTNG galaxy formation physics implementation includes sub-grid models for star-formation, stellar evolution and galactic winds, as well as supermassive black hole (SMBH) seeding, merging, accretion and feedback. The latter operates in two modes, selected based on SMBH mass and Eddington ratio, where the high-accretion mode is thermal and the low accretion mode is kinetic and is the more efficient one in ejecting gas and quenching massive galaxies. The galactic winds feedback is kinetic, implemented via briefly hydrodynamically decoupled wind particles, with energy and mass loading factors that are prescribed based on local velocity dispersion and metallicity. Much more detail can be found on the `IllustrisTNG project website <https://www.tng-project.org/>`_.

Ramses
~~~~~~

N-body
~~~~~~

All the N-body simulations hve been run with the `AREPO code <https://arxiv.org/abs/1909.04667>`__. The number of voxels in the PM grid is typically set to be 8 times that of the number of particles. The gravitational softening is set to :math:`\sim1/40` of the mean inter-particle distance. 
