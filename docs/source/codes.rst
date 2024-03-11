.. _codes:

Simulation codes
================

The simulations of the DREAMS project have been run using three different codes. Below, we provide details about these codes and the physics they model.

IllustrisTNG
~~~~~~~~~~~~

The simulations in the IllustrisTNG suite have been run with the `Arepo code <https://arxiv.org/abs/1909.04667>`__ using the same subgrid physics as the IllustrisTNG simulation. Arepo uses TreePM to solve for gravity and a moving Voronoi mesh to solve for ideal magnetohydrodynamics (MHD). The IllustrisTNG galaxy formation physics implementation includes sub-grid models for star-formation, stellar evolution and galactic winds, as well as supermassive black hole (SMBH) seeding, merging, accretion and feedback. The latter operates in two modes, selected based on SMBH mass and Eddington ratio, where the high-accretion mode is thermal and the low accretion mode is kinetic and is the more efficient one in ejecting gas and quenching massive galaxies. The galactic winds feedback is kinetic, implemented via briefly hydrodynamically decoupled wind particles, with energy and mass loading factors that are prescribed based on local velocity dispersion and metallicity. Much more detail can be found on the `IllustrisTNG project website <https://www.tng-project.org/>`_.

Ramses
~~~~~~

The simulations in the RAMSES suite have been run with the `RAMSES code <https://bitbucket.org/rteyssie/ramses/src/master/>`__ using the same subgrid physics as in `Kretschmer & Teyssier (2021) <https://arxiv.org/abs/1906.11836>`__ and `Teyssier et al. (2011) <https://arxiv.org/abs/1003.4744>`__. RAMSES uses Adaptive Particle Mesh to solve for gravity and the Godunov Finite Volume Constrained Transport method to solve for ideal magnetohydrodynamics (MHD). The galaxy formation physics implementation includes a multi-freefall sub-grid model for star-formation and supernovae momentum feedback as in `Kretschmer and Teyssier (2021) <https://arxiv.org/abs/1906.11836>`__, as well as supermassive black hole (SMBH) seeding, merging, accretion and feedback as in `Teyssier et al. (2011) <https://arxiv.org/abs/1003.4744>`__ and `Pellissier et al. (2023) <https://arxiv.org/abs/2301.02684>`__. RAMSES also models metallicity dependent radiative cooling, as well as radiation heating from a self-shielded UV background consistent with standard reionization models.

N-body
~~~~~~

All the N-body simulations hve been run with the `AREPO code <https://arxiv.org/abs/1909.04667>`__. The number of voxels in the PM grid is typically set to be 8 times that of the number of particles. The gravitational softening is set to :math:`\sim1/40` of the mean inter-particle distance. 
