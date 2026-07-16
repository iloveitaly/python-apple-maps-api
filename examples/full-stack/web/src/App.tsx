import { useState } from "react"
import { AutocompletePage } from "./AutocompletePage"
import { MapPage } from "./MapPage"

type Page = "map" | "autocomplete"

export default function App() {
  const [page, setPage] = useState<Page>("map")

  return (
    <div style={{ display: "flex", flexDirection: "column", height: "100%" }}>
      <nav style={{ display: "flex", gap: 12, padding: "10px 16px", borderBottom: "1px solid #ddd" }}>
        <button type="button" onClick={() => setPage("map")} disabled={page === "map"}>
          Map
        </button>
        <button
          type="button"
          onClick={() => setPage("autocomplete")}
          disabled={page === "autocomplete"}
        >
          Autocomplete
        </button>
      </nav>
      <div style={{ flex: 1, minHeight: 0 }}>{page === "map" ? <MapPage /> : <AutocompletePage />}</div>
    </div>
  )
}
