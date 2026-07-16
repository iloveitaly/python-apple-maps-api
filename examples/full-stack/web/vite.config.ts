import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

export default defineConfig({
  plugins: [react()],
  server: {
    // token_server.py (apple_maps_api.create_mapkit_token)
    proxy: {
      "/api": "http://127.0.0.1:8765",
    },
  },
})
