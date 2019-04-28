## Chaotic-Duffing-Oscillator

<dl>
  <dt>About</dt>
  <dd>This project aims to demonstrate a nonlinear (chaotic) dynamic system by an application of Duffing Osillator (Equation). This chaotic structural model poses a chaotic behavior for a set of defined parameters and initial conditions, and to approximate the dynamics of the system, a fourth-order Runge-Kutta method will be applied to solve the problem.</dd>

  <dt>Abstract</dt>
  <dd>The chaotic behavior in motion is not unusual to observe in practice in common nonlinear differential equations. Through close examination of nonlinear dynamics of a system governed by a Duffing’s Equation, one can observe how phase-space motion follows a strange attractor as harmonic excitations are applied to the system. A Duffing oscillator system of complexity as simple as a second-order ordinary differential equation exhibits bifurcation past some threshold value of excitation due to periodic doubling, bounded by five parameters and initial conditions. Through visual aids and graphical responses, the chaotic motion of a Duffing system (i.e. spring) is observed, and verified in simple visualization techniques in Python.</dd>

  <dt>Tools/Packages</dt>
  <dd>Visual Python, Matplotlib, Scipy, Numpy, FFMpeg</dd>

  <dt>Purpose</dt>
  <dd>Analyze stability through measures including eigenvalues of Jacobian/Lyapunov exponent, strange attractor in phase-space diagram, Poincare Sections and bifurcation due to period doubling</dd>
  <dd>Determine point of bifurcation in terms of ratio of excitationo amplitude to damping coefficient</dd>
  <dd>Make graphs representing periodic, quasi-periodic, and chaotic behavior of the system</dd>
  <dd>Compare behaviors in time-,space- and frequency- domains under different conditions for initial conditions and parameters of interest </dd>

  <dt>Related Topics</dt>
  <dd>Visualization of numerically approximated data</dd>
  <dd>Solving second-order ordinary differential equations</dd>
  <dd>Observing chaos through eigenvalues and time series graphs</dd>
  
  <dt>Methods Used</dt>
  <dd>Runge-Kutta Algorithm (4th order)</dd>
  <dd>Harmonic Balance Method</dd>
  --- most commonly used method in studying the steady-state frequency response in a nonlinear dynamical system (autonomous and non-autonomous). By assumed the response in terms of a Fourier series in the differential equation and separating the harmonic coefficients, the frequency amplitude and the unknown coefficients in the response relation of the system can be determined (assuming the response to be in form of a sinusoid).</dd>

  <dt>Duffing Oscillator</dt>
  <dd>Duffing Oscillator(Equation) is a (nonlinear) system that is often periodically forced and damped with some nonlinear elasticity associated. The governing equation is <img src="https://latex.codecogs.com/gif.latex?\frac{\partial^2&space;x}{\partial&space;t^2}&space;&plus;&space;\delta\frac{\partial&space;x}{\partial&space;t}&space;&plus;&space;\beta&space;x&space;&plus;&space;\alpha&space;x^3&space;=&space;\gamma&space;cos(\omega&space;t)" title="\frac{\partial^2 x}{\partial t^2} + \delta\frac{\partial x}{\partial t} + \beta x + \alpha x^3 = \gamma cos(\omega t)" />, where the parameters are damping coefficient, nonlinearity coefficient, linear stiffness, excitation amplitude, excitation angular frequency, in order.
</dl>

