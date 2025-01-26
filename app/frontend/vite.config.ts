/// <reference types="vitest" />
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  test: {
    globals: true, // Enables global variables like `describe`, `it`
    environment: "jsdom", // Simulates a browser environment
    setupFiles: "./src/setupTests.ts", // Path to setup file for global configurations
  },
});
