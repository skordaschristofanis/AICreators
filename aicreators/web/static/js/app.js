// SPDX-License-Identifier: MIT

(() => {
  const shell = document.querySelector(".app-shell");
  const toggle = document.getElementById("nav-toggle");
  const healthStatus = document.getElementById("health-status");
  const overviewHealth = document.getElementById("overview-health");
  const healthUrl = healthStatus?.dataset.healthUrl;

  toggle?.addEventListener("click", () => {
    const open = shell?.classList.toggle("nav-open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });

  async function refreshHealth() {
    if (!healthUrl) {
      return;
    }

    try {
      const response = await fetch(healthUrl);
      const ok = response.ok;
      const label = ok ? "API · ok" : "API · error";

      if (healthStatus) {
        healthStatus.textContent = label;
        healthStatus.classList.toggle("is-ok", ok);
        healthStatus.classList.toggle("is-bad", !ok);
      }

      if (overviewHealth) {
        overviewHealth.textContent = ok ? "ok" : "error";
        overviewHealth.classList.toggle("muted", !ok);
      }
    } catch {
      if (healthStatus) {
        healthStatus.textContent = "API · unreachable";
        healthStatus.classList.add("is-bad");
        healthStatus.classList.remove("is-ok");
      }

      if (overviewHealth) {
        overviewHealth.textContent = "unreachable";
        overviewHealth.classList.add("muted");
      }
    }
  }

  refreshHealth();
})();
