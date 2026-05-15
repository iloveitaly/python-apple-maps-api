import { readFileSync } from "node:fs"
import { dirname, isAbsolute, resolve } from "node:path"
import { fileURLToPath } from "node:url"

import react from "@vitejs/plugin-react"
import { SignJWT, importPKCS8 } from "jose"
import tailwindcss from "@tailwindcss/vite"
import { defineConfig } from "vite"

const __dirname = dirname(fileURLToPath(import.meta.url))

export default defineConfig({
  plugins: [
    tailwindcss(),
    react(),
    {
      name: "apple-maps-token",
      configureServer(server) {
        server.middlewares.use("/api/maps-token", async (_req, res) => {
          try {
            const keyPath = process.env.APPLE_MAPS_KEY_PATH ?? ""
            const keyId = process.env.APPLE_MAPS_KEY_ID ?? ""
            const teamId = process.env.APPLE_MAPS_TEAM_ID ?? ""

            // resolve relative paths against project root (parent of web/)
            const resolvedPath = isAbsolute(keyPath)
              ? keyPath
              : resolve(__dirname, "..", keyPath)

            const privateKey = readFileSync(resolvedPath, "utf-8")
            const ecKey = await importPKCS8(privateKey, "ES256")

            const token = await new SignJWT({})
              .setProtectedHeader({ alg: "ES256", kid: keyId, typ: "JWT" })
              .setIssuer(teamId)
              .setIssuedAt()
              .setExpirationTime("30m")
              .sign(ecKey)

            res.setHeader("Content-Type", "application/json")
            res.end(JSON.stringify({ token }))
          } catch (err) {
            res.statusCode = 500
            res.end(JSON.stringify({ error: String(err) }))
          }
        })
      },
    },
  ],
})
