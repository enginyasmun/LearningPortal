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

    /* Guided lab progress */
    const labShell = document.querySelector("[data-lab-id]");
    if (labShell) {
      const labId = labShell.dataset.labId;
      const checks = [...labShell.querySelectorAll("[data-lab-step-check]")];
      const progressText = labShell.querySelector("[data-lab-progress-text]");
      const progressBar = labShell.querySelector("[data-lab-progress-bar]");
      const storageKey = `academy-guided-lab:${labId}`;

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
          // Progress remains available for the current page.
        }
      };
      const updateProgress = () => {
        checks.forEach((check) => {
          const step = check.dataset.labStepCheck;
          check.checked = completed.has(step);
          check.closest(".guided-step")?.classList.toggle("completed", completed.has(step));
        });
        const count = completed.size;
        const percentage = checks.length ? Math.round((count / checks.length) * 100) : 0;
        if (progressText) progressText.textContent = `${count} of ${checks.length} steps`;
        if (progressBar) progressBar.style.width = `${percentage}%`;
      };

      checks.forEach((check) => {
        check.addEventListener("change", () => {
          const step = check.dataset.labStepCheck;
          check.checked ? completed.add(step) : completed.delete(step);
          save();
          updateProgress();
        });
      });
      updateProgress();
    }

    /* Copy code blocks */
    document.querySelectorAll("[data-copy-command-group]").forEach((button) => {
      button.addEventListener("click", async () => {
        const code = button.closest(".command-group")?.querySelector("code")?.textContent?.trim();
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
