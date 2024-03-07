.. _dark_matter_models:

Dark matter models
==================

The simulations of the DREAMS project have been run using five different dark matter models. The scheme belows show the different dark matter models we consider together with their relationship. For instance, the cold dark matter, warm dark matter, and :math:`h_{\rm p}-k_{\rm p}` models are subclasses of the ETHOS models, that is more general than all those. 

.. image:: Images/Scheme2.png
   :alt: Dark matter models
   

Cold dark matter
~~~~~~~~~~~~~~~~

Cold dark matter is the simplest model we consider and it is the model assumed in the standard model of cosmology :math:`\Lambda {\rm CDM}`. This model assumes that dark matter only interacts gravitationally with itself and with baryons and have negligible thermal velocities on all scales at all redshifts of interest. In this case, dark matter can be represented as a collisionless and pressureless fluid in the numerical simulations.

Note that this model do not have any free parameters. We will refer to this model as either Cold dark matter or CDM.


Warm dark matter
~~~~~~~~~~~~~~~~

Warm dark matter (WDM) is perhaps the simplest extension to CDM. These models consider that dark matter was in thermal equilibrium in the early Universe. Due to the expansion of the Universe, dark matter interactions became inefficient and its thermal distribution was frozen. Candidates for WDM include sterile neutrinos. In the model we use, we only have one free parameter, the WDM mass, :math:`M_{\rm WDM}`. This parameter fully characterizes the distribution of the WDM thermal velocities (which is described by the Fermi-Dirac distribution).

We implement these models in the simulations by assuming that WDM is a collisionless and pressureless fluid (in the same way as CDM). The only difference is that when we generate the initial conditions, we need to account for the impact of WDM mass on the linear power spectrum, that can be described as (`Bode et al. 2001 <https://ui.adsabs.harvard.edu/abs/2001ApJ...556...93B/abstract>`_)

.. math::

   P_{\rm WDM}(k)=\beta(k)P_{\rm CDM}(k)~,

where 

.. math::

       \beta(k) &= \left[ \left( 1 + (\alpha k)^{2.4} \right)^{-5.0/1.2} \right]^2 \\
    \alpha &= 0.048 \left(\frac{M_{\rm WDM}}{1~\mathrm{keV}}\right)^{-1.15} \left( \frac{\Omega_{\rm m} - \Omega_{\rm b}}{0.4} \right)^{0.15} \left(\frac{h}{0.65} \right)^{1.3}  ~.

.. Note::

   In our simulations we do not assign thermal velocities to the WDM particles. See `Leo et al. 2017 <https://ui.adsabs.harvard.edu/abs/2017JCAP...11..017L/abstract>`_ for a justification.

We emphasize that cold dark matter is contained in these models: cold dark matter can be recovered by taking large WDM masses. 


Hpeak - Kpeak and ETHOS
~~~~~~~~~~~~~~~~~~~~~~~





Atomic dark matter
~~~~~~~~~~~~~~~~~~
