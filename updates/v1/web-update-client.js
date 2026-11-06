/*
 * ARTEFAKT-LAB web/PWA update helper — v1 integration reference.
 *
 * This helper checks for a new service-worker version. It does not install
 * native APK/desktop updates. Serve from the same origin as the PWA.
 * Call startArtefaktWebUpdateCheck() from the application's entry point.
 */
(function (global) {
  "use strict";

  async function startArtefaktWebUpdateCheck(options) {
    const config = Object.assign({
      serviceWorkerUrl: "/service-worker.js",
      onUpdateAvailable: function (applyUpdate) {
        // Default is deliberately non-disruptive: let the host app present UI.
        console.info("[ARTEFAKT] Web update available.");
        global.dispatchEvent(new CustomEvent("artefakt:update-available", {
          detail: { applyUpdate: applyUpdate }
        }));
      },
      onError: function (error) {
        console.warn("[ARTEFAKT] Update check failed:", error);
      }
    }, options || {});

    if (!("serviceWorker" in navigator)) return { supported: false };

    try {
      const registration = await navigator.serviceWorker.register(
        config.serviceWorkerUrl,
        { updateViaCache: "none" }
      );

      await registration.update();

      function inspect(worker) {
        if (!worker || worker.state !== "installed" || !navigator.serviceWorker.controller) return;
        config.onUpdateAvailable(function applyUpdate() {
          if (registration.waiting) {
            registration.waiting.postMessage({ type: "SKIP_WAITING" });
          }
        });
      }

      inspect(registration.installing);
      registration.addEventListener("updatefound", function () {
        const worker = registration.installing;
        if (!worker) return;
        worker.addEventListener("statechange", function () { inspect(worker); });
      });

      navigator.serviceWorker.addEventListener("controllerchange", function () {
        // The host app may choose to reload after its own save/confirmation flow.
        global.dispatchEvent(new CustomEvent("artefakt:update-applied"));
      });

      return { supported: true, registration: registration };
    } catch (error) {
      config.onError(error);
      return { supported: true, error: error };
    }
  }

  global.startArtefaktWebUpdateCheck = startArtefaktWebUpdateCheck;
})(window);
