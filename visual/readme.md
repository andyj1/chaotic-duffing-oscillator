## Chaotic-Duffing-Oscillator: Visualization

<dl>
  <dt>Frequency Response</dt>
  <dd>case10i: hardening system; nonlinearity is greater than 0</dd>
  <dd>case10ii: softening system; nonlinearity is less than 0</dd>
  <dd>case10ii: linear system neither hardening or softening necessarily; nonlinearity is 0, and this is the threshold at which bifurcation occurs</dd>

  <dt>Lyapunov Exponent</dt>
  <dd>This is to confirm that given damping coefficient = 0.1, linear stiffness = -1 in an unforced system, the eigenvalues(~Lyapunov exponent) of the Jacobian matrix hints at where stable equilbrium (fixed) points lie. For this case, the eigenvalues are close to 0 (~0.05) at x = +/- 1, whereas equals 1 for x = 0 fixed point. Thus x = 0 is unstable and the rest two are relatively more stable. Lyapunov exponent would simply be natural log of this eigenvalue, which would then be greater 0 for unstable and less than 0 for stable.</dd>

  <dt>Phase-Space Diagram</dt>
  This diagram is, simply put, a plot of first derivative against displacement. This is useful in identifying convergence points (fixed point) and divergence in transient and steady-state.
  <dd>case3: damped motion</dd>
  <dd>case4: damped driven motion</dd>
  <dd>case7: complete chaotic motion</dd>

  <dt>Poincare Sections</dt>
  Poincare Sections are plots of phase-space, whose data points are taken every period of the system. This is useful for identifying chaotic characteristics of the system undergoing period doubling, which is an effect that exhibits the period of excitation doubling, causing the system period to increase by a factor of 2.
  <dd>case1: free motion</dd>
  <dd>case3: damped motion</dd>
  <dd>case4: damped driven motion</dd>
  <dd>case5: damped driven motion with increased amplitude</dd>
  <dd>case7: complete chaotic motion</dd>

</dl>