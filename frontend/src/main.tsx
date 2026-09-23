import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import AppV2 from "./AppV2";
import { ToastProvider } from "./components/primitives/Toast";
import { initTheme } from "./lib/theme";
import "./index.css";
import "./styles/theme.css";

initTheme();

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <BrowserRouter>
      <ToastProvider>
        <AppV2 />
      </ToastProvider>
    </BrowserRouter>
  </StrictMode>,
);
