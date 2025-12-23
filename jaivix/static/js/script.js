// Scroll animation using Intersection Observer
document.addEventListener('DOMContentLoaded', () => {
  // Select all elements with class fade-up OR animated-section
  const faders = document.querySelectorAll('.fade-up, .animated-section');

  const options = {
    threshold: 0.2
  };

  const appearOnScroll = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('show'); // add 'show' to trigger CSS animation
        observer.unobserve(entry.target);
      }
    });
  }, options);

  faders.forEach(fader => {
    appearOnScroll.observe(fader);
  });
});
