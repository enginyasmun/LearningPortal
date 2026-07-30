document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;
  const sidebar = document.getElementById("app-sidebar");
  const openButton = document.querySelector("[data-sidebar-toggle]");
  const closeTarget = document.querySelector("[data-sidebar-close]");
  const collapseButton = document.querySelector("[data-sidebar-collapse]");
  const desktopSidebar = window.matchMedia("(min-width: 901px)");
  const collapseStorageKey = "academy-sidebar-collapsed";

  const closeSidebar = () => body.classList.remove("sidebar-open");
  if (openButton && sidebar) openButton.addEventListener("click", () => body.classList.toggle("sidebar-open"));
  if (closeTarget) closeTarget.addEventListener("click", closeSidebar);
  document.querySelectorAll(".sidebar a").forEach(link => link.addEventListener("click", closeSidebar));
  document.addEventListener("keydown", event => { if (event.key === "Escape") closeSidebar(); });

  const setSidebarCollapsed = collapsed => {
    body.classList.toggle("sidebar-collapsed", collapsed && desktopSidebar.matches);
    if (collapseButton) {
      collapseButton.setAttribute("aria-expanded", String(!collapsed));
      collapseButton.setAttribute("aria-label", collapsed ? "Expand navigation" : "Collapse navigation");
      const label = collapseButton.querySelector(".sr-only");
      if (label) label.textContent = collapsed ? "Expand navigation" : "Collapse navigation";
    }
  };

  document.querySelectorAll(".sidebar .nav-link").forEach(link => {
    const label = link.querySelector("span")?.textContent?.trim();
    if (!label) return;
    link.dataset.tooltip = label;
    link.setAttribute("aria-label", label);
  });

  if (collapseButton) {
    let collapsed = false;
    try { collapsed = localStorage.getItem(collapseStorageKey) === "true"; } catch (_) { collapsed = false; }
    setSidebarCollapsed(collapsed);

    collapseButton.addEventListener("click", () => {
      collapsed = !body.classList.contains("sidebar-collapsed");
      setSidebarCollapsed(collapsed);
      try { localStorage.setItem(collapseStorageKey, String(collapsed)); } catch (_) { /* Preference remains active for this page. */ }
    });

    desktopSidebar.addEventListener?.("change", () => setSidebarCollapsed(collapsed));
  }

  const normalize = value => (value || "").toLowerCase().trim();
  const updateTable = tableId => {
    const table = document.getElementById(tableId);
    if (!table) return;
    const search = document.querySelector(`[data-table-search="${tableId}"]`);
    const filter = document.querySelector(`[data-table-filter="${tableId}"]`);
    const query = normalize(search?.value);
    const category = filter?.value || "";
    const filterRows = table.querySelectorAll("tbody tr[data-filter-row]");
    const rows = filterRows.length ? filterRows : table.querySelectorAll("tbody tr:not([data-edit-row])");
    let visible = 0;

    rows.forEach(row => {
      const matchesText = !query || normalize(row.textContent).includes(query);
      const matchesCategory = !category || row.dataset.category === category;
      const show = matchesText && matchesCategory;
      row.hidden = !show;
      if (show) visible += 1;

      const studentId = row.dataset.studentRow;
      if (!show && studentId) {
        const editRow = table.querySelector(`[data-edit-for="${studentId}"]`);
        const editButton = row.querySelector("[data-student-edit-toggle]");
        if (editRow) editRow.hidden = true;
        if (editButton) editButton.setAttribute("aria-expanded", "false");
      }
    });

    const empty = document.querySelector(`[data-empty-for="${tableId}"]`);
    if (empty) empty.classList.toggle("visible", visible === 0);
  };

  document.querySelectorAll("[data-table-search]").forEach(input => {
    const id = input.dataset.tableSearch;
    input.addEventListener("input", () => updateTable(id));
  });
  document.querySelectorAll("[data-table-filter]").forEach(select => {
    const id = select.dataset.tableFilter;
    select.addEventListener("change", () => updateTable(id));
  });

  const setStudentEditState = (targetId, open) => {
    const row = document.getElementById(targetId);
    const toggle = document.querySelector(`[data-student-edit-toggle="${targetId}"]`);
    if (!row || !toggle) return;
    row.hidden = !open;
    toggle.setAttribute("aria-expanded", String(open));
    toggle.textContent = open ? "Close" : "Edit";
    if (open) row.querySelector("input, select, button")?.focus();
    else toggle.focus();
  };

  document.querySelectorAll("[data-student-edit-toggle]").forEach(button => {
    button.addEventListener("click", () => {
      const targetId = button.dataset.studentEditToggle;
      const target = document.getElementById(targetId);
      setStudentEditState(targetId, Boolean(target?.hidden));
    });
  });

  document.querySelectorAll("[data-student-edit-close]").forEach(button => {
    button.addEventListener("click", () => setStudentEditState(button.dataset.studentEditClose, false));
  });

  document.querySelectorAll("[data-password-toggle]").forEach(button => {
    const wrapper = button.closest("[data-password-shell], .login-input-shell");
    const input = wrapper?.querySelector('input[type="password"], input[data-password-field]');
    if (!input) return;
    button.addEventListener("click", () => {
      const showing = input.type === "text";
      input.type = showing ? "password" : "text";
      button.setAttribute("aria-pressed", String(!showing));
      button.setAttribute("aria-label", showing ? "Show password" : "Hide password");
      wrapper.classList.toggle("password-visible", !showing);
      input.focus();
    });
  });

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

    const save = completed => {
      try {
        localStorage.setItem(storageKey, JSON.stringify([...completed]));
      } catch (_) {
        // Progress still works for the current page when browser storage is unavailable.
      }
    };

    const completed = readSaved();

    const updateLabProgress = () => {
      checks.forEach(check => {
        const step = check.dataset.labStepCheck;
        check.checked = completed.has(step);
        check.closest(".guided-step")?.classList.toggle("completed", completed.has(step));
      });
      const count = completed.size;
      const percentage = checks.length ? Math.round((count / checks.length) * 100) : 0;
      if (progressText) progressText.textContent = `${count} of ${checks.length} steps`;
      if (progressBar) progressBar.style.width = `${percentage}%`;
    };

    checks.forEach(check => {
      check.addEventListener("change", () => {
        const step = check.dataset.labStepCheck;
        if (check.checked) completed.add(step);
        else completed.delete(step);
        save(completed);
        updateLabProgress();
      });
    });

    updateLabProgress();
  }

  document.querySelectorAll("[data-copy-command-group]").forEach(button => {
    button.addEventListener("click", async () => {
      const code = button.closest(".command-group")?.querySelector("code")?.textContent?.trim();
      if (!code) return;
      const original = button.textContent;
      try {
        await navigator.clipboard.writeText(code);
        button.textContent = "Copied";
      } catch (_) {
        button.textContent = "Select and copy";
      }
      window.setTimeout(() => { button.textContent = original; }, 1600);
    });
  });
});
