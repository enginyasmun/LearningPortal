(() => {
  "use strict";

  const ready = (callback) => {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", callback, { once: true });
    } else {
      callback();
    }
  };

  ready(() => {
    const body = document.body;
    const sidebar = document.getElementById("app-sidebar");
    const mobileToggle = document.querySelector("[data-sidebar-toggle]");
    const mobileClose = document.querySelector("[data-sidebar-close]");
    const desktopCollapse = document.querySelector("[data-sidebar-collapse]");
    const collapseKey = "learning-portal:sidebar-collapsed";

    const closeMobileSidebar = () => body.classList.remove("sidebar-open");
    const toggleMobileSidebar = () => body.classList.toggle("sidebar-open");

    if (mobileToggle && sidebar) mobileToggle.addEventListener("click", toggleMobileSidebar);
    if (mobileClose) mobileClose.addEventListener("click", closeMobileSidebar);
    document.querySelectorAll(".workspace-sidebar a").forEach((link) => {
      link.addEventListener("click", closeMobileSidebar);
    });

    const setSidebarCollapsed = (collapsed) => {
      body.classList.toggle("sidebar-collapsed", collapsed);
      desktopCollapse?.setAttribute("aria-expanded", String(!collapsed));
      desktopCollapse?.setAttribute(
        "aria-label",
        collapsed ? "Expand navigation" : "Collapse navigation"
      );
      try {
        localStorage.setItem(collapseKey, collapsed ? "1" : "0");
      } catch (_) {
        // The layout still works when browser storage is disabled.
      }
    };

    if (desktopCollapse && sidebar) {
      let initiallyCollapsed = false;
      try {
        initiallyCollapsed = localStorage.getItem(collapseKey) === "1";
      } catch (_) {
        initiallyCollapsed = false;
      }
      setSidebarCollapsed(initiallyCollapsed);
      desktopCollapse.addEventListener("click", () => {
        setSidebarCollapsed(!body.classList.contains("sidebar-collapsed"));
      });
    }

    /* Command palette */
    const commandDialog = document.querySelector("[data-command-dialog]");
    const commandOpenButtons = document.querySelectorAll("[data-command-open]");
    const commandCloseButtons = document.querySelectorAll("[data-command-close]");
    const commandSearch = document.querySelector("[data-command-search]");
    const commandList = document.querySelector("[data-command-list]");
    const commandItems = commandList ? [...commandList.querySelectorAll("a")] : [];

    const closeCommand = () => {
      if (!commandDialog) return;
      commandDialog.hidden = true;
      body.classList.remove("command-open");
      if (commandSearch) commandSearch.value = "";
      commandItems.forEach((item) => {
        item.hidden = false;
        item.classList.remove("keyboard-active");
      });
    };

    const openCommand = () => {
      if (!commandDialog) return;
      commandDialog.hidden = false;
      body.classList.add("command-open");
      window.requestAnimationFrame(() => commandSearch?.focus());
    };

    commandOpenButtons.forEach((button) => button.addEventListener("click", openCommand));
    commandCloseButtons.forEach((button) => button.addEventListener("click", closeCommand));

    const normalize = (value) => (value || "").toLowerCase().trim();
    const filterCommandItems = () => {
      const query = normalize(commandSearch?.value);
      commandItems.forEach((item) => {
        item.hidden = Boolean(query) && !normalize(item.textContent).includes(query);
        item.classList.remove("keyboard-active");
      });
      commandItems.find((item) => !item.hidden)?.classList.add("keyboard-active");
    };

    commandSearch?.addEventListener("input", filterCommandItems);
    commandSearch?.addEventListener("keydown", (event) => {
      const visible = commandItems.filter((item) => !item.hidden);
      if (!visible.length) return;
      const current = visible.findIndex((item) => item.classList.contains("keyboard-active"));
      if (event.key === "ArrowDown" || event.key === "ArrowUp") {
        event.preventDefault();
        visible.forEach((item) => item.classList.remove("keyboard-active"));
        const delta = event.key === "ArrowDown" ? 1 : -1;
        const nextIndex = current < 0 ? 0 : (current + delta + visible.length) % visible.length;
        visible[nextIndex].classList.add("keyboard-active");
        visible[nextIndex].scrollIntoView({ block: "nearest" });
      }
      if (event.key === "Enter") {
        const active = visible.find((item) => item.classList.contains("keyboard-active")) || visible[0];
        if (active) window.location.href = active.href;
      }
    });

    document.addEventListener("keydown", (event) => {
      const target = event.target;
      const typing = target instanceof HTMLInputElement || target instanceof HTMLTextAreaElement || target instanceof HTMLSelectElement || target?.isContentEditable;
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k") {
        event.preventDefault();
        commandDialog?.hidden ? openCommand() : closeCommand();
      } else if (event.key === "/" && !typing && commandDialog) {
        event.preventDefault();
        openCommand();
      } else if (event.key === "Escape") {
        closeCommand();
        closeMobileSidebar();
      }
    });

    /* Dismissible alerts */
    document.querySelectorAll("[data-flash-close]").forEach((button) => {
      button.addEventListener("click", () => {
        const flash = button.closest(".flash");
        if (!flash) return;
        flash.classList.add("flash-leaving");
        window.setTimeout(() => flash.remove(), 220);
      });
    });

    /* Data tables */
    const updateTable = (tableId) => {
      const table = document.getElementById(tableId);
      if (!table) return;
      const search = document.querySelector(`[data-table-search="${tableId}"]`);
      const filter = document.querySelector(`[data-table-filter="${tableId}"]`);
      const query = normalize(search?.value);
      const category = filter?.value || "";
      let visible = 0;

      table.querySelectorAll("tbody tr").forEach((row) => {
        const matchesText = !query || normalize(row.textContent).includes(query);
        const matchesCategory = !category || row.dataset.category === category;
        const show = matchesText && matchesCategory;
        row.hidden = !show;
        if (show) visible += 1;
      });

      const empty = document.querySelector(`[data-empty-for="${tableId}"]`);
      if (empty) empty.classList.toggle("visible", visible === 0);
    };

    document.querySelectorAll("[data-table-search]").forEach((input) => {
      const id = input.dataset.tableSearch;
      input.addEventListener("input", () => updateTable(id));
    });
    document.querySelectorAll("[data-table-filter]").forEach((select) => {
      const id = select.dataset.tableFilter;
      select.addEventListener("change", () => updateTable(id));
    });

    /* Password visibility */
    document.querySelectorAll("[data-password-toggle]").forEach((button) => {
      const wrapper = button.closest(".login-input-shell, .password-field, .input-shell");
      const input = wrapper?.querySelector('input[type="password"], input[data-password-field]');
      if (!input) return;
      button.addEventListener("click", () => {
        const showing = input.type === "text";
        input.type = showing ? "password" : "text";
        button.setAttribute("aria-pressed", String(!showing));
        button.setAttribute("aria-label", showing ? "Show password" : "Hide password");
        input.focus();
      });
    });

    /* Focus-mode week workspace */
    const focusWorkspace = document.querySelector("[data-focus-workspace]");
    if (focusWorkspace) {
      const tabButtons = [...focusWorkspace.querySelectorAll("[data-focus-tab]")];
      const panels = [...focusWorkspace.querySelectorAll("[data-focus-panel]")];

      const aliases = {
        "guided-lab": "build",
        "research-lab": "research",
        "linkedin-lab": "linkedin",
        assignments: "submit",
      };

      const openFocusTab = (name, options = {}) => {
        const requested = aliases[name] || name;
        const valid = panels.some((panel) => panel.dataset.focusPanel === requested);
        const target = valid ? requested : "build";

        tabButtons.forEach((button) => {
          const active = button.dataset.focusTab === target;
          button.classList.toggle("active", active);
          button.setAttribute("aria-selected", String(active));
        });
        panels.forEach((panel) => {
          const active = panel.dataset.focusPanel === target;
          panel.hidden = !active;
          panel.classList.toggle("active", active);
        });

        if (options.updateHash !== false) {
          history.replaceState(null, "", `#${target}`);
        }
        if (options.scroll !== false) {
          focusWorkspace.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      };

      tabButtons.forEach((button) => {
        button.addEventListener("click", () => openFocusTab(button.dataset.focusTab));
      });
      focusWorkspace.querySelectorAll("[data-open-focus-tab]").forEach((button) => {
        button.addEventListener("click", () => openFocusTab(button.dataset.openFocusTab));
      });

      const initialHash = window.location.hash.replace("#", "");
      openFocusTab(initialHash || "build", { updateHash: false, scroll: false });
    }

    /* Guided lab manual progress and one-step-at-a-time navigation */
    const labShell = document.querySelector("[data-lab-id]");
    if (labShell) {
      const labId = labShell.dataset.labId;
      const steps = [...labShell.querySelectorAll("[data-guided-step]")];
      const stepButtons = [...labShell.querySelectorAll("[data-step-jump]")];
      const completeButtons = [...labShell.querySelectorAll("[data-step-complete]")];
      const progressText = labShell.querySelector("[data-lab-progress-text]");
      const progressBar = labShell.querySelector("[data-lab-progress-bar]");
      const globalProgressText = document.querySelector("[data-global-progress-count]");
      const globalProgressBar = document.querySelector("[data-global-progress-bar]");
      const qualityGate = labShell.querySelector("[data-lab-quality-gate]");
      const storageKey = `academy-guided-lab:${labId}`;
      let currentStep = 1;

      const readSaved = () => {
        try {
          return new Set(JSON.parse(localStorage.getItem(storageKey) || "[]").map(String));
        } catch (_) {
          return new Set();
        }
      };
      const completed = readSaved();
      const save = () => {
        try {
          localStorage.setItem(storageKey, JSON.stringify([...completed]));
        } catch (_) {
          // The current page still reflects progress when browser storage is disabled.
        }
      };

      const showStep = (number, options = {}) => {
        const bounded = Math.min(Math.max(Number(number) || 1, 1), steps.length);
        currentStep = bounded;
        steps.forEach((step) => {
          const active = Number(step.dataset.guidedStep) === currentStep;
          step.hidden = !active;
          step.classList.toggle("active", active);
        });
        stepButtons.forEach((button) => {
          button.classList.toggle("active", Number(button.dataset.stepJump) === currentStep);
        });
        if (options.scroll !== false) {
          labShell.querySelector(".focus-step-stage")?.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      };

      const updateProgress = () => {
        const count = [...completed].filter((value) => Number(value) <= steps.length).length;
        const percentage = steps.length ? Math.round((count / steps.length) * 100) : 0;
        if (progressText) progressText.textContent = `${count} of ${steps.length} steps completed`;
        if (progressBar) progressBar.style.width = `${percentage}%`;
        if (globalProgressText) globalProgressText.textContent = `${percentage}%`;
        if (globalProgressBar) globalProgressBar.style.width = `${percentage}%`;

        stepButtons.forEach((button) => {
          const done = completed.has(button.dataset.stepJump);
          button.classList.toggle("completed", done);
          button.setAttribute("aria-label", `${button.textContent.trim()}${done ? ", completed" : ""}`);
        });
        completeButtons.forEach((button) => {
          const done = completed.has(button.dataset.stepComplete);
          button.classList.toggle("completed", done);
          button.textContent = done ? "Completed ✓  Click to undo" : "Mark step complete ✓";
        });
        if (qualityGate) qualityGate.hidden = count !== steps.length;
      };

      stepButtons.forEach((button) => {
        button.addEventListener("click", () => showStep(button.dataset.stepJump));
      });
      steps.forEach((step) => {
        step.querySelector("[data-step-previous]")?.addEventListener("click", () => showStep(currentStep - 1));
        step.querySelector("[data-step-next]")?.addEventListener("click", () => showStep(currentStep + 1));
      });
      completeButtons.forEach((button) => {
        button.addEventListener("click", () => {
          const value = button.dataset.stepComplete;
          const wasComplete = completed.has(value);
          if (wasComplete) {
            completed.delete(value);
          } else {
            completed.add(value);
          }
          save();
          updateProgress();
          const status = button.closest(".focus-guided-step")?.querySelector("[data-step-save-status]");
          if (status) {
            status.textContent = wasComplete
              ? "Step reopened. Your change was saved in this browser."
              : "Step completed. Progress saved automatically in this browser.";
          }
          if (!wasComplete && currentStep < steps.length) {
            window.setTimeout(() => showStep(currentStep + 1), 320);
          }
        });
      });

      const firstIncomplete = steps.find((step) => !completed.has(step.dataset.guidedStep));
      currentStep = firstIncomplete ? Number(firstIncomplete.dataset.guidedStep) : steps.length;
      updateProgress();
      showStep(currentStep, { scroll: false });
    }

    /* Copy code blocks */
    document.querySelectorAll("[data-copy-command-group]").forEach((button) => {
      button.addEventListener("click", async () => {
        const code = button.closest(".command-card, .command-group")?.querySelector("code")?.textContent?.trim();
        if (!code) return;
        const original = button.textContent;
        try {
          await navigator.clipboard.writeText(code);
          button.textContent = "Copied";
          button.classList.add("copied");
        } catch (_) {
          button.textContent = "Select and copy";
        }
        window.setTimeout(() => {
          button.textContent = original;
          button.classList.remove("copied");
        }, 1600);
      });
    });

    /* Sticky week navigation and active section */
    const jumpLinks = [...document.querySelectorAll(".week-jump-nav a[href^='#']")];
    if (jumpLinks.length && "IntersectionObserver" in window) {
      const targets = jumpLinks
        .map((link) => document.querySelector(link.getAttribute("href")))
        .filter(Boolean);
      const linkForTarget = new Map(
        jumpLinks.map((link) => [link.getAttribute("href")?.slice(1), link])
      );
      const observer = new IntersectionObserver(
        (entries) => {
          const visible = entries
            .filter((entry) => entry.isIntersecting)
            .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
          if (!visible) return;
          jumpLinks.forEach((link) => link.classList.remove("active"));
          linkForTarget.get(visible.target.id)?.classList.add("active");
        },
        { rootMargin: "-20% 0px -68% 0px", threshold: [0.05, 0.25, 0.6] }
      );
      targets.forEach((target) => observer.observe(target));
    }

    /* Entrance animation without blocking non-JS rendering */
    const revealNodes = document.querySelectorAll(
      ".metric-card, .bento-card, .modern-card, .track-card, .roadmap-week, .assignment-card-modern"
    );
    if ("IntersectionObserver" in window) {
      const revealObserver = new IntersectionObserver(
        (entries, observer) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          });
        },
        { threshold: 0.08 }
      );
      revealNodes.forEach((node, index) => {
        node.classList.add("reveal-item");
        node.style.setProperty("--reveal-delay", `${Math.min(index % 8, 7) * 35}ms`);
        revealObserver.observe(node);
      });
    } else {
      revealNodes.forEach((node) => node.classList.add("is-visible"));
    }

    /* Built-in avatar gallery */
    const avatarPreview = document.querySelector("[data-avatar-preview]");
    const avatarPresetInputs = document.querySelectorAll("[data-avatar-preset]");
    avatarPresetInputs.forEach((input) => {
      input.addEventListener("change", () => {
        if (!input.checked) return;
        if (avatarPreview && input.dataset.avatarUrl) avatarPreview.src = input.dataset.avatarUrl;
        document.querySelectorAll(".avatar-option").forEach((option) => option.classList.remove("selected"));
        input.closest(".avatar-option")?.classList.add("selected");
      });
    });

  });
})();


// Profile picture preview
const avatarInput = document.querySelector('[data-avatar-input]');
const avatarPreview = document.querySelector('[data-avatar-preview]');
if (avatarInput && avatarPreview) {
  avatarInput.addEventListener('change', () => {
    const file = avatarInput.files && avatarInput.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.addEventListener('load', () => { avatarPreview.src = reader.result; });
    reader.readAsDataURL(file);
  });
}
